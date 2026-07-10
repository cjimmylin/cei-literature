#!/usr/bin/env python3
import json
import sys
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).resolve().parent.parent
GOLD_FILE = PROJECT_ROOT / "trials" / "20260404-trial-T2-sample-30-gold.json"

def score_results(results_file):
    if not results_file.exists():
        print(f"Error: {results_file} not found.")
        return

    with open(GOLD_FILE, "r") as f:
        gold_items = json.load(f)
    
    gold_map = {item["item_id"]: item for item in gold_items}

    with open(results_file, "r") as f:
        results_data = json.load(f)
    
    model_name = results_data.get("model", "Unknown")
    results = results_data.get("results", [])

    correct_total = 0
    correct_beg = 0
    correct_adv = 0
    n_beg = 0
    n_adv = 0
    
    detailed_results = []

    for res in results:
        item_id = res.get("item_id")
        gold_item = gold_map.get(item_id)
        if not gold_item:
            print(f"Warning: No gold label for item_id {item_id}")
            continue
            
        gold_answer = gold_item["gold"]
        predicted_answer = res.get("answer")
        level = gold_item["level"]
        
        is_correct = str(predicted_answer).strip().upper() == str(gold_answer).strip().upper()
        
        if is_correct:
            correct_total += 1
        
        if level.lower() == "beginner":
            n_beg += 1
            if is_correct:
                correct_beg += 1
        else:
            n_adv += 1
            if is_correct:
                correct_adv += 1
        
        detailed_results.append({
            "index": res.get("index"),
            "item_id": item_id,
            "level": level,
            "gold": gold_answer,
            "predicted": predicted_answer,
            "correct": is_correct,
            "reasoning": res.get("reasoning")
        })

    summary = {
        "model": model_name,
        "total_items": len(detailed_results),
        "total_correct": correct_total,
        "total_accuracy": round(correct_total / len(detailed_results) * 100, 1) if detailed_results else 0,
        "beginner_items": n_beg,
        "beginner_correct": correct_beg,
        "beginner_accuracy": round(correct_beg / n_beg * 100, 1) if n_beg else 0,
        "advanced_items": n_adv,
        "advanced_correct": correct_adv,
        "advanced_accuracy": round(correct_adv / n_adv * 100, 1) if n_adv else 0,
    }

    print(f"\nScoring Results for {model_name}:")
    print(f"{'='*30}")
    print(f"Total:    {summary['total_correct']}/{summary['total_items']} ({summary['total_accuracy']}%)")
    print(f"Beginner: {summary['beginner_correct']}/{summary['beginner_items']} ({summary['beginner_accuracy']}%)")
    print(f"Advanced: {summary['advanced_correct']}/{summary['advanced_items']} ({summary['advanced_accuracy']}%)")
    
    return summary

def main():
    if len(sys.argv) < 2:
        print("Usage: python score_t2_results.py <results_json_file>")
        return
    
    results_file = Path(sys.argv[1])
    score_results(results_file)

if __name__ == "__main__":
    main()
