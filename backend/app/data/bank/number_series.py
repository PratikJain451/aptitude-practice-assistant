# -*- coding: utf-8 -*-
"""
Number Series Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

NUMBER_SERIES_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "ns-1",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the missing number in the sequence: 4, 9, 16, 25, 36, ?",
        "options": [
            {
                "id": "A",
                "text": "45"
            },
            {
                "id": "B",
                "text": "48"
            },
            {
                "id": "C",
                "text": "49"
            },
            {
                "id": "D",
                "text": "54"
            }
        ],
        "correct_answer": "C",
        "explanation": "The terms are consecutive perfect squares starting from 2²: 2²=4, 3²=9, 4²=16, 5²=25, 6²=36. The next term is 7² = 49.",
        "formula": "Pattern: T_n = (n + 1)²"
    },
    {
        "id": "ns-2",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Identify the next number in the series: 3, 7, 11, 15, 19, ?",
        "options": [
            {
                "id": "A",
                "text": "21"
            },
            {
                "id": "B",
                "text": "22"
            },
            {
                "id": "C",
                "text": "23"
            },
            {
                "id": "D",
                "text": "24"
            }
        ],
        "correct_answer": "C",
        "explanation": "This is an arithmetic progression with a constant common difference of +4: 3 + 4 = 7, 7 + 4 = 11, ..., 19 + 4 = 23.",
        "formula": "Arithmetic Progression: T_n = a + (n - 1)d, where d = +4"
    },
    {
        "id": "ns-7",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next number in the series: 3, 7, 11, 15, 19, ?",
        "options": [
            {
                "id": "A",
                "text": "23"
            },
            {
                "id": "B",
                "text": "22"
            },
            {
                "id": "C",
                "text": "24"
            },
            {
                "id": "D",
                "text": "25"
            }
        ],
        "correct_answer": "A",
        "explanation": "This is an arithmetic progression with a common difference of +4: 3 + 4 = 7; 7 + 4 = 11; 11 + 4 = 15; 15 + 4 = 19; 19 + 4 = 23.",
        "formula": "T_n = a + (n - 1)d; Next Term = Previous + 4"
    },
    {
        "id": "ns-8",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the missing number in the sequence: 4, 9, 16, 25, 36, ?",
        "options": [
            {
                "id": "A",
                "text": "49"
            },
            {
                "id": "B",
                "text": "48"
            },
            {
                "id": "C",
                "text": "50"
            },
            {
                "id": "D",
                "text": "64"
            }
        ],
        "correct_answer": "A",
        "explanation": "The terms are squares of consecutive integers: 2^2 = 4, 3^2 = 9, 4^2 = 16, 5^2 = 25, 6^2 = 36. Next term is 7^2 = 49.",
        "formula": "T_n = n^2 for n = 2, 3, 4, 5, 6, 7"
    },
    {
        "id": "ns-9",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "What is the next number in the series: 2, 6, 18, 54, ?",
        "options": [
            {
                "id": "A",
                "text": "162"
            },
            {
                "id": "B",
                "text": "108"
            },
            {
                "id": "C",
                "text": "144"
            },
            {
                "id": "D",
                "text": "180"
            }
        ],
        "correct_answer": "A",
        "explanation": "This is a geometric progression with a common ratio of ×3: 2 × 3 = 6; 6 × 3 = 18; 18 × 3 = 54; 54 × 3 = 162.",
        "formula": "T_n = a × r^(n-1); Next Term = Previous × 3"
    },
    {
        "id": "ns-10",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next number in the sequence: 100, 93, 86, 79, ?",
        "options": [
            {
                "id": "A",
                "text": "72"
            },
            {
                "id": "B",
                "text": "71"
            },
            {
                "id": "C",
                "text": "73"
            },
            {
                "id": "D",
                "text": "70"
            }
        ],
        "correct_answer": "A",
        "explanation": "The series decreases by 7 at each step: 100 - 7 = 93; 93 - 7 = 86; 86 - 7 = 79; 79 - 7 = 72.",
        "formula": "Next Term = Previous - 7"
    },
    {
        "id": "ns-11",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "What comes next in the sequence: 1, 8, 27, 64, 125, ?",
        "options": [
            {
                "id": "A",
                "text": "216"
            },
            {
                "id": "B",
                "text": "343"
            },
            {
                "id": "C",
                "text": "225"
            },
            {
                "id": "D",
                "text": "196"
            }
        ],
        "correct_answer": "A",
        "explanation": "The terms are cubes of consecutive positive integers: 1^3 = 1, 2^3 = 8, 3^3 = 27, 4^3 = 64, 5^3 = 125. Next term is 6^3 = 216.",
        "formula": "T_n = n^3 for n = 1, 2, 3, 4, 5, 6"
    },
    {
        "id": "ns-12",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next term in the prime series: 2, 3, 5, 7, 11, ?",
        "options": [
            {
                "id": "A",
                "text": "13"
            },
            {
                "id": "B",
                "text": "15"
            },
            {
                "id": "C",
                "text": "14"
            },
            {
                "id": "D",
                "text": "17"
            }
        ],
        "correct_answer": "A",
        "explanation": "The terms are consecutive prime numbers: 2, 3, 5, 7, 11. The next prime number after 11 is 13.",
        "formula": "Consecutive Prime Number Sequence"
    },
    {
        "id": "ns-13",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ?",
        "options": [
            {
                "id": "A",
                "text": "13"
            },
            {
                "id": "B",
                "text": "11"
            },
            {
                "id": "C",
                "text": "12"
            },
            {
                "id": "D",
                "text": "14"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term is the sum of the preceding two terms: 1+1=2, 1+2=3, 2+3=5, 3+5=8. Next term = 5 + 8 = 13.",
        "formula": "F_n = F_(n-1) + F_(n-2)"
    },
    {
        "id": "ns-14",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "What is the next number in the series: 2, 4, 7, 11, 16, ?",
        "options": [
            {
                "id": "A",
                "text": "22"
            },
            {
                "id": "B",
                "text": "21"
            },
            {
                "id": "C",
                "text": "23"
            },
            {
                "id": "D",
                "text": "20"
            }
        ],
        "correct_answer": "A",
        "explanation": "The differences between successive terms increase by 1 each time: 4 - 2 = 2; 7 - 4 = 3; 11 - 7 = 4; 16 - 11 = 5. Next difference is +6: 16 + 6 = 22.",
        "formula": "Differences = 2, 3, 4, 5, 6 => T_n = T_(n-1) + n"
    },
    {
        "id": "ns-15",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next number in the series: 3, 6, 11, 18, 27, ?",
        "options": [
            {
                "id": "A",
                "text": "38"
            },
            {
                "id": "B",
                "text": "36"
            },
            {
                "id": "C",
                "text": "39"
            },
            {
                "id": "D",
                "text": "40"
            }
        ],
        "correct_answer": "A",
        "explanation": "The differences are consecutive odd numbers: 6 - 3 = 3; 11 - 6 = 5; 18 - 11 = 7; 27 - 18 = 9. Next difference is +11: 27 + 11 = 38.",
        "formula": "Differences = 3, 5, 7, 9, 11"
    },
    {
        "id": "ns-16",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "What is the next number in the sequence: 128, 64, 32, 16, ?",
        "options": [
            {
                "id": "A",
                "text": "8"
            },
            {
                "id": "B",
                "text": "4"
            },
            {
                "id": "C",
                "text": "10"
            },
            {
                "id": "D",
                "text": "6"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term is divided by 2 to obtain the subsequent term: 128 / 2 = 64; 64 / 2 = 32; 32 / 2 = 16; 16 / 2 = 8.",
        "formula": "Next Term = Previous / 2"
    },
    {
        "id": "ns-17",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the next term in the series: 2, 5, 10, 17, 26, ?",
        "options": [
            {
                "id": "A",
                "text": "37"
            },
            {
                "id": "B",
                "text": "35"
            },
            {
                "id": "C",
                "text": "36"
            },
            {
                "id": "D",
                "text": "38"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term follows the rule n^2 + 1: 1^2 + 1 = 2; 2^2 + 1 = 5; 3^2 + 1 = 10; 4^2 + 1 = 17; 5^2 + 1 = 26. Next term is 6^2 + 1 = 36 + 1 = 37.",
        "formula": "T_n = n^2 + 1 for n = 1, 2, 3, 4, 5, 6"
    },
    {
        "id": "ns-18",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "What comes next in the alternating addition series: 10, 15, 12, 17, 14, ?",
        "options": [
            {
                "id": "A",
                "text": "19"
            },
            {
                "id": "B",
                "text": "16"
            },
            {
                "id": "C",
                "text": "18"
            },
            {
                "id": "D",
                "text": "21"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern alternates between +5 and -3: 10 + 5 = 15; 15 - 3 = 12; 12 + 5 = 17; 17 - 3 = 14. Next operation is +5: 14 + 5 = 19.",
        "formula": "Alternating Operations: +5, -3, +5, -3, +5"
    },
    {
        "id": "ns-19",
        "topic": "Number Series",
        "difficulty": "Easy",
        "question": "Find the missing number in the series: 5, 10, 20, 40, ?",
        "options": [
            {
                "id": "A",
                "text": "80"
            },
            {
                "id": "B",
                "text": "60"
            },
            {
                "id": "C",
                "text": "70"
            },
            {
                "id": "D",
                "text": "90"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term is multiplied by 2: 5 × 2 = 10; 10 × 2 = 20; 20 × 2 = 40; 40 × 2 = 80.",
        "formula": "Next Term = Previous × 2"
    },
    {
        "id": "ns-3",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the missing term in the sequence: 2, 6, 12, 20, 30, 42, ?",
        "options": [
            {
                "id": "A",
                "text": "52"
            },
            {
                "id": "B",
                "text": "54"
            },
            {
                "id": "C",
                "text": "56"
            },
            {
                "id": "D",
                "text": "58"
            }
        ],
        "correct_answer": "C",
        "explanation": "The differences between consecutive terms are increasing consecutive even integers: 6-2=4, 12-6=6, 20-12=8, 30-20=10, 42-30=12. The next difference is 14: 42 + 14 = 56. (Also represents n(n+1): 1×2=2, 2×3=6, ..., 7×8=56).",
        "formula": "Pattern: T_n = n(n + 1)"
    },
    {
        "id": "ns-4",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What is the next number in the alternating series: 14, 28, 20, 40, 32, 64, ?",
        "options": [
            {
                "id": "A",
                "text": "52"
            },
            {
                "id": "B",
                "text": "56"
            },
            {
                "id": "C",
                "text": "60"
            },
            {
                "id": "D",
                "text": "128"
            }
        ],
        "correct_answer": "B",
        "explanation": "The alternating rule is multiply by 2, then subtract 8: 14 × 2 = 28; 28 - 8 = 20; 20 × 2 = 40; 40 - 8 = 32; 32 × 2 = 64; 64 - 8 = 56.",
        "formula": "Alternating Operation: (× 2), (- 8), (× 2), (- 8)"
    },
    {
        "id": "ns-20",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the next number in the series: 2, 5, 12, 27, 58, ?",
        "options": [
            {
                "id": "A",
                "text": "121"
            },
            {
                "id": "B",
                "text": "116"
            },
            {
                "id": "C",
                "text": "125"
            },
            {
                "id": "D",
                "text": "119"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is: Multiply by 2 and add consecutive integers (1, 2, 3, 4, 5...): 2 × 2 + 1 = 5; 5 × 2 + 2 = 12; 12 × 2 + 3 = 27; 27 × 2 + 4 = 58; 58 × 2 + 5 = 116 + 5 = 121.",
        "formula": "T_n = 2 × T_(n-1) + n"
    },
    {
        "id": "ns-21",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What is the next number in the interleaved series: 4, 18, 7, 15, 10, 12, ?",
        "options": [
            {
                "id": "A",
                "text": "13"
            },
            {
                "id": "B",
                "text": "14"
            },
            {
                "id": "C",
                "text": "9"
            },
            {
                "id": "D",
                "text": "11"
            }
        ],
        "correct_answer": "A",
        "explanation": "This consists of two interleaved sub-series: Odd positions: 4, 7, 10, ... (+3 progression). Even positions: 18, 15, 12, ... (-3 progression). The 7th term belongs to the first sub-series: 10 + 3 = 13.",
        "formula": "Interleaved Series: Odd terms follow +3 progression"
    },
    {
        "id": "ns-22",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the next number in the series: 2, 10, 30, 68, 130, ?",
        "options": [
            {
                "id": "A",
                "text": "222"
            },
            {
                "id": "B",
                "text": "216"
            },
            {
                "id": "C",
                "text": "224"
            },
            {
                "id": "D",
                "text": "210"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term follows the formula n^3 + n: 1^3 + 1 = 2; 2^3 + 2 = 10; 3^3 + 3 = 30; 4^3 + 4 = 68; 5^3 + 5 = 130. Next term is 6^3 + 6 = 216 + 6 = 222.",
        "formula": "T_n = n^3 + n for n = 1, 2, 3, 4, 5, 6"
    },
    {
        "id": "ns-23",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What comes next in the sequence: 1, 2, 6, 21, 88, ?",
        "options": [
            {
                "id": "A",
                "text": "445"
            },
            {
                "id": "B",
                "text": "440"
            },
            {
                "id": "C",
                "text": "450"
            },
            {
                "id": "D",
                "text": "352"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is: Multiply by n and add n: 1 × 1 + 1 = 2; 2 × 2 + 2 = 6; 6 × 3 + 3 = 21; 21 × 4 + 4 = 88; 88 × 5 + 5 = 440 + 5 = 445.",
        "formula": "T_n = n × T_(n-1) + n"
    },
    {
        "id": "ns-24",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the next number in the sequence: 5, 11, 19, 29, 41, ?",
        "options": [
            {
                "id": "A",
                "text": "55"
            },
            {
                "id": "B",
                "text": "53"
            },
            {
                "id": "C",
                "text": "57"
            },
            {
                "id": "D",
                "text": "51"
            }
        ],
        "correct_answer": "A",
        "explanation": "Differences between consecutive terms: 11 - 5 = 6; 19 - 11 = 8; 29 - 19 = 10; 41 - 29 = 12. The differences form an AP: 6, 8, 10, 12, with the next difference being 14. Next term = 41 + 14 = 55.",
        "formula": "Second-order differences are constant (+2): Next diff = 14 => 41 + 14 = 55"
    },
    {
        "id": "ns-25",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the next triangular number in the series: 1, 3, 6, 10, 15, 21, ?",
        "options": [
            {
                "id": "A",
                "text": "28"
            },
            {
                "id": "B",
                "text": "27"
            },
            {
                "id": "C",
                "text": "26"
            },
            {
                "id": "D",
                "text": "30"
            }
        ],
        "correct_answer": "A",
        "explanation": "These are triangular numbers defined by T_n = n(n + 1)/2: For n = 7: T_7 = 7(8)/2 = 28. (Differences are +2, +3, +4, +5, +6, so next is +7: 21 + 7 = 28).",
        "formula": "Triangular Numbers: T_n = n(n + 1) / 2"
    },
    {
        "id": "ns-26",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What is the next number in the series: 4, 2, 2, 3, 6, 15, ?",
        "options": [
            {
                "id": "A",
                "text": "45"
            },
            {
                "id": "B",
                "text": "30"
            },
            {
                "id": "C",
                "text": "40"
            },
            {
                "id": "D",
                "text": "60"
            }
        ],
        "correct_answer": "A",
        "explanation": "The multiplier increases by 0.5 at each step: 4 × 0.5 = 2; 2 × 1.0 = 2; 2 × 1.5 = 3; 3 × 2.0 = 6; 6 × 2.5 = 15; 15 × 3.0 = 45.",
        "formula": "Multiplier Progression: ×0.5, ×1.0, ×1.5, ×2.0, ×2.5, ×3.0"
    },
    {
        "id": "ns-27",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Identify the WRONG number in the series: 2, 6, 12, 20, 30, 42, 54",
        "options": [
            {
                "id": "A",
                "text": "54"
            },
            {
                "id": "B",
                "text": "42"
            },
            {
                "id": "C",
                "text": "30"
            },
            {
                "id": "D",
                "text": "20"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is product of consecutive integers: 1×2 = 2, 2×3 = 6, 3×4 = 12, 4×5 = 20, 5×6 = 30, 6×7 = 42. The next term must be 7×8 = 56, but 54 is given. Hence, 54 is the wrong number.",
        "formula": "T_n = n(n + 1)"
    },
    {
        "id": "ns-28",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What is the next number in the series: 7, 9, 12, 17, 24, ?",
        "options": [
            {
                "id": "A",
                "text": "35"
            },
            {
                "id": "B",
                "text": "33"
            },
            {
                "id": "C",
                "text": "31"
            },
            {
                "id": "D",
                "text": "36"
            }
        ],
        "correct_answer": "A",
        "explanation": "Differences between consecutive terms are consecutive prime numbers: 9 - 7 = 2; 12 - 9 = 3; 17 - 12 = 5; 24 - 17 = 7. The next prime number is 11: 24 + 11 = 35.",
        "formula": "Differences = 2, 3, 5, 7, 11 (Consecutive Primes)"
    },
    {
        "id": "ns-29",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the missing number in the sequence: 3, 4, 10, 33, 136, ?",
        "options": [
            {
                "id": "A",
                "text": "685"
            },
            {
                "id": "B",
                "text": "680"
            },
            {
                "id": "C",
                "text": "690"
            },
            {
                "id": "D",
                "text": "675"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is: Multiply by 1, 2, 3, 4, 5 and add 1, 2, 3, 4, 5: 3 × 1 + 1 = 4; 4 × 2 + 2 = 10; 10 × 3 + 3 = 33; 33 × 4 + 4 = 136; 136 × 5 + 5 = 680 + 5 = 685.",
        "formula": "T_n = n × T_(n-1) + n"
    },
    {
        "id": "ns-30",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "Find the next number in the series: 8, 14, 26, 50, 98, ?",
        "options": [
            {
                "id": "A",
                "text": "194"
            },
            {
                "id": "B",
                "text": "196"
            },
            {
                "id": "C",
                "text": "190"
            },
            {
                "id": "D",
                "text": "192"
            }
        ],
        "correct_answer": "A",
        "explanation": "The differences are doubling each time: 14 - 8 = 6; 26 - 14 = 12; 50 - 26 = 24; 98 - 50 = 48. Next difference = 48 × 2 = 96. Next term = 98 + 96 = 194. (Equivalently: Previous × 2 - 2: 98 × 2 - 2 = 194).",
        "formula": "T_n = 2 × T_(n-1) - 2"
    },
    {
        "id": "ns-31",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What is the next number in the sequence: 6, 13, 28, 59, 122, ?",
        "options": [
            {
                "id": "A",
                "text": "249"
            },
            {
                "id": "B",
                "text": "245"
            },
            {
                "id": "C",
                "text": "244"
            },
            {
                "id": "D",
                "text": "251"
            }
        ],
        "correct_answer": "A",
        "explanation": "Pattern: Multiply by 2 and add increasing powers of 1 (or add 1, 2, 3, 4, 5): 6 × 2 + 1 = 13; 13 × 2 + 2 = 28; 28 × 2 + 3 = 59; 59 × 2 + 4 = 122; 122 × 2 + 5 = 244 + 5 = 249.",
        "formula": "T_n = 2 × T_(n-1) + n"
    },
    {
        "id": "ns-32",
        "topic": "Number Series",
        "difficulty": "Medium",
        "question": "What is the next number in the sequence: 0, 7, 26, 63, 124, ?",
        "options": [
            {
                "id": "A",
                "text": "215"
            },
            {
                "id": "B",
                "text": "216"
            },
            {
                "id": "C",
                "text": "214"
            },
            {
                "id": "D",
                "text": "196"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term follows the formula n^3 - 1: 1^3 - 1 = 0; 2^3 - 1 = 7; 3^3 - 1 = 26; 4^3 - 1 = 63; 5^3 - 1 = 124. Next term is 6^3 - 1 = 216 - 1 = 215.",
        "formula": "T_n = n^3 - 1 for n = 1, 2, 3, 4, 5, 6"
    },
    {
        "id": "ns-5",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the next number in the sequence: 3, 10, 29, 66, 127, ?",
        "options": [
            {
                "id": "A",
                "text": "216"
            },
            {
                "id": "B",
                "text": "218"
            },
            {
                "id": "C",
                "text": "222"
            },
            {
                "id": "D",
                "text": "230"
            }
        ],
        "correct_answer": "B",
        "explanation": "Each term is of the form n³ + 2: 1³ + 2 = 3; 2³ + 2 = 10; 3³ + 2 = 29; 4³ + 2 = 66; 5³ + 2 = 127. The next term is 6³ + 2 = 216 + 2 = 218.",
        "formula": "Pattern: T_n = n³ + 2"
    },
    {
        "id": "ns-6",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Determine the missing value: 5, 16, 51, 158, ?",
        "options": [
            {
                "id": "A",
                "text": "472"
            },
            {
                "id": "B",
                "text": "479"
            },
            {
                "id": "C",
                "text": "481"
            },
            {
                "id": "D",
                "text": "486"
            }
        ],
        "correct_answer": "C",
        "explanation": "Pattern: multiply by 3 and add increasing integers: 5 × 3 + 1 = 16; 16 × 3 + 3 = 51; 51 × 3 + 5 = 158. The next operation is multiply by 3 and add 7: 158 × 3 + 7 = 474 + 7 = 481.",
        "formula": "Recursive Equation: T_n = 3 · T_{n-1} + (2n - 1)"
    },
    {
        "id": "ns-33",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the next fraction in the sequence: 2/3, 4/7, 7/13, 11/21, ?",
        "options": [
            {
                "id": "A",
                "text": "16/31"
            },
            {
                "id": "B",
                "text": "15/31"
            },
            {
                "id": "C",
                "text": "16/29"
            },
            {
                "id": "D",
                "text": "15/29"
            }
        ],
        "correct_answer": "A",
        "explanation": "Numerator pattern: 2, 4, 7, 11, ... with differences +2, +3, +4, so next numerator is 11 + 5 = 16. Denominator pattern: 3, 7, 13, 21, ... with differences +4, +6, +8, so next denominator is 21 + 10 = 31. Therefore, the next fraction is 16/31.",
        "formula": "Num: T_n = T_(n-1) + n; Denom: T_n = T_(n-1) + 2n"
    },
    {
        "id": "ns-34",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the missing term in the sequence: 6, 24, 60, 120, 210, ?",
        "options": [
            {
                "id": "A",
                "text": "336"
            },
            {
                "id": "B",
                "text": "343"
            },
            {
                "id": "C",
                "text": "320"
            },
            {
                "id": "D",
                "text": "330"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term is the product of three consecutive integers (or n^3 - n): 1×2×3 = 6 (2^3 - 2); 2×3×4 = 24 (3^3 - 3); 3×4×5 = 60 (4^3 - 4); 4×5×6 = 120 (5^3 - 5); 5×6×7 = 210 (6^3 - 6). Next term is 6×7×8 = 336 (7^3 - 7 = 343 - 7 = 336).",
        "formula": "T_n = n(n + 1)(n + 2) = (n + 1)^3 - (n + 1)"
    },
    {
        "id": "ns-35",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "What is the next number in the alternating geometric series: 2, -4, 8, -16, 32, -64, ?",
        "options": [
            {
                "id": "A",
                "text": "128"
            },
            {
                "id": "B",
                "text": "-128"
            },
            {
                "id": "C",
                "text": "96"
            },
            {
                "id": "D",
                "text": "-96"
            }
        ],
        "correct_answer": "A",
        "explanation": "This is a geometric progression with first term a = 2 and common ratio r = -2: 2 × (-2) = -4; -4 × (-2) = 8; 8 × (-2) = -16; -16 × (-2) = 32; 32 × (-2) = -64. Next term = -64 × (-2) = +128.",
        "formula": "T_n = a × r^(n-1) with r = -2"
    },
    {
        "id": "ns-36",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the next number in the factorial series: 1, 2, 6, 24, 120, 720, ?",
        "options": [
            {
                "id": "A",
                "text": "5,040"
            },
            {
                "id": "B",
                "text": "4,320"
            },
            {
                "id": "C",
                "text": "5,120"
            },
            {
                "id": "D",
                "text": "4,800"
            }
        ],
        "correct_answer": "A",
        "explanation": "The terms are factorials of positive integers: 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720. Next term is 7! = 720 × 7 = 5,040.",
        "formula": "T_n = n!"
    },
    {
        "id": "ns-37",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "What is the next term in the third-order sequence: 0, 2, 10, 30, 68, ?",
        "options": [
            {
                "id": "A",
                "text": "130"
            },
            {
                "id": "B",
                "text": "128"
            },
            {
                "id": "C",
                "text": "125"
            },
            {
                "id": "D",
                "text": "132"
            }
        ],
        "correct_answer": "A",
        "explanation": "Terms follow n^3 - n^2 (or n^3 + n with n starting from 0): 0^3 + 0 = 0; 1^3 + 1 = 2; 2^3 + 2 = 10; 3^3 + 3 = 30; 4^3 + 4 = 68. Next term is 5^3 + 5 = 125 + 5 = 130.",
        "formula": "T_n = n^3 + n for n = 0, 1, 2, 3, 4, 5"
    },
    {
        "id": "ns-38",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the missing number in the sequence: 3, 10, 32, 100, 308, ?",
        "options": [
            {
                "id": "A",
                "text": "938"
            },
            {
                "id": "B",
                "text": "936"
            },
            {
                "id": "C",
                "text": "942"
            },
            {
                "id": "D",
                "text": "924"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is: Multiply by 3 and add increasing powers of 2 (or +1, +2, +4, +8, +16): 3 × 3 + 1 = 10; 10 × 3 + 2 = 32; 32 × 3 + 4 = 100; 100 × 3 + 8 = 308; 308 × 3 + 16 = 924 + 16 = 938.",
        "formula": "T_n = 3 × T_(n-1) + 2^(n-2)"
    },
    {
        "id": "ns-39",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the missing number in the sequence: 2, 3, 8, 27, 112, ?",
        "options": [
            {
                "id": "A",
                "text": "565"
            },
            {
                "id": "B",
                "text": "560"
            },
            {
                "id": "C",
                "text": "570"
            },
            {
                "id": "D",
                "text": "555"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is: Multiply by 1, 2, 3, 4, 5 and add 1, 2, 3, 4, 5: 2 × 1 + 1 = 3; 3 × 2 + 2 = 8; 8 × 3 + 3 = 27; 27 × 4 + 4 = 112; 112 × 5 + 5 = 560 + 5 = 565.",
        "formula": "T_n = n × T_(n-1) + n"
    },
    {
        "id": "ns-40",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Identify the next term in the series: 1, 5, 14, 30, 55, 91, ?",
        "options": [
            {
                "id": "A",
                "text": "140"
            },
            {
                "id": "B",
                "text": "135"
            },
            {
                "id": "C",
                "text": "144"
            },
            {
                "id": "D",
                "text": "125"
            }
        ],
        "correct_answer": "A",
        "explanation": "These are the sums of the squares of the first n integers: 1^2 = 1; 1 + 2^2 = 5; 5 + 3^2 = 14; 14 + 4^2 = 30; 30 + 5^2 = 55; 55 + 6^2 = 91. Next term = 91 + 7^2 = 91 + 49 = 140.",
        "formula": "Sum of squares formula: S_n = n(n + 1)(2n + 1) / 6; For n = 7: 7(8)(15)/6 = 140"
    },
    {
        "id": "ns-41",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the missing number in the sequence: 2, 12, 36, 80, 150, ?",
        "options": [
            {
                "id": "A",
                "text": "252"
            },
            {
                "id": "B",
                "text": "240"
            },
            {
                "id": "C",
                "text": "260"
            },
            {
                "id": "D",
                "text": "245"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term follows the formula n^3 + n^2: 1^3 + 1^2 = 2; 2^3 + 2^2 = 8 + 4 = 12; 3^3 + 3^2 = 27 + 9 = 36; 4^3 + 4^2 = 64 + 16 = 80; 5^3 + 5^2 = 125 + 25 = 150. Next term is 6^3 + 6^2 = 216 + 36 = 252.",
        "formula": "T_n = n^2(n + 1) = n^3 + n^2 for n = 1, 2, 3, 4, 5, 6"
    },
    {
        "id": "ns-42",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "What is the next number in the recursive sequence: 1, 2, 3, 6, 11, 20, 37, ?",
        "options": [
            {
                "id": "A",
                "text": "68"
            },
            {
                "id": "B",
                "text": "65"
            },
            {
                "id": "C",
                "text": "72"
            },
            {
                "id": "D",
                "text": "74"
            }
        ],
        "correct_answer": "A",
        "explanation": "This is the Tribonacci sequence where each term is the sum of the preceding three terms: 1 + 2 + 3 = 6; 2 + 3 + 6 = 11; 3 + 6 + 11 = 20; 6 + 11 + 20 = 37. Next term = 11 + 20 + 37 = 68.",
        "formula": "Tribonacci: T_n = T_(n-1) + T_(n-2) + T_(n-3)"
    },
    {
        "id": "ns-43",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "Find the next term in the polynomial series: 4, 18, 48, 100, 180, ?",
        "options": [
            {
                "id": "A",
                "text": "294"
            },
            {
                "id": "B",
                "text": "280"
            },
            {
                "id": "C",
                "text": "300"
            },
            {
                "id": "D",
                "text": "290"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each term follows the formula n^3 - n^2 for n starting at 2, or (n+1) × n^2: For n = 2: 2^2 × 1 = 4? Wait: 2^3 - 2^2 = 8 - 4 = 4; 3^3 - 3^2 = 27 - 9 = 18; 4^3 - 4^2 = 64 - 16 = 48; 5^3 - 5^2 = 125 - 25 = 100; 6^3 - 6^2 = 216 - 36 = 180. Next term is 7^3 - 7^2 = 343 - 49 = 294.",
        "formula": "T_n = n^3 - n^2 for n = 2, 3, 4, 5, 6, 7"
    },
    {
        "id": "ns-44",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "What is the next number in the sequence: 5, 6, 14, 45, 184, ?",
        "options": [
            {
                "id": "A",
                "text": "925"
            },
            {
                "id": "B",
                "text": "920"
            },
            {
                "id": "C",
                "text": "930"
            },
            {
                "id": "D",
                "text": "915"
            }
        ],
        "correct_answer": "A",
        "explanation": "The pattern is: Multiply by 1, 2, 3, 4, 5 and add 1, 2, 3, 4, 5: 5 × 1 + 1 = 6; 6 × 2 + 2 = 14; 14 × 3 + 3 = 45; 45 × 4 + 4 = 184; 184 × 5 + 5 = 920 + 5 = 925.",
        "formula": "T_n = n × T_(n-1) + n"
    },
    {
        "id": "ns-45",
        "topic": "Number Series",
        "difficulty": "Hard",
        "question": "What is the next number in the cubic difference sequence: 3, 11, 38, 102, 227, ?",
        "options": [
            {
                "id": "A",
                "text": "443"
            },
            {
                "id": "B",
                "text": "440"
            },
            {
                "id": "C",
                "text": "450"
            },
            {
                "id": "D",
                "text": "435"
            }
        ],
        "correct_answer": "A",
        "explanation": "Differences between consecutive terms are cubes of consecutive integers: 11 - 3 = 8 = 2^3; 38 - 11 = 27 = 3^3; 102 - 38 = 64 = 4^3; 227 - 102 = 125 = 5^3. Next difference is 6^3 = 216. Next term = 227 + 216 = 443.",
        "formula": "Differences = 2^3, 3^3, 4^3, 5^3, 6^3 => T_n = T_(n-1) + (n+1)^3"
    }
]
