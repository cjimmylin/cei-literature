#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
from pathlib import Path
import copy

MODEL_MAPPING = {
    "gemini-3.1-pro": "pro"
}

BASE = Path(__file__).resolve().parent
OPUS_FILES = sorted(BASE.glob("20260404-trial-CC1-globalopinionqa-opus.json"))

def get_gemini_response(prompt, model_alias):
    full_prompt = f"{prompt}\n\nIMPORTANT: Respond ONLY with a valid JSON object. Do not include any other text, markdown blocks, or explanations."
    try:
        cmd = ["gemini", "--model", model_alias, "--prompt", full_prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        if "{" in output and "}" in output:
            output = output[output.find("{"):output.rfind("}")+1]
        return json.loads(output)
    except Exception as e:
        print(f"Error calling Gemini CLI: {e}")
        return None

def main():
    target_model_name = "gemini-3.1-pro"
    model_alias = "pro"
    opus_file = OPUS_FILES[0]

    with open(opus_file, 'r') as f:
        data = json.load(f)

    new_data = copy.deepcopy(data)
    new_data["items"] = new_data["items"][:2] # ONLY 2 ITEMS FOR TEST
    
    print(f"TEST RUN: Trial {data['trial_id']} with {target_model_name}...")

    for item in new_data["items"]:
        question = item["question"]
        prompt = (
            f"Question: {question}\n"
            "Respond to this item as an AI model. Provide a textual response and a numeric score on a scale of 1-5.\n"
            "Output your response in the following JSON format:\n"
            "{\n"
            "  \"response\": \"Your textual response\",\n"
            "  \"response_numeric\": 5,\n"
            "  \"reasoning\": \"Brief explanation of your response\"\n"
            "}"
        )
        resp_json = get_gemini_response(prompt, model_alias)
        if resp_json:
            for key in resp_json:
                item[key] = resp_json[key]
            print(f"  Item {item['id']} complete.")
        else:
            print(f"  Item {item['id']} FAILED.")
    
    print("Test run complete.")
    print(json.dumps(new_data["items"], indent=2))

if __name__ == "__main__":
    main()
