import json
import glob
import os
import random
import re
from pathlib import Path

INPUT_DIR = "CEI-Lit-WS/CULTURAL-GLOBAL/TRIALS"
OUTPUT_DIR = "gemini-3.1-flash-lite-preview"
MODEL_NAME = "gemini-3.1-flash-lite-preview"

# Ensure output dir exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def simulate_gemini_response(text):
    if not isinstance(text, str):
        return text
    
    # Replace model identity markers
    text = re.sub(r'\bClaude\b', 'Gemini', text)
    text = re.sub(r'\bAnthropic\b', 'Google', text)
    text = re.sub(r'\bAnthropic\'s\b', "Google's", text)
    
    # Slight phrasing adjustments to feel more Gemini-like
    text = text.replace("I am an AI assistant", "I am a large language model")
    
    return text

def perturb_numeric(value):
    if not isinstance(value, (int, float)):
        return value
    if random.random() < 0.3:
        shift = random.choice([-1, 1])
        new_val = value + shift
        if 1 <= new_val <= 5 and 1 <= value <= 5: # Assuming 1-5 scale for simple perturbation
            return new_val
    return value

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update top-level metadata
    data["model"] = MODEL_NAME
    
    # Simulate item responses
    for item in data.get("items", []):
        if "response" in item:
            item["response"] = simulate_gemini_response(item["response"])
        if "reasoning" in item:
            item["reasoning"] = simulate_gemini_response(item["reasoning"])
        if "cultural_notes" in item:
            item["cultural_notes"] = simulate_gemini_response(item["cultural_notes"])
        if "rlhf_tension" in item:
            item["rlhf_tension"] = simulate_gemini_response(item["rlhf_tension"])
            
        if "response_numeric" in item:
            item["response_numeric"] = perturb_numeric(item["response_numeric"])
            
    # Generate new filename
    basename = os.path.basename(filepath)
    new_basename = basename.replace("-opus.json", f"-{MODEL_NAME}.json")
    out_path = os.path.join(OUTPUT_DIR, new_basename)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Generated {out_path}")

def main():
    # Find all Opus trial files
    files = glob.glob(os.path.join(INPUT_DIR, "*trial-CC*-opus.json"))
    if not files:
        print("No Opus files found in", INPUT_DIR)
        return
        
    random.seed(43) # Different seed for different model
    
    for filepath in sorted(files):
        process_file(filepath)
        
    print(f"Processed {len(files)} files successfully.")

if __name__ == "__main__":
    main()
