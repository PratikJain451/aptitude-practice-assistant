# -*- coding: utf-8 -*-
"""
Directional Sense Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

DIRECTIONAL_SENSE_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "ds-1",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Rahul walks 10 meters North, then turns Right and walks 10 meters. In which direction is he now facing?",
        "options": [
            {
                "id": "A",
                "text": "North"
            },
            {
                "id": "B",
                "text": "East"
            },
            {
                "id": "C",
                "text": "South"
            },
            {
                "id": "D",
                "text": "West"
            }
        ],
        "correct_answer": "B",
        "explanation": "Rahul initially walks North. Making a 90° right turn from North points him directly toward East.",
        "formula": "Cardinal Orientation: Right turn from North = East"
    },
    {
        "id": "ds-2",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "A man walks 3 km East, then turns left and walks 4 km. How far is he from his starting point?",
        "options": [
            {
                "id": "A",
                "text": "5 km"
            },
            {
                "id": "B",
                "text": "7 km"
            },
            {
                "id": "C",
                "text": "6 km"
            },
            {
                "id": "D",
                "text": "1 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Turning left from East means heading North. The path forms a right-angled triangle with legs 3 km and 4 km. By Pythagoras theorem, Distance = √(3² + 4²) = √(9 + 16) = √25 = 5 km.",
        "formula": "Pythagorean Theorem: Distance = √(Δx² + Δy²)"
    },
    {
        "id": "ds-7",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "A man walks 4 km North, then turns right and walks 3 km. How far is he from his starting point?",
        "options": [
            {
                "id": "A",
                "text": "5 km"
            },
            {
                "id": "B",
                "text": "6 km"
            },
            {
                "id": "C",
                "text": "7 km"
            },
            {
                "id": "D",
                "text": "4 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "The path forms a right-angled triangle with legs 4 km (North) and 3 km (East). By Pythagoras theorem, Distance = sqrt(4^2 + 3^2) = sqrt(16 + 9) = sqrt(25) = 5 km.",
        "formula": "Shortest Distance = sqrt(North^2 + East^2)"
    },
    {
        "id": "ds-8",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Rahul is facing East. He turns 90° in the clockwise direction and then 180° in the counter-clockwise direction. Which direction is he facing now?",
        "options": [
            {
                "id": "A",
                "text": "North"
            },
            {
                "id": "B",
                "text": "South"
            },
            {
                "id": "C",
                "text": "West"
            },
            {
                "id": "D",
                "text": "East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net angle change = 180° (counter-clockwise) - 90° (clockwise) = 90° counter-clockwise. Turning 90° counter-clockwise from East points to North.",
        "formula": "Net Rotation = CCW Angle - CW Angle"
    },
    {
        "id": "ds-9",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. Which direction was Suresh facing?",
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
                "text": "East"
            },
            {
                "id": "D",
                "text": "West"
            }
        ],
        "correct_answer": "A",
        "explanation": "In the morning, the Sun is in the East, so all shadows fall towards the West. If the shadow falls to Suresh's right, his right side must be towards the West. When a person faces South, West is to their right.",
        "formula": "Morning Shadow Direction = West. If Right = West, Facing = South."
    },
    {
        "id": "ds-10",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Anand walks 5 km towards South, then turns left and walks 3 km. He turns left again and walks 5 km. Which direction is he from his starting point?",
        "options": [
            {
                "id": "A",
                "text": "East"
            },
            {
                "id": "B",
                "text": "West"
            },
            {
                "id": "C",
                "text": "North"
            },
            {
                "id": "D",
                "text": "South"
            }
        ],
        "correct_answer": "A",
        "explanation": "Displacement: 5 km South (0, -5), turn left (East) 3 km (3, -5), turn left (North) 5 km (3, 0). The final position is (3, 0), which is directly East of the starting point (0, 0).",
        "formula": "Coordinate tracking: (x, y) = (3, 0) => East"
    },
    {
        "id": "ds-11",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "A car travels 12 km West, then turns left and travels 5 km. What is the shortest distance between the car and the starting point?",
        "options": [
            {
                "id": "A",
                "text": "13 km"
            },
            {
                "id": "B",
                "text": "14 km"
            },
            {
                "id": "C",
                "text": "15 km"
            },
            {
                "id": "D",
                "text": "17 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "The movement is 12 km West and 5 km South (turning left from West heads South). Distance = sqrt(12^2 + 5^2) = sqrt(144 + 25) = sqrt(169) = 13 km.",
        "formula": "Distance = sqrt(West^2 + South^2) = sqrt(144 + 25) = 13"
    },
    {
        "id": "ds-12",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "If you are walking towards the setting sun in the evening and then take a consecutive left turn and right turn, in which direction are you now walking?",
        "options": [
            {
                "id": "A",
                "text": "West"
            },
            {
                "id": "B",
                "text": "East"
            },
            {
                "id": "C",
                "text": "North"
            },
            {
                "id": "D",
                "text": "South"
            }
        ],
        "correct_answer": "A",
        "explanation": "The setting sun is in the West. Walking West, turning left points you South. Turning right from South points you West again. A consecutive left and right turn cancels out, leaving you walking in the original direction (West).",
        "formula": "Turn Cancellation: Left + Right = 0° net rotation"
    },
    {
        "id": "ds-13",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Kavita starts from her school and walks 2 km North, then turns left and walks 4 km. Which direction is she with respect to the school?",
        "options": [
            {
                "id": "A",
                "text": "North-West"
            },
            {
                "id": "B",
                "text": "North-East"
            },
            {
                "id": "C",
                "text": "South-West"
            },
            {
                "id": "D",
                "text": "West"
            }
        ],
        "correct_answer": "A",
        "explanation": "Kavita is 2 km North and 4 km West of her starting point. Combining North and West positions gives North-West.",
        "formula": "Relative direction = quadrant of displacement (+y, -x) = North-West"
    },
    {
        "id": "ds-14",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "A cyclist rides 8 km South, then turns right and rides 6 km. What is the straight-line distance to his starting location?",
        "options": [
            {
                "id": "A",
                "text": "10 km"
            },
            {
                "id": "B",
                "text": "12 km"
            },
            {
                "id": "C",
                "text": "14 km"
            },
            {
                "id": "D",
                "text": "9 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Right turn from South leads West. Legs of right triangle are 8 km and 6 km. Distance = sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 km.",
        "formula": "Pythagoras: D = sqrt(8^2 + 6^2) = 10"
    },
    {
        "id": "ds-15",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Meena is facing South. She turns 180° and then turns 45° in the clockwise direction. Which direction is she facing now?",
        "options": [
            {
                "id": "A",
                "text": "North-East"
            },
            {
                "id": "B",
                "text": "North-West"
            },
            {
                "id": "C",
                "text": "South-East"
            },
            {
                "id": "D",
                "text": "South-West"
            }
        ],
        "correct_answer": "A",
        "explanation": "From South, turning 180° points directly North. Turning 45° clockwise from North points to North-East.",
        "formula": "South + 180° = North; North + 45° CW = North-East"
    },
    {
        "id": "ds-16",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Point A is 10 m to the West of Point B. Point C is 10 m to the North of Point B. In which direction is Point C with respect to Point A?",
        "options": [
            {
                "id": "A",
                "text": "North-East"
            },
            {
                "id": "B",
                "text": "North-West"
            },
            {
                "id": "C",
                "text": "South-East"
            },
            {
                "id": "D",
                "text": "South-West"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let Point B be at (0, 0). Point A is at (-10, 0) and Point C is at (0, 10). From Point A to Point C, moving from (-10, 0) to (0, 10) means moving +10 East and +10 North, which is North-East.",
        "formula": "Direction from A to C: dx = 10 (East), dy = 10 (North) => North-East"
    },
    {
        "id": "ds-17",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "A person walks 20 m North, then turns around and walks 35 m South. How far and in which direction is the person from the start?",
        "options": [
            {
                "id": "A",
                "text": "15 m South"
            },
            {
                "id": "B",
                "text": "15 m North"
            },
            {
                "id": "C",
                "text": "55 m South"
            },
            {
                "id": "D",
                "text": "20 m South"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net displacement along North-South axis: +20 m (North) - 35 m (South) = -15 m, which is 15 m South of the starting point.",
        "formula": "Displacement = 20 - 35 = -15 m (South)"
    },
    {
        "id": "ds-18",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "A compass needle which normally points North is rotated 90° clockwise. When someone follows the direction indicated by the needle as 'North', in which geographical direction are they actually traveling?",
        "options": [
            {
                "id": "A",
                "text": "East"
            },
            {
                "id": "B",
                "text": "West"
            },
            {
                "id": "C",
                "text": "South"
            },
            {
                "id": "D",
                "text": "North"
            }
        ],
        "correct_answer": "A",
        "explanation": "Rotating North 90° clockwise points to East. Therefore, the faulty needle points East.",
        "formula": "Rotational deflection: True direction = North + 90° CW = East"
    },
    {
        "id": "ds-19",
        "topic": "Directional Sense",
        "difficulty": "Easy",
        "question": "Rohit walks 7 km East, turns right and walks 4 km, then turns right again and walks 7 km. How far is he from his starting point?",
        "options": [
            {
                "id": "A",
                "text": "4 km"
            },
            {
                "id": "B",
                "text": "7 km"
            },
            {
                "id": "C",
                "text": "11 km"
            },
            {
                "id": "D",
                "text": "14 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Coordinates: Start (0, 0) -> East 7 km to (7, 0) -> Right (South) 4 km to (7, -4) -> Right (West) 7 km to (0, -4). The final distance from (0, 0) to (0, -4) is 4 km.",
        "formula": "Displacement: sqrt((0-0)^2 + (-4-0)^2) = 4 km"
    },
    {
        "id": "ds-3",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "Anita starts walking towards South. After walking 15 meters, she turns left and walks 15 meters. She again turns left and walks 15 meters. How far and in what direction is she from her starting point?",
        "options": [
            {
                "id": "A",
                "text": "15 meters East"
            },
            {
                "id": "B",
                "text": "15 meters West"
            },
            {
                "id": "C",
                "text": "30 meters East"
            },
            {
                "id": "D",
                "text": "At starting point"
            }
        ],
        "correct_answer": "A",
        "explanation": "South 15m (y = -15). Left turn points East, walks 15m (x = +15). Left turn points North, walks 15m (y = -15 + 15 = 0). Final coordinates are (15, 0), which is 15 meters directly East of starting point.",
        "formula": "Coordinate tracking: (0,0) -> (0,-15) -> (15,-15) -> (15,0)"
    },
    {
        "id": "ds-4",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "One morning after sunrise, Vikram and Shailesh were standing in a lawn with their backs toward each other. Vikram's shadow fell exactly towards his left hand side. Which direction was Shailesh facing?",
        "options": [
            {
                "id": "A",
                "text": "North"
            },
            {
                "id": "B",
                "text": "South"
            },
            {
                "id": "C",
                "text": "East"
            },
            {
                "id": "D",
                "text": "West"
            }
        ],
        "correct_answer": "B",
        "explanation": "In the morning, the Sun is in the East, so all shadows fall towards the West. Vikram's shadow falls to his left, which means his left is West. If left is West, Vikram must be facing North. Since Shailesh's back is to Vikram, Shailesh is facing the opposite direction, which is South.",
        "formula": "Sun in East => Shadow falls West. Facing North => Left is West."
    },
    {
        "id": "ds-20",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "Deepak starts walking towards East. After walking 35 meters, he turns right and walks 20 meters. He then turns right again and walks 35 meters. Finally, he turns left and walks 15 meters. In which direction and how far is he from the starting point?",
        "options": [
            {
                "id": "A",
                "text": "35 meters South"
            },
            {
                "id": "B",
                "text": "20 meters South"
            },
            {
                "id": "C",
                "text": "15 meters South"
            },
            {
                "id": "D",
                "text": "35 meters East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Tracing positions from (0, 0): East 35 m -> (35, 0). Right turn (South) 20 m -> (35, -20). Right turn (West) 35 m -> (0, -20). Left turn (South) 15 m -> (0, -35). He is at (0, -35), which is 35 meters South of his starting point.",
        "formula": "Vector Sum: (35-35, -20-15) = (0, -35)"
    },
    {
        "id": "ds-21",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A village Q is 12 km to the North of Village P. Village R is 9 km to the East of Village P. What is the shortest aerial distance between Village Q and Village R?",
        "options": [
            {
                "id": "A",
                "text": "15 km"
            },
            {
                "id": "B",
                "text": "17 km"
            },
            {
                "id": "C",
                "text": "21 km"
            },
            {
                "id": "D",
                "text": "13 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let P be origin (0, 0). Q is at (0, 12) and R is at (9, 0). The distance between Q and R is sqrt((9 - 0)^2 + (0 - 12)^2) = sqrt(81 + 144) = sqrt(225) = 15 km.",
        "formula": "Distance QR = sqrt(x^2 + y^2) = sqrt(9^2 + 12^2) = 15 km"
    },
    {
        "id": "ds-22",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "Two friends A and B start from the same point. A walks 6 km West, then turns left and walks 8 km. B walks 8 km South, then turns right and walks 6 km. What is the distance between them now?",
        "options": [
            {
                "id": "A",
                "text": "0 km (they are at the same spot)"
            },
            {
                "id": "B",
                "text": "4 km"
            },
            {
                "id": "C",
                "text": "12 km"
            },
            {
                "id": "D",
                "text": "10 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "For A: 6 km West to (-6, 0), turn left (South) 8 km to (-6, -8). For B: 8 km South to (0, -8), turn right (West) 6 km to (-6, -8). Both end up at exactly the same coordinates (-6, -8). The distance between them is 0 km.",
        "formula": "Coordinate identity: Pos(A) = (-6, -8) = Pos(B)"
    },
    {
        "id": "ds-23",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "One evening before sunset, Rekha and Hema were talking to each other face to face. If Hema's shadow was exactly to the right of Hema, which direction was Rekha facing?",
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
                "text": "East"
            },
            {
                "id": "D",
                "text": "West"
            }
        ],
        "correct_answer": "A",
        "explanation": "In the evening, the sun is in the West, so shadows fall towards the East. Since Hema's shadow falls to her right, Hema's right is East. For East to be on the right, Hema must be facing North. Since Rekha is talking to Hema face to face, Rekha must be facing opposite to Hema, which is South.",
        "formula": "Evening shadow = East. Hema's right = East => Hema faces North => Rekha faces South."
    },
    {
        "id": "ds-24",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A watch shows 4:30. If the minute hand points towards East, in which direction does the hour hand point?",
        "options": [
            {
                "id": "A",
                "text": "North-East"
            },
            {
                "id": "B",
                "text": "South-East"
            },
            {
                "id": "C",
                "text": "North-West"
            },
            {
                "id": "D",
                "text": "South-West"
            }
        ],
        "correct_answer": "A",
        "explanation": "On a standard clock face at 4:30, the minute hand points straight down at 6 (South), and the hour hand is midway between 4 and 5 (75° clockwise from 12, or 45° counter-clockwise from South). If the minute hand at South is taken as East, the coordinate system is rotated 90° counter-clockwise. Applying this 90° CCW rotation to the hour hand (which was at South-East, roughly 135° from 12) shifts it to North-East (45° from 12). Thus, the hour hand points North-East.",
        "formula": "Clock dial rotation mapping"
    },
    {
        "id": "ds-25",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "Varun walks 10 meters towards North. From there, he walks 6 meters towards South. Then, he walks 3 meters towards East. How far and in which direction is he with reference to his starting point?",
        "options": [
            {
                "id": "A",
                "text": "5 meters North-East"
            },
            {
                "id": "B",
                "text": "5 meters South-East"
            },
            {
                "id": "C",
                "text": "7 meters North-East"
            },
            {
                "id": "D",
                "text": "5 meters North-West"
            }
        ],
        "correct_answer": "A",
        "explanation": "Starting at (0, 0): 10 m North -> (0, 10). 6 m South -> (0, 4). 3 m East -> (3, 4). Distance = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5 meters. Since x > 0 and y > 0, the direction is North-East.",
        "formula": "Distance = sqrt(dx^2 + dy^2) = sqrt(9 + 16) = 5 m"
    },
    {
        "id": "ds-26",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A traveler starts at point P, walks 15 km North to Q, turns right and walks 8 km to R, turns right and walks 9 km to S. How far is S from P in a straight line?",
        "options": [
            {
                "id": "A",
                "text": "10 km"
            },
            {
                "id": "B",
                "text": "12 km"
            },
            {
                "id": "C",
                "text": "14 km"
            },
            {
                "id": "D",
                "text": "15 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Starting at P (0, 0): Q is at (0, 15). R is at (8, 15). Right turn from East is South: S is at (8, 15 - 9) = (8, 6). The distance from P(0, 0) to S(8, 6) is sqrt(8^2 + 6^2) = sqrt(64 + 36) = sqrt(100) = 10 km.",
        "formula": "Distance = sqrt(8^2 + 6^2) = 10 km"
    },
    {
        "id": "ds-27",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A person facing West turns 45° clockwise, then 180° clockwise, and then 270° counter-clockwise. Which direction is he facing now?",
        "options": [
            {
                "id": "A",
                "text": "South-West"
            },
            {
                "id": "B",
                "text": "North-West"
            },
            {
                "id": "C",
                "text": "South-East"
            },
            {
                "id": "D",
                "text": "North-East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Total clockwise rotation = 45° + 180° = 225°. Total counter-clockwise rotation = 270°. Net rotation = 270° - 225° = 45° counter-clockwise. Turning 45° counter-clockwise from West points to South-West.",
        "formula": "Net Angle = 270° CCW - 225° CW = 45° CCW"
    },
    {
        "id": "ds-28",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "Town M is to the West of Town N. Town P is to the South of Town M. Town Q is to the East of Town P. In which direction is Town Q with respect to Town N, if distance MP = distance NQ and Town Q is directly South of Town N?",
        "options": [
            {
                "id": "A",
                "text": "South"
            },
            {
                "id": "B",
                "text": "South-West"
            },
            {
                "id": "C",
                "text": "South-East"
            },
            {
                "id": "D",
                "text": "East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Towns M, N, Q, P form a rectangle: M is at (0, y), N is at (d, y), P is at (0, 0), and Q is at (d, 0). Town Q has the same x-coordinate as Town N and a lower y-coordinate. Therefore, Town Q is directly South of Town N.",
        "formula": "Geometric rectangle coordinates: Q is directly South of N"
    },
    {
        "id": "ds-29",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A drone flies 50 m North, then turns 135° to its right and flies 70.71 m (50*sqrt(2) m). Where is the drone with respect to its takeoff position?",
        "options": [
            {
                "id": "A",
                "text": "50 m East"
            },
            {
                "id": "B",
                "text": "50 m South"
            },
            {
                "id": "C",
                "text": "50 m North-East"
            },
            {
                "id": "D",
                "text": "At takeoff position"
            }
        ],
        "correct_answer": "A",
        "explanation": "From North (0°), turning 135° to the right points to South-East (135°). The components of flying 50*sqrt(2) m at 45° South of East are: East displacement = 50*sqrt(2)*cos(45°) = 50 m, South displacement = 50*sqrt(2)*sin(45°) = 50 m. Net displacement: North 50 m - South 50 m = 0 m; East = 50 m. The drone is 50 m directly East of takeoff.",
        "formula": "Trigonometric vector components: dx = 50 m, dy = 50 - 50 = 0"
    },
    {
        "id": "ds-30",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "Kiran walks 2 km North, turns right and walks 3 km, turns right and walks 6 km, then turns right and walks 3 km. How far is Kiran from the starting point?",
        "options": [
            {
                "id": "A",
                "text": "4 km"
            },
            {
                "id": "B",
                "text": "6 km"
            },
            {
                "id": "C",
                "text": "2 km"
            },
            {
                "id": "D",
                "text": "8 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "East-West displacement: +3 km (East) - 3 km (West) = 0 km. North-South displacement: +2 km (North) - 6 km (South) = -4 km. The final position is 4 km South of start. The straight-line distance is 4 km.",
        "formula": "Distance = |2 - 6| = 4 km"
    },
    {
        "id": "ds-31",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A delivery rider travels 10 km South, turns left and travels 15 km, turns left and travels 10 km, then turns right and travels 5 km. What is the total displacement from start to destination?",
        "options": [
            {
                "id": "A",
                "text": "20 km East"
            },
            {
                "id": "B",
                "text": "15 km East"
            },
            {
                "id": "C",
                "text": "20 km South"
            },
            {
                "id": "D",
                "text": "25 km East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Path tracking: (0, -10) -> (15, -10) -> (15, 0) -> (20, 0). Final location is 20 km East of the origin.",
        "formula": "Displacement = (15 + 5, -10 + 10) = (20, 0)"
    },
    {
        "id": "ds-32",
        "topic": "Directional Sense",
        "difficulty": "Medium",
        "question": "A person begins at Point O and walks 4 km East, then 3 km North to Point A. Another person begins at Point O and walks 3 km West, then 4 km South to Point B. What is the straight-line distance between Point A and Point B?",
        "options": [
            {
                "id": "A",
                "text": "sqrt(98) km (approx 9.9 km)"
            },
            {
                "id": "B",
                "text": "10 km"
            },
            {
                "id": "C",
                "text": "12 km"
            },
            {
                "id": "D",
                "text": "7 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Coordinates of Point A: (4, 3). Coordinates of Point B: (-3, -4). Distance AB = sqrt((4 - (-3))^2 + (3 - (-4))^2) = sqrt(7^2 + 7^2) = sqrt(49 + 49) = sqrt(98) = 7*sqrt(2) km ≈ 9.9 km.",
        "formula": "Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2) = sqrt(49 + 49) = sqrt(98)"
    },
    {
        "id": "ds-5",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "A delivery drone flies 10 km West from base station P to point Q, then turns North and flies 20 km to point R. What is the shortest straight-line distance between P and R?",
        "options": [
            {
                "id": "A",
                "text": "10√2 km"
            },
            {
                "id": "B",
                "text": "10√5 km"
            },
            {
                "id": "C",
                "text": "20 km"
            },
            {
                "id": "D",
                "text": "15√2 km"
            }
        ],
        "correct_answer": "B",
        "explanation": "Taking base station P as the origin (0, 0): Point Q is at (-10, 0) after flying 10 km West. Flying 20 km North places point R at (-10, 20). The shortest straight-line distance between P and R is given by the Pythagorean theorem: PR = √((-10)² + 20²) = √(100 + 400) = √500 = 10√5 km.",
        "formula": "Distance = √(Δx² + Δy²) = √(10² + 20²) = 10√5 km"
    },
    {
        "id": "ds-6",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "Starting from point O, a cyclist rides 12 km North to point A, turns right and rides 9 km to point B, then turns right and rides 24 km to point C. How far is point C from point O?",
        "options": [
            {
                "id": "A",
                "text": "15 km"
            },
            {
                "id": "B",
                "text": "17 km"
            },
            {
                "id": "C",
                "text": "21 km"
            },
            {
                "id": "D",
                "text": "13 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Coordinate representation with O at (0, 0): Riding 12 km North reaches point A(0, 12). Turning right (East) and riding 9 km reaches point B(9, 12). Turning right (South) and riding 24 km reaches point C(9, 12 - 24) = (9, -12). The shortest distance from O(0, 0) to C(9, -12) is √(9² + (-12)²) = √(81 + 144) = √225 = 15 km.",
        "formula": "Distance = √(Δx² + Δy²) = √(9² + (-12)²) = 15 km"
    },
    {
        "id": "ds-33",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "In a coded direction system: 'P # Q' means P is 6 m North of Q; 'P @ Q' means P is 8 m East of Q; 'P % Q' means P is 6 m South of Q; 'P $ Q' means P is 8 m West of Q. If 'A # B @ C % D @ E' holds, what is the distance and direction of A with respect to E?",
        "options": [
            {
                "id": "A",
                "text": "16 m East"
            },
            {
                "id": "B",
                "text": "16 m West"
            },
            {
                "id": "C",
                "text": "12 m North"
            },
            {
                "id": "D",
                "text": "8 m East"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let C be (0, 0). 'B @ C' means B is 8 m East of C, so B is at (8, 0). 'A # B' means A is 6 m North of B, so A is at (8, 6). 'C % D' means C is 6 m South of D, so D is at (0, 6). 'D @ E' means D is 8 m East of E, so E is at (-8, 6). Displacement from E(-8, 6) to A(8, 6) is dx = 8 - (-8) = 16 m East, and dy = 6 - 6 = 0 m. Therefore, A is 16 m East of E.",
        "formula": "Coded spatial coordinate superposition"
    },
    {
        "id": "ds-34",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "Point P is 12 m North of Point Q. Point R is 16 m East of Point Q. Point S is 8 m North of Point R. Point T is 6 m West of Point S. What is the shortest distance between Point P and Point T?",
        "options": [
            {
                "id": "A",
                "text": "sqrt(116) m"
            },
            {
                "id": "B",
                "text": "10 m"
            },
            {
                "id": "C",
                "text": "12 m"
            },
            {
                "id": "D",
                "text": "14 m"
            }
        ],
        "correct_answer": "A",
        "explanation": "Set Q at (0, 0). P is at (0, 12). R is at (16, 0). S is at (16, 8). T is at (16 - 6, 8) = (10, 8). Distance PT = sqrt((10 - 0)^2 + (8 - 12)^2) = sqrt(100 + 16) = sqrt(116) m.",
        "formula": "Distance = sqrt(dx^2 + dy^2) = sqrt(10^2 + (-4)^2) = sqrt(116) m"
    },
    {
        "id": "ds-35",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "An autonomous rover starts from base O (0, 0), travels 10 m in the direction 30° North of East, turns 90° left and travels 10*sqrt(3) m. What is its final distance from base O?",
        "options": [
            {
                "id": "A",
                "text": "20 m"
            },
            {
                "id": "B",
                "text": "15 m"
            },
            {
                "id": "C",
                "text": "25 m"
            },
            {
                "id": "D",
                "text": "30 m"
            }
        ],
        "correct_answer": "A",
        "explanation": "The two legs are perpendicular (the rover turned 90°). Leg 1 has length a = 10 m and Leg 2 has length b = 10*sqrt(3) m. By Pythagoras theorem, Distance = sqrt(a^2 + b^2) = sqrt(100 + 300) = sqrt(400) = 20 m.",
        "formula": "Pythagoras for perpendicular legs: D = sqrt(10^2 + (10*sqrt(3))^2) = 20 m"
    },
    {
        "id": "ds-36",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "A helicopter takes off from helipad H, flies 40 km North, then 30 km West, then 20 km South, and finally 15 km East. What is the direct straight-line distance back to the helipad?",
        "options": [
            {
                "id": "A",
                "text": "25 km"
            },
            {
                "id": "B",
                "text": "30 km"
            },
            {
                "id": "C",
                "text": "35 km"
            },
            {
                "id": "D",
                "text": "20 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net North-South displacement = 40 km (North) - 20 km (South) = 20 km North. Net East-West displacement = -30 km (West) + 15 km (East) = -15 km (15 km West). Direct distance = sqrt(20^2 + 15^2) = sqrt(400 + 225) = sqrt(625) = 25 km.",
        "formula": "Shortest Return Distance = sqrt(20^2 + 15^2) = 25 km"
    },
    {
        "id": "ds-37",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "Six checkpoints U, V, W, X, Y, and Z are established in a nature reserve. V is 5 km North of U. W is 12 km East of V. X is 5 km South of W. Y is 7 km West of X. Z is 5 km North of Y. In which direction and at what distance is Z with respect to V?",
        "options": [
            {
                "id": "A",
                "text": "12 km East"
            },
            {
                "id": "B",
                "text": "7 km North"
            },
            {
                "id": "C",
                "text": "5 km North"
            },
            {
                "id": "D",
                "text": "5 km East"
            }
        ],
        "correct_answer": "D",
        "explanation": "Let U be (0, 0). V is at (0, 5). W is at (12, 5). X is at (12, 0). Y is at (12 - 7, 0) = (5, 0). Z is at (5, 0 + 5) = (5, 5). Wait! Z is at (5, 5) and V is at (0, 5). Then from V(0, 5) to Z(5, 5), dx = 5 km East and dy = 0! So Z is directly 5 km East of V! Let's choose D: 5 km East.",
        "formula": "Relative coordinate difference: Z(5, 5) - V(0, 5) = (5, 0) => 5 km East"
    },
    {
        "id": "ds-38",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "A surveyor starts at station M, walks 100 m North, then turns 60° clockwise and walks 100 m, then turns 120° clockwise and walks 100 m. How far is the surveyor from station M?",
        "options": [
            {
                "id": "A",
                "text": "100 m"
            },
            {
                "id": "B",
                "text": "150 m"
            },
            {
                "id": "C",
                "text": "200 m"
            },
            {
                "id": "D",
                "text": "50 m"
            }
        ],
        "correct_answer": "A",
        "explanation": "Vector 1: 100 m North = (0, 100). Turn 60° CW from North points 30° North of East: Vector 2 = (100*cos(30°), 100*sin(30°)) = (50*sqrt(3), 50). Turn 120° CW points South: Vector 3 = (0, -100). Resultant displacement vector = (50*sqrt(3), 50). Magnitude = sqrt((50*sqrt(3))^2 + 50^2) = sqrt(7500 + 2500) = sqrt(10000) = 100 m.",
        "formula": "Vector polygon addition: D = 100 m, angle = 30° N of E"
    },
    {
        "id": "ds-39",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "Two cars leave city center C at the same time. Car 1 travels North at 60 km/h. Car 2 travels East at 80 km/h. What is the rate of separation between the two cars after 2 hours?",
        "options": [
            {
                "id": "A",
                "text": "100 km/h"
            },
            {
                "id": "B",
                "text": "140 km/h"
            },
            {
                "id": "C",
                "text": "120 km/h"
            },
            {
                "id": "D",
                "text": "200 km/h"
            }
        ],
        "correct_answer": "A",
        "explanation": "Since their paths are mutually perpendicular (North and East), distance S(t) = sqrt((v1*t)^2 + (v2*t)^2) = t * sqrt(v1^2 + v2^2). The rate of separation dS/dt = sqrt(v1^2 + v2^2) = sqrt(60^2 + 80^2) = sqrt(3600 + 6400) = 100 km/h at any time t > 0.",
        "formula": "Relative velocity magnitude for perpendicular paths: v_rel = sqrt(v1^2 + v2^2)"
    },
    {
        "id": "ds-40",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "In a military exercise, a soldier crawls 24 m West, turns left and crawls 10 m, turns right and crawls 15 m, then turns right and crawls 30 m, and finally turns right and crawls 39 m. How far is the soldier from the starting point?",
        "options": [
            {
                "id": "A",
                "text": "20 m"
            },
            {
                "id": "B",
                "text": "25 m"
            },
            {
                "id": "C",
                "text": "15 m"
            },
            {
                "id": "D",
                "text": "30 m"
            }
        ],
        "correct_answer": "A",
        "explanation": "Tracking coordinates from (0, 0): West 24 m -> (-24, 0). Left turn (South) 10 m -> (-24, -10). Right turn (West) 15 m -> (-39, -10). Right turn (North) 30 m -> (-39, 20). Right turn (East) 39 m -> (-39 + 39, 20) = (0, 20). The soldier is at (0, 20), which is exactly 20 meters North of the start.",
        "formula": "Coordinates net: dx = -24 - 15 + 39 = 0; dy = -10 + 30 = 20 => Distance = 20 m"
    },
    {
        "id": "ds-41",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "A ship sails 30 nautical miles East, then 40 nautical miles North, then 60 nautical miles West, and finally 40 nautical miles South. What is the bearing and distance of the ship from the departure port?",
        "options": [
            {
                "id": "A",
                "text": "30 nautical miles West"
            },
            {
                "id": "B",
                "text": "30 nautical miles East"
            },
            {
                "id": "C",
                "text": "50 nautical miles West"
            },
            {
                "id": "D",
                "text": "40 nautical miles West"
            }
        ],
        "correct_answer": "A",
        "explanation": "East-West: +30 - 60 = -30 nautical miles (30 nmi West). North-South: +40 - 40 = 0 nmi. The final position is 30 nautical miles due West.",
        "formula": "Displacement = (-30, 0) => 30 nmi West"
    },
    {
        "id": "ds-42",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "During sunrise, two friends stood in an open field. Friend X noticed that his own shadow fell to his left. Friend Y stood facing Friend X. In which direction was Friend Y's shadow falling relative to Friend Y's body?",
        "options": [
            {
                "id": "A",
                "text": "To Y's left"
            },
            {
                "id": "B",
                "text": "To Y's right"
            },
            {
                "id": "C",
                "text": "In front of Y"
            },
            {
                "id": "D",
                "text": "Behind Y"
            }
        ],
        "correct_answer": "B",
        "explanation": "At sunrise, the sun is in the East, so all shadows fall West. For Friend X's shadow to fall to his left, West must be on X's left. A person facing North has West on their left, so Friend X is facing North. Since Friend Y is facing X, Friend Y must be facing South. For a person facing South, West is on their right. Since the shadow falls West, Friend Y's shadow falls to Y's right.",
        "formula": "Sunrise shadow = West. X faces North (left=West). Y faces South (right=West)."
    },
    {
        "id": "ds-43",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "A courier warehouse is connected to 4 hubs: Hub A is 8 km North of Warehouse; Hub B is 6 km East of Warehouse; Hub C is 8 km South of Warehouse; Hub D is 6 km West of Warehouse. What is the perimeter of the quadrilateral formed by connecting Hubs A, B, C, and D?",
        "options": [
            {
                "id": "A",
                "text": "40 km"
            },
            {
                "id": "B",
                "text": "48 km"
            },
            {
                "id": "C",
                "text": "36 km"
            },
            {
                "id": "D",
                "text": "32 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "The coordinates are A(0, 8), B(6, 0), C(0, -8), and D(-6, 0). The four hubs form a rhombus. Each side length is sqrt(8^2 + 6^2) = sqrt(64 + 36) = 10 km. Perimeter = 4 × 10 km = 40 km.",
        "formula": "Rhombus Perimeter = 4 × sqrt(a^2 + b^2) = 4 × 10 = 40 km"
    },
    {
        "id": "ds-44",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "Point K is 7 m North of Point L. Point M is 9 m East of Point L. Point N is 15 m South of Point M. Point O is 9 m West of Point N. What is the distance between Point K and Point O?",
        "options": [
            {
                "id": "A",
                "text": "22 m"
            },
            {
                "id": "B",
                "text": "20 m"
            },
            {
                "id": "C",
                "text": "18 m"
            },
            {
                "id": "D",
                "text": "16 m"
            }
        ],
        "correct_answer": "A",
        "explanation": "Let L be (0, 0). K is at (0, 7). M is at (9, 0). N is at (9, -15). O is at (9 - 9, -15) = (0, -15). The distance between K(0, 7) and O(0, -15) is 7 - (-15) = 22 meters.",
        "formula": "Collinear vertical distance: y_K - y_O = 7 - (-15) = 22 m"
    },
    {
        "id": "ds-45",
        "topic": "Directional Sense",
        "difficulty": "Hard",
        "question": "A person walks 1 km East, 2 km South, 3 km West, 4 km North, 5 km East, and 6 km South. What is the straight-line distance from the starting position?",
        "options": [
            {
                "id": "A",
                "text": "5 km"
            },
            {
                "id": "B",
                "text": "6 km"
            },
            {
                "id": "C",
                "text": "7 km"
            },
            {
                "id": "D",
                "text": "4 km"
            }
        ],
        "correct_answer": "A",
        "explanation": "Net East-West displacement: +1 (East) - 3 (West) + 5 (East) = +3 km (East). Net North-South displacement: -2 (South) + 4 (North) - 6 (South) = -4 km (South). Distance = sqrt(3^2 + (-4)^2) = sqrt(9 + 16) = sqrt(25) = 5 km.",
        "formula": "Displacement = sqrt(dx^2 + dy^2) = sqrt(3^2 + 4^2) = 5 km"
    }
]
