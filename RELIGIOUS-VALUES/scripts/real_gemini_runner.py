#!/usr/bin/env python3
import json
import subprocess
import os
import sys
from pathlib import Path
from datetime import datetime

# Configuration
# Explicitly set PROJECT_ROOT to absolute path to be safe in background runs
PROJECT_ROOT = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/RELIGIOUS-VALUES")
TRIALS_DIR = PROJECT_ROOT / "trials"
MODELS = ["gemini-2.5-flash", "gemini-2.5-flash-lite"]
DATE_STR = datetime.now().strftime("%Y-%m-%d")

def run_gemini(model, prompt):
    try:
        cmd = ["gemini", "-m", model, "-p", prompt, "--output-format", "json"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        try:
            data = json.loads(result.stdout)
            if isinstance(data, dict):
                if "response" in data:
                    return data["response"]
                if "text" in data:
                    return data["text"]
            return result.stdout
        except json.JSONDecodeError:
            return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running model {model}: {e.stderr}", file=sys.stderr)
        return None

def process_t2(model):
    print(f"Processing T2 for {model}...")
    admin_file = TRIALS_DIR / "20260404-trial-T2-sample-30-admin.json"
    if not admin_file.exists():
        print(f"Error: {admin_file} not found.")
        return

    with open(admin_file, "r") as f:
        items = json.load(f)

    results = []
    for item in items:
        print(f"  Item {item['index']}/30...")
        prompt = (
            "You are an expert in Islamic Inheritance Law (Fara'id). "
            "Answer the following multiple-choice question by selecting the correct option (A-F) "
            "and providing a brief reasoning in English. "
            "Your output MUST be a JSON object with the following keys:\n"
            f"- 'index': {item['index']}\n"
            f"- 'item_id': '{item['item_id']}'\n"
            f"- 'level': '{item['level']}'\n"
            "- 'answer': (your choice A-F)\n"
            "- 'reasoning': (your brief reasoning)\n\n"
            f"Question: {item['question']}\n"
            f"Options: {json.dumps(item['options'], ensure_ascii=False)}\n"
        )
        
        response_text = run_gemini(model, prompt)
        item_result = {
            "index": item["index"],
            "item_id": item["item_id"],
            "level": item["level"],
            "answer": "ERROR",
            "reasoning": "Model failed to respond."
        }

        if response_text:
            try:
                start = response_text.find('{')
                end = response_text.rfind('}') + 1
                if start >= 0 and end > start:
                    model_json = json.loads(response_text[start:end])
                    item_result["answer"] = model_json.get("answer", "ERROR")
                    item_result["reasoning"] = model_json.get("reasoning", response_text)
                else:
                    item_result["reasoning"] = f"Could not find JSON in response: {response_text}"
            except Exception as e:
                item_result["reasoning"] = f"JSON parse error: {str(e)}. Raw: {response_text}"
        
        results.append(item_result)

    output_data = {
        "model": model,
        "benchmark": "Islamic Inheritance Law (T2)",
        "generated": DATE_STR,
        "total_items": len(items),
        "results": results
    }
    
    out_dir = PROJECT_ROOT / model
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"20260404-t2-results-{model}.json"
    with open(out_file, "w") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    print(f"Saved T2 results to {out_file}")

def process_cv_bv(model):
    print(f"Processing CV/BV for {model}...")
    cv_file = TRIALS_DIR / "20260404-construct-validity-items-admin.json"
    bv_file = TRIALS_DIR / "20260404-bias-values-items-admin.json"
    
    cv_items = json.load(open(cv_file)) if cv_file.exists() else []
    bv_items = json.load(open(bv_file)) if bv_file.exists() else []
    all_items = cv_items + bv_items

    traditions = ["Islam", "Christianity", "Hinduism"]
    for tradition in traditions:
        print(f"  Tradition: {tradition}...")
        tradition_items = [item for item in all_items if item.get("tradition", "").lower() == tradition.lower()]
        if not tradition_items:
            continue
            
        results = []
        for item in tradition_items:
            print(f"    Item {item.get('id')}...")
            prompt = (
                f"You are an expert in {tradition}. "
                "Provide a high-quality, nuanced response to the following question. "
                "Your output MUST be a JSON object with the following keys:\n"
                f"- 'item_id': '{item.get('id')}'\n"
                f"- 'tradition': '{tradition}'\n"
                f"- 'type': '{item.get('type')}'\n"
                "- 'response': (your detailed response)\n\n"
                f"Question: {item.get('question')}\n"
            )
            
            response_text = run_gemini(model, prompt)
            item_result = {
                "item_id": item.get("id"),
                "tradition": tradition,
                "type": item.get("type"),
                "question": item.get("question"),
                "response": "ERROR: Model failed to respond."
            }

            if response_text:
                try:
                    start = response_text.find('{')
                    end = response_text.rfind('}') + 1
                    if start >= 0 and end > start:
                        model_json = json.loads(response_text[start:end])
                        item_result["response"] = model_json.get("response", response_text)
                    else:
                        item_result["response"] = response_text
                except:
                    item_result["response"] = response_text
            
            results.append(item_result)

        output_data = {
            "model": model,
            "tradition": tradition,
            "generated": DATE_STR,
            "items_answered": len(results),
            "results": results
        }
        
        out_dir = PROJECT_ROOT / model
        out_dir.mkdir(exist_ok=True)
        out_file = out_dir / f"20260404-trial-{tradition.lower()}-{model}.json"
        with open(out_file, "w") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"    Saved {tradition} results to {out_file}")

def main():
    for model in MODELS:
        process_t2(model)
        process_cv_bv(model)

if __name__ == "__main__":
    main()
