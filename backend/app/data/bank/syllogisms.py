# -*- coding: utf-8 -*-
"""
Syllogisms Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
Universal, particular, complementary pairs, conditional possibilities, and 'Only a few' logic.
"""

from typing import List, Dict, Any

SYLLOGISMS_QUESTIONS: List[Dict[str, Any]] = [
    # -------------------------------------------------------------------------
    # EASY (15 Questions: syl-1, syl-2, syl-7 to syl-19)
    # -------------------------------------------------------------------------
    {
        "id": "syl-1",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All cats are animals.\n2. All animals are creatures.\nConclusions:\nI. All cats are creatures.\nII. Some creatures are cats.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither conclusion follows"}
        ],
        "correct_answer": "C",
        "explanation": "Cats ⊆ Animals and Animals ⊆ Creatures. Therefore Cats ⊆ Creatures (Conclusion I follows). Since the set Cats is non-empty within Creatures, Some creatures are cats (Conclusion II follows). Both conclusions strictly follow.",
        "formula": "Transitive Syllogism: All A are B + All B are C => All A are C; All A are C => Some C are A"
    },
    {
        "id": "syl-2",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. Some pens are pencils.\n2. Some pencils are erasers.\nConclusions:\nI. Some pens are erasers.\nII. No pen is an eraser.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Either I or II follows"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Between 'pens' and 'erasers' there is no definite link from two particular premises ('Some'). However, Conclusions I ('Some') and II ('No') form a complementary pair (I and E propositions with identical subjects and predicates). Therefore, either I or II must hold true.",
        "formula": "Complementary Pair Rule: 'Some A are B' and 'No A is B' with uncertain relation forms an Either-Or case."
    },
    {
        "id": "syl-7",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All dogs are mammals.\n2. All mammals are animals.\nConclusions:\nI. All dogs are animals.\nII. Some animals are dogs.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither conclusion follows"}
        ],
        "correct_answer": "C",
        "explanation": "Dogs are a subset of Mammals, and Mammals are a subset of Animals. Hence Dogs are a subset of Animals (I follows). Since Dogs are inside Animals, Some animals are dogs (II follows). Both follow.",
        "formula": "All A are B + All B are C => All A are C, and Some C are A"
    },
    {
        "id": "syl-8",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. Some flowers are roses.\n2. All roses are red.\nConclusions:\nI. Some flowers are red.\nII. All red things are flowers.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "Those flowers that are roses are also red, so Some flowers are red (I follows). We cannot deduce that All red things are flowers (II does not follow).",
        "formula": "Some A are B + All B are C => Some A are C"
    },
    {
        "id": "syl-9",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All trees are plants.\n2. No plant is a stone.\nConclusions:\nI. No tree is a stone.\nII. Some plants are trees.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Trees are entirely within Plants, and Plants and Stones do not overlap. Hence no tree can be a stone (I follows). All trees are plants implies Some plants are trees (II follows).",
        "formula": "All A are B + No B is C => No A is C"
    },
    {
        "id": "syl-10",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. Some apples are sweet.\n2. All sweet fruits are tasty.\nConclusions:\nI. Some apples are tasty.\nII. All apples are tasty.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "The apples that are sweet are definitely tasty, so Some apples are tasty follows. We cannot conclude that all apples are tasty.",
        "formula": "Some A are B + All B are C => Some A are C"
    },
    {
        "id": "syl-11",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. No fish is an insect.\n2. All insects have wings.\nConclusions:\nI. Some winged creatures are insects.\nII. No fish has wings.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "All insects have wings directly converts to Some winged creatures are insects (I follows). Fish cannot be insects, but fish could hypothetically overlap with other winged creatures outside insects, so II is not guaranteed.",
        "formula": "Subalternation / Conversion: All A are B => Some B are A"
    },
    {
        "id": "syl-12",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All kings are warriors.\n2. All warriors are brave.\nConclusions:\nI. Some brave people are kings.\nII. All kings are brave.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Kings ⊆ Warriors ⊆ Brave. Thus All kings are brave (II follows), which converts to Some brave people are kings (I follows).",
        "formula": "All A are B + All B are C => All A are C & Some C are A"
    },
    {
        "id": "syl-13",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. Some books are novels.\n2. No novel is a biography.\nConclusions:\nI. Some books are not biographies.\nII. All novels are books.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "The books that are novels cannot be biographies, so Some books are not biographies follows (I follows). 'Some books are novels' does not imply all novels are books (II does not follow).",
        "formula": "Some A are B + No B is C => Some A are not C"
    },
    {
        "id": "syl-14",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All metals are conductors.\n2. Some conductors are wires.\nConclusions:\nI. Some metals are wires.\nII. Some wires are conductors.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "B",
        "explanation": "Conductors overlap with wires, but wires need not overlap with metals specifically (I is not definite). 'Some conductors are wires' converts directly to 'Some wires are conductors' (II follows).",
        "formula": "Particular affirmative conversion: Some A are B => Some B are A"
    },
    {
        "id": "syl-15",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. Some cups are plates.\n2. Some plates are spoons.\nConclusions:\nI. Some cups are spoons.\nII. No cup is a spoon.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Either I or II follows"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "The relationship between cups and spoons is undetermined. Since Conclusion I (Some) and Conclusion II (No) form an affirmative/negative complementary pair with the same subject and predicate, either I or II must be true.",
        "formula": "Either-Or Complementary Pair: 'Some A are B' vs 'No A is B'"
    },
    {
        "id": "syl-16",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All circles are shapes.\n2. All shapes have dimensions.\nConclusions:\nI. All circles have dimensions.\nII. Some shapes are circles.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Circles are entirely inside Shapes, and Shapes are entirely within entities with dimensions. Hence All circles have dimensions (I follows), and Some shapes are circles (II follows).",
        "formula": "Universal Affirmative Transitivity: All A are B + All B are C => All A are C"
    },
    {
        "id": "syl-17",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. No triangle is a square.\n2. All squares are rectangles.\nConclusions:\nI. No square is a triangle.\nII. All rectangles are squares.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "'No triangle is a square' converts simply to 'No square is a triangle' (I follows). 'All squares are rectangles' does not imply all rectangles are squares (II does not follow).",
        "formula": "Conversion of E-type proposition: No A is B <=> No B is A"
    },
    {
        "id": "syl-18",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. All birds can fly.\n2. All creatures that can fly have wings.\nConclusions:\nI. All birds have wings.\nII. Some creatures that have wings are birds.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Birds ⊆ Flying ⊆ Winged. Thus All birds have wings (I follows), and Some creatures that have wings are birds (II follows).",
        "formula": "Transitive Syllogism: All A are B + All B are C => All A are C & Some C are A"
    },
    {
        "id": "syl-19",
        "topic": "Syllogisms",
        "difficulty": "Easy",
        "question": "Statements:\n1. Some computers are laptops.\n2. All laptops are portable.\nConclusions:\nI. Some computers are portable.\nII. All portable devices are laptops.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "Laptops are in both Computers and Portable, so Some computers are portable follows (I). We cannot conclude that all portable devices are laptops (II does not follow).",
        "formula": "Some A are B + All B are C => Some A are C"
    },

    # -------------------------------------------------------------------------
    # MEDIUM (15 Questions: syl-3, syl-4, syl-20 to syl-32)
    # -------------------------------------------------------------------------
    {
        "id": "syl-3",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All cars are vehicles.\n2. No vehicle is an airplane.\nConclusions:\nI. No car is an airplane.\nII. Some vehicles are cars.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither I nor II follows"}
        ],
        "correct_answer": "C",
        "explanation": "Cars are completely inside Vehicles. Vehicles and Airplanes are completely disjoint. Therefore, no Car can be an Airplane (Conclusion I follows). Also, since All cars are vehicles, some vehicles must be cars (Conclusion II follows).",
        "formula": "A + E => E: All A are B + No B is C => No A is C"
    },
    {
        "id": "syl-4",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some doctors are teachers.\n2. All teachers are counselors.\nConclusions:\nI. Some doctors are counselors.\nII. Some counselors are teachers.",
        "options": [
            {"id": "A", "text": "Only I follows"},
            {"id": "B", "text": "Only II follows"},
            {"id": "C", "text": "Both I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Some doctors overlap with teachers, and all teachers are inside counselors. Hence the doctors that are teachers are definitely counselors (I follows). All teachers are counselors implies Some counselors are teachers (II follows). Both follow.",
        "formula": "I + A => I proposition logic"
    },
    {
        "id": "syl-20",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All planets are round.\n2. Some satellites are planets.\nConclusions:\nI. Some satellites are round.\nII. No satellite is round.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Either I or II follows"}
        ],
        "correct_answer": "A",
        "explanation": "Since some satellites are planets and all planets are round, those satellites that are planets are definitely round. Thus Conclusion I is definitely true. Since I is definitely true, an Either-Or case does not apply.",
        "formula": "Some A are B + All B are C => Some A are C"
    },
    {
        "id": "syl-21",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. No river is a sea.\n2. All seas are oceans.\nConclusions:\nI. Some oceans are seas.\nII. Some oceans are not rivers.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "All seas are oceans converts to Some oceans are seas (I follows). The seas are inside oceans, and no sea is a river; therefore the oceans that are seas are not rivers (II follows). Both follow.",
        "formula": "No A is B + All A are C => Some C are not B"
    },
    {
        "id": "syl-22",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some doctors are poets.\n2. All poets are dreamers.\nConclusions:\nI. Some dreamers are doctors.\nII. Some doctors are dreamers.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "The doctors who are poets are dreamers, so Some doctors are dreamers (II follows). By conversion, Some dreamers are doctors (I follows). Both conclusions follow.",
        "formula": "Some A are B + All B are C => Some A are C & Some C are A"
    },
    {
        "id": "syl-23",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All chairs are tables.\n2. No table is a desk.\nConclusions:\nI. No chair is a desk.\nII. No desk is a chair.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Chairs ⊆ Tables, and Tables ∩ Desks = ∅. Thus Chairs ∩ Desks = ∅, which means No chair is a desk (I follows) and No desk is a chair (II follows).",
        "formula": "All A are B + No B is C => No A is C <=> No C is A"
    },
    {
        "id": "syl-24",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some tigers are lions.\n2. No lion is a cheetah.\nConclusions:\nI. Some tigers are not cheetahs.\nII. All tigers are cheetahs.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "The tigers that are lions cannot be cheetahs because no lion is a cheetah. Hence Some tigers are not cheetahs strictly follows (I). Since I is true, II ('All tigers are cheetahs') is impossible.",
        "formula": "Some A are B + No B is C => Some A are not C"
    },
    {
        "id": "syl-25",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All squares are rhombuses.\n2. All rhombuses are parallelograms.\nConclusions:\nI. All squares are parallelograms.\nII. Some parallelograms are squares.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Squares ⊆ Rhombuses ⊆ Parallelograms. Therefore All squares are parallelograms (I follows) and Some parallelograms are squares (II follows).",
        "formula": "Transitive inclusion: All A are B + All B are C => All A are C & Some C are A"
    },
    {
        "id": "syl-26",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some trains are metros.\n2. Some metros are monorails.\nConclusions:\nI. Some trains are monorails.\nII. No train is a monorail.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Either I or II follows"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "From two particular affirmative premises (Some + Some), no definite conclusion can be drawn between extreme terms. Since Conclusion I and II are an I and E complementary pair with identical terms, either I or II follows.",
        "formula": "Complementary Pair: Some + No between indeterminate terms => Either I or II"
    },
    {
        "id": "syl-27",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All novels are fiction.\n2. Some fiction is drama.\nConclusions:\nI. Some novels are drama.\nII. No novel is drama.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Either I or II follows"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Novels are within fiction, and drama overlaps with fiction, but whether novels and drama overlap is unknown. Since I ('Some') and II ('No') form a complementary pair, either I or II must follow.",
        "formula": "All A are B + Some B are C => indeterminate relationship between A and C => Either I or II"
    },
    {
        "id": "syl-28",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. No politician is an actor.\n2. Some actors are singers.\nConclusions:\nI. Some singers are not politicians.\nII. All politicians are singers.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "Those singers that are actors cannot be politicians (since no politician is an actor). Therefore Some singers are not politicians follows (I). There is no ground for II.",
        "formula": "No A is B + Some B are C => Some C are not A"
    },
    {
        "id": "syl-29",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All artists are creative.\n2. Some creative people are eccentric.\nConclusions:\nI. Some artists are eccentric.\nII. All eccentric people are artists.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither conclusion follows"}
        ],
        "correct_answer": "D",
        "explanation": "The middle term 'creative' is undistributed in both premises (predicate of an affirmative statement, and subject of a particular statement). Hence no definite relation exists between artists and eccentric. Neither follows.",
        "formula": "Fallacy of Undistributed Middle Term"
    },
    {
        "id": "syl-30",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some medicines are tablets.\n2. All tablets are capsules.\nConclusions:\nI. Some medicines are capsules.\nII. All capsules are medicines.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "Tablets overlap with medicines, and all tablets are inside capsules. Hence capsules must overlap with medicines (I follows). All capsules being medicines is not supported (II does not follow).",
        "formula": "Some A are B + All B are C => Some A are C"
    },
    {
        "id": "syl-31",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. All cars are machines.\n2. No machine is foolproof.\nConclusions:\nI. No car is foolproof.\nII. Some machines are cars.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Cars are inside machines, and machines are disjoint from foolproof. Hence no car is foolproof (I follows). 'All cars are machines' converts to 'Some machines are cars' (II follows). Both follow.",
        "formula": "Universal negative deduction and subalternation"
    },
    {
        "id": "syl-32",
        "topic": "Syllogisms",
        "difficulty": "Medium",
        "question": "Statements:\n1. Some heroes are villains.\n2. All villains are dangerous.\nConclusions:\nI. Some heroes are dangerous.\nII. Some dangerous people are heroes.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Heroes overlap with villains, and all villains are inside dangerous. Hence heroes overlap with dangerous (I follows). By conversion, dangerous people overlap with heroes (II follows). Both follow.",
        "formula": "Some A are B + All B are C => Some A are C & Some C are A"
    },

    # -------------------------------------------------------------------------
    # HARD (15 Questions: syl-5, syl-6, syl-33 to syl-45)
    # -------------------------------------------------------------------------
    {
        "id": "syl-5",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few engineers are coders.\n2. All coders are problem-solvers.\nConclusions:\nI. All engineers can never be coders.\nII. Some problem-solvers are engineers.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "'Only a few engineers are coders' means 'Some engineers are coders' AND 'Some engineers are NOT coders'. Because some engineers are definitively not coders, All engineers can never be coders (Conclusion I follows). Coders ⊆ Problem-solvers and Engineers ∩ Coders ≠ ∅, so Some problem-solvers are engineers (Conclusion II follows).",
        "formula": "'Only a few A are B' = Some A are B + Some A are not B."
    },
    {
        "id": "syl-6",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. No bird is a mammal.\n2. All mammals are warm-blooded.\nConclusions:\nI. Some warm-blooded animals are not birds.\nII. No bird is warm-blooded.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "A",
        "explanation": "Mammals are warm-blooded, but no mammal is a bird. Therefore, those warm-blooded creatures that are mammals cannot be birds (Conclusion I follows). Birds could still potentially be warm-blooded outside the mammal circle, so Conclusion II cannot be stated with certainty.",
        "formula": "Venn Deduction: E + A => O* (Particular Negative)"
    },
    {
        "id": "syl-33",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few doctors are surgeons.\n2. All surgeons are specialists.\nConclusions:\nI. All doctors being surgeons is a possibility.\nII. Some specialists are doctors.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "B",
        "explanation": "'Only a few doctors are surgeons' strictly implies Some doctors are NOT surgeons, making 'All doctors are surgeons' impossible (I does not follow). Surgeons overlap with doctors and all surgeons are specialists, so Some specialists are doctors (II follows).",
        "formula": "'Only a few A are B' restricts total inclusion possibility."
    },
    {
        "id": "syl-34",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few papers are books.\n2. No book is a pen.\nConclusions:\nI. All papers can never be books.\nII. Some papers are not pens.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "By definition of 'Only a few', some papers are not books, so all papers can never be books (I follows). The papers that are books cannot be pens, so Some papers are not pens (II follows). Both follow.",
        "formula": "Only a few A are B => Some A are not B; Some A are B + No B is C => Some A are not C"
    },
    {
        "id": "syl-35",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Some red are green.\n2. All green are blue.\n3. No blue is yellow.\nConclusions:\nI. No green is yellow.\nII. Some red are not yellow.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Green ⊆ Blue and Blue ∩ Yellow = ∅ $\implies$ Green ∩ Yellow = ∅, so No green is yellow (I follows). Those red that are green are inside blue and cannot be yellow, so Some red are not yellow (II follows).",
        "formula": "All A are B + No B is C => No A is C; Some D are A => Some D are not C"
    },
    {
        "id": "syl-36",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few apples are oranges.\n2. All oranges are grapes.\nConclusions:\nI. Some apples are not oranges.\nII. All grapes being apples is a possibility.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "'Only a few apples are oranges' gives Some apples are not oranges (I follows). While apples cannot be fully inside oranges, grapes can expand and be completely within apples without violating the statement (II follows). Both follow.",
        "formula": "Possibility with 'Only a few': B ⊆ A is possible even if A ⊆ B is false."
    },
    {
        "id": "syl-37",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. No cat is a dog.\n2. All dogs are foxes.\n3. Only a few foxes are wolves.\nConclusions:\nI. Some foxes are not cats.\nII. All cats being foxes is a possibility.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Dogs are inside foxes, and no dog is a cat, so the foxes that are dogs cannot be cats (I follows). Cats cannot overlap with dogs, but cats can exist inside the non-dog area of foxes (II follows as a valid possibility). Both follow.",
        "formula": "Negative deduction + Possibility analysis in Venn spaces"
    },
    {
        "id": "syl-38",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Some stones are rocks.\n2. All rocks are mountains.\n3. No mountain is a volcano.\nConclusions:\nI. Some stones are mountains.\nII. No rock is a volcano.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Stones overlap with rocks, and all rocks are mountains, so stones overlap with mountains (I follows). Rocks are completely inside mountains, and mountains are disjoint from volcanoes, so no rock is a volcano (II follows).",
        "formula": "Compound categorical deduction"
    },
    {
        "id": "syl-39",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few pens are pencils.\n2. Only a few pencils are erasers.\nConclusions:\nI. All pens being pencils is a possibility.\nII. Some pencils are not erasers.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "B",
        "explanation": "Since 'Only a few pens are pencils', all pens can never be pencils, making Conclusion I false. Statement 2 explicitly states 'Only a few pencils are erasers', which directly means 'Some pencils are erasers' AND 'Some pencils are not erasers', so Conclusion II strictly follows.",
        "formula": "'Only a few A are B' strictly defines 'Some A are not B'."
    },
    {
        "id": "syl-40",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. All circles are ellipses.\n2. Some ellipses are parabolas.\n3. No parabola is a hyperbola.\nConclusions:\nI. Some ellipses are not hyperbolas.\nII. All circles being parabolas is a possibility.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "The ellipses that are parabolas cannot be hyperbolas (I follows). Circles are inside ellipses, and there is no negative constraint between circles and parabolas, so All circles being parabolas is a possibility (II follows). Both follow.",
        "formula": "Particular negative + Unrestricted positive possibility"
    },
    {
        "id": "syl-41",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few mobiles are tablets.\n2. All tablets are laptops.\nConclusions:\nI. Some mobiles are not tablets.\nII. All laptops being mobiles is a possibility.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "'Only a few mobiles are tablets' implies Some mobiles are not tablets (I follows). While mobiles cannot be all tablets, laptops can be completely inside mobiles without violating any condition (II follows). Both follow.",
        "formula": "Asymmetric restriction under 'Only a few'"
    },
    {
        "id": "syl-42",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. No gold is silver.\n2. All silver is platinum.\n3. Some platinum is diamond.\nConclusions:\nI. Some platinum is not gold.\nII. All gold being diamond is a possibility.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "The platinum that is silver cannot be gold (I follows). There is no negative statement between gold and diamond, so All gold being diamond is a valid possibility (II follows). Both follow.",
        "formula": "Negative cross-set deduction and possibility"
    },
    {
        "id": "syl-43",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few roads are highways.\n2. No highway is a track.\nConclusions:\nI. Some roads are not highways.\nII. Some roads are not tracks.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "By 'Only a few', some roads are not highways (I follows). The roads that are highways cannot be tracks, so Some roads are not tracks (II follows). Both follow.",
        "formula": "Compound negative consequence of 'Only a few'"
    },
    {
        "id": "syl-44",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. All doors are windows.\n2. Some windows are walls.\n3. No wall is a roof.\nConclusions:\nI. Some windows are not roofs.\nII. All doors being walls is a possibility.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "Those windows that are walls cannot be roofs (I follows). There is no restriction preventing doors from being inside walls (II follows as a possibility). Both follow.",
        "formula": "Disjoint overlap and unconstrained inclusion possibility"
    },
    {
        "id": "syl-45",
        "topic": "Syllogisms",
        "difficulty": "Hard",
        "question": "Statements:\n1. Only a few keys are locks.\n2. All locks are doors.\n3. No door is a window.\nConclusions:\nI. All keys can never be locks.\nII. No lock is a window.",
        "options": [
            {"id": "A", "text": "Only conclusion I follows"},
            {"id": "B", "text": "Only conclusion II follows"},
            {"id": "C", "text": "Both conclusions I and II follow"},
            {"id": "D", "text": "Neither follows"}
        ],
        "correct_answer": "C",
        "explanation": "'Only a few keys are locks' implies that some keys are definitely not locks, so all keys can never be locks (I follows). Locks ⊆ Doors and Doors ∩ Windows = ∅ $\implies$ No lock is a window (II follows). Both follow.",
        "formula": "Transitive negative disjointness + 'Only a few' constraint"
    }
]
