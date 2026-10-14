# -*- coding: utf-8 -*-
"""
Probability Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

PROBABILITY_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "prob-1",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A fair 6-sided die is rolled. What is the probability of rolling a prime number?",
        "options": [
            {
                "id": "A",
                "text": "1/6"
            },
            {
                "id": "B",
                "text": "1/3"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "2/3"
            }
        ],
        "correct_answer": "C",
        "explanation": "The possible outcomes are {1, 2, 3, 4, 5, 6}. The prime numbers are {2, 3, 5} (total 3 primes). Probability = 3 / 6 = 1/2.",
        "formula": "Probability P(E) = n(E) / n(S)"
    },
    {
        "id": "prob-2",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A card is drawn from a well-shuffled standard pack of 52 cards. What is the probability that the drawn card is a King?",
        "options": [
            {
                "id": "A",
                "text": "1/13"
            },
            {
                "id": "B",
                "text": "1/26"
            },
            {
                "id": "C",
                "text": "1/52"
            },
            {
                "id": "D",
                "text": "4/13"
            }
        ],
        "correct_answer": "A",
        "explanation": "There are 4 Kings in a deck of 52 cards. Probability = 4 / 52 = 1 / 13.",
        "formula": "P(King) = (Number of Kings) / (Total Cards) = 4 / 52 = 1/13"
    },
    {
        "id": "prob-7",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "What is the probability of getting a prime number when a single fair 6-sided die is rolled?",
        "options": [
            {
                "id": "A",
                "text": "1/2"
            },
            {
                "id": "B",
                "text": "1/3"
            },
            {
                "id": "C",
                "text": "2/3"
            },
            {
                "id": "D",
                "text": "1/6"
            }
        ],
        "correct_answer": "A",
        "explanation": "Possible outcomes on a fair die: {1, 2, 3, 4, 5, 6} (6 total outcomes). Prime numbers are {2, 3, 5} (3 favorable outcomes). Probability = 3/6 = 1/2.",
        "formula": "P(E) = n(E) / n(S) = 3 / 6 = 1/2"
    },
    {
        "id": "prob-8",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A card is drawn from a well-shuffled pack of 52 playing cards. What is the probability that the card drawn is an Ace?",
        "options": [
            {
                "id": "A",
                "text": "1/13"
            },
            {
                "id": "B",
                "text": "1/52"
            },
            {
                "id": "C",
                "text": "1/26"
            },
            {
                "id": "D",
                "text": "4/13"
            }
        ],
        "correct_answer": "A",
        "explanation": "A standard deck contains 52 cards, of which 4 are Aces (one per suit). Probability = 4 / 52 = 1 / 13.",
        "formula": "P(Ace) = Number of Aces / Total Cards = 4 / 52 = 1/13"
    },
    {
        "id": "prob-9",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "Two unbiased coins are tossed simultaneously. What is the probability of getting at least one Head?",
        "options": [
            {
                "id": "A",
                "text": "3/4"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "1/4"
            },
            {
                "id": "D",
                "text": "2/3"
            }
        ],
        "correct_answer": "A",
        "explanation": "Sample space S = {HH, HT, TH, TT} (4 outcomes). Favorable outcomes with at least one Head = {HH, HT, TH} (3 outcomes). Probability = 3/4.",
        "formula": "P(At least 1 Head) = 1 - P(No Heads) = 1 - 1/4 = 3/4"
    },
    {
        "id": "prob-10",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A bag contains 5 red balls, 3 green balls, and 2 blue balls. If one ball is drawn at random, what is the probability that it is green?",
        "options": [
            {
                "id": "A",
                "text": "3/10"
            },
            {
                "id": "B",
                "text": "1/5"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "1/3"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total balls = 5 + 3 + 2 = 10. Favorable green balls = 3. Probability = 3 / 10.",
        "formula": "P(Green) = Green Balls / Total Balls = 3 / 10"
    },
    {
        "id": "prob-11",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "What is the probability of drawing a face card (Jack, Queen, or King) from a standard 52-card deck?",
        "options": [
            {
                "id": "A",
                "text": "3/13"
            },
            {
                "id": "B",
                "text": "1/13"
            },
            {
                "id": "C",
                "text": "4/13"
            },
            {
                "id": "D",
                "text": "12/52 (3/13)"
            }
        ],
        "correct_answer": "A",
        "explanation": "There are 3 face cards per suit (Jack, Queen, King) across 4 suits, giving 3 × 4 = 12 face cards in total. Probability = 12 / 52 = 3 / 13.",
        "formula": "P(Face Card) = 12 / 52 = 3 / 13"
    },
    {
        "id": "prob-12",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "Three unbiased coins are tossed together. What is the probability of getting exactly two Heads?",
        "options": [
            {
                "id": "A",
                "text": "3/8"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "1/4"
            },
            {
                "id": "D",
                "text": "5/8"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total outcomes = 2^3 = 8: {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}. Favorable outcomes with exactly two Heads = {HHT, HTH, THH} (3 outcomes). Probability = 3/8.",
        "formula": "P(X = 2) = C(3, 2) × (1/2)^3 = 3 / 8"
    },
    {
        "id": "prob-13",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "What is the probability that an ordinary (non-leap) year chosen at random contains 53 Sundays?",
        "options": [
            {
                "id": "A",
                "text": "1/7"
            },
            {
                "id": "B",
                "text": "2/7"
            },
            {
                "id": "C",
                "text": "53/365"
            },
            {
                "id": "D",
                "text": "1/365"
            }
        ],
        "correct_answer": "A",
        "explanation": "An ordinary year has 365 days = 52 weeks + 1 extra day. The 52 full weeks give exactly 52 Sundays. The 53rd Sunday occurs only if the 1 extra day is a Sunday. The extra day can be any of the 7 days of the week with equal probability. Probability = 1/7.",
        "formula": "P(53 Sundays in Ordinary Year) = 1 / 7"
    },
    {
        "id": "prob-14",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "What is the probability that a leap year contains 53 Sundays?",
        "options": [
            {
                "id": "A",
                "text": "2/7"
            },
            {
                "id": "B",
                "text": "1/7"
            },
            {
                "id": "C",
                "text": "3/7"
            },
            {
                "id": "D",
                "text": "53/366"
            }
        ],
        "correct_answer": "A",
        "explanation": "A leap year has 366 days = 52 weeks + 2 extra days. The 2 extra days can be: (Sun, Mon), (Mon, Tue), (Tue, Wed), (Wed, Thu), (Thu, Fri), (Fri, Sat), or (Sat, Sun) (7 equally likely pairs). Of these 7 pairs, 2 pairs contain Sunday ((Sat, Sun) and (Sun, Mon)). Probability = 2/7.",
        "formula": "P(53 Sundays in Leap Year) = 2 / 7"
    },
    {
        "id": "prob-15",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "From a box of 20 lottery tickets numbered 1 to 20, one ticket is drawn at random. What is the probability that the number on the ticket is a multiple of 3 or 5?",
        "options": [
            {
                "id": "A",
                "text": "9/20"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "2/5"
            },
            {
                "id": "D",
                "text": "7/20"
            }
        ],
        "correct_answer": "A",
        "explanation": "Multiples of 3 in [1..20]: {3, 6, 9, 12, 15, 18} (6 numbers). Multiples of 5 in [1..20]: {5, 10, 15, 20} (4 numbers). Multiple of both (15): {15} (1 number). Total unique multiples = 6 + 4 - 1 = 9 numbers: {3, 5, 6, 9, 10, 12, 15, 18, 20}. Probability = 9/20.",
        "formula": "P(A U B) = P(A) + P(B) - P(A ∩ B) = (6 + 4 - 1)/20 = 9/20"
    },
    {
        "id": "prob-16",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A card is drawn from a standard pack of 52 cards. What is the probability that it is a Heart or a King?",
        "options": [
            {
                "id": "A",
                "text": "4/13"
            },
            {
                "id": "B",
                "text": "17/52"
            },
            {
                "id": "C",
                "text": "1/4"
            },
            {
                "id": "D",
                "text": "7/26"
            }
        ],
        "correct_answer": "A",
        "explanation": "Hearts = 13. Kings = 4. The King of Hearts is common to both. Total favorable cards = 13 + 4 - 1 = 16 cards. Probability = 16 / 52 = 4 / 13.",
        "formula": "P(Heart U King) = (13 + 4 - 1)/52 = 16/52 = 4/13"
    },
    {
        "id": "prob-17",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "In a spinning wheel game with numbers 1 through 8, all outcomes are equally likely. What is the probability that the pointer lands on an odd number greater than 3?",
        "options": [
            {
                "id": "A",
                "text": "1/4"
            },
            {
                "id": "B",
                "text": "3/8"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "1/8"
            }
        ],
        "correct_answer": "A",
        "explanation": "Odd numbers greater than 3 in {1, 2, 3, 4, 5, 6, 7, 8} are {5, 7} (2 numbers). Total outcomes = 8. Probability = 2 / 8 = 1 / 4.",
        "formula": "P = Favorable / Total = 2 / 8 = 1/4"
    },
    {
        "id": "prob-18",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "If P(A) = 0.65, what is the probability of the complement event P(not A)?",
        "options": [
            {
                "id": "A",
                "text": "0.35"
            },
            {
                "id": "B",
                "text": "0.45"
            },
            {
                "id": "C",
                "text": "0.25"
            },
            {
                "id": "D",
                "text": "-0.65"
            }
        ],
        "correct_answer": "A",
        "explanation": "The sum of probabilities of an event and its complement is 1. P(not A) = 1 - P(A) = 1 - 0.65 = 0.35.",
        "formula": "P(A') = 1 - P(A)"
    },
    {
        "id": "prob-19",
        "topic": "Probability",
        "difficulty": "Easy",
        "question": "A fair 6-sided die is rolled. What is the probability of rolling a number greater than 4?",
        "options": [
            {
                "id": "A",
                "text": "1/3"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "2/3"
            },
            {
                "id": "D",
                "text": "1/6"
            }
        ],
        "correct_answer": "A",
        "explanation": "Outcomes strictly greater than 4 are {5, 6} (2 outcomes). Total outcomes = 6. Probability = 2 / 6 = 1 / 3.",
        "formula": "P(X > 4) = 2 / 6 = 1 / 3"
    },
    {
        "id": "prob-3",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Two fair dice are thrown simultaneously. What is the probability of getting a sum of 8?",
        "options": [
            {
                "id": "A",
                "text": "5/36"
            },
            {
                "id": "B",
                "text": "1/6"
            },
            {
                "id": "C",
                "text": "7/36"
            },
            {
                "id": "D",
                "text": "1/9"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total possible outcomes = 6 × 6 = 36. Favorable outcomes for a sum of 8 are (2,6), (3,5), (4,4), (5,3), (6,2), giving 5 pairs. Probability = 5 / 36.",
        "formula": "P(Sum = 8) = Favorable outcomes / 36 = 5 / 36"
    },
    {
        "id": "prob-4",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A bag contains 4 red balls and 6 blue balls. If two balls are drawn at random without replacement, what is the probability that both balls are red?",
        "options": [
            {
                "id": "A",
                "text": "2/15"
            },
            {
                "id": "B",
                "text": "4/15"
            },
            {
                "id": "C",
                "text": "1/5"
            },
            {
                "id": "D",
                "text": "3/10"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total balls = 10. Number of ways to choose 2 balls from 10 is 10C2 = (10 × 9) / 2 = 45. Number of ways to choose 2 red balls from 4 is 4C2 = (4 × 3) / 2 = 6. Probability = 6 / 45 = 2 / 15.",
        "formula": "Combinatorial Probability: P(Both Red) = (4C2) / (10C2) = 6 / 45 = 2/15"
    },
    {
        "id": "prob-20",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Two fair dice are thrown simultaneously. What is the probability that the sum of the scores on the two dice is 7?",
        "options": [
            {
                "id": "A",
                "text": "1/6"
            },
            {
                "id": "B",
                "text": "7/36"
            },
            {
                "id": "C",
                "text": "5/36"
            },
            {
                "id": "D",
                "text": "1/12"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total outcomes = 6 × 6 = 36. Outcomes giving sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) (6 outcomes). Probability = 6 / 36 = 1 / 6.",
        "formula": "P(Sum = 7) = 6 / 36 = 1/6"
    },
    {
        "id": "prob-21",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Two fair dice are thrown simultaneously. What is the probability of obtaining a total score of 8?",
        "options": [
            {
                "id": "A",
                "text": "5/36"
            },
            {
                "id": "B",
                "text": "1/6"
            },
            {
                "id": "C",
                "text": "4/36"
            },
            {
                "id": "D",
                "text": "7/36"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total outcomes = 36. Outcomes with sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) (5 outcomes). Probability = 5 / 36.",
        "formula": "P(Sum = 8) = 5 / 36"
    },
    {
        "id": "prob-22",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Two cards are drawn from a pack of 52 cards without replacement. What is the probability that both cards are Kings?",
        "options": [
            {
                "id": "A",
                "text": "1/221"
            },
            {
                "id": "B",
                "text": "1/169"
            },
            {
                "id": "C",
                "text": "4/663"
            },
            {
                "id": "D",
                "text": "2/221"
            }
        ],
        "correct_answer": "A",
        "explanation": "Probability of first King = 4 / 52 = 1 / 13. Given the first is a King, 3 Kings remain among 51 cards: Probability of second King = 3 / 51 = 1 / 17. Joint probability = (1 / 13) × (1 / 17) = 1 / 221.",
        "formula": "P(K1 ∩ K2) = (4/52) × (3/51) = 1 / 221"
    },
    {
        "id": "prob-23",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A bag contains 6 black balls and 4 white balls. Two balls are drawn at random one after another without replacement. What is the probability that both balls are black?",
        "options": [
            {
                "id": "A",
                "text": "1/3"
            },
            {
                "id": "B",
                "text": "3/10"
            },
            {
                "id": "C",
                "text": "2/5"
            },
            {
                "id": "D",
                "text": "9/25"
            }
        ],
        "correct_answer": "A",
        "explanation": "Using combinations: Total ways to choose 2 balls from 10 = C(10, 2) = (10 × 9)/2 = 45. Ways to choose 2 black balls from 6 = C(6, 2) = (6 × 5)/2 = 15. Probability = 15 / 45 = 1 / 3.",
        "formula": "P(Both Black) = C(6, 2) / C(10, 2) = 15 / 45 = 1/3"
    },
    {
        "id": "prob-24",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A problem is given to two students A and B whose chances of solving it independently are 1/2 and 1/3 respectively. What is the probability that the problem will be solved?",
        "options": [
            {
                "id": "A",
                "text": "2/3"
            },
            {
                "id": "B",
                "text": "5/6"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "1/6"
            }
        ],
        "correct_answer": "A",
        "explanation": "Probability that A fails to solve = 1 - 1/2 = 1/2. Probability that B fails to solve = 1 - 1/3 = 2/3. Probability that neither solves = (1/2) × (2/3) = 1/3. Probability that the problem is solved = 1 - P(neither solves) = 1 - 1/3 = 2/3.",
        "formula": "P(Solved) = 1 - P(A') × P(B') = 1 - (1/2 × 2/3) = 2/3"
    },
    {
        "id": "prob-25",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A box contains 5 green, 4 yellow, and 3 white marbles. Three marbles are drawn at random. What is the probability that all three marbles are of different colors?",
        "options": [
            {
                "id": "A",
                "text": "3/11"
            },
            {
                "id": "B",
                "text": "4/11"
            },
            {
                "id": "C",
                "text": "2/11"
            },
            {
                "id": "D",
                "text": "5/22"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total marbles = 5 + 4 + 3 = 12. Total ways to select 3 marbles = C(12, 3) = (12 × 11 × 10) / (3 × 2 × 1) = 220. Ways to select 1 green, 1 yellow, and 1 white = C(5, 1) × C(4, 1) × C(3, 1) = 5 × 4 × 3 = 60. Probability = 60 / 220 = 6 / 22 = 3 / 11.",
        "formula": "P(All Different) = [C(5,1) × C(4,1) × C(3,1)] / C(12, 3) = 60 / 220 = 3/11"
    },
    {
        "id": "prob-26",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "In a class, 30% of the students study Hindi, 45% study Sanskrit, and 15% study both. If a student is chosen at random, what is the probability that the student studies neither Hindi nor Sanskrit?",
        "options": [
            {
                "id": "A",
                "text": "40%"
            },
            {
                "id": "B",
                "text": "35%"
            },
            {
                "id": "C",
                "text": "45%"
            },
            {
                "id": "D",
                "text": "50%"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(Hindi U Sanskrit) = P(Hindi) + P(Sanskrit) - P(Both) = 30% + 45% - 15% = 60%. P(Neither) = 100% - 60% = 40% (or 0.40).",
        "formula": "P(Neither) = 1 - P(H U S) = 1 - 0.60 = 0.40 = 40%"
    },
    {
        "id": "prob-27",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Two independent events A and B have probabilities P(A) = 0.4 and P(B) = 0.5. What is P(A ∪ B)?",
        "options": [
            {
                "id": "A",
                "text": "0.70"
            },
            {
                "id": "B",
                "text": "0.90"
            },
            {
                "id": "C",
                "text": "0.20"
            },
            {
                "id": "D",
                "text": "0.60"
            }
        ],
        "correct_answer": "A",
        "explanation": "For independent events, P(A ∩ B) = P(A) × P(B) = 0.4 × 0.5 = 0.20. P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 0.4 + 0.5 - 0.20 = 0.70.",
        "formula": "P(A U B) = P(A) + P(B) - P(A)P(B) = 0.4 + 0.5 - 0.2 = 0.70"
    },
    {
        "id": "prob-28",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A speaks truth in 75% of cases and B in 80% of cases. In what percentage of cases are they likely to contradict each other when stating the same fact?",
        "options": [
            {
                "id": "A",
                "text": "35%"
            },
            {
                "id": "B",
                "text": "40%"
            },
            {
                "id": "C",
                "text": "30%"
            },
            {
                "id": "D",
                "text": "25%"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(A speaks truth) = 3/4, P(A lies) = 1/4. P(B speaks truth) = 4/5, P(B lies) = 1/5. They contradict each other when one speaks the truth and the other lies: P(Contradiction) = P(A)P(B') + P(A')P(B) = (3/4 × 1/5) + (1/4 × 4/5) = 3/20 + 4/20 = 7/20 = 35%.",
        "formula": "P(Contradiction) = P(A)P(B') + P(A')P(B) = 7/20 = 35%"
    },
    {
        "id": "prob-29",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "What is the probability of rolling a total sum of at least 10 with two fair dice?",
        "options": [
            {
                "id": "A",
                "text": "1/6"
            },
            {
                "id": "B",
                "text": "1/12"
            },
            {
                "id": "C",
                "text": "5/36"
            },
            {
                "id": "D",
                "text": "7/36"
            }
        ],
        "correct_answer": "A",
        "explanation": "Sums of at least 10 are: Sum 10: (4,6), (5,5), (6,4) (3 outcomes); Sum 11: (5,6), (6,5) (2 outcomes); Sum 12: (6,6) (1 outcome). Total favorable outcomes = 3 + 2 + 1 = 6. Probability = 6 / 36 = 1 / 6.",
        "formula": "P(Sum >= 10) = (3 + 2 + 1) / 36 = 6/36 = 1/6"
    },
    {
        "id": "prob-30",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Four cards are drawn from a pack of 52 cards. What is the probability that all four cards are of different suits?",
        "options": [
            {
                "id": "A",
                "text": "2,197 / 20,825"
            },
            {
                "id": "B",
                "text": "13 / 52"
            },
            {
                "id": "C",
                "text": "1 / 256"
            },
            {
                "id": "D",
                "text": "1,000 / 20,825"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total ways to choose 4 cards = C(52, 4) = 270,725. To get exactly one card from each of the 4 suits: C(13, 1) × C(13, 1) × C(13, 1) × C(13, 1) = 13^4 = 28,561. Probability = 28,561 / 270,725 = 2,197 / 20,825 ≈ 0.1055.",
        "formula": "P = 13^4 / C(52, 4) = 28561 / 270725 = 2197 / 20825"
    },
    {
        "id": "prob-31",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "A committee of 3 people is to be formed from 4 men and 3 women. What is the probability that the committee contains at least 1 woman?",
        "options": [
            {
                "id": "A",
                "text": "31/35"
            },
            {
                "id": "B",
                "text": "4/35"
            },
            {
                "id": "C",
                "text": "27/35"
            },
            {
                "id": "D",
                "text": "6/7"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total people = 4 + 3 = 7. Total ways to choose 3 people = C(7, 3) = (7 × 6 × 5) / (3 × 2 × 1) = 35. The only case with no women is selecting all 3 men from 4: C(4, 3) = 4. Ways with at least one woman = 35 - 4 = 31. Probability = 31 / 35.",
        "formula": "P(At least 1 Woman) = 1 - [C(Men, 3) / C(Total, 3)] = 1 - 4/35 = 31/35"
    },
    {
        "id": "prob-32",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": "Five letters are placed into five addressed envelopes at random. What is the probability that all 5 letters are placed into their correct envelopes?",
        "options": [
            {
                "id": "A",
                "text": "1/120"
            },
            {
                "id": "B",
                "text": "1/24"
            },
            {
                "id": "C",
                "text": "1/60"
            },
            {
                "id": "D",
                "text": "1/5"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total permutations of placing 5 distinct letters into 5 distinct envelopes = 5! = 120. There is only 1 permutation where every letter matches its intended envelope. Probability = 1 / 120.",
        "formula": "P(All Correct) = 1 / n! = 1 / 120"
    },
    {
        "id": "prob-5",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "Three unbiased coins are tossed together. What is the probability of getting at least two heads?",
        "options": [
            {
                "id": "A",
                "text": "3/8"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "5/8"
            },
            {
                "id": "D",
                "text": "3/4"
            }
        ],
        "correct_answer": "B",
        "explanation": "Total outcomes = 2³ = 8: {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}. 'At least two heads' means 2 heads or 3 heads: {HHT, HTH, THH, HHH} = 4 outcomes. Probability = 4 / 8 = 1/2.",
        "formula": "Binomial Probability: P(X ≥ 2) = 3C2 · (1/2)³ + 3C3 · (1/2)³ = 3/8 + 1/8 = 4/8 = 1/2"
    },
    {
        "id": "prob-6",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "The probability that student A passes an aptitude test is 3/5, and the probability that student B passes is 2/3. If they attempt independently, what is the probability that exactly one of them passes?",
        "options": [
            {
                "id": "A",
                "text": "7/15"
            },
            {
                "id": "B",
                "text": "8/15"
            },
            {
                "id": "C",
                "text": "2/5"
            },
            {
                "id": "D",
                "text": "1/3"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(A passes) = 3/5 => P(A fails) = 2/5. P(B passes) = 2/3 => P(B fails) = 1/3. Exactly one passes = P(A passes and B fails) + P(A fails and B passes) = (3/5 × 1/3) + (2/5 × 2/3) = (3/15) + (4/15) = 7/15.",
        "formula": "P(Exactly one) = P(A) · P(B') + P(A') · P(B)"
    },
    {
        "id": "prob-33",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "In a factory, Machine A produces 60% of daily output and Machine B produces 40%. It is known that 2% of items from Machine A are defective and 1% of items from Machine B are defective. An item is selected at random from the day's production and found to be defective. What is the probability that it was produced by Machine A?",
        "options": [
            {
                "id": "A",
                "text": "3/4 (75%)"
            },
            {
                "id": "B",
                "text": "2/3 (66.7%)"
            },
            {
                "id": "C",
                "text": "1/2 (50%)"
            },
            {
                "id": "D",
                "text": "4/5 (80%)"
            }
        ],
        "correct_answer": "A",
        "explanation": "By Bayes' Theorem: P(A) = 0.60, P(B) = 0.40. P(Def|A) = 0.02, P(Def|B) = 0.01. Total probability of defective P(Def) = P(A)P(Def|A) + P(B)P(Def|B) = (0.60 × 0.02) + (0.40 × 0.01) = 0.012 + 0.004 = 0.016. Posterior probability P(A|Def) = (0.60 × 0.02) / 0.016 = 0.012 / 0.016 = 12 / 16 = 3 / 4 (75%).",
        "formula": "Bayes' Theorem: P(A|D) = [P(A)P(D|A)] / [P(A)P(D|A) + P(B)P(D|B)] = 0.012 / 0.016 = 3/4"
    },
    {
        "id": "prob-34",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "Bag I contains 4 white and 6 black balls. Bag II contains 5 white and 5 black balls. One ball is transferred from Bag I to Bag II and then a ball is drawn from Bag II. What is the probability that the ball drawn from Bag II is white?",
        "options": [
            {
                "id": "A",
                "text": "27/55"
            },
            {
                "id": "B",
                "text": "26/55"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "28/55"
            }
        ],
        "correct_answer": "A",
        "explanation": "Case 1: White ball transferred from Bag I (prob = 4/10 = 2/5). Bag II now has 6 white and 5 black balls (11 total). Prob of drawing white from Bag II = 6/11. Joint prob = (2/5) × (6/11) = 12/55. Case 2: Black ball transferred from Bag I (prob = 6/10 = 3/5). Bag II now has 5 white and 6 black balls (11 total). Prob of drawing white from Bag II = 5/11. Joint prob = (3/5) × (5/11) = 15/55. Total probability = 12/55 + 15/55 = 27/55.",
        "formula": "Law of Total Probability: P(W) = P(W_trans)P(W|W_trans) + P(B_trans)P(W|B_trans) = 27/55"
    },
    {
        "id": "prob-35",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "A medical screening test for a rare disease has a sensitivity of 95% (identifies 95% of diseased patients) and a false positive rate of 5% on healthy people. The disease has a prevalence rate of 1% in the population. If a randomly chosen person tests positive, what is the probability that the person actually has the disease?",
        "options": [
            {
                "id": "A",
                "text": "19/118 (approx 16.1%)"
            },
            {
                "id": "B",
                "text": "95%"
            },
            {
                "id": "C",
                "text": "50%"
            },
            {
                "id": "D",
                "text": "1/20 (5%)"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(Disease D) = 0.01, P(Healthy H) = 0.99. P(+|D) = 0.95, P(+|H) = 0.05. Total P(+) = P(D)P(+|D) + P(H)P(+|H) = (0.01 × 0.95) + (0.99 × 0.05) = 0.0095 + 0.0495 = 0.0590. P(D|+) = 0.0095 / 0.0590 = 95 / 590 = 19 / 118 ≈ 16.1%.",
        "formula": "Bayes' Rule: P(D|+) = 0.0095 / 0.0590 = 19 / 118 ≈ 16.1%"
    },
    {
        "id": "prob-36",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "A coin is tossed until a Head appears for the first time. What is the probability that the coin is tossed an odd number of times (1st, 3rd, 5th... toss)?",
        "options": [
            {
                "id": "A",
                "text": "2/3"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "3/4"
            },
            {
                "id": "D",
                "text": "1/3"
            }
        ],
        "correct_answer": "A",
        "explanation": "First head on 1st toss = 1/2. On 3rd toss = (1/2)^3 = 1/8. On 5th toss = (1/2)^5 = 1/32. This forms an infinite geometric series with first term a = 1/2 and common ratio r = (1/2)^2 = 1/4. Sum = a / (1 - r) = (1/2) / (1 - 1/4) = (1/2) / (3/4) = 2/3.",
        "formula": "Sum of Infinite GP: S = a / (1 - r) = (1/2) / (3/4) = 2/3"
    },
    {
        "id": "prob-37",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "A box contains 3 fair coins and 1 two-headed coin (heads on both sides). A coin is chosen at random and tossed twice. If it shows Heads on both tosses, what is the probability that it was the two-headed coin?",
        "options": [
            {
                "id": "A",
                "text": "4/7"
            },
            {
                "id": "B",
                "text": "1/4"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "3/7"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(Fair) = 3/4, P(2-Head) = 1/4. P(HH|Fair) = (1/2)^2 = 1/4. P(HH|2-Head) = 1^2 = 1. Total P(HH) = (3/4 × 1/4) + (1/4 × 1) = 3/16 + 4/16 = 7/16. Posterior P(2-Head|HH) = (1/4 × 1) / (7/16) = (4/16) / (7/16) = 4/7.",
        "formula": "Bayes' Rule: P(2-Head|HH) = (1/4) / (7/16) = 4/7"
    },
    {
        "id": "prob-38",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "Three hunters A, B, and C aim at a target simultaneously. Their probabilities of hitting the target are 1/2, 2/3, and 3/4 respectively. What is the probability that exactly two of them hit the target?",
        "options": [
            {
                "id": "A",
                "text": "11/24"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "7/24"
            },
            {
                "id": "D",
                "text": "3/8"
            }
        ],
        "correct_answer": "A",
        "explanation": "Probabilities of hitting: pA = 1/2, pB = 2/3, pC = 3/4. Missing: qA = 1/2, qB = 1/3, qC = 1/4. Case 1 (A, B hit; C misses): (1/2) × (2/3) × (1/4) = 2/24. Case 2 (A, C hit; B misses): (1/2) × (1/3) × (3/4) = 3/24. Case 3 (B, C hit; A misses): (1/2) × (2/3) × (3/4) = 6/24. Total probability = 2/24 + 3/24 + 6/24 = 11/24.",
        "formula": "P(Exactly 2) = pA*pB*qC + pA*qB*pC + qA*pB*pC = (2 + 3 + 6)/24 = 11/24"
    },
    {
        "id": "prob-39",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "An urn contains 5 red and 5 black balls. A ball is drawn at random, its color is noted, and it is returned to the urn along with 2 additional balls of the same color. What is the probability that the second ball drawn is red?",
        "options": [
            {
                "id": "A",
                "text": "1/2"
            },
            {
                "id": "B",
                "text": "5/12"
            },
            {
                "id": "C",
                "text": "7/12"
            },
            {
                "id": "D",
                "text": "1/3"
            }
        ],
        "correct_answer": "A",
        "explanation": "Case 1: First ball was red (prob = 5/10 = 1/2). Two red balls added, so urn has 7 red and 5 black (12 total). Prob second is red = 7/12. Joint prob = 1/2 × 7/12 = 7/24. Case 2: First ball was black (prob = 5/10 = 1/2). Two black balls added, so urn has 5 red and 7 black (12 total). Prob second is red = 5/12. Joint prob = 1/2 × 5/12 = 5/24. Total probability = 7/24 + 5/24 = 12/24 = 1/2. (This is a classic Polya's Urn invariant property).",
        "formula": "Polya's Urn Invariant: P(R2) = P(R1) = 5/10 = 1/2"
    },
    {
        "id": "prob-40",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "If 4 distinct letters are placed at random into 4 addressed envelopes, what is the probability of a complete derangement (i.e., that NO letter goes into its correct envelope)?",
        "options": [
            {
                "id": "A",
                "text": "3/8"
            },
            {
                "id": "B",
                "text": "1/3"
            },
            {
                "id": "C",
                "text": "11/24"
            },
            {
                "id": "D",
                "text": "1/4"
            }
        ],
        "correct_answer": "A",
        "explanation": "The number of derangements of n objects is !n = n! × [1 - 1/1! + 1/2! - 1/3! + ... + (-1)^n/n!]. For n = 4: !4 = 4! × (1/2 - 1/6 + 1/24) = 24 × (12 - 4 + 1)/24 = 9. Total permutations = 4! = 24. Probability = 9 / 24 = 3 / 8 = 0.375.",
        "formula": "Derangement Probability: P(!4) = !4 / 4! = 9 / 24 = 3/8"
    },
    {
        "id": "prob-41",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "In a game of rolling a fair die, Player X rolls first. Players X and Y take turns rolling the die. The first player to roll a '6' wins the game. What is the probability that Player X wins?",
        "options": [
            {
                "id": "A",
                "text": "6/11"
            },
            {
                "id": "B",
                "text": "5/11"
            },
            {
                "id": "C",
                "text": "1/2"
            },
            {
                "id": "D",
                "text": "7/12"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(rolling 6) = p = 1/6; P(not 6) = q = 5/6. Player X wins on roll 1, 3, 5, ... X wins on roll 1: 1/6. X wins on roll 3: (5/6)^2 × (1/6). X wins on roll 5: (5/6)^4 × (1/6). Infinite GP with a = 1/6, r = (5/6)^2 = 25/36. Sum = a / (1 - r) = (1/6) / (1 - 25/36) = (1/6) / (11/36) = (1/6) × (36/11) = 6/11.",
        "formula": "First-Player Advantage: P(X wins) = p / [1 - (1-p)^2] = (1/6) / (11/36) = 6/11"
    },
    {
        "id": "prob-42",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "A random variable X follows a Binomial distribution B(n=5, p=1/3). What is the probability of obtaining at least 4 successes?",
        "options": [
            {
                "id": "A",
                "text": "11 / 243"
            },
            {
                "id": "B",
                "text": "10 / 243"
            },
            {
                "id": "C",
                "text": "1 / 81"
            },
            {
                "id": "D",
                "text": "13 / 243"
            }
        ],
        "correct_answer": "A",
        "explanation": "P(X >= 4) = P(X = 4) + P(X = 5). P(X = 4) = C(5, 4) × (1/3)^4 × (2/3)^1 = 5 × (1/81) × (2/3) = 10 / 243. P(X = 5) = C(5, 5) × (1/3)^5 × (2/3)^0 = 1 × 1 / 243 = 1 / 243. P(X >= 4) = 10/243 + 1/243 = 11 / 243.",
        "formula": "Binomial: P(X >= 4) = C(5,4)(1/3)^4(2/3) + C(5,5)(1/3)^5 = 11/243"
    },
    {
        "id": "prob-43",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "A committee of 4 people is selected at random from 6 men and 4 women. Given that at least one woman is chosen, what is the conditional probability that exactly two women are chosen?",
        "options": [
            {
                "id": "A",
                "text": "90/195 (6/13)"
            },
            {
                "id": "B",
                "text": "1/2"
            },
            {
                "id": "C",
                "text": "45/195 (3/13)"
            },
            {
                "id": "D",
                "text": "8/15"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total ways to choose 4 from 10 = C(10, 4) = 210. Ways with no women (all men) = C(6, 4) = 15. Ways with at least one woman = 210 - 15 = 195. Ways to choose exactly 2 women (and 2 men) = C(4, 2) × C(6, 2) = 6 × 15 = 90. Conditional probability = 90 / 195 = 6 / 13.",
        "formula": "Conditional Probability: P(2W | >=1W) = C(4,2)C(6,2) / [C(10,4) - C(6,4)] = 90 / 195 = 6/13"
    },
    {
        "id": "prob-44",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "Two numbers a and b are chosen at random from the set {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} with replacement. What is the probability that their product (a × b) is an even number?",
        "options": [
            {
                "id": "A",
                "text": "3/4 (75%)"
            },
            {
                "id": "B",
                "text": "1/2 (50%)"
            },
            {
                "id": "C",
                "text": "1/4 (25%)"
            },
            {
                "id": "D",
                "text": "2/3 (66.7%)"
            }
        ],
        "correct_answer": "A",
        "explanation": "The product (a × b) is odd if and only if both a and b are odd. In the set, there are 5 odd numbers {1, 3, 5, 7, 9} and 5 even numbers {2, 4, 6, 8, 10}. Probability that a is odd = 5/10 = 1/2. Probability that b is odd = 5/10 = 1/2. P(Product is odd) = 1/2 × 1/2 = 1/4. P(Product is even) = 1 - 1/4 = 3/4 (75%).",
        "formula": "P(Even Product) = 1 - P(Both Odd) = 1 - (1/2 × 1/2) = 3/4"
    },
    {
        "id": "prob-45",
        "topic": "Probability",
        "difficulty": "Hard",
        "question": "A 10-cm long stick is broken into two pieces at a uniformly random point along its length. What is the probability that the longer piece is at least 3 times as long as the shorter piece?",
        "options": [
            {
                "id": "A",
                "text": "1/2 (50%)"
            },
            {
                "id": "B",
                "text": "1/3 (33.3%)"
            },
            {
                "id": "C",
                "text": "1/4 (25%)"
            },
            {
                "id": "D",
                "text": "2/3 (66.7%)"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let the break point be x in [0, 10]. Shorter piece <= 10/4 = 2.5 cm. This occurs if x is in [0, 2.5] (shorter piece on left) or in [7.5, 10] (shorter piece on right). Total favorable length = (2.5 - 0) + (10 - 7.5) = 2.5 + 2.5 = 5.0 cm. Probability = 5.0 / 10 = 1/2 (50%).",
        "formula": "Geometric Probability: Favorable Interval Length / Total Length = (2.5 + 2.5) / 10 = 1/2"
    }
]
