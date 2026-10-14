# -*- coding: utf-8 -*-
"""
Coding-Decoding Question Bank (45 verified questions: 15 Easy, 15 Medium, 15 Hard).
"""

from typing import List, Dict, Any

CODING_DECODING_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "cd-1",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code, 'APPLE' is written as 'BQQMF'. How is 'GRAPE' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "HSBQF"
            },
            {
                "id": "B",
                "text": "HSBPF"
            },
            {
                "id": "C",
                "text": "HTBQF"
            },
            {
                "id": "D",
                "text": "HQBQF"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is shifted forward by +1: A->B, P->Q, P->Q, L->M, E->F. Applying +1 to GRAPE: G+1=H, R+1=S, A+1=B, P+1=Q, E+1=F => HSBQF.",
        "formula": "Forward Shift: Letter(i) -> Letter(i) + 1"
    },
    {
        "id": "cd-2",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If 'CAT' is coded as 24 and 'DOG' is coded as 26, how will 'FOX' be coded?",
        "options": [
            {
                "id": "A",
                "text": "42"
            },
            {
                "id": "B",
                "text": "45"
            },
            {
                "id": "C",
                "text": "48"
            },
            {
                "id": "D",
                "text": "50"
            }
        ],
        "correct_answer": "B",
        "explanation": "The code is the sum of alphabetical positions: CAT = 3 + 1 + 20 = 24. DOG = 4 + 15 + 7 = 26. For FOX: F = 6, O = 15, X = 24. Sum = 6 + 15 + 24 = 45.",
        "formula": "Alphabetical Position Sum: Code = Sum(Position(Char))"
    },
    {
        "id": "cd-7",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code, 'LIGHT' is written as 'MJHIU'. How is 'FLAME' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "GMBOF"
            },
            {
                "id": "B",
                "text": "GMBNF"
            },
            {
                "id": "C",
                "text": "GLBNF"
            },
            {
                "id": "D",
                "text": "HMBNF"
            }
        ],
        "correct_answer": "B",
        "explanation": "Each letter is shifted forward by +1: L+1=M, I+1=J, G+1=H, H+1=I, T+1=U. Applying the +1 shift to 'FLAME': F+1=G, L+1=M, A+1=B, M+1=N, E+1=F, giving 'GMBNF'.",
        "formula": "Forward Shift: C_i = P_i + 1"
    },
    {
        "id": "cd-8",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code language, 'SMART' is written as 'TRAMS'. How will 'BRAIN' be written in that code?",
        "options": [
            {
                "id": "A",
                "text": "NIRAB"
            },
            {
                "id": "B",
                "text": "NIAER"
            },
            {
                "id": "C",
                "text": "NIARB"
            },
            {
                "id": "D",
                "text": "NIBRA"
            }
        ],
        "correct_answer": "C",
        "explanation": "The letters of the word are written in completely reversed order: S-M-A-R-T becomes T-R-A-M-S. Reversing the letters of 'BRAIN' (B-R-A-I-N) gives 'NIARB'.",
        "formula": "Reversal Pattern: Word[i] -> Word[n - 1 - i]"
    },
    {
        "id": "cd-9",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If each letter is assigned a numerical value corresponding to its alphabetical position (A = 1, B = 2, ..., Z = 26), what is the code for the word 'MATH'?",
        "options": [
            {
                "id": "A",
                "text": "38"
            },
            {
                "id": "B",
                "text": "40"
            },
            {
                "id": "C",
                "text": "42"
            },
            {
                "id": "D",
                "text": "45"
            }
        ],
        "correct_answer": "C",
        "explanation": "Substitute each letter with its 1-indexed alphabetical position and sum them: M = 13, A = 1, T = 20, H = 8. Sum = 13 + 1 + 20 + 8 = 42.",
        "formula": "Alphabetical Position Sum: Code = Sum(Position(char))"
    },
    {
        "id": "cd-10",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a code language, 'COLD' is written as 'BNKC'. How will 'WARM' be written in that code?",
        "options": [
            {
                "id": "A",
                "text": "UYPK"
            },
            {
                "id": "B",
                "text": "VZRL"
            },
            {
                "id": "C",
                "text": "UZQL"
            },
            {
                "id": "D",
                "text": "VZQL"
            }
        ],
        "correct_answer": "D",
        "explanation": "Each letter is shifted backward by -1: C-1=B, O-1=N, L-1=K, D-1=C. Applying -1 to 'WARM': W-1=V, A-1=Z (wrapping around), R-1=Q, M-1=L, yielding 'VZQL'.",
        "formula": "Backward Shift (-1): C_i = P_i - 1"
    },
    {
        "id": "cd-19",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code, 'CLOUD' is written as 'DMPVE'. How is 'SMILE' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "TNJMF"
            },
            {
                "id": "B",
                "text": "TMJMF"
            },
            {
                "id": "C",
                "text": "TNJME"
            },
            {
                "id": "D",
                "text": "SNJMF"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is shifted +1: C(+1)=D, L(+1)=M, O(+1)=P, U(+1)=V, D(+1)=E. Applying this to SMILE: S(+1)=T, M(+1)=N, I(+1)=J, L(+1)=M, E(+1)=F. Thus, the code is TNJMF.",
        "formula": "Letter Shift: New Letter = (Position + 1)"
    },
    {
        "id": "cd-20",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If 'PAPER' is coded as 'OZODQ', how is 'PENNY' coded in that system?",
        "options": [
            {
                "id": "A",
                "text": "ODMMX"
            },
            {
                "id": "B",
                "text": "QFOOZ"
            },
            {
                "id": "C",
                "text": "OEMMX"
            },
            {
                "id": "D",
                "text": "ODLLX"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is shifted backward by 1 position (-1): P(-1)=O, A(-1)=Z, P(-1)=O, E(-1)=D, R(-1)=Q. For PENNY: P(-1)=O, E(-1)=D, N(-1)=M, N(-1)=M, Y(-1)=X. The resulting code is ODMMX.",
        "formula": "Letter Shift: New Letter = (Position - 1)"
    },
    {
        "id": "cd-21",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code language, 'WATER' is coded as 'RETAW'. How is 'DREAM' coded in that language?",
        "options": [
            {
                "id": "A",
                "text": "MAERD"
            },
            {
                "id": "B",
                "text": "MARD"
            },
            {
                "id": "C",
                "text": "MDAER"
            },
            {
                "id": "D",
                "text": "EMARD"
            }
        ],
        "correct_answer": "A",
        "explanation": "The word is written in reverse order of its letters: WATER -> RETAW. Similarly, DREAM written backwards is MAERD.",
        "formula": "Reversal Rule: Word is written from right to left."
    },
    {
        "id": "cd-22",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If 'ROSE' is coded as 6821 and 'CHAIR' is coded as 73456, what is the code for 'SEARCH'?",
        "options": [
            {
                "id": "A",
                "text": "214673"
            },
            {
                "id": "B",
                "text": "214763"
            },
            {
                "id": "C",
                "text": "216473"
            },
            {
                "id": "D",
                "text": "241673"
            }
        ],
        "correct_answer": "A",
        "explanation": "Direct letter-to-digit substitution: R=6, O=8, S=2, E=1, C=7, H=3, A=4, I=5. For SEARCH: S=2, E=1, A=4, R=6, C=7, H=3 -> 214673.",
        "formula": "Direct Symbol Substitution"
    },
    {
        "id": "cd-23",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If 'CAT' is coded as 24 and 'DOG' is coded as 26, how is 'PIG' coded in that language?",
        "options": [
            {
                "id": "A",
                "text": "30"
            },
            {
                "id": "B",
                "text": "32"
            },
            {
                "id": "C",
                "text": "34"
            },
            {
                "id": "D",
                "text": "28"
            }
        ],
        "correct_answer": "B",
        "explanation": "The code represents the sum of alphabetical positions of the letters: CAT = 3 + 1 + 20 = 24. DOG = 4 + 15 + 7 = 26. For PIG: P=16, I=9, G=7. Sum = 16 + 9 + 7 = 32.",
        "formula": "Alphabetical Positional Sum: Code = Sum(Position(letter))"
    },
    {
        "id": "cd-24",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code, 'BIRD' is written as 'CJSE'. How is 'FROG' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "GSPH"
            },
            {
                "id": "B",
                "text": "GTOH"
            },
            {
                "id": "C",
                "text": "GROH"
            },
            {
                "id": "D",
                "text": "GSQI"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is advanced by +1: B(+1)=C, I(+1)=J, R(+1)=S, D(+1)=E. Applying this to FROG: F(+1)=G, R(+1)=S, O(+1)=P, G(+1)=H. The result is GSPH.",
        "formula": "Letter Shift: +1 to each letter"
    },
    {
        "id": "cd-25",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If 'LIGHT' is written as 'MJHIU', what is the code for 'HEAVY'?",
        "options": [
            {
                "id": "A",
                "text": "IFBWZ"
            },
            {
                "id": "B",
                "text": "IFCWZ"
            },
            {
                "id": "C",
                "text": "IEBWZ"
            },
            {
                "id": "D",
                "text": "JGBWZ"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is shifted forward by +1: L->M, I->J, G->H, H->I, T->U. For HEAVY: H(+1)=I, E(+1)=F, A(+1)=B, V(+1)=W, Y(+1)=Z. The code is IFBWZ.",
        "formula": "Shift Rule: +1 forward shift"
    },
    {
        "id": "cd-26",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "If 'APPLE' is coded as 50, what is the code for 'ORANGE'?",
        "options": [
            {
                "id": "A",
                "text": "58"
            },
            {
                "id": "B",
                "text": "60"
            },
            {
                "id": "C",
                "text": "62"
            },
            {
                "id": "D",
                "text": "64"
            }
        ],
        "correct_answer": "B",
        "explanation": "The code is the sum of standard 1-indexed alphabetical positions: APPLE = 1 + 16 + 16 + 12 + 5 = 50. ORANGE = O(15) + R(18) + A(1) + N(14) + G(7) + E(5) = 15 + 18 + 1 + 14 + 7 + 5 = 60.",
        "formula": "Word Value = Sum of 1-indexed alphabetical positions"
    },
    {
        "id": "cd-27",
        "topic": "Coding-Decoding",
        "difficulty": "Easy",
        "question": "In a certain code, 'STOVE' is written as 'EVOTS'. How is 'CANDLE' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "ELDNAC"
            },
            {
                "id": "B",
                "text": "ELDCAN"
            },
            {
                "id": "C",
                "text": "EDLNAC"
            },
            {
                "id": "D",
                "text": "ELDNCA"
            }
        ],
        "correct_answer": "A",
        "explanation": "The letters of the word are written in completely reversed order: S-T-O-V-E becomes E-V-O-T-S. Reversing C-A-N-D-L-E gives E-L-D-N-A-C.",
        "formula": "Reversal of string"
    },
    {
        "id": "cd-3",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "In a code language, 'ROSE' is coded as 'ILHV'. How will 'TULIP' be coded in the same system?",
        "options": [
            {
                "id": "A",
                "text": "GFORK"
            },
            {
                "id": "B",
                "text": "GFOKK"
            },
            {
                "id": "C",
                "text": "GFOVR"
            },
            {
                "id": "D",
                "text": "GEORK"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is replaced by its reverse alphabet counterpart (sum of positions = 27): R(18)<->I(9), O(15)<->L(12), S(19)<->H(8), E(5)<->V(22). For TULIP: T(20)<->G(7), U(21)<->F(6), L(12)<->O(15), I(9)<->R(18), P(16)<->K(11) => GFORK.",
        "formula": "Reverse Alphabet Rule: Position_new = 27 - Position_original"
    },
    {
        "id": "cd-4",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'WATER' is coded as 'YCVGT', how will 'FIRE' be coded?",
        "options": [
            {
                "id": "A",
                "text": "HKTG"
            },
            {
                "id": "B",
                "text": "GJSF"
            },
            {
                "id": "C",
                "text": "HKTF"
            },
            {
                "id": "D",
                "text": "HKSG"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is shifted forward by +2: W+2=Y, A+2=C, T+2=V, E+2=G, R+2=T. For FIRE: F+2=H, I+2=K, R+2=T, E+2=G => HKTG.",
        "formula": "Forward Shift (+2): C_i = (P_i + 2)"
    },
    {
        "id": "cd-11",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "In a code language, 'CLOUD' is written as 'DKPTE'. What is the code for 'SMILE'?",
        "options": [
            {
                "id": "A",
                "text": "TKJKF"
            },
            {
                "id": "B",
                "text": "TLJKF"
            },
            {
                "id": "C",
                "text": "TLIKF"
            },
            {
                "id": "D",
                "text": "TMJLE"
            }
        ],
        "correct_answer": "B",
        "explanation": "The letters undergo alternating shifts (+1, -1, +1, -1, +1): C+1=D, L-1=K, O+1=P, U-1=T, D+1=E. Applying the same alternating pattern to 'SMILE': S+1=T, M-1=L, I+1=J, L-1=K, E+1=F, resulting in 'TLJKF'.",
        "formula": "Alternating Shift: (+1, -1, +1, -1, +1)"
    },
    {
        "id": "cd-12",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "In a certain code, 'PRISM' is written as 'QTLWR' by progressively increasing the forward shift (+1, +2, +3, +4, +5). How is 'TRACK' coded under the same rule?",
        "options": [
            {
                "id": "A",
                "text": "UTDHP"
            },
            {
                "id": "B",
                "text": "UTEGP"
            },
            {
                "id": "C",
                "text": "UTDGP"
            },
            {
                "id": "D",
                "text": "USDGP"
            }
        ],
        "correct_answer": "C",
        "explanation": "The shift increases progressively with position (+1, +2, +3, +4, +5). For 'TRACK': T+1=U, R+2=T, A+3=D, C+4=G, K+5=P. The resulting coded word is 'UTDGP'.",
        "formula": "Progressive Forward Shift: C_i = P_i + i"
    },
    {
        "id": "cd-13",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "In a certain code, each vowel is replaced by the next sequential vowel (A->E, E->I, I->O, O->U, U->A) and each consonant is replaced by the next consonant letter (+1 in alphabet). How is 'DRIVE' written in this code?",
        "options": [
            {
                "id": "A",
                "text": "EROVI"
            },
            {
                "id": "B",
                "text": "ESOWE"
            },
            {
                "id": "C",
                "text": "FTOWI"
            },
            {
                "id": "D",
                "text": "ESOWI"
            }
        ],
        "correct_answer": "D",
        "explanation": "Following the rule: Consonant D+1 = E; Consonant R+1 = S; Vowel I -> next vowel O; Consonant V+1 = W; Vowel E -> next vowel I. Combining these gives 'ESOWI'.",
        "formula": "Vowels: Next Vowel in (A, E, I, O, U); Consonants: Next Letter (+1)"
    },
    {
        "id": "cd-14",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'orange' is called 'butter', 'butter' is called 'soap', 'soap' is called 'ink', 'ink' is called 'honey', and 'honey' is called 'orange', which of the following is used for washing clothes?",
        "options": [
            {
                "id": "A",
                "text": "honey"
            },
            {
                "id": "B",
                "text": "ink"
            },
            {
                "id": "C",
                "text": "butter"
            },
            {
                "id": "D",
                "text": "soap"
            }
        ],
        "correct_answer": "B",
        "explanation": "In reality, 'soap' is used for washing clothes. According to the substitution rule, 'soap' is called 'ink'. Therefore, 'ink' is the correct answer.",
        "formula": "Direct Substitution: Target Object -> Assigned Code Word"
    },
    {
        "id": "cd-28",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'MONKEY' is written as 'XDJMNL', how is 'TIGER' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "QDFHS"
            },
            {
                "id": "B",
                "text": "SDFHQ"
            },
            {
                "id": "C",
                "text": "UJHFS"
            },
            {
                "id": "D",
                "text": "SHFDQ"
            }
        ],
        "correct_answer": "A",
        "explanation": "The word is read from right to left, and each letter is shifted backward by 1: Y-1=X, E-1=D, K-1=J, N-1=M, O-1=N, M-1=L. For TIGER: R-1=Q, E-1=D, G-1=F, I-1=H, T-1=S. Result: QDFHS.",
        "formula": "Reversal followed by -1 shift: Output[i] = Word[n - 1 - i] - 1"
    },
    {
        "id": "cd-29",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'SPRING' is coded as 'USTLPJ' under an alternating shift pattern (+2, +3), how is 'WINTER' coded under the same rule?",
        "options": [
            {
                "id": "A",
                "text": "YLPWGU"
            },
            {
                "id": "B",
                "text": "YMPVGU"
            },
            {
                "id": "C",
                "text": "XKPWGU"
            },
            {
                "id": "D",
                "text": "YLPWHV"
            }
        ],
        "correct_answer": "A",
        "explanation": "Alternating pattern is (+2, +3): S(+2)=U, P(+3)=S, R(+2)=T, I(+3)=L, N(+2)=P, G(+3)=J. Applying to WINTER: W(+2)=Y, I(+3)=L, N(+2)=P, T(+3)=W, E(+2)=G, R(+3)=U. Result: YLPWGU.",
        "formula": "Alternating shift: +2, +3, +2, +3..."
    },
    {
        "id": "cd-30",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "In a certain code language: 'pit dar na' means 'you are good', 'dar tok pa' means 'good and bad', and 'tim na tok' means 'they are bad'. What is the code for 'and'?",
        "options": [
            {
                "id": "A",
                "text": "pa"
            },
            {
                "id": "B",
                "text": "dar"
            },
            {
                "id": "C",
                "text": "tok"
            },
            {
                "id": "D",
                "text": "na"
            }
        ],
        "correct_answer": "A",
        "explanation": "Comparing 'pit dar na' (you are good) and 'dar tok pa' (good and bad), the common word is 'good' and common code is 'dar' -> good = dar. Comparing 'dar tok pa' (good and bad) and 'tim na tok' (they are bad), the common word is 'bad' and common code is 'tok' -> bad = tok. In 'dar tok pa' (good and bad), with good=dar and bad=tok, the remaining code 'pa' stands for 'and'.",
        "formula": "Fictitious Language Elimination: Match common words across statements."
    },
    {
        "id": "cd-31",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'DELHI' is coded as 73541 and 'CALCUTTA' is coded as 82589662, how is 'CALICUT' coded?",
        "options": [
            {
                "id": "A",
                "text": "8251896"
            },
            {
                "id": "B",
                "text": "8251869"
            },
            {
                "id": "C",
                "text": "8521896"
            },
            {
                "id": "D",
                "text": "8251986"
            }
        ],
        "correct_answer": "A",
        "explanation": "Direct letter mapping from given words: C=8, A=2, L=5, I=1 (from DELHI: I=1), C=8, U=9, T=6. Assembling 'CALICUT': C=8, A=2, L=5, I=1, C=8, U=9, T=6 -> 8251896.",
        "formula": "Direct letter-digit correlation"
    },
    {
        "id": "cd-32",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'SYSTEM' is written as 'SYSMET' and 'NEARER' is written as 'AENRER', how is 'FRACTION' written in that code?",
        "options": [
            {
                "id": "A",
                "text": "CARFNOIT"
            },
            {
                "id": "B",
                "text": "CRAFNOIT"
            },
            {
                "id": "C",
                "text": "CARFTION"
            },
            {
                "id": "D",
                "text": "ARCFNOIT"
            }
        ],
        "correct_answer": "A",
        "explanation": "The 8-letter word is split into two halves of 4 letters each: 'FRAC' and 'TION'. Each half is reversed independently: 'FRAC' reversed is 'CARF', and 'TION' reversed is 'NOIT'. Combining them gives 'CARFNOIT'.",
        "formula": "Partition and reverse each half"
    },
    {
        "id": "cd-33",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'LEMON' is coded as 'ELMNO' and 'GRAPE' is coded as 'AEGPR', how is 'ORANGE' coded under the same rule?",
        "options": [
            {
                "id": "A",
                "text": "AEGNOR"
            },
            {
                "id": "B",
                "text": "AEGORN"
            },
            {
                "id": "C",
                "text": "AENOGR"
            },
            {
                "id": "D",
                "text": "EAGNOR"
            }
        ],
        "correct_answer": "A",
        "explanation": "The rule sorts the letters of the word in ascending alphabetical order. For ORANGE: A, E, G, N, O, R -> AEGNOR.",
        "formula": "Alphabetical sorting of constituent letters"
    },
    {
        "id": "cd-34",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If each consonant in 'PRODUCT' is replaced by the preceding letter in English alphabet and each vowel is replaced by the next letter, what will be the resulting word?",
        "options": [
            {
                "id": "A",
                "text": "OQPCVBS"
            },
            {
                "id": "B",
                "text": "OQPBVAS"
            },
            {
                "id": "C",
                "text": "OQPDCBS"
            },
            {
                "id": "D",
                "text": "PQPBVBS"
            }
        ],
        "correct_answer": "A",
        "explanation": "Consonants shift -1; vowels shift +1: P(consonant)->O, R(consonant)->Q, O(vowel)->P, D(consonant)->C, U(vowel)->V, C(consonant)->B, T(consonant)->S. The word formed is OQPCVBS.",
        "formula": "Consonants: Letter - 1; Vowels: Letter + 1"
    },
    {
        "id": "cd-35",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "In a certain code, '786' means 'study very hard', '958' means 'hard work pays', and '645' means 'study and work'. Which digit represents 'and'?",
        "options": [
            {
                "id": "A",
                "text": "4"
            },
            {
                "id": "B",
                "text": "6"
            },
            {
                "id": "C",
                "text": "5"
            },
            {
                "id": "D",
                "text": "8"
            }
        ],
        "correct_answer": "A",
        "explanation": "Comparing 786 and 958: common digit is 8, common word is 'hard' -> hard = 8. Comparing 786 and 645: common digit is 6, common word is 'study' -> study = 6. Comparing 958 and 645: common digit is 5, common word is 'work' -> work = 5. In 645 ('study and work'), 6 is study and 5 is work, so the remaining digit 4 must represent 'and'.",
        "formula": "Elimination of common coded elements"
    },
    {
        "id": "cd-36",
        "topic": "Coding-Decoding",
        "difficulty": "Medium",
        "question": "If 'GLAMOUR' is coded as 'IKCLQTT' with an alternating shift of (+2, -1), how is 'MISRULE' coded under the same rule?",
        "options": [
            {
                "id": "A",
                "text": "OHUQWKG"
            },
            {
                "id": "B",
                "text": "OIUQWKG"
            },
            {
                "id": "C",
                "text": "OHUQVJG"
            },
            {
                "id": "D",
                "text": "PHUQWKG"
            }
        ],
        "correct_answer": "A",
        "explanation": "Pattern is alternating (+2, -1): M(+2)=O, I(-1)=H, S(+2)=U, R(-1)=Q, U(+2)=W, L(-1)=K, E(+2)=G. The coded word is OHUQWKG.",
        "formula": "Alternating pattern: +2, -1, +2, -1, +2, -1, +2"
    },
    {
        "id": "cd-5",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a military cipher, 'BRAVE' is written as 'EUDYH'. If a message is received as 'SKBVL', what was the original decrypted word?",
        "options": [
            {
                "id": "A",
                "text": "PHESI"
            },
            {
                "id": "B",
                "text": "PHYSICS"
            },
            {
                "id": "C",
                "text": "PHYSI"
            },
            {
                "id": "D",
                "text": "PEYSI"
            }
        ],
        "correct_answer": "C",
        "explanation": "The encryption rule shifts each letter forward by +3 (B+3=E, R+3=U, A+3=D, V+3=Y, E+3=H). To decrypt 'SKBVL', each letter must be shifted backward by 3 positions: S(19)-3=P(16), K(11)-3=H(8), B(2)-3=Y(25), V(22)-3=S(19), L(12)-3=I(9). Thus, the original decrypted word is 'PHYSI'.",
        "formula": "Decryption Shift: P_i = (C_i - 3) mod 26"
    },
    {
        "id": "cd-6",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a substitution cipher: 'pit dar na' means 'books are good', 'dar tok pa' means 'we are ready', and 'na tok se' means 'good ready pens'. What code word stands for 'books'?",
        "options": [
            {
                "id": "A",
                "text": "pit"
            },
            {
                "id": "B",
                "text": "dar"
            },
            {
                "id": "C",
                "text": "na"
            },
            {
                "id": "D",
                "text": "tok"
            }
        ],
        "correct_answer": "A",
        "explanation": "Comparing 1 & 2: 'dar' is common to both, and 'are' is common, so 'dar' = 'are'. Comparing 1 & 3: 'na' is common to both, and 'good' is common, so 'na' = 'good'. In sentence 1 ('books are good' = 'pit dar na'), 'dar'='are' and 'na'='good'. Therefore, the remaining code 'pit' corresponds to 'books'.",
        "formula": "Fictitious Language Elimination Method"
    },
    {
        "id": "cd-15",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a code language, each letter is first replaced by its opposite letter in the alphabet (where A corresponds to Z, B to Y, etc., sum = 27), and then shifted forward by +1. Under this system, what is the code for 'GOLD'?",
        "options": [
            {
                "id": "A",
                "text": "TLOX"
            },
            {
                "id": "B",
                "text": "VMPX"
            },
            {
                "id": "C",
                "text": "UMPX"
            },
            {
                "id": "D",
                "text": "UMQY"
            }
        ],
        "correct_answer": "C",
        "explanation": "Step 1: Find reverse alphabet pairs (27 - position): G(7)->T(20), O(15)->L(12), L(12)->O(15), D(4)->W(23). Step 2: Shift each resulting letter forward by +1: T+1=U, L+1=M, O+1=P, W+1=X. The resulting code is 'UMPX'.",
        "formula": "Combined Cipher: C_i = (27 - P_i) + 1"
    },
    {
        "id": "cd-16",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a certain code language: 'tik pod sun' means 'sky is clear', 'pod ler mot' means 'clear water blue', and 'mot sun dar' means 'blue sky bright'. Which code word represents 'bright'?",
        "options": [
            {
                "id": "A",
                "text": "mot"
            },
            {
                "id": "B",
                "text": "sun"
            },
            {
                "id": "C",
                "text": "pod"
            },
            {
                "id": "D",
                "text": "dar"
            }
        ],
        "correct_answer": "D",
        "explanation": "Comparing statement 1 ('tik pod sun' = 'sky is clear') and statement 2 ('pod ler mot' = 'clear water blue'): common code is 'pod' and common word is 'clear', so 'pod' = 'clear'. Comparing statements 1 and 3 ('mot sun dar' = 'blue sky bright'): common code is 'sun' and common word is 'sky', so 'sun' = 'sky'. Comparing statements 2 and 3: common code is 'mot' and common word is 'blue', so 'mot' = 'blue'. In statement 3, the remaining code 'dar' corresponds to the remaining word 'bright'.",
        "formula": "Set Intersection and Elimination Method"
    },
    {
        "id": "cd-17",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a code language, a 6-letter word is split into two equal halves of 3 letters each. Each half is reversed, and then every letter is shifted forward by +2. If 'MASTER' becomes 'UCOTGF' (MAS->SAM->UCO, TER->RET->TGF), how will 'SYSTEM' be coded?",
        "options": [
            {
                "id": "A",
                "text": "UAUOHV"
            },
            {
                "id": "B",
                "text": "UAUOGV"
            },
            {
                "id": "C",
                "text": "VAUOGV"
            },
            {
                "id": "D",
                "text": "UATOGV"
            }
        ],
        "correct_answer": "B",
        "explanation": "First half: 'SYS'. Reversing gives 'SYS'. Shifting each letter by +2: S(19)+2=U(21), Y(25)+2=A(1), S(19)+2=U(21) => 'UAU'. Second half: 'TEM'. Reversing gives 'MET'. Shifting each letter by +2: M(13)+2=O(15), E(5)+2=G(7), T(20)+2=V(22) => 'OGV'. Combining both halves gives 'UAUOGV'.",
        "formula": "Half-Word Reversal + Forward Shift (+2)"
    },
    {
        "id": "cd-18",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "If 'PEN' is coded as 105 (sum of letter positions 16+5+14 = 35, multiplied by 3 letters = 105), and 'BOOK' is coded as 172 (sum of positions 2+15+15+11 = 43, multiplied by 4 letters = 172), how will 'NOTE' be coded?",
        "options": [
            {
                "id": "A",
                "text": "208"
            },
            {
                "id": "B",
                "text": "224"
            },
            {
                "id": "C",
                "text": "216"
            },
            {
                "id": "D",
                "text": "212"
            }
        ],
        "correct_answer": "C",
        "explanation": "Calculate the sum of alphabetical positions for 'NOTE': N = 14, O = 15, T = 20, E = 5. Sum = 14 + 15 + 20 + 5 = 54. The number of letters in 'NOTE' is 4. Multiply the sum by the letter count: 54 × 4 = 216.",
        "formula": "Code = (Sum of alphabetical positions) × (Number of letters)"
    },
    {
        "id": "cd-37",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a special code, letters at odd positions (1st, 3rd, 5th) are shifted +3, while letters at even positions (2nd, 4th, 6th) are replaced by their opposite alphabet pairs (A<->Z, B<->Y, etc.). How is 'STREAM' coded?",
        "options": [
            {
                "id": "A",
                "text": "VGUVDN"
            },
            {
                "id": "B",
                "text": "VGUWEN"
            },
            {
                "id": "C",
                "text": "UGUVDN"
            },
            {
                "id": "D",
                "text": "VGVVDN"
            }
        ],
        "correct_answer": "A",
        "explanation": "Positions: 1st (S): S(+3) = V; 2nd (T): T opposite is G (27 - 20 = 7); 3rd (R): R(+3) = U; 4th (E): E opposite is V (27 - 5 = 22); 5th (A): A(+3) = D; 6th (M): M opposite is N (27 - 13 = 14). Resulting code: VGUVDN.",
        "formula": "Odd pos: Pos + 3; Even pos: 27 - Pos"
    },
    {
        "id": "cd-38",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "If each consonant is assigned its standard alphabetical position and each vowel is assigned twice its position, what is the total numerical value of the word 'INSIGHT'?",
        "options": [
            {
                "id": "A",
                "text": "104"
            },
            {
                "id": "B",
                "text": "98"
            },
            {
                "id": "C",
                "text": "112"
            },
            {
                "id": "D",
                "text": "100"
            }
        ],
        "correct_answer": "A",
        "explanation": "Vowels take 2 × position; consonants take 1 × position. I (vowel): 9 × 2 = 18; N (consonant): 14; S (consonant): 19; I (vowel): 9 × 2 = 18; G (consonant): 7; H (consonant): 8; T (consonant): 20. Total = 18 + 14 + 19 + 18 + 7 + 8 + 20 = 104.",
        "formula": "Value = Sum(Consonant values) + 2 × Sum(Vowel values)"
    },
    {
        "id": "cd-39",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a certain code language, 'MACHINE' is coded as '19-7-9-14-15-20-11'. How is 'DANGER' coded in that language?",
        "options": [
            {
                "id": "A",
                "text": "10-7-20-13-11-24"
            },
            {
                "id": "B",
                "text": "11-7-20-13-11-24"
            },
            {
                "id": "C",
                "text": "10-7-20-14-11-24"
            },
            {
                "id": "D",
                "text": "10-8-20-13-11-24"
            }
        ],
        "correct_answer": "A",
        "explanation": "Each letter is represented by its standard numerical position plus 6: M(13)+6=19, A(1)+6=7, C(3)+6=9, H(8)+6=14, I(9)+6=15, N(14)+6=20, E(5)+6=11. For DANGER: D(4)+6=10, A(1)+6=7, N(14)+6=20, G(7)+6=13, E(5)+6=11, R(18)+6=24. The code is 10-7-20-13-11-24.",
        "formula": "Code = Positional Rank + 6"
    },
    {
        "id": "cd-40",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a certain code language:\n'economics is not money' is coded as 'ka la ho ga'\n'demand and supply economics' is coded as 'mo ta pa ka'\n'money makes only part' is coded as 'zi ne ho ki'\n'demand makes supply easy' is coded as 'zi mo pa zo'\nWhat is the code for 'makes'?",
        "options": [
            {
                "id": "A",
                "text": "zi"
            },
            {
                "id": "B",
                "text": "mo"
            },
            {
                "id": "C",
                "text": "pa"
            },
            {
                "id": "D",
                "text": "ho"
            }
        ],
        "correct_answer": "A",
        "explanation": "Compare the 3rd sentence ('money makes only part' = 'zi ne ho ki') and the 4th sentence ('demand makes supply easy' = 'zi mo pa zo'). In sentences 1, 2, 3, 4: 'money' appears in 1 & 3 ('ho'); 'demand' and 'supply' appear in 2 & 4 ('mo', 'pa'). The only word common exclusively to sentences 3 and 4 is 'makes', and the only code common to both is 'zi'. Thus, 'makes' = 'zi'.",
        "formula": "Multi-statement intersection analysis"
    },
    {
        "id": "cd-41",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "Based on the code system in the previous question:\n'economics is not money' -> 'ka la ho ga'\n'demand and supply economics' -> 'mo ta pa ka'\n'money makes only part' -> 'zi ne ho ki'\nWhat is the code for 'not'?",
        "options": [
            {
                "id": "A",
                "text": "la"
            },
            {
                "id": "B",
                "text": "ga"
            },
            {
                "id": "C",
                "text": "Either la or ga"
            },
            {
                "id": "D",
                "text": "ho"
            }
        ],
        "correct_answer": "C",
        "explanation": "From 'economics is not money' = 'ka la ho ga': 'economics' is 'ka' (common with sentence 2), 'money' is 'ho' (common with sentence 3). The remaining two words are 'is' and 'not', and the remaining two codes are 'la' and 'ga'. Neither appears in any other sentence, so 'not' can be either 'la' or 'ga'.",
        "formula": "Indeterminate deduction: Disjunction of remaining valid codes"
    },
    {
        "id": "cd-42",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a certain code, 'TRIANGLE' is written as 'SSHBMHKF' with an alternating shift of (-1, +1, -1, +1...). How is 'POLYGON' coded under this pattern?",
        "options": [
            {
                "id": "A",
                "text": "OPKZFPM"
            },
            {
                "id": "B",
                "text": "OQKZFPM"
            },
            {
                "id": "C",
                "text": "OPKZFON"
            },
            {
                "id": "D",
                "text": "PQKZFPM"
            }
        ],
        "correct_answer": "A",
        "explanation": "Pattern: T(-1)=S, R(+1)=S, I(-1)=H, A(+1)=B, N(-1)=M, G(+1)=H, L(-1)=K, E(+1)=F. Applying (-1, +1, -1, +1, -1, +1, -1) to POLYGON: P(-1)=O, O(+1)=P, L(-1)=K, Y(+1)=Z, G(-1)=F, O(+1)=P, N(-1)=M. Result: OPKZFPM.",
        "formula": "Alternating pattern: -1, +1, -1, +1, -1, +1, -1"
    },
    {
        "id": "cd-43",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a code, each word is transformed into: [Length of word] + [First letter + 1] + [Last letter - 1]. For example, 'TALK' -> 4UJ (Length=4, T+1=U, K-1=J). How is 'STREAM' coded under this rule?",
        "options": [
            {
                "id": "A",
                "text": "6TL"
            },
            {
                "id": "B",
                "text": "6SL"
            },
            {
                "id": "C",
                "text": "6TM"
            },
            {
                "id": "D",
                "text": "5TL"
            }
        ],
        "correct_answer": "A",
        "explanation": "Word: 'STREAM'. Length = 6. First letter S + 1 = T. Last letter M - 1 = L. Combining the parts: 6 + T + L = '6TL'.",
        "formula": "Composite Rule: Length + Shift(First, +1) + Shift(Last, -1)"
    },
    {
        "id": "cd-44",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "If 'MASTER' is coded by writing the positional numbers of its letters in reverse order: '18-5-20-19-1-13', how is 'KNIGHT' coded?",
        "options": [
            {
                "id": "A",
                "text": "20-8-7-9-14-11"
            },
            {
                "id": "B",
                "text": "20-8-7-9-11-14"
            },
            {
                "id": "C",
                "text": "11-14-9-7-8-20"
            },
            {
                "id": "D",
                "text": "20-7-8-9-14-11"
            }
        ],
        "correct_answer": "A",
        "explanation": "Letter positions in forward order for KNIGHT: K=11, N=14, I=9, G=7, H=8, T=20. Reversed order gives: 20-8-7-9-14-11.",
        "formula": "Positional values listed from right to left"
    },
    {
        "id": "cd-45",
        "topic": "Coding-Decoding",
        "difficulty": "Hard",
        "question": "In a symbol-based binary system, 0 is coded as '*' and 1 is coded as '$'. A number is coded by its standard binary representation. For example, 3 is '11' -> '$$', and 4 is '100' -> '$**'. How is the decimal number 21 coded?",
        "options": [
            {
                "id": "A",
                "text": "$*$*$"
            },
            {
                "id": "B",
                "text": "$**$$"
            },
            {
                "id": "C",
                "text": "$$*$$"
            },
            {
                "id": "D",
                "text": "*$*$*"
            }
        ],
        "correct_answer": "A",
        "explanation": "Converting 21 to binary: 21 = 16 + 4 + 1 = 10101 in base 2. Replacing 1 with '$' and 0 with '*': 1 -> $, 0 -> *, 1 -> $, 0 -> *, 1 -> $. The final code is '$*$*$'.",
        "formula": "Decimal to Binary conversion with Symbol Substitution"
    }
]
