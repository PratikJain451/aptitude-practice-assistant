# -*- coding: utf-8 -*-
"""
Percentages Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

PERCENTAGES_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "pct-1",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "If 20% of a number is equal to 45, what is 80% of that number?",
        "options": [
            {
                "id": "A",
                "text": "160"
            },
            {
                "id": "B",
                "text": "180"
            },
            {
                "id": "C",
                "text": "200"
            },
            {
                "id": "D",
                "text": "225"
            }
        ],
        "correct_answer": "B",
        "explanation": "Since 80% is exactly 4 times 20%, 80% of the number is 45 × 4 = 180.",
        "formula": "Direct Proportion: 80% = 4 × (20%) => 4 × 45 = 180"
    },
    {
        "id": "pct-2",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "A student scored 360 marks out of a maximum of 500. What is the student's percentage?",
        "options": [
            {
                "id": "A",
                "text": "70%"
            },
            {
                "id": "B",
                "text": "72%"
            },
            {
                "id": "C",
                "text": "74%"
            },
            {
                "id": "D",
                "text": "75%"
            }
        ],
        "correct_answer": "B",
        "explanation": "Percentage = (Obtained Marks / Total Marks) × 100 = (360 / 500) × 100 = 360 / 5 = 72%.",
        "formula": "Percentage = (Part / Whole) × 100"
    },
    {
        "id": "pct-7",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "What is 25% of 480?",
        "options": [
            {
                "id": "A",
                "text": "120"
            },
            {
                "id": "B",
                "text": "110"
            },
            {
                "id": "C",
                "text": "125"
            },
            {
                "id": "D",
                "text": "140"
            }
        ],
        "correct_answer": "A",
        "explanation": "25% of 480 = (25 / 100) × 480 = (1 / 4) × 480 = 120.",
        "formula": "Percentage Value = (P / 100) × Total"
    },
    {
        "id": "pct-8",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "A number increased by 20% becomes 180. What is the original number?",
        "options": [
            {
                "id": "A",
                "text": "150"
            },
            {
                "id": "B",
                "text": "144"
            },
            {
                "id": "C",
                "text": "160"
            },
            {
                "id": "D",
                "text": "135"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let the original number be N. N × 1.20 = 180 => N = 180 / 1.20 = 150.",
        "formula": "Original Number = New Value / (1 + Rate / 100)"
    },
    {
        "id": "pct-9",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "If A's salary is 25% more than B's salary, by what percentage is B's salary less than A's salary?",
        "options": [
            {
                "id": "A",
                "text": "20%"
            },
            {
                "id": "B",
                "text": "25%"
            },
            {
                "id": "C",
                "text": "16.67%"
            },
            {
                "id": "D",
                "text": "33.33%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let B's salary be 100. Then A's salary is 125. B's salary is less by 25. Percentage less = (25 / 125) × 100% = 1/5 × 100% = 20%.",
        "formula": "Percentage Decrease = [r / (100 + r)] × 100%"
    },
    {
        "id": "pct-10",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "In an examination, a candidate must secure 40% marks to pass. A student gets 175 marks and fails by 25 marks. What are the maximum aggregate marks?",
        "options": [
            {
                "id": "A",
                "text": "500"
            },
            {
                "id": "B",
                "text": "450"
            },
            {
                "id": "C",
                "text": "600"
            },
            {
                "id": "D",
                "text": "400"
            }
        ],
        "correct_answer": "A",
        "explanation": "Pass marks = 175 + 25 = 200 marks. 40% of Maximum Marks = 200 => Maximum Marks = 200 / 0.40 = 500.",
        "formula": "Maximum Marks = Pass Marks / Pass Percentage"
    },
    {
        "id": "pct-11",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "The price of sugar rises from ₹20 per kg to ₹25 per kg. What is the percentage increase in the price of sugar?",
        "options": [
            {
                "id": "A",
                "text": "25%"
            },
            {
                "id": "B",
                "text": "20%"
            },
            {
                "id": "C",
                "text": "30%"
            },
            {
                "id": "D",
                "text": "15%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Absolute increase = 25 - 20 = ₹5. Percentage increase = (Increase / Original Price) × 100% = (5 / 20) × 100% = 25%.",
        "formula": "Percentage Increase = (Change / Original) × 100%"
    },
    {
        "id": "pct-12",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "What is the single discount equivalent to two successive discounts of 20% and 10%?",
        "options": [
            {
                "id": "A",
                "text": "28%"
            },
            {
                "id": "B",
                "text": "30%"
            },
            {
                "id": "C",
                "text": "26%"
            },
            {
                "id": "D",
                "text": "32%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Formula for successive discounts d1 and d2: Single Discount = d1 + d2 - (d1 × d2)/100 = 20 + 10 - (20 × 10)/100 = 30 - 2 = 28%.",
        "formula": "Equivalent Discount = d1 + d2 - (d1 × d2)/100"
    },
    {
        "id": "pct-13",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "If 60% of students in a school of 1,200 pupils are boys, how many girls are there in the school?",
        "options": [
            {
                "id": "A",
                "text": "480"
            },
            {
                "id": "B",
                "text": "420"
            },
            {
                "id": "C",
                "text": "500"
            },
            {
                "id": "D",
                "text": "520"
            }
        ],
        "correct_answer": "A",
        "explanation": "Percentage of girls = 100% - 60% = 40%. Number of girls = 40% of 1,200 = 0.40 × 1,200 = 480.",
        "formula": "Number = (100 - Boy%)% × Total"
    },
    {
        "id": "pct-14",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "A fruit seller had some apples. He sells 40% of the apples and still has 420 apples left. How many apples did he have originally?",
        "options": [
            {
                "id": "A",
                "text": "700"
            },
            {
                "id": "B",
                "text": "650"
            },
            {
                "id": "C",
                "text": "720"
            },
            {
                "id": "D",
                "text": "800"
            }
        ],
        "correct_answer": "A",
        "explanation": "Remaining percentage = 100% - 40% = 60%. 60% of total apples = 420 => Total apples = 420 / 0.60 = 700.",
        "formula": "Original = Remaining / (1 - Fraction Sold)"
    },
    {
        "id": "pct-15",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "Convert the fraction 7/8 into a percentage.",
        "options": [
            {
                "id": "A",
                "text": "87.5%"
            },
            {
                "id": "B",
                "text": "85.0%"
            },
            {
                "id": "C",
                "text": "82.5%"
            },
            {
                "id": "D",
                "text": "90.0%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Percentage = (7 / 8) × 100% = 7 × 12.5% = 87.5%.",
        "formula": "Percentage = Fraction × 100%"
    },
    {
        "id": "pct-16",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "If the price of a commodity increases by 10% and then decreases by 10%, what is the net percentage change in price?",
        "options": [
            {
                "id": "A",
                "text": "1% decrease"
            },
            {
                "id": "B",
                "text": "No change (0%)"
            },
            {
                "id": "C",
                "text": "1% increase"
            },
            {
                "id": "D",
                "text": "2% decrease"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net effect = a + b + (ab/100). Here a = +10, b = -10. Net change = 10 - 10 + (10 × -10)/100 = 0 - 1 = -1%. Hence, a 1% net decrease.",
        "formula": "Net Change = a + b + (ab/100) = -1%"
    },
    {
        "id": "pct-17",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "The population of a town increases by 5% annually. If the present population is 80,000, what will it be after 2 years?",
        "options": [
            {
                "id": "A",
                "text": "88,200"
            },
            {
                "id": "B",
                "text": "88,000"
            },
            {
                "id": "C",
                "text": "86,400"
            },
            {
                "id": "D",
                "text": "89,100"
            }
        ],
        "correct_answer": "A",
        "explanation": "Population after 2 years = P × (1 + r/100)^2 = 80,000 × (1.05)^2 = 80,000 × 1.1025 = 88,200.",
        "formula": "Future Population = Present × (1 + r/100)^n"
    },
    {
        "id": "pct-18",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "Express 45 seconds as a percentage of 1 hour.",
        "options": [
            {
                "id": "A",
                "text": "1.25%"
            },
            {
                "id": "B",
                "text": "1.50%"
            },
            {
                "id": "C",
                "text": "1.00%"
            },
            {
                "id": "D",
                "text": "0.75%"
            }
        ],
        "correct_answer": "A",
        "explanation": "1 hour = 60 minutes = 3,600 seconds. Percentage = (45 / 3600) × 100% = 45 / 36 = 5 / 4 = 1.25%.",
        "formula": "Percentage = (Part in seconds / Whole in seconds) × 100%"
    },
    {
        "id": "pct-19",
        "topic": "Percentages",
        "difficulty": "Easy",
        "question": "If 15% of a number is 45, what is 40% of the same number?",
        "options": [
            {
                "id": "A",
                "text": "120"
            },
            {
                "id": "B",
                "text": "100"
            },
            {
                "id": "C",
                "text": "135"
            },
            {
                "id": "D",
                "text": "150"
            }
        ],
        "correct_answer": "A",
        "explanation": "15% corresponds to 45, so 1% = 45 / 15 = 3. Therefore, 40% of the number = 40 × 3 = 120.",
        "formula": "Value = (Given Value / Given %) × Desired % = (45 / 15) × 40 = 120"
    },
    {
        "id": "pct-3",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "The price of sugar rises by 25%. By what percentage must a household reduce its consumption so that the total expenditure remains unchanged?",
        "options": [
            {
                "id": "A",
                "text": "15%"
            },
            {
                "id": "B",
                "text": "20%"
            },
            {
                "id": "C",
                "text": "25%"
            },
            {
                "id": "D",
                "text": "30%"
            }
        ],
        "correct_answer": "B",
        "explanation": "Reduction percentage = [r / (100 + r)] × 100. Here r = 25. Reduction = [25 / (100 + 25)] × 100 = (25 / 125) × 100 = (1 / 5) × 100 = 20%.",
        "formula": "Expenditure Constant Reduction % = [r / (100 + r)] × 100"
    },
    {
        "id": "pct-4",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "An item is marked 30% above its cost price and sold at a discount of 10%. What is the net profit percentage?",
        "options": [
            {
                "id": "A",
                "text": "15%"
            },
            {
                "id": "B",
                "text": "17%"
            },
            {
                "id": "C",
                "text": "18%"
            },
            {
                "id": "D",
                "text": "20%"
            }
        ],
        "correct_answer": "B",
        "explanation": "Let Cost Price = 100. Marked Price = 130. Discount = 10% of 130 = 13. Selling Price = 130 - 13 = 117. Profit = 117 - 100 = 17%. Alternatively: Net % = a - b - (a × b)/100 = 30 - 10 - 3 = 17%.",
        "formula": "Net % = Markup - Discount - (Markup × Discount) / 100"
    },
    {
        "id": "pct-20",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "In an examination, 70% of candidates passed in English, 80% passed in Mathematics, and 10% failed in both subjects. If 144 candidates passed in both subjects, what is the total number of candidates?",
        "options": [
            {
                "id": "A",
                "text": "240"
            },
            {
                "id": "B",
                "text": "200"
            },
            {
                "id": "C",
                "text": "280"
            },
            {
                "id": "D",
                "text": "300"
            }
        ],
        "correct_answer": "A",
        "explanation": "Failed in both = 10%, so passed in at least one subject = 100% - 10% = 90%. By Principle of Inclusion-Exclusion: % Passed Both = % Passed English + % Passed Math - % Passed at least one = 70% + 80% - 90% = 60%. Given that 60% corresponds to 144 candidates: Total candidates = 144 / 0.60 = 240.",
        "formula": "% Passed Both = P(E) + P(M) - P(E U M) = 70 + 80 - 90 = 60%"
    },
    {
        "id": "pct-21",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "Fresh fruit contains 68% water and dry fruit contains 20% water. How many kilograms of dry fruit can be obtained from 100 kg of fresh fruit?",
        "options": [
            {
                "id": "A",
                "text": "40 kg"
            },
            {
                "id": "B",
                "text": "32 kg"
            },
            {
                "id": "C",
                "text": "50 kg"
            },
            {
                "id": "D",
                "text": "45 kg"
            }
        ],
        "correct_answer": "A",
        "explanation": "Pulp content remains constant. In fresh fruit: Pulp = (100 - 68)% of 100 kg = 32% of 100 kg = 32 kg. In dry fruit: Pulp = (100 - 20)% = 80%. Let dry fruit weight be W: 80% of W = 32 kg => 0.80 × W = 32 => W = 32 / 0.80 = 40 kg.",
        "formula": "Pulp Invariance: Fresh_Pulp% × Fresh_Weight = Dry_Pulp% × Dry_Weight"
    },
    {
        "id": "pct-22",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "In an election between two candidates, 20% of voters did not cast their votes and 10% of cast votes were declared invalid. The winning candidate got 55% of the valid votes and won by a majority of 720 votes. Find the total number of voters enrolled on the voter list.",
        "options": [
            {
                "id": "A",
                "text": "10,000"
            },
            {
                "id": "B",
                "text": "8,000"
            },
            {
                "id": "C",
                "text": "12,000"
            },
            {
                "id": "D",
                "text": "9,500"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let total enrolled voters be V. Votes polled = 0.80 V. Valid votes = 0.90 × (0.80 V) = 0.72 V. Majority percentage among valid votes = 55% - 45% = 10% of valid votes. Majority votes = 0.10 × (0.72 V) = 0.072 V. Given 0.072 V = 720 => V = 720 / 0.072 = 10,000 voters.",
        "formula": "Majority = (Win% - Lose%) × Valid% × Polled% × Total = 720"
    },
    {
        "id": "pct-23",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "The price of petrol goes up by 25%. By how much percent must a motorist reduce petrol consumption so that the total expenditure remains unchanged?",
        "options": [
            {
                "id": "A",
                "text": "20%"
            },
            {
                "id": "B",
                "text": "25%"
            },
            {
                "id": "C",
                "text": "16.67%"
            },
            {
                "id": "D",
                "text": "15%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Formula: Reduction in consumption = [r / (100 + r)] × 100%. Here r = 25. Reduction = [25 / (100 + 25)] × 100% = (25 / 125) × 100% = 1/5 × 100% = 20%.",
        "formula": "Reduction % = [r / (100 + r)] × 100%"
    },
    {
        "id": "pct-24",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "A student multiplied a number by 3/5 instead of 5/3. What is the percentage error in the calculation?",
        "options": [
            {
                "id": "A",
                "text": "64%"
            },
            {
                "id": "B",
                "text": "54%"
            },
            {
                "id": "C",
                "text": "45%"
            },
            {
                "id": "D",
                "text": "36%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let the number be 15 (LCM of 3 and 5). Correct value = 15 × (5/3) = 25. Incorrect value = 15 × (3/5) = 9. Absolute error = 25 - 9 = 16. Percentage error = (Error / Correct Value) × 100% = (16 / 25) × 100% = 64%.",
        "formula": "Percentage Error = (|Correct - Measured| / Correct) × 100%"
    },
    {
        "id": "pct-25",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "A person spends 30% of his income on house rent, 20% of the remaining on food, and 10% of the balance on education. If he is left with ₹5,040, what is his total monthly income?",
        "options": [
            {
                "id": "A",
                "text": "₹10,000"
            },
            {
                "id": "B",
                "text": "₹12,000"
            },
            {
                "id": "C",
                "text": "₹9,500"
            },
            {
                "id": "D",
                "text": "₹10,500"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let income be I. After rent: 0.70 I remaining. After food: 0.80 × (0.70 I) = 0.56 I remaining. After education: 0.90 × (0.56 I) = 0.504 I remaining. 0.504 I = 5,040 => I = 5,040 / 0.504 = ₹10,000.",
        "formula": "Remaining Fraction = (1 - r1) × (1 - r2) × (1 - r3) = 0.504"
    },
    {
        "id": "pct-26",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "If the length of a rectangle is increased by 20% and its breadth is decreased by 15%, what is the net percentage change in its area?",
        "options": [
            {
                "id": "A",
                "text": "2% increase"
            },
            {
                "id": "B",
                "text": "5% increase"
            },
            {
                "id": "C",
                "text": "2% decrease"
            },
            {
                "id": "D",
                "text": "4% increase"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net change = l + b + (l × b)/100. Here l = +20, b = -15. Net change = 20 - 15 + (20 × -15)/100 = 5 - 3 = +2%. Thus, the area increases by 2%.",
        "formula": "Area Change = a + b + (ab / 100) = 20 - 15 - 3 = +2%"
    },
    {
        "id": "pct-27",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "A manufacturer sells an article to a wholesale dealer at a profit of 20%. The wholesaler sells it to a shopkeeper at 15% profit. The shopkeeper sells it to a consumer for ₹1,656, making a profit of 20%. What is the cost of manufacturing the article?",
        "options": [
            {
                "id": "A",
                "text": "₹1,000"
            },
            {
                "id": "B",
                "text": "₹1,100"
            },
            {
                "id": "C",
                "text": "₹1,200"
            },
            {
                "id": "D",
                "text": "₹950"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let manufacturer's cost be C. Final price = C × 1.20 × 1.15 × 1.20 = 1,656. 1.20 × 1.15 × 1.20 = 1.38 × 1.20 = 1.656. C × 1.656 = 1,656 => C = ₹1,000.",
        "formula": "Final Price = Initial Cost × (1 + r1) × (1 + r2) × (1 + r3)"
    },
    {
        "id": "pct-28",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "In an alloy, there is 12% nickel. To obtain 36 kg of nickel, how much alloy is required?",
        "options": [
            {
                "id": "A",
                "text": "300 kg"
            },
            {
                "id": "B",
                "text": "280 kg"
            },
            {
                "id": "C",
                "text": "320 kg"
            },
            {
                "id": "D",
                "text": "360 kg"
            }
        ],
        "correct_answer": "A",
        "explanation": "12% of Total Alloy = 36 kg => Total Alloy = 36 / 0.12 = 300 kg.",
        "formula": "Alloy Mass = Target Component / Component Fraction = 36 / 0.12 = 300 kg"
    },
    {
        "id": "pct-29",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "Two numbers are respectively 20% and 50% more than a third number. What percentage is the first number of the second number?",
        "options": [
            {
                "id": "A",
                "text": "80%"
            },
            {
                "id": "B",
                "text": "75%"
            },
            {
                "id": "C",
                "text": "85%"
            },
            {
                "id": "D",
                "text": "70%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let the third number be 100. First number = 120, Second number = 150. Percentage = (120 / 150) × 100% = 4/5 × 100% = 80%.",
        "formula": "Ratio Percentage = (N1 / N2) × 100% = (120 / 150) × 100% = 80%"
    },
    {
        "id": "pct-30",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "A reduction of 20% in the price of wheat enables a person to buy 5 kg more wheat for ₹320. What is the original price per kg of wheat?",
        "options": [
            {
                "id": "A",
                "text": "₹16 per kg"
            },
            {
                "id": "B",
                "text": "₹12.80 per kg"
            },
            {
                "id": "C",
                "text": "₹15 per kg"
            },
            {
                "id": "D",
                "text": "₹20 per kg"
            }
        ],
        "correct_answer": "A",
        "explanation": "Amount saved due to 20% price drop = 20% of ₹320 = ₹64. This ₹64 buys the extra 5 kg. Reduced price per kg = 64 / 5 = ₹12.80/kg. Since reduced price is 80% of original price: Original Price = 12.80 / 0.80 = ₹16 per kg.",
        "formula": "Original Price = (Saved Amount / Extra Quantity) / (1 - Discount Rate) = 12.80 / 0.80 = ₹16/kg"
    },
    {
        "id": "pct-31",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "The value of a machine depreciates at the rate of 10% per annum. It was purchased 3 years ago. If its present value is ₹8,748, what was its purchase price?",
        "options": [
            {
                "id": "A",
                "text": "₹12,000"
            },
            {
                "id": "B",
                "text": "₹11,500"
            },
            {
                "id": "C",
                "text": "₹12,500"
            },
            {
                "id": "D",
                "text": "₹10,000"
            }
        ],
        "correct_answer": "A",
        "explanation": "Present Value = P × (1 - 10/100)^3 = P × (0.9)^3 = P × 0.729. P = 8,748 / 0.729 = ₹12,000.",
        "formula": "Initial Cost P = Present Value / (1 - r)^n = 8748 / 0.729 = ₹12,000"
    },
    {
        "id": "pct-32",
        "topic": "Percentages",
        "difficulty": "Medium",
        "question": "In an entrance exam, 45% of students failed in Physics and 35% failed in Chemistry. If 15% failed in both subjects, what percentage of students passed in both subjects?",
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
        "explanation": "Failed in at least one subject = Failed(P) + Failed(C) - Failed(Both) = 45% + 35% - 15% = 65%. Passed in both subjects = 100% - 65% = 35%.",
        "formula": "Passed Both = 100 - [F(P) + F(C) - F(P ∩ C)] = 100 - 65 = 35%"
    },
    {
        "id": "pct-5",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "The population of a city increases by 10% in the first year and decreases by 10% in the second year. If the current population is 99,000, what was the population two years ago?",
        "options": [
            {
                "id": "A",
                "text": "98,000"
            },
            {
                "id": "B",
                "text": "100,000"
            },
            {
                "id": "C",
                "text": "101,000"
            },
            {
                "id": "D",
                "text": "105,000"
            }
        ],
        "correct_answer": "B",
        "explanation": "Let initial population be P. After year 1: P × 1.10. After year 2: P × 1.10 × 0.90 = 0.99P. Given 0.99P = 99,000 => P = 99,000 / 0.99 = 100,000.",
        "formula": "Successive Percentage Factor: P_final = P_initial × (1 + r1/100) × (1 - r2/100)"
    },
    {
        "id": "pct-6",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "Fresh grapes contain 80% water, while dry raisins contain 10% water. How many kilograms of dry raisins can be obtained from 180 kg of fresh grapes?",
        "options": [
            {
                "id": "A",
                "text": "36 kg"
            },
            {
                "id": "B",
                "text": "40 kg"
            },
            {
                "id": "C",
                "text": "45 kg"
            },
            {
                "id": "D",
                "text": "50 kg"
            }
        ],
        "correct_answer": "B",
        "explanation": "The pulp content remains constant during drying. In 180 kg fresh grapes, pulp = (100 - 80)% = 20% of 180 = 36 kg. In dry raisins, pulp is (100 - 10)% = 90%. Therefore, 90% of Raisin Weight = 36 kg => Raisin Weight = 36 / 0.90 = 40 kg.",
        "formula": "Dry Pulp Invariance: %Pulp_fresh × Weight_fresh = %Pulp_dry × Weight_dry"
    },
    {
        "id": "pct-33",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A tax policy levies 0% on annual income up to ₹2,50,000, 10% on income between ₹2,50,001 and ₹5,00,000, and 20% on any amount above ₹5,00,000. An individual pays a total tax of ₹45,000. What is the individual's annual income?",
        "options": [
            {
                "id": "A",
                "text": "₹6,00,000"
            },
            {
                "id": "B",
                "text": "₹6,50,000"
            },
            {
                "id": "C",
                "text": "₹5,50,000"
            },
            {
                "id": "D",
                "text": "₹7,00,000"
            }
        ],
        "correct_answer": "A",
        "explanation": "Tax on first slab (up to ₹2.5L) = 0. Tax on second slab (from ₹2.5L to ₹5.0L) = 10% of ₹2,50,000 = ₹25,000. Remaining tax paid = 45,000 - 25,000 = ₹20,000. This ₹20,000 is taxed at 20% on income exceeding ₹5,00,000: Excess income = 20,000 / 0.20 = ₹1,00,000. Total annual income = ₹5,00,000 + ₹1,00,000 = ₹6,00,000.",
        "formula": "Progressive Tax Inversion: Total Income = Base + (Residual Tax / Highest Marginal Rate)"
    },
    {
        "id": "pct-34",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A large vessel contains an 80-liter mixture of milk and water containing 25% water. How many liters of pure water must be added to this mixture so that the new mixture contains 40% water?",
        "options": [
            {
                "id": "A",
                "text": "20 liters"
            },
            {
                "id": "B",
                "text": "15 liters"
            },
            {
                "id": "C",
                "text": "25 liters"
            },
            {
                "id": "D",
                "text": "18 liters"
            }
        ],
        "correct_answer": "A",
        "explanation": "Milk quantity remains unchanged. In initial mixture: Milk = (100 - 25)% of 80 = 75% of 80 = 60 liters. In new mixture, water is 40%, so milk is 60%. Let new total volume be V: 60% of V = 60 liters => V = 60 / 0.60 = 100 liters. Pure water added = New Volume - Initial Volume = 100 - 80 = 20 liters.",
        "formula": "Component conservation: Milk_Initial = Milk_Final => 0.75 × 80 = 0.60 × V => V = 100 L"
    },
    {
        "id": "pct-35",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "In a town, 60% of the families own a car, 30% own a motorcycle, and 15% own both a car and a motorcycle. In all, there are 96 families that do not own either a car or a motorcycle. How many families live in the town?",
        "options": [
            {
                "id": "A",
                "text": "384 families"
            },
            {
                "id": "B",
                "text": "400 families"
            },
            {
                "id": "C",
                "text": "360 families"
            },
            {
                "id": "D",
                "text": "420 families"
            }
        ],
        "correct_answer": "A",
        "explanation": "Percentage owning at least one vehicle = % Car + % Motorcycle - % Both = 60% + 30% - 15% = 75%. Percentage owning neither = 100% - 75% = 25%. 25% corresponds to 96 families. Total families = 96 / 0.25 = 96 × 4 = 384 families.",
        "formula": "Neither% = 100 - (A + B - A ∩ B) = 100 - 75 = 25% => Total = 96 / 0.25 = 384"
    },
    {
        "id": "pct-36",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A merchant charges 20% above the production cost for his goods. Due to inflation, the cost of production increases by 25%, and he consequently raises his selling price by 10%. What is his new profit percentage?",
        "options": [
            {
                "id": "A",
                "text": "5.6%"
            },
            {
                "id": "B",
                "text": "6.0%"
            },
            {
                "id": "C",
                "text": "5.0%"
            },
            {
                "id": "D",
                "text": "7.5%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let initial production cost = 100. Initial selling price = 100 × 1.20 = 120. New production cost = 100 × 1.25 = 125. New selling price = 120 × 1.10 = 132. New profit = 132 - 125 = 7. New profit percentage = (7 / 125) × 100% = 7 × (4/5) = 28 / 5 = 5.6%.",
        "formula": "Profit % = [(New SP - New CP) / New CP] × 100% = (7 / 125) × 100 = 5.6%"
    },
    {
        "id": "pct-37",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A solution contains 15% alcohol. It is mixed with another solution containing 25% alcohol to produce 50 liters of an 18% alcohol mixture. How many liters of the 15% alcohol solution were used?",
        "options": [
            {
                "id": "A",
                "text": "35 liters"
            },
            {
                "id": "B",
                "text": "30 liters"
            },
            {
                "id": "C",
                "text": "25 liters"
            },
            {
                "id": "D",
                "text": "40 liters"
            }
        ],
        "correct_answer": "A",
        "explanation": "Using alligation rule: Cheaper solution = 15%, Dearer solution = 25%, Mean solution = 18%. Ratio of (15% sol) : (25% sol) = (25 - 18) : (18 - 15) = 7 : 3. Volume of 15% solution = 7 / (7 + 3) × 50 = 7/10 × 50 = 35 liters.",
        "formula": "Alligation Ratio = (25 - 18) : (18 - 15) = 7 : 3 => Vol = (7/10) × 50 = 35 L"
    },
    {
        "id": "pct-38",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "In a municipal election between candidates X and Y, 10% of voters on the list did not cast votes and 60 ballot papers were rejected as completely blank/invalid. Candidate X won by securing 47% of the total voters on the list and received 308 votes more than Candidate Y. Find the total number of voters on the municipal list.",
        "options": [
            {
                "id": "A",
                "text": "6,200"
            },
            {
                "id": "B",
                "text": "6,000"
            },
            {
                "id": "C",
                "text": "5,800"
            },
            {
                "id": "D",
                "text": "6,400"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let total voters on list be V. Votes polled = 0.90 V. Valid votes = 0.90 V - 60. Votes polled by X = 47% of V = 0.47 V. Votes polled by Y = (0.90 V - 60) - 0.47 V = 0.43 V - 60. Majority = X - Y = 0.47 V - (0.43 V - 60) = 0.04 V + 60 = 308 => 0.04 V = 248 => V = 248 / 0.04 = 6,200 voters.",
        "formula": "Linear Balance: (0.47 V) - (0.43 V - 60) = 308 => V = 6,200"
    },
    {
        "id": "pct-39",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A salesman gets a fixed salary of ₹4,000 per month plus a commission of 5% on all sales above ₹10,000. In a particular month, his total earnings were ₹7,000. What was the total value of sales he made that month?",
        "options": [
            {
                "id": "A",
                "text": "₹70,000"
            },
            {
                "id": "B",
                "text": "₹60,000"
            },
            {
                "id": "C",
                "text": "₹65,000"
            },
            {
                "id": "D",
                "text": "₹75,000"
            }
        ],
        "correct_answer": "A",
        "explanation": "Commission earned = Total Earnings - Fixed Salary = ₹7,000 - ₹4,000 = ₹3,000. Commission is 5% on sales over ₹10,000: 5% of (Sales - 10,000) = 3,000 => Sales - 10,000 = 3,000 / 0.05 = 60,000 => Total Sales = 60,000 + 10,000 = ₹70,000.",
        "formula": "Total Sales = Threshold + (Commission / Rate) = 10,000 + 60,000 = ₹70,000"
    },
    {
        "id": "pct-40",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A cylinder's radius is decreased by 20% while its height is increased by 50%. What is the net percentage change in the volume of the cylinder?",
        "options": [
            {
                "id": "A",
                "text": "4% decrease"
            },
            {
                "id": "B",
                "text": "4% increase"
            },
            {
                "id": "C",
                "text": "10% increase"
            },
            {
                "id": "D",
                "text": "2% decrease"
            }
        ],
        "correct_answer": "A",
        "explanation": "Volume of cylinder V = π × r^2 × h. New volume V' = π × (0.80 r)^2 × (1.50 h) = π × 0.64 r^2 × 1.50 h = 0.96 V. Net change = (0.96 - 1) × 100% = -4%, which is a 4% decrease.",
        "formula": "Volume Scaling Factor = (1 - dr)^2 × (1 + dh) = (0.8)^2 × 1.5 = 0.96 => 4% decrease"
    },
    {
        "id": "pct-41",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A candidate answered 70% of the first 50 questions correctly in an examination containing 80 questions in total. What percentage of the remaining 30 questions must she answer correctly to score 75% overall in the examination?",
        "options": [
            {
                "id": "A",
                "text": "83.33% (83 1/3%)"
            },
            {
                "id": "B",
                "text": "80.00%"
            },
            {
                "id": "C",
                "text": "85.00%"
            },
            {
                "id": "D",
                "text": "87.50%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total correct answers needed = 75% of 80 = 60 questions. Correct answers in first 50 = 70% of 50 = 35 questions. Correct answers needed in remaining 30 questions = 60 - 35 = 25 questions. Percentage needed = (25 / 30) × 100% = 5/6 × 100% = 83.33% (83 1/3%).",
        "formula": "Required% = (Target Correct - Achieved Correct) / Remaining Questions = 25 / 30 = 83.33%"
    },
    {
        "id": "pct-42",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "The population of a city was 1,50,000. In the first year, it increased by 10%, in the second year it decreased by 20%, and in the third year it increased by 30%. What is the population of the city at the end of 3 years?",
        "options": [
            {
                "id": "A",
                "text": "1,71,600"
            },
            {
                "id": "B",
                "text": "1,68,400"
            },
            {
                "id": "C",
                "text": "1,72,000"
            },
            {
                "id": "D",
                "text": "1,75,000"
            }
        ],
        "correct_answer": "A",
        "explanation": "Population = 1,50,000 × 1.10 × 0.80 × 1.30 = 1,50,000 × 1.144 = 1,71,600.",
        "formula": "Final Population = P0 × (1 + r1) × (1 - r2) × (1 + r3) = 150000 × 1.144 = 171,600"
    },
    {
        "id": "pct-43",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A piece of commercial land appreciated by 20% in value in its first year and 25% in its second year. Due to a market downturn, its value dropped by 10% in the third year. What was the overall percentage appreciation over the 3-year period?",
        "options": [
            {
                "id": "A",
                "text": "35%"
            },
            {
                "id": "B",
                "text": "32%"
            },
            {
                "id": "C",
                "text": "37.5%"
            },
            {
                "id": "D",
                "text": "40%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Cumulative multiplier = (1 + 0.20) × (1 + 0.25) × (1 - 0.10) = 1.20 × 1.25 × 0.90 = 1.50 × 0.90 = 1.35. Net appreciation = (1.35 - 1) × 100% = 35%.",
        "formula": "Net Appreciation = [(1.20 × 1.25 × 0.90) - 1] × 100% = 35%"
    },
    {
        "id": "pct-44",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "If 80% of a company's employees are full-time, 40% of full-time employees own shares, and 20% of part-time employees own shares, what percentage of all employees in the company own shares?",
        "options": [
            {
                "id": "A",
                "text": "36%"
            },
            {
                "id": "B",
                "text": "32%"
            },
            {
                "id": "C",
                "text": "40%"
            },
            {
                "id": "D",
                "text": "30%"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let total employees be 100. Full-time employees = 80; part-time employees = 20. Shareholders among full-time = 40% of 80 = 32. Shareholders among part-time = 20% of 20 = 4. Total shareholders = 32 + 4 = 36. Percentage = 36%.",
        "formula": "Weighted Average: P_total = w1*P1 + w2*P2 = 0.80 × 0.40 + 0.20 × 0.20 = 0.36 = 36%"
    },
    {
        "id": "pct-45",
        "topic": "Percentages",
        "difficulty": "Hard",
        "question": "A merchant purchases two items for ₹1,200 each. He sells the first item at a profit of 20% and the second item at a loss of 20%. What is his overall profit or loss percentage on the entire transaction?",
        "options": [
            {
                "id": "A",
                "text": "No profit, no loss (0%)"
            },
            {
                "id": "B",
                "text": "4% loss"
            },
            {
                "id": "C",
                "text": "4% profit"
            },
            {
                "id": "D",
                "text": "2% loss"
            }
        ],
        "correct_answer": "A",
        "explanation": "Both items have the identical cost price of ₹1,200. Profit on item 1 = +20% of 1200 = +₹240. Loss on item 2 = -20% of 1200 = -₹240. Net profit/loss = +240 - 240 = ₹0. Overall percentage = 0% (no profit, no loss). Note: This contrasts with cases where Selling Prices are equal.",
        "formula": "Equal Cost Price Rule: Net Gain% = (Gain% - Loss%) / 2 = 0%"
    }
]
