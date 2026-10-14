# -*- coding: utf-8 -*-
"""
Time and Work Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

TIME_AND_WORK_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "tw-1",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A can finish a task in 10 days, while B can finish the same task in 15 days. How many days will they take working together?",
        "options": [
            {
                "id": "A",
                "text": "5 days"
            },
            {
                "id": "B",
                "text": "6 days"
            },
            {
                "id": "C",
                "text": "7.5 days"
            },
            {
                "id": "D",
                "text": "8 days"
            }
        ],
        "correct_answer": "B",
        "explanation": "Combined efficiency = (1/10) + (1/15) = (3 + 2)/30 = 5/30 = 1/6 of total work per day. Hence, together they take 6 days.",
        "formula": "Combined Time = (A × B) / (A + B) = (10 × 15) / 25 = 150 / 25 = 6 days"
    },
    {
        "id": "tw-2",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A and B together can do a job in 8 days. If A alone can do it in 12 days, in how many days can B do it alone?",
        "options": [
            {
                "id": "A",
                "text": "16 days"
            },
            {
                "id": "B",
                "text": "20 days"
            },
            {
                "id": "C",
                "text": "24 days"
            },
            {
                "id": "D",
                "text": "28 days"
            }
        ],
        "correct_answer": "C",
        "explanation": "B's 1-day work = (1/Combined) - (1/A) = (1/8) - (1/12) = (3 - 2)/24 = 1/24. Thus B alone takes 24 days.",
        "formula": "B's Time = (Combined × A) / (A - Combined) = (8 × 12) / (12 - 8) = 96 / 4 = 24 days"
    },
    {
        "id": "tw-7",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A can complete a piece of work in 10 days and B can do the same work in 15 days. How many days will they take to complete the work together?",
        "options": [
            {
                "id": "A",
                "text": "6 days"
            },
            {
                "id": "B",
                "text": "5 days"
            },
            {
                "id": "C",
                "text": "7.5 days"
            },
            {
                "id": "D",
                "text": "8 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Combined 1-day work = 1/10 + 1/15 = (3 + 2)/30 = 5/30 = 1/6. Therefore, together they will finish the work in 6 days.",
        "formula": "Time = (A × B) / (A + B) = (10 × 15) / 25 = 6 days"
    },
    {
        "id": "tw-8",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A is twice as efficient as B. If B can complete a piece of work alone in 18 days, in how many days can A complete it alone?",
        "options": [
            {
                "id": "A",
                "text": "9 days"
            },
            {
                "id": "B",
                "text": "12 days"
            },
            {
                "id": "C",
                "text": "36 days"
            },
            {
                "id": "D",
                "text": "6 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Since A is twice as efficient as B, A takes half the time B takes. Time taken by A = 18 / 2 = 9 days.",
        "formula": "Time is inversely proportional to Efficiency: Time_A = Time_B / Ratio"
    },
    {
        "id": "tw-9",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "If 12 men can build a wall in 20 days, how many days will 15 men take to build the same wall working at the same pace?",
        "options": [
            {
                "id": "A",
                "text": "16 days"
            },
            {
                "id": "B",
                "text": "18 days"
            },
            {
                "id": "C",
                "text": "15 days"
            },
            {
                "id": "D",
                "text": "14 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = Men × Days = 12 × 20 = 240 man-days. Days required by 15 men = 240 / 15 = 16 days.",
        "formula": "M1 × D1 = M2 × D2 => D2 = (12 × 20) / 15 = 16"
    },
    {
        "id": "tw-10",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "Pipe A can fill a tank in 6 hours and Pipe B can empty it in 9 hours. If both pipes are opened together, how many hours will it take to fill the tank?",
        "options": [
            {
                "id": "A",
                "text": "18 hours"
            },
            {
                "id": "B",
                "text": "15 hours"
            },
            {
                "id": "C",
                "text": "12 hours"
            },
            {
                "id": "D",
                "text": "24 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net rate per hour = 1/6 - 1/9 = (3 - 2)/18 = 1/18. Therefore, the empty tank will be filled in 18 hours.",
        "formula": "Net Rate = 1/Fill - 1/Empty => Time = (A × B) / (B - A) = (6 × 9) / 3 = 18 hours"
    },
    {
        "id": "tw-11",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A, B, and C can complete a task in 12, 15, and 20 days respectively. How many days will they take working all together?",
        "options": [
            {
                "id": "A",
                "text": "5 days"
            },
            {
                "id": "B",
                "text": "6 days"
            },
            {
                "id": "C",
                "text": "4 days"
            },
            {
                "id": "D",
                "text": "7 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Combined 1-day rate = 1/12 + 1/15 + 1/20. LCM(12, 15, 20) = 60. Rate = (5 + 4 + 3)/60 = 12/60 = 1/5. Thus, they will complete the task together in 5 days.",
        "formula": "Time = 1 / (1/A + 1/B + 1/C) = 60 / 12 = 5 days"
    },
    {
        "id": "tw-12",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A and B working together can do a work in 8 days. If A alone can do it in 12 days, how many days will B take to complete it alone?",
        "options": [
            {
                "id": "A",
                "text": "24 days"
            },
            {
                "id": "B",
                "text": "20 days"
            },
            {
                "id": "C",
                "text": "16 days"
            },
            {
                "id": "D",
                "text": "18 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "B's 1-day work = (A + B)'s rate - A's rate = 1/8 - 1/12 = (3 - 2)/24 = 1/24. Therefore, B alone takes 24 days.",
        "formula": "B = (AB × A) / (A - AB) = (8 × 12) / 4 = 24 days"
    },
    {
        "id": "tw-13",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "If 8 workers can manufacture 160 units in 5 days, how many units can 12 workers manufacture in 3 days at the same rate?",
        "options": [
            {
                "id": "A",
                "text": "144 units"
            },
            {
                "id": "B",
                "text": "150 units"
            },
            {
                "id": "C",
                "text": "160 units"
            },
            {
                "id": "D",
                "text": "136 units"
            }
        ],
        "correct_answer": "A",
        "explanation": "Rate per worker per day = 160 / (8 × 5) = 160 / 40 = 4 units/day. For 12 workers in 3 days: 12 × 3 × 4 = 144 units.",
        "formula": "Units = M2 × D2 × (W1 / (M1 × D1)) = 12 × 3 × 4 = 144 units"
    },
    {
        "id": "tw-14",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "Ravi can do 1/4 of a work in 5 days. In how many days can he finish the entire work?",
        "options": [
            {
                "id": "A",
                "text": "20 days"
            },
            {
                "id": "B",
                "text": "15 days"
            },
            {
                "id": "C",
                "text": "25 days"
            },
            {
                "id": "D",
                "text": "10 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total days = Days for fractional part ÷ Fraction = 5 ÷ (1/4) = 5 × 4 = 20 days.",
        "formula": "Total Days = Days / Fraction"
    },
    {
        "id": "tw-15",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "Two taps P and Q can fill an overhead tank in 10 hours and 15 hours respectively. If both are turned on simultaneously, how long does it take to fill the tank?",
        "options": [
            {
                "id": "A",
                "text": "6 hours"
            },
            {
                "id": "B",
                "text": "5 hours"
            },
            {
                "id": "C",
                "text": "7.5 hours"
            },
            {
                "id": "D",
                "text": "8 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "1-hour combined filling rate = 1/10 + 1/15 = 5/30 = 1/6. The tank will be full in 6 hours.",
        "formula": "Time = (P × Q) / (P + Q) = (10 × 15) / 25 = 6 hours"
    },
    {
        "id": "tw-16",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A can copy 75 pages in 15 hours. A and B together can copy 135 pages in 15 hours. In how many hours can B copy 40 pages alone?",
        "options": [
            {
                "id": "A",
                "text": "10 hours"
            },
            {
                "id": "B",
                "text": "12 hours"
            },
            {
                "id": "C",
                "text": "8 hours"
            },
            {
                "id": "D",
                "text": "15 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "A's speed = 75 / 15 = 5 pages/hour. Combined speed of A and B = 135 / 15 = 9 pages/hour. B's speed = 9 - 5 = 4 pages/hour. Time taken by B to copy 40 pages = 40 / 4 = 10 hours.",
        "formula": "Time = Required Pages / Rate_B"
    },
    {
        "id": "tw-17",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A alone can paint a house in 20 days and B alone can paint it in 30 days. They work together and are paid ₹1,500. What is A's share of the payment?",
        "options": [
            {
                "id": "A",
                "text": "₹900"
            },
            {
                "id": "B",
                "text": "₹600"
            },
            {
                "id": "C",
                "text": "₹750"
            },
            {
                "id": "D",
                "text": "₹1,000"
            }
        ],
        "correct_answer": "A",
        "explanation": "Wages are distributed in proportion to individual daily work efficiencies: A's efficiency : B's efficiency = 1/20 : 1/30 = 3 : 2. A's share = 3/(3 + 2) × 1500 = 3/5 × 1500 = ₹900.",
        "formula": "Wage Share = Total Wage × (Efficiency_A / Total Efficiency)"
    },
    {
        "id": "tw-18",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "15 laborers can dig a trench in 8 days. How many laborers are needed to dig the same trench in 6 days?",
        "options": [
            {
                "id": "A",
                "text": "20 laborers"
            },
            {
                "id": "B",
                "text": "18 laborers"
            },
            {
                "id": "C",
                "text": "24 laborers"
            },
            {
                "id": "D",
                "text": "16 laborers"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total labor = 15 × 8 = 120 man-days. Number of laborers needed for 6 days = 120 / 6 = 20 laborers.",
        "formula": "M2 = (M1 × D1) / D2 = (15 × 8) / 6 = 20"
    },
    {
        "id": "tw-19",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "question": "A person can weed a garden in 6 hours. With the help of his son, he can weed it in 4 hours. How long would the son take to weed it alone?",
        "options": [
            {
                "id": "A",
                "text": "12 hours"
            },
            {
                "id": "B",
                "text": "10 hours"
            },
            {
                "id": "C",
                "text": "8 hours"
            },
            {
                "id": "D",
                "text": "14 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "Son's rate = 1/4 - 1/6 = (3 - 2)/12 = 1/12. The son alone takes 12 hours.",
        "formula": "Time = (4 × 6) / (6 - 4) = 24 / 2 = 12 hours"
    },
    {
        "id": "tw-3",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A is twice as efficient as B and therefore is able to finish a job in 30 days less than B. Working together, in how many days can they complete the job?",
        "options": [
            {
                "id": "A",
                "text": "18 days"
            },
            {
                "id": "B",
                "text": "20 days"
            },
            {
                "id": "C",
                "text": "22 days"
            },
            {
                "id": "D",
                "text": "25 days"
            }
        ],
        "correct_answer": "B",
        "explanation": "Ratio of efficiencies of A : B = 2 : 1, so ratio of times taken = 1 : 2. Difference in time = 2x - x = x = 30 days. Hence A takes 30 days and B takes 60 days. Together: (30 × 60) / (30 + 60) = 1800 / 90 = 20 days.",
        "formula": "Combined Time = (Time_A × Time_B) / (Time_A + Time_B)"
    },
    {
        "id": "tw-4",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "12 men can complete a project in 16 days. How many men are required to complete the same project in 24 days?",
        "options": [
            {
                "id": "A",
                "text": "6 men"
            },
            {
                "id": "B",
                "text": "8 men"
            },
            {
                "id": "C",
                "text": "10 men"
            },
            {
                "id": "D",
                "text": "14 men"
            }
        ],
        "correct_answer": "B",
        "explanation": "Using Men × Days formula: M1 × D1 = M2 × D2 => 12 × 16 = M2 × 24 => 192 = 24 × M2 => M2 = 192 / 24 = 8 men.",
        "formula": "M1 × D1 × H1 / W1 = M2 × D2 × H2 / W2"
    },
    {
        "id": "tw-20",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A can do a piece of work in 14 days and B in 21 days. They begin together, but 3 days before the completion of the work, A leaves off. What is the total number of days to complete the work?",
        "options": [
            {
                "id": "A",
                "text": "10.2 days (51/5 days)"
            },
            {
                "id": "B",
                "text": "9 days"
            },
            {
                "id": "C",
                "text": "12 days"
            },
            {
                "id": "D",
                "text": "11 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(14, 21) = 42 units. A's rate = 3 units/day, B's rate = 2 units/day. In the last 3 days, only B worked, completing 3 × 2 = 6 units. Remaining work = 42 - 6 = 36 units. Days worked together = 36 / (3 + 2) = 36 / 5 = 7.2 days. Total time = 7.2 + 3 = 10.2 days (51/5 days).",
        "formula": "Total Days = ((Total Work - Work done by B alone) / (Rate_A + Rate_B)) + 3"
    },
    {
        "id": "tw-21",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A and B can do a work in 8 days and 12 days respectively. They work on alternate days starting with A. In how many days will the entire work be completed?",
        "options": [
            {
                "id": "A",
                "text": "9.5 days (19/2 days)"
            },
            {
                "id": "B",
                "text": "10 days"
            },
            {
                "id": "C",
                "text": "9 days"
            },
            {
                "id": "D",
                "text": "8.5 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(8, 12) = 24 units. A's rate = 3 units/day, B's rate = 2 units/day. In a 2-day cycle: A + B = 3 + 2 = 5 units. In 4 cycles (8 days): 4 × 5 = 20 units. Remaining work = 24 - 20 = 4 units. On Day 9, A works and does 3 units, leaving 1 unit. On Day 10, B works and does 1 unit in 1/2 day. Total time = 8 + 1 + 0.5 = 9.5 days.",
        "formula": "Alternate day cycles: Total Time = Complete cycles × 2 + fractional days"
    },
    {
        "id": "tw-22",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "3 men or 5 women can cultivate a field in 43 days. How many days will 5 men and 6 women take to cultivate the same field?",
        "options": [
            {
                "id": "A",
                "text": "15 days"
            },
            {
                "id": "B",
                "text": "18 days"
            },
            {
                "id": "C",
                "text": "12 days"
            },
            {
                "id": "D",
                "text": "20 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "3 Men = 5 Women => 1 Man = 5/3 Women. 5 Men + 6 Women = 5 × (5/3) + 6 = 25/3 + 18/3 = 43/3 Women. Since 5 Women take 43 days: Time = (5 × 43) / (43/3) = 5 × 3 = 15 days.",
        "formula": "Equivalence: Time = (W1 × D1) / Equivalent Women = (5 × 43) / (43/3) = 15 days"
    },
    {
        "id": "tw-23",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A cistern has two filling pipes A and B which can fill it in 12 hours and 15 hours respectively, and an emptying tap C which can empty it in 20 hours. If all three are opened together, how long does it take to fill the cistern?",
        "options": [
            {
                "id": "A",
                "text": "10 hours"
            },
            {
                "id": "B",
                "text": "8 hours"
            },
            {
                "id": "C",
                "text": "12 hours"
            },
            {
                "id": "D",
                "text": "9 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net rate per hour = 1/12 + 1/15 - 1/20. LCM(12, 15, 20) = 60. Rate = (5 + 4 - 3)/60 = 6/60 = 1/10. Thus, the cistern fills in 10 hours.",
        "formula": "Time = 1 / (1/A + 1/B - 1/C) = 60 / 6 = 10 hours"
    },
    {
        "id": "tw-24",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A and B can do a work in 18 days, B and C in 24 days, and A and C in 36 days. In how many days can A, B, and C complete it working together?",
        "options": [
            {
                "id": "A",
                "text": "16 days"
            },
            {
                "id": "B",
                "text": "18 days"
            },
            {
                "id": "C",
                "text": "14 days"
            },
            {
                "id": "D",
                "text": "20 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "2 × (A + B + C)'s daily rate = 1/18 + 1/24 + 1/36. LCM(18, 24, 36) = 72. Sum = (4 + 3 + 2)/72 = 9/72 = 1/8. Therefore, (A + B + C)'s daily rate = (1/8) / 2 = 1/16. Together they finish in 16 days.",
        "formula": "Rate(A+B+C) = 0.5 × [Rate(AB) + Rate(BC) + Rate(AC)] = 1/16"
    },
    {
        "id": "tw-25",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A is 3 times as efficient as B and therefore is able to finish a job in 60 days less than B. Working together, in how many days can they do it?",
        "options": [
            {
                "id": "A",
                "text": "22.5 days (45/2 days)"
            },
            {
                "id": "B",
                "text": "20 days"
            },
            {
                "id": "C",
                "text": "25 days"
            },
            {
                "id": "D",
                "text": "18 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Ratio of times = 1 : 3. Difference = 3x - x = 2x = 60 days => x = 30 days. So A takes 30 days and B takes 90 days. Together: (30 × 90) / (30 + 90) = 2700 / 120 = 22.5 days (45/2 days).",
        "formula": "Time = (x × 3x) / 4x = (3/4)x = (3/4) × 30 = 22.5 days"
    },
    {
        "id": "tw-26",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A contractor undertook to complete a road in 40 days and engaged 25 men. After 24 days, only 1/3 of the work was completed. How many additional men must be employed to finish the project on time?",
        "options": [
            {
                "id": "A",
                "text": "50 additional men"
            },
            {
                "id": "B",
                "text": "45 additional men"
            },
            {
                "id": "C",
                "text": "40 additional men"
            },
            {
                "id": "D",
                "text": "75 additional men"
            }
        ],
        "correct_answer": "A",
        "explanation": "Work done = 1/3 in 24 days by 25 men: M1 × D1 / W1 = (25 × 24) / (1/3) = 600 × 3 = 1800. Remaining work = 2/3 in remaining 40 - 24 = 16 days. Let total men be M2: (M2 × 16) / (2/3) = 1800 => M2 × 24 = 1800 => M2 = 75 men. Additional men required = 75 - 25 = 50 men.",
        "formula": "(M1 × D1) / W1 = (M2 × D2) / W2"
    },
    {
        "id": "tw-27",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "Two pipes can fill a cistern in 14 hours and 16 hours respectively. They are opened together, but due to a leak at the bottom, it took 32 minutes longer to fill the cistern. In what time can the leak empty the full cistern?",
        "options": [
            {
                "id": "A",
                "text": "112 hours"
            },
            {
                "id": "B",
                "text": "100 hours"
            },
            {
                "id": "C",
                "text": "96 hours"
            },
            {
                "id": "D",
                "text": "120 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "Normal filling time = (14 × 16) / 30 = 224 / 30 = 112 / 15 hours = 7 hours 28 minutes. With leak, time taken = 7 hours 28 min + 32 min = 8 hours. Leak's emptying rate = 1/(112/15) - 1/8 = 15/112 - 14/112 = 1/112. Hence the leak alone can empty the cistern in 112 hours.",
        "formula": "Rate_Leak = Rate_Normal - Rate_WithLeak = 15/112 - 1/8 = 1/112"
    },
    {
        "id": "tw-28",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A and B can do a work in 45 and 40 days respectively. They began the work together, but A left after some days and B finished the remaining work in 23 days. After how many days did A leave?",
        "options": [
            {
                "id": "A",
                "text": "9 days"
            },
            {
                "id": "B",
                "text": "8 days"
            },
            {
                "id": "C",
                "text": "10 days"
            },
            {
                "id": "D",
                "text": "12 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(45, 40) = 360 units. A's rate = 8 units/day, B's rate = 9 units/day. Work done by B alone in last 23 days = 23 × 9 = 207 units. Remaining work done by A and B together = 360 - 207 = 153 units. Days worked together = 153 / (8 + 9) = 153 / 17 = 9 days. Thus, A left after 9 days.",
        "formula": "Days = (Total Work - B_alone_work) / (Rate_A + Rate_B) = 153 / 17 = 9 days"
    },
    {
        "id": "tw-29",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A can finish a work in 18 days and B can do the same work in 15 days. B worked for 10 days and then left the job. In how many days can A alone finish the remaining work?",
        "options": [
            {
                "id": "A",
                "text": "6 days"
            },
            {
                "id": "B",
                "text": "5 days"
            },
            {
                "id": "C",
                "text": "8 days"
            },
            {
                "id": "D",
                "text": "7 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(18, 15) = 90 units. A's rate = 5 units/day, B's rate = 6 units/day. Work done by B in 10 days = 10 × 6 = 60 units. Remaining work = 90 - 60 = 30 units. Days taken by A = 30 / 5 = 6 days.",
        "formula": "Remaining Days = Remaining Work / Rate_A = 30 / 5 = 6 days"
    },
    {
        "id": "tw-30",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A, B, and C can complete a work in 10, 20, and 30 days respectively. They all start together, but A leaves after 2 days and B leaves after another 2 days. In how many more days will C complete the work?",
        "options": [
            {
                "id": "A",
                "text": "14 days"
            },
            {
                "id": "B",
                "text": "12 days"
            },
            {
                "id": "C",
                "text": "16 days"
            },
            {
                "id": "D",
                "text": "10 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(10, 20, 30) = 60 units. Rates: A=6, B=3, C=2 units/day. First 2 days (A+B+C): 2 × (6+3+2) = 22 units. Next 2 days (B+C): 2 × (3+2) = 10 units. Total done = 32 units. Remaining work = 60 - 32 = 28 units. Days taken by C alone = 28 / 2 = 14 days.",
        "formula": "Remaining Time = (Total - Work_done) / Rate_C = 28 / 2 = 14 days"
    },
    {
        "id": "tw-31",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "2 men and 3 boys can do a piece of work in 10 days, while 3 men and 2 boys can do the same work in 8 days. In how many days can 2 men and 1 boy do the work?",
        "options": [
            {
                "id": "A",
                "text": "12.5 days (25/2 days)"
            },
            {
                "id": "B",
                "text": "12 days"
            },
            {
                "id": "C",
                "text": "15 days"
            },
            {
                "id": "D",
                "text": "10 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "10 × (2M + 3B) = 8 × (3M + 2B) => 20M + 30B = 24M + 16B => 4M = 14B => 1M = 3.5B (7/2 B). Total work = 10 × (2 × 3.5B + 3B) = 10 × 10B = 100 boy-days. 2 men and 1 boy = 2 × 3.5B + 1B = 8B. Time taken = 100 / 8 = 12.5 days (25/2 days).",
        "formula": "Equivalence: 1M = 3.5B => Total Work / Effective Capacity = 100 / 8 = 12.5 days"
    },
    {
        "id": "tw-32",
        "topic": "Time and Work",
        "difficulty": "Medium",
        "question": "A and B undertake to do a piece of work for ₹4,800. A alone can do it in 16 days, B in 24 days. With the help of C, they complete it in 8 days. What is C's share of the money?",
        "options": [
            {
                "id": "A",
                "text": "₹800"
            },
            {
                "id": "B",
                "text": "₹1,200"
            },
            {
                "id": "C",
                "text": "₹600"
            },
            {
                "id": "D",
                "text": "₹1,000"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(16, 24, 8) = 48 units. A's rate = 3 units/day; B's rate = 2 units/day; Combined (A+B+C)'s rate = 6 units/day. C's rate = 6 - (3 + 2) = 1 unit/day. Ratio of efficiencies = 3 : 2 : 1. C's share = 1/(3+2+1) × 4800 = 1/6 × 4800 = ₹800.",
        "formula": "C's Share = Total Wage × (Rate_C / Rate_Total) = 4800 × (1/6) = ₹800"
    },
    {
        "id": "tw-5",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "Pipe A can fill a tank in 12 hours, Pipe B in 15 hours, and Pipe C can empty it in 20 hours. If all three pipes are opened together, how long does it take to fill the tank?",
        "options": [
            {
                "id": "A",
                "text": "8 hours"
            },
            {
                "id": "B",
                "text": "10 hours"
            },
            {
                "id": "C",
                "text": "12 hours"
            },
            {
                "id": "D",
                "text": "14 hours"
            }
        ],
        "correct_answer": "B",
        "explanation": "LCM(12, 15, 20) = 60 units capacity. Pipe A adds +5 units/hr, Pipe B adds +4 units/hr, Pipe C removes -3 units/hr. Net filling rate = 5 + 4 - 3 = 6 units/hr. Total time = 60 / 6 = 10 hours.",
        "formula": "Net Rate = 1/A + 1/B - 1/C = 1/12 + 1/15 - 1/20 = 1/10"
    },
    {
        "id": "tw-6",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A, B, and C can complete a piece of work in 20, 30, and 60 days respectively. A is assisted by B and C on every third day. In how many days will the entire work be completed?",
        "options": [
            {
                "id": "A",
                "text": "12 days"
            },
            {
                "id": "B",
                "text": "15 days"
            },
            {
                "id": "C",
                "text": "16 days"
            },
            {
                "id": "D",
                "text": "18 days"
            }
        ],
        "correct_answer": "B",
        "explanation": "Total Work = LCM(20, 30, 60) = 60 units. A's rate = 3 units/day, B's rate = 2 units/day, C's rate = 1 unit/day. Day 1: A works alone = 3 units. Day 2: A works alone = 3 units. Day 3: A+B+C work together = 3 + 2 + 1 = 6 units. Total work in 3 days = 3 + 3 + 6 = 12 units. To complete 60 units: (60 / 12) × 3 days = 5 cycles × 3 days = 15 days.",
        "formula": "Cycle Method: Total Work / Work per Cycle × Cycle Duration"
    },
    {
        "id": "tw-33",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A, B, and C can do a job in 24, 36, and 48 days respectively. They started together, but C left after 4 days of starting, and A left 3 days before the completion of the work. For how many total days did the work last?",
        "options": [
            {
                "id": "A",
                "text": "15 days"
            },
            {
                "id": "B",
                "text": "16 days"
            },
            {
                "id": "C",
                "text": "18 days"
            },
            {
                "id": "D",
                "text": "14 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(24, 36, 48) = 144 units. Rates: A=6, B=4, C=3 units/day. Let total days be T. C worked 4 days: 4 × 3 = 12 units. A worked (T - 3) days: 6(T - 3) units. B worked all T days: 4T units. Equation: 12 + 6(T - 3) + 4T = 144 => 12 + 6T - 18 + 4T = 144 => 10T - 6 = 144 => 10T = 150 => T = 15 days.",
        "formula": "Work balance equation: Sum of individual work = Total Work"
    },
    {
        "id": "tw-34",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "Three pipes A, B, and C can fill an empty reservoir in 30, 20, and 10 minutes respectively. When the reservoir is completely empty, chemical solution X is introduced through pipe A, solution Y through B, and solution Z through C. If all pipes operate together for 3 minutes, what proportion of the liquid in the reservoir is chemical solution Y?",
        "options": [
            {
                "id": "A",
                "text": "3/11"
            },
            {
                "id": "B",
                "text": "2/11"
            },
            {
                "id": "C",
                "text": "6/11"
            },
            {
                "id": "D",
                "text": "1/3"
            }
        ],
        "correct_answer": "A",
        "explanation": "LCM(30, 20, 10) = 60 units. Rate of A = 2 units/min; Rate of B = 3 units/min; Rate of C = 6 units/min. Total rate = 2 + 3 + 6 = 11 units/min. Proportion contributed by pipe B (solution Y) is independent of time and equals Rate_B / Total_Rate = 3 / 11.",
        "formula": "Component Fraction = Rate_B / (Rate_A + Rate_B + Rate_C) = 3 / 11"
    },
    {
        "id": "tw-35",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "4 men and 6 women can complete a work in 8 days, while 3 men and 7 women can complete it in 10 days. In how many days will 10 women complete it working alone?",
        "options": [
            {
                "id": "A",
                "text": "40 days"
            },
            {
                "id": "B",
                "text": "35 days"
            },
            {
                "id": "C",
                "text": "45 days"
            },
            {
                "id": "D",
                "text": "50 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "8 × (4M + 6W) = 10 × (3M + 7W) => 32M + 48W = 30M + 70W => 2M = 22W => 1M = 11W. Total work = 8 × (4 × 11W + 6W) = 8 × (44W + 6W) = 8 × 50W = 400 woman-days. Time taken by 10 women = 400 / 10 = 40 days.",
        "formula": "Woman-Days equivalence: D = 400 / 10 = 40 days"
    },
    {
        "id": "tw-36",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A tank is fitted with 8 pipes. Some are filling pipes and the others are emptying pipes. Each filling pipe can fill the tank in 8 hours and each emptying pipe can empty it in 6 hours. When all 8 pipes are open, a full tank is completely emptied in 6 hours. How many filling pipes are there?",
        "options": [
            {
                "id": "A",
                "text": "4 filling pipes"
            },
            {
                "id": "B",
                "text": "3 filling pipes"
            },
            {
                "id": "C",
                "text": "5 filling pipes"
            },
            {
                "id": "D",
                "text": "2 filling pipes"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let n be the number of filling pipes, so (8 - n) are emptying pipes. Rate of a filling pipe = +1/8 per hour. Rate of an emptying pipe = -1/6 per hour. Net rate = -1/6 (empties full tank in 6 hours). Equation: n/8 - (8 - n)/6 = -1/6. Multiplying through by 24 gives: 3n - 4(8 - n) = -4 => 3n - 32 + 4n = -4 => 7n = 28 => n = 4 filling pipes.",
        "formula": "Pipe balance: n/Fill - (Total - n)/Empty = Net Rate"
    },
    {
        "id": "tw-37",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "Two workers A and B are assigned a job. A alone takes 9 hours more to complete the job than A and B together. B alone takes 4 hours more to complete the job than A and B together. How many hours do they take working together?",
        "options": [
            {
                "id": "A",
                "text": "6 hours"
            },
            {
                "id": "B",
                "text": "8 hours"
            },
            {
                "id": "C",
                "text": "5 hours"
            },
            {
                "id": "D",
                "text": "7.5 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "Standard theorem for joint work with excess times: If together they take T hours, A takes (T + a) and B takes (T + b), then T = sqrt(a × b). Here a = 9 and b = 4. T = sqrt(9 × 4) = sqrt(36) = 6 hours.",
        "formula": "Joint Time Formula: T = sqrt(a × b)"
    },
    {
        "id": "tw-38",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A can build a wall in 20 days, and B can destroy it in 30 days. They work on alternate days starting with A. On which day will the wall be completed for the first time?",
        "options": [
            {
                "id": "A",
                "text": "115th day"
            },
            {
                "id": "B",
                "text": "119th day"
            },
            {
                "id": "C",
                "text": "120th day"
            },
            {
                "id": "D",
                "text": "116th day"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(20, 30) = 60 units. A builds 3 units on Day 1, B destroys 2 units on Day 2. Net progress per 2-day cycle = 3 - 2 = 1 unit. Before the final cycle, A can build 3 units in 1 day, so we need 60 - 3 = 57 units built via full cycles. To achieve 57 units: 57 cycles = 57 × 2 = 114 days. On Day 115, A works and adds 3 units: 57 + 3 = 60 units, finishing the wall! Thus, completed on the 115th day.",
        "formula": "Alternate constructive/destructive cycle: Days = 2 × (Target - Final_Step) + 1 = 2 × 57 + 1 = 115"
    },
    {
        "id": "tw-39",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A and B together can do a piece of work in 12 days. B and C together can do it in 16 days. After A has been working at it for 5 days and B for 7 days, C finishes the remaining work in 13 days. In how many days could C alone do the entire work?",
        "options": [
            {
                "id": "A",
                "text": "24 days"
            },
            {
                "id": "B",
                "text": "20 days"
            },
            {
                "id": "C",
                "text": "18 days"
            },
            {
                "id": "D",
                "text": "30 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Group the work done: 5 days of (A + B) + 2 days of (B + C) + 11 days of C alone = Total Work (1). 5 × (1/12) + 2 × (1/16) + 11 × Rate_C = 1 => 5/12 + 1/8 + 11 × Rate_C = 1 => (10 + 3)/24 + 11 × Rate_C = 1 => 13/24 + 11 × Rate_C = 1 => 11 × Rate_C = 11/24 => Rate_C = 1/24. Therefore, C alone can finish the entire work in 24 days.",
        "formula": "Regrouping composite labor terms: 5(A+B) + 2(B+C) + 11C = 1 => C = 24 days"
    },
    {
        "id": "tw-40",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A team of 30 men is supposed to do a work in 38 days. After 25 days, 5 more men were employed and the work finished one day early. How many days behind schedule would the work have been if the additional men were not employed?",
        "options": [
            {
                "id": "A",
                "text": "1 day late"
            },
            {
                "id": "B",
                "text": "2 days late"
            },
            {
                "id": "C",
                "text": "On time"
            },
            {
                "id": "D",
                "text": "3 days late"
            }
        ],
        "correct_answer": "A",
        "explanation": "Work finished 1 day early = in 37 days. So the 35 men worked for 37 - 25 = 12 days. Total remaining work = 35 men × 12 days = 420 man-days. If only 30 men worked: time taken = 420 / 30 = 14 days. Total days taken = 25 + 14 = 39 days. Scheduled days = 38 days. Thus, it would have been 39 - 38 = 1 day behind schedule.",
        "formula": "Delay = (Remaining Man-Days / Original Men) - Scheduled remaining days = 14 - 13 = 1 day"
    },
    {
        "id": "tw-41",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "Pipe A and Pipe B can fill a cistern in 15 hours and 20 hours respectively, while Pipe C can empty it in 25 hours. All three pipes are opened in the beginning. After 10 hours, Pipe C is closed. In how much total time will the cistern be filled?",
        "options": [
            {
                "id": "A",
                "text": "12 hours"
            },
            {
                "id": "B",
                "text": "11.5 hours"
            },
            {
                "id": "C",
                "text": "13 hours"
            },
            {
                "id": "D",
                "text": "14 hours"
            }
        ],
        "correct_answer": "A",
        "explanation": "LCM(15, 20, 25) = 300 units. Rate A = +20, Rate B = +15, Rate C = -12. Combined rate with all three = 20 + 15 - 12 = 23 units/hr. Work done in first 10 hours = 10 × 23 = 230 units. Remaining work = 300 - 230 = 70 units. With C closed, filling rate of A and B = 20 + 15 = 35 units/hr. Time required for remaining = 70 / 35 = 2 hours. Total time = 10 + 2 = 12 hours.",
        "formula": "Total Time = Initial Duration + (Remaining Work / (Rate_A + Rate_B)) = 10 + 2 = 12 hours"
    },
    {
        "id": "tw-42",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A can do a work in 16 days and B in 12 days. With the help of C, they completed the work in 4 days. If the total payment of ₹4,800 is distributed according to work done, what is C's share?",
        "options": [
            {
                "id": "A",
                "text": "₹2,000"
            },
            {
                "id": "B",
                "text": "₹1,800"
            },
            {
                "id": "C",
                "text": "₹2,200"
            },
            {
                "id": "D",
                "text": "₹1,600"
            }
        ],
        "correct_answer": "A",
        "explanation": "In 4 days: A does 4/16 = 1/4 of the work. B does 4/12 = 1/3 of the work. Work done by C = 1 - (1/4 + 1/3) = 1 - 7/12 = 5/12 of the work. C's share of payment = 5/12 × ₹4,800 = 5 × 400 = ₹2,000.",
        "formula": "Payment = Total Payment × Fractional Work Done = 4800 × (5/12) = ₹2,000"
    },
    {
        "id": "tw-43",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "Working 8 hours a day, 15 men can build a monument in 21 days. How many days will 14 men working 6 hours a day take to build a monument 1.5 times as large?",
        "options": [
            {
                "id": "A",
                "text": "45 days"
            },
            {
                "id": "B",
                "text": "42 days"
            },
            {
                "id": "C",
                "text": "40 days"
            },
            {
                "id": "D",
                "text": "48 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Compound proportion: (M1 × D1 × H1) / W1 = (M2 × D2 × H2) / W2. (15 × 21 × 8) / 1 = (14 × D2 × 6) / 1.5 => 2520 = 56 × D2 => D2 = 2520 / 56 = 45 days.",
        "formula": "D2 = (M1 × D1 × H1 × W2) / (M2 × H2 × W1) = (15 × 21 × 8 × 1.5) / (14 × 6 × 1) = 45 days"
    },
    {
        "id": "tw-44",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A leak in the bottom of a tank can empty the full tank in 8 hours. An inlet pipe fills water at the rate of 6 liters a minute. When the tank is full, the inlet is opened and due to the leak, the tank is emptied in 12 hours. What is the capacity of the tank?",
        "options": [
            {
                "id": "A",
                "text": "8,640 liters"
            },
            {
                "id": "B",
                "text": "7,200 liters"
            },
            {
                "id": "C",
                "text": "9,600 liters"
            },
            {
                "id": "D",
                "text": "8,000 liters"
            }
        ],
        "correct_answer": "A",
        "explanation": "Work rate of inlet pipe = 1/8 - 1/12 = (3 - 2)/24 = 1/24 tank per hour. Therefore, the inlet pipe alone would fill the tank in 24 hours. Rate of inlet pipe = 6 liters/min = 6 × 60 = 360 liters/hour. Capacity = 24 hours × 360 liters/hour = 8,640 liters.",
        "formula": "Capacity = Filling Time × Volume Rate = 24 hr × 360 L/hr = 8,640 liters"
    },
    {
        "id": "tw-45",
        "topic": "Time and Work",
        "difficulty": "Hard",
        "question": "A, B, and C can complete a task in 20, 30, and 60 days respectively. In how many days can A do the work if he is assisted by B and C on every third day?",
        "options": [
            {
                "id": "A",
                "text": "15 days"
            },
            {
                "id": "B",
                "text": "12 days"
            },
            {
                "id": "C",
                "text": "16 days"
            },
            {
                "id": "D",
                "text": "18 days"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total work = LCM(20, 30, 60) = 60 units. Daily rates: A=3, B=2, C=1. Day 1: A works = 3 units. Day 2: A works = 3 units. Day 3: A+B+C work = 3+2+1 = 6 units. Total work in a 3-day cycle = 3 + 3 + 6 = 12 units. Number of cycles required = 60 / 12 = 5 cycles. Total days = 5 × 3 = 15 days.",
        "formula": "Cyclic work schedule: Total Time = Cycles × Cycle Length = 5 × 3 = 15 days"
    }
]
