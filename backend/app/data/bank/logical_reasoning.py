# -*- coding: utf-8 -*-
"""
Logical Reasoning Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

LOGICAL_REASONING_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "lr-1",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "In a row of 35 students facing north, Priya is 12th from the left end. What is her position from the right end?",
        "options": [
            {
                "id": "A",
                "text": "23rd"
            },
            {
                "id": "B",
                "text": "24th"
            },
            {
                "id": "C",
                "text": "25th"
            },
            {
                "id": "D",
                "text": "22nd"
            }
        ],
        "correct_answer": "B",
        "explanation": "Position from right end = Total students - Position from left end + 1. Position = 35 - 12 + 1 = 24th.",
        "formula": "Rank from other end = Total - Given Rank + 1"
    },
    {
        "id": "lr-2",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Book is to Reading as Fork is to:",
        "options": [
            {
                "id": "A",
                "text": "Writing"
            },
            {
                "id": "B",
                "text": "Cooking"
            },
            {
                "id": "C",
                "text": "Eating"
            },
            {
                "id": "D",
                "text": "Cutting"
            }
        ],
        "correct_answer": "C",
        "explanation": "The relationship is object and its primary direct human purpose. A book is used for reading; a fork is used for eating.",
        "formula": "Analogy Rule: [Tool] is to [Primary Function]"
    },
    {
        "id": "lr-7",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "In a class of 40 students, Rohan ranks 15th from the top. What is his rank from the bottom?",
        "options": [
            {
                "id": "A",
                "text": "25th"
            },
            {
                "id": "B",
                "text": "26th"
            },
            {
                "id": "C",
                "text": "27th"
            },
            {
                "id": "D",
                "text": "24th"
            }
        ],
        "correct_answer": "B",
        "explanation": "Rank from bottom = Total students - Rank from top + 1. Here: 40 - 15 + 1 = 26th.",
        "formula": "Rank from bottom = Total - Rank from top + 1"
    },
    {
        "id": "lr-8",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Doctor is to Patient as Teacher is to:",
        "options": [
            {
                "id": "A",
                "text": "School"
            },
            {
                "id": "B",
                "text": "Student"
            },
            {
                "id": "C",
                "text": "Books"
            },
            {
                "id": "D",
                "text": "Classroom"
            }
        ],
        "correct_answer": "B",
        "explanation": "A doctor provides professional care to a patient; similarly, a teacher provides professional education to a student.",
        "formula": "Analogy: Professional is to Client/Recipient"
    },
    {
        "id": "lr-9",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Pointing to a photograph of a boy, Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?",
        "options": [
            {
                "id": "A",
                "text": "Brother"
            },
            {
                "id": "B",
                "text": "Father"
            },
            {
                "id": "C",
                "text": "Uncle"
            },
            {
                "id": "D",
                "text": "Grandfather"
            }
        ],
        "correct_answer": "B",
        "explanation": "The 'only son of Suresh's mother' is Suresh himself. Therefore, the boy is the son of Suresh. Suresh is the boy's father.",
        "formula": "Only son of my mother = Myself (for a male speaker)"
    },
    {
        "id": "lr-10",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "If South-East becomes North, North-East becomes West, and so on, what will West become?",
        "options": [
            {
                "id": "A",
                "text": "South-East"
            },
            {
                "id": "B",
                "text": "South-West"
            },
            {
                "id": "C",
                "text": "North-East"
            },
            {
                "id": "D",
                "text": "North-West"
            }
        ],
        "correct_answer": "A",
        "explanation": "The entire compass rotates 135 degrees counter-clockwise (South-East at 135° becomes North at 0°, a rotation of 135° CCW). Turning West (270°) by 135° counter-clockwise brings it to 135°, which is South-East.",
        "formula": "Compass Rotation: Angle of Shift = 135° CCW"
    },
    {
        "id": "lr-11",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Find the odd one out from the given group: Apple, Mango, Potato, Banana.",
        "options": [
            {
                "id": "A",
                "text": "Apple"
            },
            {
                "id": "B",
                "text": "Mango"
            },
            {
                "id": "C",
                "text": "Potato"
            },
            {
                "id": "D",
                "text": "Banana"
            }
        ],
        "correct_answer": "C",
        "explanation": "Apple, Mango, and Banana are fruits that grow on trees/plants above ground, whereas Potato is a tuber vegetable that grows underground.",
        "formula": "Classification: Botanical category & growth environment"
    },
    {
        "id": "lr-12",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "If '+' means '×', '×' means '÷', and '÷' means '+', what is the value of 12 + 4 × 2 ÷ 6?",
        "options": [
            {
                "id": "A",
                "text": "30"
            },
            {
                "id": "B",
                "text": "24"
            },
            {
                "id": "C",
                "text": "18"
            },
            {
                "id": "D",
                "text": "36"
            }
        ],
        "correct_answer": "A",
        "explanation": "Substituting the operators: 12 × 4 ÷ 2 + 6. Applying BODMAS: 12 × (4 ÷ 2) + 6 = 12 × 2 + 6 = 24 + 6 = 30.",
        "formula": "Operator substitution followed by standard BODMAS priority"
    },
    {
        "id": "lr-13",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Arrange the following in a meaningful developmental order: 1. Seed, 2. Plant, 3. Fruit, 4. Tree, 5. Flower.",
        "options": [
            {
                "id": "A",
                "text": "1, 2, 4, 5, 3"
            },
            {
                "id": "B",
                "text": "1, 2, 5, 4, 3"
            },
            {
                "id": "C",
                "text": "2, 1, 4, 5, 3"
            },
            {
                "id": "D",
                "text": "1, 4, 2, 5, 3"
            }
        ],
        "correct_answer": "A",
        "explanation": "Natural life cycle: Seed (1) germinates into a Plant (2), which grows into a Tree (4), produces Flowers (5), which turn into Fruit (3). Thus, 1, 2, 4, 5, 3.",
        "formula": "Sequential order of botanical growth"
    },
    {
        "id": "lr-14",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Pen is to Ink as Needle is to:",
        "options": [
            {
                "id": "A",
                "text": "Cloth"
            },
            {
                "id": "B",
                "text": "Thread"
            },
            {
                "id": "C",
                "text": "Stitch"
            },
            {
                "id": "D",
                "text": "Sewing"
            }
        ],
        "correct_answer": "B",
        "explanation": "Ink is the essential medium passed through or fed into a pen to write; similarly, thread is the essential material passed through a needle to sew.",
        "formula": "Tool to Medium relationship"
    },
    {
        "id": "lr-15",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Introducing a girl, Vipin said, 'Her mother is the only daughter of my mother-in-law.' How is Vipin related to the girl?",
        "options": [
            {
                "id": "A",
                "text": "Uncle"
            },
            {
                "id": "B",
                "text": "Father"
            },
            {
                "id": "C",
                "text": "Brother"
            },
            {
                "id": "D",
                "text": "Husband"
            }
        ],
        "correct_answer": "B",
        "explanation": "The only daughter of Vipin's mother-in-law is Vipin's wife. The girl's mother is Vipin's wife. Therefore, Vipin is the father of the girl.",
        "formula": "Only daughter of mother-in-law = Wife"
    },
    {
        "id": "lr-16",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Which of the following words CANNOT be formed using the letters of the word 'MEASUREMENT'?",
        "options": [
            {
                "id": "A",
                "text": "MASTER"
            },
            {
                "id": "B",
                "text": "STEAM"
            },
            {
                "id": "C",
                "text": "SUMMIT"
            },
            {
                "id": "D",
                "text": "MEETS"
            }
        ],
        "correct_answer": "C",
        "explanation": "The word 'SUMMIT' requires the letter 'I', but the word 'MEASUREMENT' does not contain the letter 'I'.",
        "formula": "Character frequency and presence check"
    },
    {
        "id": "lr-17",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "If 1st January 2006 was a Sunday, what day of the week was 1st January 2007?",
        "options": [
            {
                "id": "A",
                "text": "Monday"
            },
            {
                "id": "B",
                "text": "Tuesday"
            },
            {
                "id": "C",
                "text": "Sunday"
            },
            {
                "id": "D",
                "text": "Wednesday"
            }
        ],
        "correct_answer": "A",
        "explanation": "2006 is an ordinary non-leap year having 365 days. 365 ÷ 7 = 52 weeks and 1 odd day. Therefore, the day advances by 1 odd day: Sunday + 1 = Monday.",
        "formula": "Ordinary Year = 1 Odd Day"
    },
    {
        "id": "lr-18",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "What is the angle between the hour hand and minute hand of a clock at 3:30?",
        "options": [
            {
                "id": "A",
                "text": "70°"
            },
            {
                "id": "B",
                "text": "75°"
            },
            {
                "id": "C",
                "text": "80°"
            },
            {
                "id": "D",
                "text": "85°"
            }
        ],
        "correct_answer": "B",
        "explanation": "Angle formula: |30H - (11/2)M|. For H=3, M=30: |30(3) - (11/2)(30)| = |90 - 165| = |-75| = 75°.",
        "formula": "Clock Angle = |30H - 5.5M|"
    },
    {
        "id": "lr-19",
        "topic": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "In a row of trees, a tree is 7th from either end of the row. How many trees are there in the row?",
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
                "text": "15"
            },
            {
                "id": "D",
                "text": "12"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total = Rank from left + Rank from right - 1. Total = 7 + 7 - 1 = 13 trees.",
        "formula": "Total = R1 + R2 - 1"
    },
    {
        "id": "lr-3",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Five friends A, B, C, D, and E are sitting around a circular table facing the center. A sits to the immediate left of B. C sits between B and D. Who sits to the immediate left of A?",
        "options": [
            {
                "id": "A",
                "text": "D"
            },
            {
                "id": "B",
                "text": "E"
            },
            {
                "id": "C",
                "text": "C"
            },
            {
                "id": "D",
                "text": "B"
            }
        ],
        "correct_answer": "B",
        "explanation": "Facing center: B is seated. A is to the immediate left of B. Since C sits between B and D, going clockwise/counter-clockwise from B gives D - C - B. The remaining position to the left of A must be filled by E.",
        "formula": "Circular Arrangement: Facing Center implies Left is Clockwise, Right is Counter-Clockwise"
    },
    {
        "id": "lr-4",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "A is the brother of B. C is the father of A. D is the brother of E. E is the daughter of B. How is D related to A?",
        "options": [
            {
                "id": "A",
                "text": "Son"
            },
            {
                "id": "B",
                "text": "Nephew"
            },
            {
                "id": "C",
                "text": "Brother"
            },
            {
                "id": "D",
                "text": "Uncle"
            }
        ],
        "correct_answer": "B",
        "explanation": "B is the parent of E. D is the brother of E, so D is the son of B. A is the brother of B. The son of one's sibling is a nephew. Thus, D is the nephew of A.",
        "formula": "Family Tree: Brother's/Sister's son = Nephew"
    },
    {
        "id": "lr-20",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Six friends A, B, C, D, E, and F sit around a circular table facing the center. A is second to the left of C. B is to the immediate right of A. D is between A and F. Who is sitting opposite to B?",
        "options": [
            {
                "id": "A",
                "text": "E"
            },
            {
                "id": "B",
                "text": "F"
            },
            {
                "id": "C",
                "text": "C"
            },
            {
                "id": "D",
                "text": "D"
            }
        ],
        "correct_answer": "B",
        "explanation": "In a 6-seat circle facing center: Place C at position 1. Second to left of C is position 3 (A). Immediate right of A is position 2 (B). D is between A and F, so D is position 4 and F is position 5. Position 6 is E. Opposite pairs are (1,4), (2,5), (3,6). Opposite to B (pos 2) is F (pos 5).",
        "formula": "Circular Arrangement: Opposite position in 6-seat circle = (pos + 3) mod 6"
    },
    {
        "id": "lr-21",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "P is Q's sister. R is Q's mother. S is R's father. T is S's mother. How is P related to S?",
        "options": [
            {
                "id": "A",
                "text": "Granddaughter"
            },
            {
                "id": "B",
                "text": "Daughter"
            },
            {
                "id": "C",
                "text": "Grandmother"
            },
            {
                "id": "D",
                "text": "Aunt"
            }
        ],
        "correct_answer": "A",
        "explanation": "P is female and sibling of Q. R is mother of P and Q. S is father of R. Therefore, P is the daughter of S's daughter, which means P is S's granddaughter.",
        "formula": "Daughter's daughter = Granddaughter"
    },
    {
        "id": "lr-22",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "A person walks 10 meters North, turns right and walks 15 meters, turns right and walks 10 meters, and then turns left and walks 5 meters. How far and in which direction is the person from the starting point?",
        "options": [
            {
                "id": "A",
                "text": "20 meters East"
            },
            {
                "id": "B",
                "text": "15 meters East"
            },
            {
                "id": "C",
                "text": "20 meters North"
            },
            {
                "id": "D",
                "text": "25 meters East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Starting at (0, 0): 10m North -> (0, 10). Right turn (East) 15m -> (15, 10). Right turn (South) 10m -> (15, 0). Left turn (East) 5m -> (20, 0). The final point is (20, 0), which is 20 meters directly East of the origin.",
        "formula": "Coordinate tracking: (x, y) displacement vector"
    },
    {
        "id": "lr-23",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Statement: 'Should high-speed internet access be treated as a fundamental public utility for all citizens?'\nArguments:\nI. Yes, because digital infrastructure is now critical for schooling, governance, and daily livelihood.\nII. No, because the government budget should be allocated only to food and physical roads.",
        "options": [
            {
                "id": "A",
                "text": "Only argument I is strong"
            },
            {
                "id": "B",
                "text": "Only argument II is strong"
            },
            {
                "id": "C",
                "text": "Both I and II are strong"
            },
            {
                "id": "D",
                "text": "Neither I nor II is strong"
            }
        ],
        "correct_answer": "A",
        "explanation": "Argument I is strong because it provides a realistic, positive justification reflecting the modern reality of digital reliance. Argument II is weak and flawed because public spending is not mutually exclusive to only food and roads.",
        "formula": "Critical Reasoning: Logical relevance and non-fallacious rationale"
    },
    {
        "id": "lr-24",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Statements: A > B, B >= C, C = D, D < E. Which of the following conclusions is definitely true?",
        "options": [
            {
                "id": "A",
                "text": "A > D"
            },
            {
                "id": "B",
                "text": "B < E"
            },
            {
                "id": "C",
                "text": "A < C"
            },
            {
                "id": "D",
                "text": "D > B"
            }
        ],
        "correct_answer": "A",
        "explanation": "Connecting the chain: A > B >= C = D. Since A > B and B >= D, A > D is definitely true. Comparison between B and E is indeterminate because B >= D and E > D.",
        "formula": "Inequality Transitivity: A > B and B >= D => A > D"
    },
    {
        "id": "lr-25",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Statement I: The municipal authority declared a 30% cut in daily water supply for the upcoming week.\nStatement II: There was a major rupture in the city's main conduit pipeline during subway tunneling work.",
        "options": [
            {
                "id": "A",
                "text": "Statement II is the cause and Statement I is its effect"
            },
            {
                "id": "B",
                "text": "Statement I is the cause and Statement II is its effect"
            },
            {
                "id": "C",
                "text": "Both are independent causes"
            },
            {
                "id": "D",
                "text": "Both are effects of independent causes"
            }
        ],
        "correct_answer": "A",
        "explanation": "The rupture of the main conduit pipeline (Statement II) directly caused the municipal authority to reduce daily water supply (Statement I). Hence II is the cause and I is the effect.",
        "formula": "Cause and Effect Analysis"
    },
    {
        "id": "lr-26",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "A cube painted red on all faces is cut into 64 identical small cubes. How many small cubes have exactly two faces painted red?",
        "options": [
            {
                "id": "A",
                "text": "24"
            },
            {
                "id": "B",
                "text": "16"
            },
            {
                "id": "C",
                "text": "32"
            },
            {
                "id": "D",
                "text": "12"
            }
        ],
        "correct_answer": "A",
        "explanation": "For n^3 = 64, n = 4. Cubes with exactly two painted faces are located along the 12 edges (excluding the corners): Formula = 12 × (n - 2). Here 12 × (4 - 2) = 12 × 2 = 24 cubes.",
        "formula": "Two-face painted cubes = 12 × (n - 2)"
    },
    {
        "id": "lr-27",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "At what time between 4 and 5 o'clock will the two hands of a clock coincide (be together)?",
        "options": [
            {
                "id": "A",
                "text": "21 (9/11) minutes past 4"
            },
            {
                "id": "B",
                "text": "22 (8/11) minutes past 4"
            },
            {
                "id": "C",
                "text": "20 minutes past 4"
            },
            {
                "id": "D",
                "text": "21 (5/11) minutes past 4"
            }
        ],
        "correct_answer": "A",
        "explanation": "At 4 o'clock, the minute hand is 20 minute spaces behind the hour hand. Relative speed of minute hand over hour hand is 55 spaces per 60 minutes = 11/12 space per minute. Time required = 20 ÷ (11/12) = 20 × (12/11) = 240/11 = 21 (9/11) minutes past 4.",
        "formula": "Coincidence time = (60/11) × H minutes past H"
    },
    {
        "id": "lr-28",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Among five friends P, Q, R, S, and T: P scored more than Q but less than R. S scored more than T but less than Q. Who scored the highest?",
        "options": [
            {
                "id": "A",
                "text": "R"
            },
            {
                "id": "B",
                "text": "P"
            },
            {
                "id": "C",
                "text": "S"
            },
            {
                "id": "D",
                "text": "Q"
            }
        ],
        "correct_answer": "A",
        "explanation": "From the clues: R > P > Q, and Q > S > T. Combining them gives: R > P > Q > S > T. Therefore, R scored the highest.",
        "formula": "Linear ordering of transitive inequalities"
    },
    {
        "id": "lr-29",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Question: Is X older than Y?\nStatements:\nI. X's age is 5 years more than Z's age.\nII. Z's age is 2 years less than Y's age.\nTo answer the question:",
        "options": [
            {
                "id": "A",
                "text": "Both statements I and II together are sufficient"
            },
            {
                "id": "B",
                "text": "Statement I alone is sufficient"
            },
            {
                "id": "C",
                "text": "Statement II alone is sufficient"
            },
            {
                "id": "D",
                "text": "Neither statement is sufficient"
            }
        ],
        "correct_answer": "A",
        "explanation": "From I: X = Z + 5. From II: Z = Y - 2, so Y = Z + 2. Comparing X and Y: X = Z + 5 and Y = Z + 2, therefore X = Y + 3, so X is definitely older than Y. Both statements together are required and sufficient.",
        "formula": "Data Sufficiency: Combining linear relations"
    },
    {
        "id": "lr-30",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "In a certain year, the month of March had exactly 5 Sundays. Which of the following days could 1st March have been?",
        "options": [
            {
                "id": "A",
                "text": "Friday"
            },
            {
                "id": "B",
                "text": "Wednesday"
            },
            {
                "id": "C",
                "text": "Thursday"
            },
            {
                "id": "D",
                "text": "Tuesday"
            }
        ],
        "correct_answer": "A",
        "explanation": "March has 31 days (4 weeks and 3 extra days). For Sunday to occur 5 times, Sunday must fall on the 29th, 30th, or 31st of March. If Sunday is 31st, then 1st March is a Friday (31 - 1 = 30 days = 4 weeks + 2 days; Friday + 2 = Sunday). Thus, 1st March could be Friday.",
        "formula": "Extra days rule: 31 days month has 5 occurrences for days falling on 1st, 2nd, and 3rd."
    },
    {
        "id": "lr-31",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "A clock gains 5 seconds every 3 minutes. It was set right at 7:00 AM. In the afternoon of the same day, when the watch indicated quarter past 4 o'clock (4:15 PM), what was the true time?",
        "options": [
            {
                "id": "A",
                "text": "4:00 PM"
            },
            {
                "id": "B",
                "text": "3:45 PM"
            },
            {
                "id": "C",
                "text": "4:10 PM"
            },
            {
                "id": "D",
                "text": "4:05 PM"
            }
        ],
        "correct_answer": "A",
        "explanation": "Gain rate: 5 seconds in 3 minutes = 100 seconds per hour = 1 minute 40 seconds per hour = 5/3 minutes per hour. Clock shows 37/36 of true time. From 7:00 AM to 4:15 PM is 9 hours 15 minutes = 37/4 hours. True time = (37/4) × (36/37) = 9 hours. 7:00 AM + 9 hours = 4:00 PM.",
        "formula": "Faulty clock ratio: True Time = Indicated Time × (Standard Unit / Gaining Unit)"
    },
    {
        "id": "lr-32",
        "topic": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Seven athletes P, Q, R, S, T, U, and V finish a race. P finishes before Q but behind R. S finishes before T but behind U. If R finishes behind U and Q finishes before S, who finished third?",
        "options": [
            {
                "id": "A",
                "text": "P"
            },
            {
                "id": "B",
                "text": "R"
            },
            {
                "id": "C",
                "text": "Q"
            },
            {
                "id": "D",
                "text": "S"
            }
        ],
        "correct_answer": "A",
        "explanation": "Ordering relations: U > R (R is behind U). R > P > Q (P before Q, behind R). Q > S (Q before S). S > T (S before T). Combined order: U > R > P > Q > S > T. Third position is P.",
        "formula": "Chain of strict orderings"
    },
    {
        "id": "lr-5",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Statement: 'The company decided to terminate the contract of vendor X due to consistent supply delays.'\nAssumptions:\nI. Other vendors are available in the market who can supply on time.\nII. Supply delays adversely affect the operations of the company.",
        "options": [
            {
                "id": "A",
                "text": "Only assumption I is implicit"
            },
            {
                "id": "B",
                "text": "Only assumption II is implicit"
            },
            {
                "id": "C",
                "text": "Neither I nor II is implicit"
            },
            {
                "id": "D",
                "text": "Both I and II are implicit"
            }
        ],
        "correct_answer": "D",
        "explanation": "Terminating a critical contract assumes alternative vendors can step in (Assumption I) and that supply delays cause sufficient operational harm to justify termination (Assumption II). Hence both assumptions are implicit.",
        "formula": "Critical Reasoning: Implicit assumption is an unstated premise necessary for the decision to be rational."
    },
    {
        "id": "lr-6",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Six people P, Q, R, S, T, and U sit in two parallel rows of three each, facing each other. Row 1 faces South and Row 2 faces North. P is at an extreme end and faces T. Q sits to the immediate right of T. R is opposite to S. If U does not sit at an extreme end, who sits opposite to Q?",
        "options": [
            {
                "id": "A",
                "text": "P"
            },
            {
                "id": "B",
                "text": "U"
            },
            {
                "id": "C",
                "text": "R"
            },
            {
                "id": "D",
                "text": "S"
            }
        ],
        "correct_answer": "B",
        "explanation": "Row 2 faces North: T is at one end (opposite P). Q is to the immediate right of T (middle seat of Row 2). The middle seat of Row 1 must be occupied by U since U is not at an extreme end. Hence U is opposite Q.",
        "formula": "Parallel Row Geometry: Extreme positions = ends; Non-extreme = middle column."
    },
    {
        "id": "lr-33",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Eight people A, B, C, D, E, F, G, and H sit around a circular table. Four face towards the center and four face outward. No two adjacent persons face the same direction. A faces center and sits opposite to E. B sits to the immediate left of A. Which direction does B face?",
        "options": [
            {
                "id": "A",
                "text": "Away from center (outward)"
            },
            {
                "id": "B",
                "text": "Towards the center"
            },
            {
                "id": "C",
                "text": "Cannot be determined"
            },
            {
                "id": "D",
                "text": "Same as A"
            }
        ],
        "correct_answer": "A",
        "explanation": "Since no two adjacent persons face the same direction, the directions must strictly alternate: Center, Outward, Center, Outward... around the 8 seats. Since A faces towards the center, both immediate neighbors of A must face the opposite direction, which is away from the center (outward). B is an immediate neighbor, so B faces outward.",
        "formula": "Alternating parity constraint: Adjacent(Center) = Outward"
    },
    {
        "id": "lr-34",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Seven people live on floors 1 to 7 of a building. P lives on floor 3. Exactly two people live between P and Q (with Q on a higher floor). R lives on the floor immediately above Q. S lives on an even-numbered floor. If Q lives on floor 6 and R lives on floor 7, which floor does S live on if S lives on a lower floor than P?",
        "options": [
            {
                "id": "A",
                "text": "Floor 2"
            },
            {
                "id": "B",
                "text": "Floor 4"
            },
            {
                "id": "C",
                "text": "Floor 1"
            },
            {
                "id": "D",
                "text": "Floor 6"
            }
        ],
        "correct_answer": "A",
        "explanation": "P lives on floor 3. Floors below P are 1 and 2. The only even-numbered floor below floor 3 is floor 2. Since S lives on an even-numbered floor lower than P, S must live on floor 2.",
        "formula": "Floor puzzle constraint satisfaction"
    },
    {
        "id": "lr-35",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Statement: Despite repeated advisories, commuters continue to cross railway tracks directly rather than using the overbridge, resulting in fatal accidents.\nCourses of Action:\nI. The railway authorities should immediately erect fencing between the tracks and strictly penalize violators.\nII. The railway authorities should close down the railway station permanently.",
        "options": [
            {
                "id": "A",
                "text": "Only Course of Action I follows"
            },
            {
                "id": "B",
                "text": "Only Course of Action II follows"
            },
            {
                "id": "C",
                "text": "Both I and II follow"
            },
            {
                "id": "D",
                "text": "Neither follows"
            }
        ],
        "correct_answer": "A",
        "explanation": "Course of action I directly addresses the problem with practical physical barriers and regulatory enforcement. Course of action II is completely disproportionate and causes severe public disruption without solving the core behavioral issue. Therefore, only I follows.",
        "formula": "Critical Reasoning: Feasible and proportionate course of action"
    },
    {
        "id": "lr-36",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "If 'P + Q' means P is the father of Q, 'P - Q' means P is the wife of Q, 'P × Q' means P is the brother of Q, and 'P ÷ Q' means P is the daughter of Q. Which of the following expressions indicates that 'M is the maternal uncle of N'?",
        "options": [
            {
                "id": "A",
                "text": "M × T - K + N"
            },
            {
                "id": "B",
                "text": "M + T × K ÷ N"
            },
            {
                "id": "C",
                "text": "M ÷ T - K × N"
            },
            {
                "id": "D",
                "text": "M × T + K - N"
            }
        ],
        "correct_answer": "A",
        "explanation": "For M to be the maternal uncle of N, M must be a male and the brother of N's mother. In 'M × T - K + N': M × T means M is brother of T (M is male). T - K means T is wife of K. K + N means K is father of N. Since T is wife of K and K is father of N, T is the mother of N. Since M is brother of T, M is the maternal uncle of N.",
        "formula": "Coded Blood Relations: Mother's brother = Maternal Uncle"
    },
    {
        "id": "lr-37",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "In an analytical arrangement, five colleagues J, K, L, M, and N have distinct project deadlines from Monday to Friday of the same week. K's deadline is immediately before L's. Only one person has a deadline between K and M. J's deadline is on Friday. On which day is N's deadline?",
        "options": [
            {
                "id": "A",
                "text": "Monday"
            },
            {
                "id": "B",
                "text": "Wednesday"
            },
            {
                "id": "C",
                "text": "Thursday"
            },
            {
                "id": "D",
                "text": "Tuesday"
            }
        ],
        "correct_answer": "A",
        "explanation": "Days are Mon, Tue, Wed, Thu, Fri. J is on Friday. That leaves Mon, Tue, Wed, Thu for K, L, M, N. K is immediately before L (K, L consecutive). Exactly one person is between K and M: if K is Tue and L is Wed, M can be Thu (one between K and M is L? No, between K(Tue) and M(Thu) is Wed!). Then N must be on Monday! Let's check: K=Tue, L=Wed, M=Thu, N=Mon, J=Fri. K immediately before L (Tue, Wed)? Yes. Exactly one person between K (Tue) and M (Thu)? Yes (L on Wed). J on Friday? Yes. Thus N's deadline is on Monday.",
        "formula": "Linear Scheduling Grid Elimination"
    },
    {
        "id": "lr-38",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "A research study concluded that employees who drink three or more cups of coffee per day have 20% higher task productivity than those who drink no coffee. Which of the following, if true, most seriously weakens the argument that drinking coffee causes higher productivity?",
        "options": [
            {
                "id": "A",
                "text": "Employees assigned to higher-workload and critical projects naturally drink more coffee to stay alert."
            },
            {
                "id": "B",
                "text": "Coffee contains caffeine which is known to stimulate cognitive alertness."
            },
            {
                "id": "C",
                "text": "Some employees prefer tea over coffee."
            },
            {
                "id": "D",
                "text": "Drinking excessive coffee can occasionally disrupt sleep patterns."
            }
        ],
        "correct_answer": "A",
        "explanation": "Option A points out reverse causation: high workload and demanding tasks cause employees to consume more coffee, rather than coffee causing higher productivity. This directly undermines the causal conclusion.",
        "formula": "Critical Reasoning: Reverse Causality weakens correlation-based causal claims"
    },
    {
        "id": "lr-39",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "An input-output number sorting machine rearranges input numbers in steps. In each step, the smallest remaining number is moved to the left and the largest remaining number is moved to the right. Given Input: '45 12 89 23 67 34'. What is the arrangement in Step 1?",
        "options": [
            {
                "id": "A",
                "text": "12 45 23 67 34 89"
            },
            {
                "id": "B",
                "text": "12 89 45 23 67 34"
            },
            {
                "id": "C",
                "text": "89 45 12 23 67 34"
            },
            {
                "id": "D",
                "text": "12 23 34 45 67 89"
            }
        ],
        "correct_answer": "A",
        "explanation": "The smallest number in the input is 12 (moves to extreme left) and the largest is 89 (moves to extreme right). The remaining numbers (45, 23, 67, 34) maintain their relative order in the middle: '12 45 23 67 34 89'.",
        "formula": "Machine Input-Output: Stepwise extremal sorting"
    },
    {
        "id": "lr-40",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Six people P, Q, R, S, T, and U sit in a row. Some face North and some face South. P sits at an extreme end and faces North. Q sits second to the right of P. R sits to the immediate left of Q and faces South. If adjacent people face opposite directions, which direction does the person at the other extreme end face?",
        "options": [
            {
                "id": "A",
                "text": "South"
            },
            {
                "id": "B",
                "text": "North"
            },
            {
                "id": "C",
                "text": "Cannot be determined"
            },
            {
                "id": "D",
                "text": "Same as P"
            }
        ],
        "correct_answer": "A",
        "explanation": "There are 6 positions (1 to 6). Since adjacent people face opposite directions, the facing directions alternate strictly: Pos 1 (P) = North, Pos 2 = South, Pos 3 = North, Pos 4 = South, Pos 5 = North, Pos 6 = South. Therefore, the person at position 6 (the other extreme end) faces South.",
        "formula": "Parity alternation in linear arrangements: Direction(i) = (-1)^(i-1)"
    },
    {
        "id": "lr-41",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Statement: 'The state government has banned single-use plastics and mandated heavy fines on retail merchants found storing or distributing plastic bags.'\nAssumptions:\nI. Retail merchants have accessible and viable eco-friendly packaging alternatives available.\nII. Monetary penalties act as an effective deterrent against non-compliance.",
        "options": [
            {
                "id": "A",
                "text": "Both assumptions I and II are implicit"
            },
            {
                "id": "B",
                "text": "Only assumption I is implicit"
            },
            {
                "id": "C",
                "text": "Only assumption II is implicit"
            },
            {
                "id": "D",
                "text": "Neither assumption is implicit"
            }
        ],
        "correct_answer": "A",
        "explanation": "Banning single-use plastics and holding merchants accountable assumes that viable alternatives exist so commerce can continue (Assumption I). Imposing heavy fines assumes that penalties will effectively deter merchants from continuing the practice (Assumption II). Both are necessary unstated premises.",
        "formula": "Critical Reasoning: Necessary presuppositions for policy efficacy"
    },
    {
        "id": "lr-42",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Among four boxes A, B, C, and D of different weights: A is heavier than B. C is lighter than D. Is D the heaviest box?\nStatement I: C is heavier than A.\nStatement II: B is lighter than D.\nWhich statement(s) are sufficient to answer?",
        "options": [
            {
                "id": "A",
                "text": "Statement I alone is sufficient"
            },
            {
                "id": "B",
                "text": "Statement II alone is sufficient"
            },
            {
                "id": "C",
                "text": "Both together are necessary"
            },
            {
                "id": "D",
                "text": "Neither is sufficient"
            }
        ],
        "correct_answer": "A",
        "explanation": "Given: A > B and D > C. Statement I gives C > A. Combining them: D > C > A > B. This establishes that D is heavier than all other three boxes, so D is definitely the heaviest box. Thus, Statement I alone is sufficient.",
        "formula": "Data Sufficiency: Linear inequality closure"
    },
    {
        "id": "lr-43",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Given the conditional statements:\n1. If the project receives funding (P), then the laboratory will hire researchers (Q).\n2. If the laboratory hires researchers (Q), then new clinical trials will begin (R).\n3. New clinical trials did NOT begin (~R).\nWhat valid conclusion can be deduced?",
        "options": [
            {
                "id": "A",
                "text": "The project did not receive funding"
            },
            {
                "id": "B",
                "text": "The project received funding"
            },
            {
                "id": "C",
                "text": "Researchers were hired anyway"
            },
            {
                "id": "D",
                "text": "No conclusion can be drawn"
            }
        ],
        "correct_answer": "A",
        "explanation": "By Modus Tollens on premise 2: Q -> R and ~R implies ~Q (researchers were not hired). Then by Modus Tollens on premise 1: P -> Q and ~Q implies ~P (the project did not receive funding).",
        "formula": "Modus Tollens: (P -> Q) and ~Q => ~P"
    },
    {
        "id": "lr-44",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "In a group of executives: Z is older than V. V is older than Y. Y is older than X. X is older than W. Who is the oldest executive?",
        "options": [
            {
                "id": "A",
                "text": "Z"
            },
            {
                "id": "B",
                "text": "V"
            },
            {
                "id": "C",
                "text": "Y"
            },
            {
                "id": "D",
                "text": "X"
            }
        ],
        "correct_answer": "A",
        "explanation": "The strictly descending age ordering is Z > V > Y > X > W. Therefore, Z is the oldest executive.",
        "formula": "Transitive Ordering on Multiple Attributes"
    },
    {
        "id": "lr-45",
        "topic": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Statements: P © Q means P >= Q; P @ Q means P > Q; P $ Q means P = Q; P % Q means P < Q.\nGiven: M @ N, N © O, O $ P.\nConclusions:\nI. M @ P\nII. N © P",
        "options": [
            {
                "id": "A",
                "text": "Both conclusions I and II are true"
            },
            {
                "id": "B",
                "text": "Only conclusion I is true"
            },
            {
                "id": "C",
                "text": "Only conclusion II is true"
            },
            {
                "id": "D",
                "text": "Neither conclusion is true"
            }
        ],
        "correct_answer": "A",
        "explanation": "Decoding the statements: M > N, N >= O, O = P. Combining them gives M > N >= O = P. Conclusion I: M @ P means M > P, which is true because M > N >= P implies M > P. Conclusion II: N © P means N >= P, which is true because N >= O = P implies N >= P. Both follow.",
        "formula": "Coded inequalities substitution and transitive verification"
    }
]
