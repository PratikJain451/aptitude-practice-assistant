# -*- coding: utf-8 -*-
"""
Curated question bank for placement aptitude examination preparation.
Modularized topic question banks imported from app.data.bank.
Includes verified questions across all major topics and difficulty levels.
Total: 450 verified questions (45 per topic: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import Dict, List, Any
from app.data.bank import (
    QUANTITATIVE_QUESTIONS,
    LOGICAL_REASONING_QUESTIONS,
    VERBAL_ABILITY_QUESTIONS,
    CODING_DECODING_QUESTIONS,
    SYLLOGISMS_QUESTIONS,
    DIRECTIONAL_SENSE_QUESTIONS,
    TIME_AND_WORK_QUESTIONS,
    PERCENTAGES_QUESTIONS,
    PROBABILITY_QUESTIONS,
    NUMBER_SERIES_QUESTIONS,
    ALL_BANK_QUESTIONS,
)

TOPICS_LIST = [
    "Quantitative Aptitude",
    "Logical Reasoning",
    "Verbal Ability",
    "Coding-Decoding",
    "Syllogisms",
    "Directional Sense",
    "Time and Work",
    "Percentages",
    "Probability",
    "Number Series"
]

QUESTIONS_DATA: List[Dict[str, Any]] = ALL_BANK_QUESTIONS

# Quick access dictionary by unique question ID
QUESTIONS_BY_ID: Dict[str, Dict[str, Any]] = {q["id"]: q for q in QUESTIONS_DATA}

__all__ = [
    "TOPICS_LIST",
    "QUESTIONS_DATA",
    "QUESTIONS_BY_ID",
    "QUANTITATIVE_QUESTIONS",
    "LOGICAL_REASONING_QUESTIONS",
    "VERBAL_ABILITY_QUESTIONS",
    "CODING_DECODING_QUESTIONS",
    "SYLLOGISMS_QUESTIONS",
    "DIRECTIONAL_SENSE_QUESTIONS",
    "TIME_AND_WORK_QUESTIONS",
    "PERCENTAGES_QUESTIONS",
    "PROBABILITY_QUESTIONS",
    "NUMBER_SERIES_QUESTIONS",
]
