# -*- coding: utf-8 -*-
"""
Quantitative Aptitude Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

QUANTITATIVE_QUESTIONS: List[Dict[str, Any]] = [
    # -------------------------------------------------------------------------
    # EASY (15 Questions: qa-1, qa-2, qa-7 to qa-19)
    # -------------------------------------------------------------------------
    {
        "id": "qa-1",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "The average of five consecutive even numbers is 34. What is the smallest of these numbers?",
        "options": [
            {"id": "A", "text": "28"},
            {"id": "B", "text": "30"},
            {"id": "C", "text": "32"},
            {"id": "D", "text": "34"}
        ],
        "correct_answer": "B",
        "explanation": "For an odd number of terms in an arithmetic progression, the average is the middle term. Here, the middle (3rd) term is 34. The five consecutive even numbers are 30, 32, 34, 36, and 38. The smallest number is 30.",
        "formula": "Average of AP = Middle Term; Sequence = x-4, x-2, x, x+2, x+4"
    },
    {
        "id": "qa-2",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A sum of ₹12,500 is lent at simple interest of 12% per annum. What is the interest earned after 3 years?",
        "options": [
            {"id": "A", "text": "₹4,200"},
            {"id": "B", "text": "₹4,500"},
            {"id": "C", "text": "₹4,800"},
            {"id": "D", "text": "₹5,000"}
        ],
        "correct_answer": "B",
        "explanation": "Simple Interest (SI) = (P × R × T) / 100. Here, P = 12500, R = 12, T = 3. SI = (12500 × 12 × 3) / 100 = 125 × 36 = ₹4,500.",
        "formula": "SI = (P × R × T) / 100"
    },
    {
        "id": "qa-7",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "What is the average of the first 10 positive odd integers?",
        "options": [
            {"id": "A", "text": "9"},
            {"id": "B", "text": "10"},
            {"id": "C", "text": "11"},
            {"id": "D", "text": "12"}
        ],
        "correct_answer": "B",
        "explanation": "The sum of the first n odd numbers is n². The average is (n²) / n = n. For the first 10 odd numbers, the average is 10.",
        "formula": "Average of first n odd integers = n"
    },
    {
        "id": "qa-8",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A sum of ₹8,000 is deposited at simple interest of 5% per annum. How much total interest is accumulated after 4 years?",
        "options": [
            {"id": "A", "text": "₹1,400"},
            {"id": "B", "text": "₹1,500"},
            {"id": "C", "text": "₹1,600"},
            {"id": "D", "text": "₹1,800"}
        ],
        "correct_answer": "C",
        "explanation": "SI = (P × R × T) / 100 = (8000 × 5 × 4) / 100 = 80 × 20 = ₹1,600.",
        "formula": "SI = (P × R × T) / 100"
    },
    {
        "id": "qa-9",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "Two numbers are in the ratio 3 : 4 and their sum is 140. What is the smaller number?",
        "options": [
            {"id": "A", "text": "50"},
            {"id": "B", "text": "60"},
            {"id": "C", "text": "70"},
            {"id": "D", "text": "80"}
        ],
        "correct_answer": "B",
        "explanation": "Let the numbers be 3x and 4x. 3x + 4x = 140 => 7x = 140 => x = 20. The smaller number is 3x = 3 × 20 = 60.",
        "formula": "Number = (Ratio part / Sum of ratio parts) × Total"
    },
    {
        "id": "qa-10",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "The present ages of Rahul and Amit are in the ratio 5 : 7. If the sum of their present ages is 48 years, what is Rahul's present age?",
        "options": [
            {"id": "A", "text": "18 years"},
            {"id": "B", "text": "20 years"},
            {"id": "C", "text": "24 years"},
            {"id": "D", "text": "28 years"}
        ],
        "correct_answer": "B",
        "explanation": "Ratio sum = 5 + 7 = 12 parts. 12 parts = 48 years => 1 part = 4 years. Rahul's age = 5 × 4 = 20 years.",
        "formula": "Age = (Individual Ratio / Total Ratio) × Total Age"
    },
    {
        "id": "qa-11",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A train 150 meters long is running at a uniform speed of 54 km/h. How many seconds will it take to pass a stationary telegraph post?",
        "options": [
            {"id": "A", "text": "8 seconds"},
            {"id": "B", "text": "10 seconds"},
            {"id": "C", "text": "12 seconds"},
            {"id": "D", "text": "15 seconds"}
        ],
        "correct_answer": "B",
        "explanation": "Speed in m/s = 54 × (5/18) = 15 m/s. Time to cross post = Train Length / Speed = 150 / 15 = 10 seconds.",
        "formula": "Time = Distance / Speed; Speed in m/s = Speed in km/h × (5/18)"
    },
    {
        "id": "qa-12",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "The average of 5 numbers is 20. If one number is excluded, the average becomes 18. What is the value of the excluded number?",
        "options": [
            {"id": "A", "text": "26"},
            {"id": "B", "text": "28"},
            {"id": "C", "text": "30"},
            {"id": "D", "text": "32"}
        ],
        "correct_answer": "B",
        "explanation": "Total sum of 5 numbers = 5 × 20 = 100. Sum of remaining 4 numbers = 4 × 18 = 72. Excluded number = 100 - 72 = 28.",
        "formula": "Excluded Value = (Original Count × Original Avg) - (New Count × New Avg)"
    },
    {
        "id": "qa-13",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A retailer buys a textbook for ₹400 and sells it at a profit of 15%. What is the selling price?",
        "options": [
            {"id": "A", "text": "₹450"},
            {"id": "B", "text": "₹460"},
            {"id": "C", "text": "₹475"},
            {"id": "D", "text": "₹480"}
        ],
        "correct_answer": "B",
        "explanation": "Selling Price = CP × (1 + Profit% / 100) = 400 × 1.15 = ₹460.",
        "formula": "SP = CP × (100 + Gain%) / 100"
    },
    {
        "id": "qa-14",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "What is the mean proportional between 9 and 25?",
        "options": [
            {"id": "A", "text": "12"},
            {"id": "B", "text": "15"},
            {"id": "C", "text": "16"},
            {"id": "D", "text": "18"}
        ],
        "correct_answer": "B",
        "explanation": "Mean proportional between a and b is √(a × b). Mean proportional = √(9 × 25) = √(225) = 15.",
        "formula": "Mean Proportional = √(a × b)"
    },
    {
        "id": "qa-15",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A vehicle covers a distance of 216 km in 3 hours. What is its speed in meters per second?",
        "options": [
            {"id": "A", "text": "18 m/s"},
            {"id": "B", "text": "20 m/s"},
            {"id": "C", "text": "22 m/s"},
            {"id": "D", "text": "25 m/s"}
        ],
        "correct_answer": "B",
        "explanation": "Speed in km/h = 216 / 3 = 72 km/h. Converting to m/s: 72 × (5/18) = 4 × 5 = 20 m/s.",
        "formula": "Speed (m/s) = Speed (km/h) × (5/18)"
    },
    {
        "id": "qa-16",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "The sum of two numbers is 45 and their difference is 15. What is the ratio of the greater number to the smaller number?",
        "options": [
            {"id": "A", "text": "3 : 1"},
            {"id": "B", "text": "2 : 1"},
            {"id": "C", "text": "4 : 1"},
            {"id": "D", "text": "5 : 2"}
        ],
        "correct_answer": "B",
        "explanation": "Let numbers be x and y. x + y = 45 and x - y = 15 => 2x = 60 => x = 30; y = 15. Ratio = 30 : 15 = 2 : 1.",
        "formula": "Greater = (Sum + Diff) / 2; Smaller = (Sum - Diff) / 2"
    },
    {
        "id": "qa-17",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A sum of money doubles itself in 8 years at simple interest. What is the annual rate of interest?",
        "options": [
            {"id": "A", "text": "10%"},
            {"id": "B", "text": "12.5%"},
            {"id": "C", "text": "15%"},
            {"id": "D", "text": "16%"}
        ],
        "correct_answer": "B",
        "explanation": "To double, interest earned equals principal (SI = P). SI = (P × R × T) / 100 => P = (P × R × 8) / 100 => R = 100 / 8 = 12.5%.",
        "formula": "Rate for doubling = 100 / Time"
    },
    {
        "id": "qa-18",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "The average of four consecutive even numbers is 27. What is the largest of these numbers?",
        "options": [
            {"id": "A", "text": "28"},
            {"id": "B", "text": "30"},
            {"id": "C", "text": "32"},
            {"id": "D", "text": "34"}
        ],
        "correct_answer": "B",
        "explanation": "Four consecutive even numbers: x, x+2, x+4, x+6. Average = (4x + 12) / 4 = x + 3 = 27 => x = 24. The numbers are 24, 26, 28, 30. Largest is 30.",
        "formula": "Average of 4 terms = (First + Last) / 2"
    },
    {
        "id": "qa-19",
        "topic": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "If 15% of a number is 75, what is 40% of that number?",
        "options": [
            {"id": "A", "text": "180"},
            {"id": "B", "text": "200"},
            {"id": "C", "text": "220"},
            {"id": "D", "text": "250"}
        ],
        "correct_answer": "B",
        "explanation": "Let number be N. 0.15N = 75 => N = 75 / 0.15 = 500. 40% of 500 = 0.40 × 500 = 200.",
        "formula": "Target = (Known / Known %) × Target %"
    },

    # -------------------------------------------------------------------------
    # MEDIUM (15 Questions: qa-3, qa-4, qa-20 to qa-32)
    # -------------------------------------------------------------------------
    {
        "id": "qa-3",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "In what ratio must a grocer mix tea at ₹60 per kg and ₹65 per kg so that by selling the mixture at ₹68.20 per kg he may gain 10%?",
        "options": [
            {"id": "A", "text": "3 : 2"},
            {"id": "B", "text": "2 : 3"},
            {"id": "C", "text": "3 : 5"},
            {"id": "D", "text": "4 : 5"}
        ],
        "correct_answer": "A",
        "explanation": "Selling Price of mixture = ₹68.20 with 10% profit, so Cost Price of mixture = 68.20 / 1.10 = ₹62/kg. Using rule of alligation: (Cheaper tea: 60, Dearer tea: 65, Mean: 62). Ratio = (65 - 62) : (62 - 60) = 3 : 2.",
        "formula": "Alligation Rule: (Quantity of Cheaper) / (Quantity of Dearer) = (Price of Dearer - Mean Price) / (Mean Price - Price of Cheaper)"
    },
    {
        "id": "qa-4",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "The ratio of present ages of two brothers is 4 : 5. Six years ago, their ages were in the ratio 3 : 4. What will be the ratio of their ages 6 years from now?",
        "options": [
            {"id": "A", "text": "5 : 6"},
            {"id": "B", "text": "6 : 7"},
            {"id": "C", "text": "7 : 8"},
            {"id": "D", "text": "8 : 9"}
        ],
        "correct_answer": "A",
        "explanation": "Let present ages be 4x and 5x. Six years ago: (4x - 6) / (5x - 6) = 3 / 4 => 16x - 24 = 15x - 18 => x = 6. Present ages are 24 and 30. Six years hence, ages will be 30 and 36. Ratio = 30 / 36 = 5 : 6.",
        "formula": "(A - t) / (B - t) = r1; (A + t) / (B + t) = r2"
    },
    {
        "id": "qa-20",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A mixture of 60 liters contains milk and water in the ratio 2 : 1. How many liters of water must be added to this mixture so that the ratio of milk to water becomes 1 : 2?",
        "options": [
            {"id": "A", "text": "40 liters"},
            {"id": "B", "text": "50 liters"},
            {"id": "C", "text": "60 liters"},
            {"id": "D", "text": "80 liters"}
        ],
        "correct_answer": "C",
        "explanation": "Milk = (2/3) × 60 = 40 liters; Water = 20 liters. In the new mixture, milk (40 L) is 1 part, so water must be 2 parts = 2 × 40 = 80 liters. Water to add = 80 - 20 = 60 liters.",
        "formula": "New Water = Milk × (New Water Ratio / New Milk Ratio)"
    },
    {
        "id": "qa-21",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "What is the difference between compound interest and simple interest on ₹10,000 for 2 years at an annual interest rate of 10%?",
        "options": [
            {"id": "A", "text": "₹80"},
            {"id": "B", "text": "₹100"},
            {"id": "C", "text": "₹120"},
            {"id": "D", "text": "₹150"}
        ],
        "correct_answer": "B",
        "explanation": "For 2 years, Difference = P × (R / 100)² = 10000 × (10 / 100)² = 10000 × 0.01 = ₹100.",
        "formula": "CI - SI (2 years) = P × (R / 100)²"
    },
    {
        "id": "qa-22",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "Two trains of lengths 120 meters and 180 meters are traveling in opposite directions on parallel tracks at 40 km/h and 50 km/h respectively. How many seconds will they take to completely cross each other?",
        "options": [
            {"id": "A", "text": "10 seconds"},
            {"id": "B", "text": "12 seconds"},
            {"id": "C", "text": "14 seconds"},
            {"id": "D", "text": "16 seconds"}
        ],
        "correct_answer": "B",
        "explanation": "Relative speed = 40 + 50 = 90 km/h = 90 × (5/18) = 25 m/s. Total distance = 120 + 180 = 300 meters. Time = 300 / 25 = 12 seconds.",
        "formula": "Time = (Length1 + Length2) / (Speed1 + Speed2)"
    },
    {
        "id": "qa-23",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A boat covers 24 km downstream in 2 hours and covers the same distance upstream in 4 hours. What is the speed of the water stream?",
        "options": [
            {"id": "A", "text": "2 km/h"},
            {"id": "B", "text": "3 km/h"},
            {"id": "C", "text": "4 km/h"},
            {"id": "D", "text": "6 km/h"}
        ],
        "correct_answer": "B",
        "explanation": "Downstream speed (u + v) = 24 / 2 = 12 km/h. Upstream speed (u - v) = 24 / 4 = 6 km/h. Speed of stream v = (12 - 6) / 2 = 3 km/h.",
        "formula": "Stream Speed = (Downstream Speed - Upstream Speed) / 2"
    },
    {
        "id": "qa-24",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A shopkeeper marks his goods 40% above the cost price and allows a discount of 20% on the marked price. What is his net profit percentage?",
        "options": [
            {"id": "A", "text": "10%"},
            {"id": "B", "text": "12%"},
            {"id": "C", "text": "14%"},
            {"id": "D", "text": "16%"}
        ],
        "correct_answer": "B",
        "explanation": "Let CP = 100. Marked Price = 140. Discount = 20% of 140 = 28. Selling Price = 140 - 28 = 112. Profit % = 112 - 100 = 12%.",
        "formula": "Net % = Markup - Discount - (Markup × Discount) / 100"
    },
    {
        "id": "qa-25",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A box contains 50 paise, 25 paise, and 10 paise coins in the ratio 5 : 9 : 4, amounting to ₹206 in total. How many 50 paise coins are in the box?",
        "options": [
            {"id": "A", "text": "180"},
            {"id": "B", "text": "200"},
            {"id": "C", "text": "220"},
            {"id": "D", "text": "250"}
        ],
        "correct_answer": "B",
        "explanation": "Value per unit ratio = 5(0.50) + 9(0.25) + 4(0.10) = 2.50 + 2.25 + 0.40 = ₹5.15. Total ratio multiplier = 206 / 5.15 = 40. Number of 50p coins = 5 × 40 = 200.",
        "formula": "Unit Multiplier = Total Amount / Sum(Ratio_i × Value_i)"
    },
    {
        "id": "qa-26",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "The average age of 24 students and their class teacher is 15 years. If the teacher's age is excluded, the average age decreases by 1 year. What is the age of the teacher?",
        "options": [
            {"id": "A", "text": "35 years"},
            {"id": "B", "text": "37 years"},
            {"id": "C", "text": "39 years"},
            {"id": "D", "text": "42 years"}
        ],
        "correct_answer": "C",
        "explanation": "Total persons initially = 25. Total sum = 25 × 15 = 375. Sum without teacher (24 students, avg 14) = 24 × 14 = 336. Teacher's age = 375 - 336 = 39 years.",
        "formula": "Excluded Age = Old Total - New Total"
    },
    {
        "id": "qa-27",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A sum of money invested at compound interest doubles itself in 4 years. In how many years will it become 8 times of itself at the same rate?",
        "options": [
            {"id": "A", "text": "8 years"},
            {"id": "B", "text": "12 years"},
            {"id": "C", "text": "16 years"},
            {"id": "D", "text": "20 years"}
        ],
        "correct_answer": "B",
        "explanation": "At compound interest, if an amount becomes 2^1 times in 4 years, it becomes 2^3 (8 times) in 4 × 3 = 12 years.",
        "formula": "Time = Base Years × Power (n)"
    },
    {
        "id": "qa-28",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A train passes a 200-meter-long platform in 20 seconds and a 300-meter-long platform in 25 seconds at a uniform speed. What is the speed of the train in km/h?",
        "options": [
            {"id": "A", "text": "64 km/h"},
            {"id": "B", "text": "72 km/h"},
            {"id": "C", "text": "80 km/h"},
            {"id": "D", "text": "90 km/h"}
        ],
        "correct_answer": "B",
        "explanation": "Distance difference = 300 - 200 = 100 meters. Time difference = 25 - 20 = 5 seconds. Speed = 100 / 5 = 20 m/s = 20 × (18/5) = 72 km/h.",
        "formula": "Speed = (Diff in Platform Lengths) / (Diff in Times)"
    },
    {
        "id": "qa-29",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A father is currently 3 times as old as his son. In 12 years, the father will be twice as old as his son. What is the father's current age?",
        "options": [
            {"id": "A", "text": "32 years"},
            {"id": "B", "text": "36 years"},
            {"id": "C", "text": "40 years"},
            {"id": "D", "text": "45 years"}
        ],
        "correct_answer": "B",
        "explanation": "Let son's age be x, father's age is 3x. In 12 years: 3x + 12 = 2(x + 12) => 3x + 12 = 2x + 24 => x = 12. Father's current age = 3 × 12 = 36 years.",
        "formula": "Linear age equation formulation"
    },
    {
        "id": "qa-30",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "In an election between two candidates, the winning candidate received 58% of the valid votes and won by a majority of 3,200 votes. What was the total number of valid votes polled?",
        "options": [
            {"id": "A", "text": "16,000"},
            {"id": "B", "text": "18,000"},
            {"id": "C", "text": "20,000"},
            {"id": "D", "text": "24,000"}
        ],
        "correct_answer": "C",
        "explanation": "Winner = 58%, Loser = 100% - 58% = 42%. Margin = 58% - 42% = 16%. 16% of Total = 3,200 => Total = 3200 / 0.16 = 20,000 votes.",
        "formula": "Total Votes = Winning Margin / (Difference in Percentage)"
    },
    {
        "id": "qa-31",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "What is the third proportional to 16 and 24?",
        "options": [
            {"id": "A", "text": "32"},
            {"id": "B", "text": "36"},
            {"id": "C", "text": "40"},
            {"id": "D", "text": "48"}
        ],
        "correct_answer": "B",
        "explanation": "Third proportional c to a and b satisfies a/b = b/c => c = b² / a = 24² / 16 = 576 / 16 = 36.",
        "formula": "Third Proportional c = b² / a"
    },
    {
        "id": "qa-32",
        "topic": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "By selling an article for ₹840, a merchant gains 20%. At what price should he sell it to gain 30%?",
        "options": [
            {"id": "A", "text": "₹890"},
            {"id": "B", "text": "₹910"},
            {"id": "C", "text": "₹925"},
            {"id": "D", "text": "₹940"}
        ],
        "correct_answer": "B",
        "explanation": "CP = 840 / 1.20 = ₹700. For 30% gain: New SP = 700 × 1.30 = ₹910.",
        "formula": "New SP = (Old SP / (100 + Gain1%)) × (100 + Gain2%)"
    },

    # -------------------------------------------------------------------------
    # HARD (15 Questions: qa-5, qa-6, qa-33 to qa-45)
    # -------------------------------------------------------------------------
    {
        "id": "qa-5",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A vessel contains 80 liters of pure milk. From this, 8 liters is extracted and replaced with water. This process is repeated twice more. How many liters of pure milk remain in the vessel?",
        "options": [
            {"id": "A", "text": "58.32 liters"},
            {"id": "B", "text": "56.40 liters"},
            {"id": "C", "text": "60.00 liters"},
            {"id": "D", "text": "52.88 liters"}
        ],
        "correct_answer": "A",
        "explanation": "Repeated replacement formula: Final Quantity = Initial × [1 - (x / V)]^n. Here Initial = 80, x = 8, V = 80, and process is done 3 times (1 initial + 2 more). Final milk = 80 × (1 - 8/80)^3 = 80 × (9/10)^3 = 80 × 0.729 = 58.32 liters.",
        "formula": "Remaining Liquid = Initial Volume × [1 - (Replacement Volume / Total Volume)]^n"
    },
    {
        "id": "qa-6",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A sum compounded annually amounts to ₹4,840 in 2 years and to ₹5,324 in 3 years. What is the annual interest rate?",
        "options": [
            {"id": "A", "text": "8%"},
            {"id": "B", "text": "9%"},
            {"id": "C", "text": "10%"},
            {"id": "D", "text": "12%"}
        ],
        "correct_answer": "C",
        "explanation": "The interest earned in the 3rd year is on the 2nd year's accumulated amount of ₹4,840. Interest for the 3rd year = 5324 - 4840 = ₹484. Rate of interest R = (484 / 4840) × 100% = 10%.",
        "formula": "Rate R = [(Amount at year n+1 - Amount at year n) / Amount at year n] × 100"
    },
    {
        "id": "qa-33",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "What is the difference between compound interest (compounded annually) and simple interest on a principal of ₹15,000 for 3 years at 10% per annum?",
        "options": [
            {"id": "A", "text": "₹425"},
            {"id": "B", "text": "₹450"},
            {"id": "C", "text": "₹465"},
            {"id": "D", "text": "₹480"}
        ],
        "correct_answer": "C",
        "explanation": "For 3 years, CI - SI = P × (R/100)² × (3 + R/100). Here P = 15000, R = 10. Difference = 15000 × (0.10)² × (3.10) = 15000 × 0.01 × 3.10 = 150 × 3.10 = ₹465.",
        "formula": "CI - SI (3 years) = P × (R/100)² × (3 + R/100)"
    },
    {
        "id": "qa-34",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A dishonest grocer professes to sell his pulses at cost price, but he uses a false weight of 900 grams for a 1-kilogram measure. What is his actual profit percentage?",
        "options": [
            {"id": "A", "text": "10%"},
            {"id": "B", "text": "11.11%"},
            {"id": "C", "text": "12.5%"},
            {"id": "D", "text": "13.33%"}
        ],
        "correct_answer": "B",
        "explanation": "Profit % = [Error / (True Value - Error)] × 100 = [100 / (1000 - 100)] × 100 = (100 / 900) × 100 = 100 / 9 = 11.11%.",
        "formula": "Gain % = [Error / True Weight - Error] × 100"
    },
    {
        "id": "qa-35",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A sum of money invested at compound interest amounts to ₹6,690 after 3 years and to ₹10,035 after 6 years. What was the initial principal amount?",
        "options": [
            {"id": "A", "text": "₹4,200"},
            {"id": "B", "text": "₹4,460"},
            {"id": "C", "text": "₹4,680"},
            {"id": "D", "text": "₹4,850"}
        ],
        "correct_answer": "B",
        "explanation": "Since the time intervals are equal (0 to 3 yrs, 3 to 6 yrs), the growth factor is identical: P × (10035 / 6690) = 6690 => P × (3 / 2) = 6690 => P = (6690 × 2) / 3 = ₹4,460.",
        "formula": "Geometric Progression of CI: P = (Amount_1)² / Amount_2"
    },
    {
        "id": "qa-36",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A container contains 50 liters of pure alcohol. 10 liters are withdrawn and replaced with water. Next, 10 liters of the resulting mixture are withdrawn and replaced with water. How much pure alcohol remains in the container?",
        "options": [
            {"id": "A", "text": "30 liters"},
            {"id": "B", "text": "32 liters"},
            {"id": "C", "text": "34 liters"},
            {"id": "D", "text": "36 liters"}
        ],
        "correct_answer": "B",
        "explanation": "Remaining liquid = Initial × [1 - (x / V)]^n = 50 × [1 - (10 / 50)]² = 50 × (4 / 5)² = 50 × (16 / 25) = 2 × 16 = 32 liters.",
        "formula": "Remaining = Initial × (1 - Removed/Total)^n"
    },
    {
        "id": "qa-37",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A batsman in his 11th innings scores 62 runs, thereby increasing his overall batting average by 2 runs. What is his batting average after the 11th innings?",
        "options": [
            {"id": "A", "text": "40"},
            {"id": "B", "text": "42"},
            {"id": "C", "text": "44"},
            {"id": "D", "text": "46"}
        ],
        "correct_answer": "B",
        "explanation": "Let his batting average for the first 10 innings be A. Total runs in 10 innings = 10A. Adding the 11th innings: 10A + 62 = 11 × (A + 2) => 10A + 62 = 11A + 22 => A = 40. His new batting average after the 11th innings is 40 + 2 = 42.",
        "formula": "New Average = Old Average + Increase; 10A + 62 = 11(A + 2)"
    },
    {
        "id": "qa-38",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "In a 1000-meter race, runner A gives runner B a head start of 100 meters and still beats him by 50 meters. What is the ratio of the speed of runner A to the speed of runner B?",
        "options": [
            {"id": "A", "text": "19 : 17"},
            {"id": "B", "text": "20 : 17"},
            {"id": "C", "text": "20 : 19"},
            {"id": "D", "text": "25 : 21"}
        ],
        "correct_answer": "B",
        "explanation": "In the time runner A covers the full 1000 meters, runner B covers only 1000 - 100 (head start) - 50 (margin of victory) = 850 meters. Ratio of speeds = Distance_A : Distance_B = 1000 : 850 = 20 : 17.",
        "formula": "Speed Ratio = Distance_A / Distance_B (in equal time)"
    },
    {
        "id": "qa-39",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A civil contractor undertakes to build a canal in 120 days and employs 100 laborers. After 45 days, only 1/4 of the total work is completed. How many additional laborers must he hire to complete the canal strictly on schedule?",
        "options": [
            {"id": "A", "text": "60"},
            {"id": "B", "text": "80"},
            {"id": "C", "text": "90"},
            {"id": "D", "text": "100"}
        ],
        "correct_answer": "B",
        "explanation": "Work remaining = 1 - 1/4 = 3/4. Days remaining = 120 - 45 = 75 days. Using (M1 × D1) / W1 = (M2 × D2) / W2: (100 × 45) / (1/4) = (M2 × 75) / (3/4) => 4500 × 4 = M2 × 100 => 180 = M2. Additional laborers needed = 180 - 100 = 80.",
        "formula": "(M1 × D1) / W1 = (M2 × D2) / W2"
    },
    {
        "id": "qa-40",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A train running at 50 km/h crosses a man walking in the opposite direction at 4 km/h in 12 seconds. What is the length of the train in meters?",
        "options": [
            {"id": "A", "text": "160 meters"},
            {"id": "B", "text": "180 meters"},
            {"id": "C", "text": "200 meters"},
            {"id": "D", "text": "220 meters"}
        ],
        "correct_answer": "B",
        "explanation": "Relative speed in opposite directions = 50 + 4 = 54 km/h = 54 × (5/18) = 15 m/s. Train length = Relative Speed × Time = 15 m/s × 12 s = 180 meters.",
        "formula": "Train Length = (Speed_train + Speed_man) × Time"
    },
    {
        "id": "qa-41",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "The compound interest on a certain principal for 2 years at 12% per annum is ₹2,544. What would be the simple interest on the same principal at the same rate for the same time period?",
        "options": [
            {"id": "A", "text": "₹2,200"},
            {"id": "B", "text": "₹2,400"},
            {"id": "C", "text": "₹2,450"},
            {"id": "D", "text": "₹2,500"}
        ],
        "correct_answer": "B",
        "explanation": "CI rate for 2 years = 12 + 12 + (12 × 12)/100 = 25.44%. Simple interest rate = 12 × 2 = 24%. SI = 2544 × (24 / 25.44) = ₹2,400.",
        "formula": "SI = CI × [2R / (2R + R²/100)]"
    },
    {
        "id": "qa-42",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A 20% reduction in the price of sugar enables a consumer to buy 4 kg more sugar for ₹160. What is the reduced price of sugar per kg?",
        "options": [
            {"id": "A", "text": "₹6 per kg"},
            {"id": "B", "text": "₹8 per kg"},
            {"id": "C", "text": "₹10 per kg"},
            {"id": "D", "text": "₹12 per kg"}
        ],
        "correct_answer": "B",
        "explanation": "Money saved due to 20% discount = 20% of 160 = ₹32. This ₹32 buys 4 kg of extra sugar at the reduced rate. Reduced rate per kg = 32 / 4 = ₹8 per kg.",
        "formula": "Reduced Price per kg = (Total Money × % Reduction) / (100 × Extra Quantity)"
    },
    {
        "id": "qa-43",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A motorboat can travel 30 km downstream and return to the starting point upstream in a total of 8 hours. If the speed of the river current is 2 km/h, what is the speed of the motorboat in still water?",
        "options": [
            {"id": "A", "text": "6 km/h"},
            {"id": "B", "text": "8 km/h"},
            {"id": "C", "text": "10 km/h"},
            {"id": "D", "text": "12 km/h"}
        ],
        "correct_answer": "B",
        "explanation": "Let still water speed be b. 30/(b + 2) + 30/(b - 2) = 8 => 30(2b)/(b² - 4) = 8 => 60b = 8b² - 32 => 8b² - 60b - 32 = 0 => 2b² - 15b - 8 = 0 => (2b + 1)(b - 8) = 0 => b = 8 km/h.",
        "formula": "Total Time = D/(b + c) + D/(b - c)"
    },
    {
        "id": "qa-44",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "Two vessels A and B contain milk and water in the ratios 7 : 2 and 5 : 1 respectively. In what ratio must the contents of both vessels be blended to obtain a mixture with milk and water in the ratio 8 : 2 (4 : 1)?",
        "options": [
            {"id": "A", "text": "1 : 2"},
            {"id": "B", "text": "2 : 1"},
            {"id": "C", "text": "3 : 2"},
            {"id": "D", "text": "2 : 3"}
        ],
        "correct_answer": "C",
        "explanation": "Fraction of milk in Vessel A is 7/9, and in Vessel B is 5/6. The desired mixture has milk fraction 4/5. Using alligation: (5/6 - 4/5) : (4/5 - 7/9) = (1/30) : (1/45) = 45 : 30 = 3 : 2. Hence, the liquids must be mixed in the ratio 3 : 2.",
        "formula": "Alligation of fractions: |Fraction_B - Mean| / |Mean - Fraction_A|"
    },
    {
        "id": "qa-45",
        "topic": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A batsman in his 17th innings scores 85 runs, thereby increasing his overall batting average by 3 runs. What is his batting average after the 17th innings?",
        "options": [
            {"id": "A", "text": "34"},
            {"id": "B", "text": "37"},
            {"id": "C", "text": "39"},
            {"id": "D", "text": "40"}
        ],
        "correct_answer": "B",
        "explanation": "Let average of 16 innings be A. Total runs in 16 innings = 16A. In 17th innings: 16A + 85 = 17 × (A + 3) => 16A + 85 = 17A + 51 => A = 34. New average after 17th innings = 34 + 3 = 37.",
        "formula": "New Average = Old Average + Increase; 16A + 85 = 17(A + 3)"
    }
]
