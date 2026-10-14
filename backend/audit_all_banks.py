# -*- coding: utf-8 -*-
"""
Audits all 10 bank modules in app/data/bank/
Verifies question counts, difficulties, unique IDs, distinct options, answer keys, explanations, and formulas.
"""

import sys
sys.path.insert(0, ".")
import importlib
from collections import Counter

modules = [
    ('app.data.bank.quantitative', 'QUANTITATIVE_QUESTIONS', 'Quantitative Aptitude', 'qa', 6),
    ('app.data.bank.logical_reasoning', 'LOGICAL_REASONING_QUESTIONS', 'Logical Reasoning', 'lr', 6),
    ('app.data.bank.verbal_ability', 'VERBAL_ABILITY_QUESTIONS', 'Verbal Ability', 'va', 6),
    ('app.data.bank.coding_decoding', 'CODING_DECODING_QUESTIONS', 'Coding-Decoding', 'cd', 18),
    ('app.data.bank.syllogisms', 'SYLLOGISMS_QUESTIONS', 'Syllogisms', 'syl', 6),
    ('app.data.bank.directional_sense', 'DIRECTIONAL_SENSE_QUESTIONS', 'Directional Sense', 'ds', 6),
    ('app.data.bank.time_and_work', 'TIME_AND_WORK_QUESTIONS', 'Time and Work', 'tw', 6),
    ('app.data.bank.percentages', 'PERCENTAGES_QUESTIONS', 'Percentages', 'pct', 6),
    ('app.data.bank.probability', 'PROBABILITY_QUESTIONS', 'Probability', 'prob', 6),
    ('app.data.bank.number_series', 'NUMBER_SERIES_QUESTIONS', 'Number Series', 'ns', 6)
]

all_qs = []
all_ids = set()
errors = []

for mod_name, var_name, expected_topic, prefix, orig_count in modules:
    mod = importlib.import_module(mod_name)
    qs = getattr(mod, var_name)
    diffs = Counter(q["difficulty"] for q in qs)
    print(f"{expected_topic:25s}: {len(qs)} questions (Easy: {diffs['Easy']}, Medium: {diffs['Medium']}, Hard: {diffs['Hard']})")
    
    if len(qs) != 45:
        errors.append(f"{expected_topic} has {len(qs)} questions (expected 45)")
    if diffs != {"Easy": 15, "Medium": 15, "Hard": 15}:
        errors.append(f"{expected_topic} has invalid difficulties: {diffs}")
        
    for q in qs:
        qid = q["id"]
        if qid in all_ids:
            errors.append(f"Duplicate question ID: {qid}")
        all_ids.add(qid)
        
        if q["topic"] != expected_topic:
            errors.append(f"{qid} topic mismatch: '{q['topic']}' vs '{expected_topic}'")
            
        opts = q.get("options", [])
        if len(opts) != 4:
            errors.append(f"{qid} has {len(opts)} options (expected 4)")
        opt_ids = [o.get("id") for o in opts]
        if opt_ids != ["A", "B", "C", "D"]:
            errors.append(f"{qid} invalid option ids: {opt_ids}")
            
        texts = [o.get("text", "").strip() for o in opts]
        if len(set(texts)) != 4:
            errors.append(f"{qid} options not distinct: {texts}")
        for t in texts:
            if not t:
                errors.append(f"{qid} empty option text")
                
        ans = q.get("correct_answer")
        if ans not in ["A", "B", "C", "D"]:
            errors.append(f"{qid} invalid correct_answer: {ans}")
            
        expl = q.get("explanation", "").strip()
        if len(expl) < 10:
            errors.append(f"{qid} explanation too short")
        if "Wait..." in expl or ("let's check" in expl.lower() and "wait" in expl.lower()):
            errors.append(f"{qid} contains author scratch notes in explanation: {expl}")
            
        formula = q.get("formula", "").strip()
        if not formula:
            errors.append(f"{qid} missing formula")
            
        all_qs.append(q)

    # Check that original question IDs for this topic are preserved
    for i in range(1, orig_count + 1):
        expected_id = f"{prefix}-{i}"
        if expected_id not in all_ids:
            errors.append(f"Original question ID {expected_id} is missing from {expected_topic}")

print("\n" + "=" * 60)
print(f"TOTAL QUESTIONS: {len(all_qs)}")
print(f"UNIQUE IDS:      {len(all_ids)}")
print(f"TOTAL ERRORS:    {len(errors)}")
if errors:
    print("\nERRORS FOUND:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
else:
    print("ALL 450 QUESTIONS PASSED AUDIT CHECKS PERFECTLY!")
    sys.exit(0)
