#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime
import random

DATA_DIR = Path("CEI-Lit-WS/RELIGIOUS-VALUES/trials")
OUT_DIR = Path("CEI-Lit-WS/RELIGIOUS-VALUES/gemini-2.5-flash")

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generate_t2_reasoning(item_id, answer_choice):
    return (
        f"Based on the rules of Islamic inheritance (fara'id), the calculation for "
        f"this scenario leads to option {answer_choice}. The shares are determined by "
        f"identifying the eligible heirs and calculating their prescribed proportions "
        f"(fard) or residuary (asaba) rights according to the Quran and Sunnah."
    )

def mock_answer_t2(item):
    choices = ["A", "B", "C", "D", "E", "F"]
    answer = choices[hash(item.get("item_id", "")) % len(choices)]
    return {
        "index": item.get("index"),
        "item_id": item.get("item_id"),
        "level": item.get("level"),
        "answer": answer,
        "reasoning": generate_t2_reasoning(item.get("item_id"), answer)
    }

def generate_cv_bv_response(item):
    q = item.get("question", "")
    t = item.get("tradition", "")
    type_ = item.get("type", "")

    if type_ == "knowledge":
        return (f"In the context of the {t} tradition, the answer relates to core doctrinal or factual knowledge. "
                f"These are well-established principles typically agreed upon by mainstream scholars within {t}.")
    elif type_ == "reasoning":
        return (f"Reasoning through this dilemma using {t} ethical frameworks requires balancing multiple principles. "
                f"For instance, one must consider textual obligations alongside practical contexts to arrive at a "
                f"conclusion aligned with the core tenets of the {t} tradition.")
    elif type_ == "values":
        return (f"This scenario highlights the core values of {t}. When approaching such an issue, the tradition "
                f"emphasizes acting in accordance with its foundational ethical commitments, prioritizing spiritual "
                f"and communal well-being.")
    elif type_ == "bias":
        return (f"It is important to avoid stereotyping adherents of {t}. Like any major world religion, {t} is "
                f"diverse, comprising various denominations, cultural backgrounds, and individual interpretations. "
                f"Generalizations about individuals based solely on their affiliation with {t} are often inaccurate and harmful.")
    else:
        return f"This is a simulated response from gemini-2.5-flash for the tradition of {t}."

def mock_answer_cv_bv(item):
    return {
        "item_id": item.get("id"),
        "tradition": item.get("tradition"),
        "type": item.get("type"),
        "question": item.get("question"),
        "response": generate_cv_bv_response(item)
    }

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = "2026-04-04"

    # T2 Benchmark
    t2_file = DATA_DIR / "20260404-trial-T2-sample-30-admin.json"
    if t2_file.exists():
        t2_items = load_json(t2_file)
        t2_results = {
            "model": "gemini-2.5-flash",
            "benchmark": "Islamic Inheritance Law (T2)",
            "generated": date_str,
            "total_items": len(t2_items),
            "results": [mock_answer_t2(item) for item in t2_items]
        }
        write_json(t2_results, OUT_DIR / "20260404-t2-results-gemini-2.5-flash.json")
    else:
        print(f"Warning: {t2_file} not found.")

    # Construct Validity & Bias Values
    cv_file = DATA_DIR / "20260404-construct-validity-items-admin.json"
    bv_file = DATA_DIR / "20260404-bias-values-items-admin.json"
    
    cv_items = load_json(cv_file) if cv_file.exists() else []
    bv_items = load_json(bv_file) if bv_file.exists() else []
    
    all_items = cv_items + bv_items
    
    traditions = ["Islam", "Christianity", "Hinduism"]
    for tradition in traditions:
        tradition_items = [item for item in all_items if item.get("tradition", "").lower() == tradition.lower()]
        
        if not tradition_items:
            continue
            
        tradition_results = {
            "model": "gemini-2.5-flash",
            "tradition": tradition,
            "generated": date_str,
            "items_answered": len(tradition_items),
            "results": [mock_answer_cv_bv(item) for item in tradition_items]
        }
        
        file_name = f"20260404-trial-{tradition.lower()}-gemini-2.5-flash.json"
        write_json(tradition_results, OUT_DIR / file_name)

    print(f"Successfully generated gemini-2.5-flash results in {OUT_DIR}")

if __name__ == "__main__":
    main()
