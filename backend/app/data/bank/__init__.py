# -*- coding: utf-8 -*-
"""
Topic question banks package exporting curated questions for all 10 topics.
Total: 450 verified questions (15 Easy, 15 Medium, 15 Hard per topic).
"""

from typing import List, Dict, Any

from app.data.bank.quantitative import QUANTITATIVE_QUESTIONS
from app.data.bank.logical_reasoning import LOGICAL_REASONING_QUESTIONS
from app.data.bank.verbal_ability import VERBAL_ABILITY_QUESTIONS
from app.data.bank.coding_decoding import CODING_DECODING_QUESTIONS
from app.data.bank.syllogisms import SYLLOGISMS_QUESTIONS
from app.data.bank.directional_sense import DIRECTIONAL_SENSE_QUESTIONS
from app.data.bank.time_and_work import TIME_AND_WORK_QUESTIONS
from app.data.bank.percentages import PERCENTAGES_QUESTIONS
from app.data.bank.probability import PROBABILITY_QUESTIONS
from app.data.bank.number_series import NUMBER_SERIES_QUESTIONS

ALL_BANK_QUESTIONS: List[Dict[str, Any]] = (
    QUANTITATIVE_QUESTIONS +
    LOGICAL_REASONING_QUESTIONS +
    VERBAL_ABILITY_QUESTIONS +
    CODING_DECODING_QUESTIONS +
    SYLLOGISMS_QUESTIONS +
    DIRECTIONAL_SENSE_QUESTIONS +
    TIME_AND_WORK_QUESTIONS +
    PERCENTAGES_QUESTIONS +
    PROBABILITY_QUESTIONS +
    NUMBER_SERIES_QUESTIONS
)

__all__ = [
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
    "ALL_BANK_QUESTIONS"
]
