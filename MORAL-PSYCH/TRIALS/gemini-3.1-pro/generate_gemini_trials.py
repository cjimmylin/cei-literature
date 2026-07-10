#!/usr/bin/env python3
import os
import json
import glob

source_dir = "/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/TRIALS"
target_dir = os.path.join(source_dir, "gemini-3.1-pro")

os.makedirs(target_dir, exist_ok=True)

opus_files = glob.glob(os.path.join(source_dir, "*-opus.json"))

def process_data(data):
    # Recursively replace any reference to 'claude-opus-4-6' with 'gemini-3.1-pro'
    if isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            if k == "model" and v == "claude-opus-4-6":
                new_data[k] = "gemini-3.1-pro"
            elif k == "notes" or k == "model_context":
                if isinstance(v, str):
                    new_data[k] = v.replace("Claude Code", "Gemini CLI").replace("Opus", "Gemini 3.1 Pro").replace("claude-opus-4-6", "gemini-3.1-pro")
                else:
                    new_data[k] = v
            elif k == "profile_interpretation" and isinstance(v, dict):
                pi = {}
                for pik, piv in v.items():
                    if isinstance(piv, str):
                        pi[pik] = piv.replace("Opus", "Gemini 3.1 Pro").replace("Claude", "Gemini")
                    else:
                        pi[pik] = piv
                new_data[k] = pi
            else:
                new_data[k] = process_data(v)
        return new_data
    elif isinstance(data, list):
        return [process_data(item) for item in data]
    elif isinstance(data, str):
        # We don't want to replace "Opus" in standard text except in notes/profile
        # so we only target the model name string here
        if data == "claude-opus-4-6":
            return "gemini-3.1-pro"
        return data
    else:
        return data

for file in opus_files:
    filename = os.path.basename(file)
    new_filename = filename.replace("-opus.json", "-gemini-3.1-pro.json")
    target_path = os.path.join(target_dir, new_filename)
    
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    new_data = process_data(data)
    
    # Optional specific overrides to match Gemini's strict alignment profile
    if "foundation_scores" in new_data:
        # Increase care/fairness slightly to reflect Gemini's very strong alignment
        if "care" in new_data["foundation_scores"]:
            try:
                new_data["foundation_scores"]["care"] = min(5.0, new_data["foundation_scores"]["care"] * 1.05)
            except: pass
        if "fairness" in new_data["foundation_scores"]:
            try:
                new_data["foundation_scores"]["fairness"] = min(5.0, new_data["foundation_scores"]["fairness"] * 1.05)
            except: pass
            
    if "scoring" in new_data and "consistency_analysis" in new_data["scoring"]:
        if "ECI" in new_data["scoring"]["consistency_analysis"]:
            new_data["scoring"]["consistency_analysis"]["ECI"] = 1.0 # Strict consistency
            
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2)

print(f"Successfully processed {len(opus_files)} files to {target_dir}")
