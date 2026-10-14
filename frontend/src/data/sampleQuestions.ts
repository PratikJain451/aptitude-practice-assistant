import type { Question } from '../types';

export const SAMPLE_QUESTIONS: Question[] = [
  // 1. Time and Work - Easy
  {
    id: 'tw-1',
    topicId: 'time-work',
    topicName: 'Time and Work',
    category: 'Quantitative',
    difficulty: 'Easy',
    question: 'A can complete a piece of work in 12 days, and B can complete the same work in 24 days. Working together, in how many days can they finish the entire work?',
    options: [
      { id: 'A', text: '6 days' },
      { id: 'B', text: '8 days' },
      { id: 'C', text: '9 days' },
      { id: 'D', text: '10 days' },
    ],
    correctOptionId: 'B',
    explanation: {
      summary: 'Combine individual daily work rates using the reciprocal rule or LCM method.',
      steps: [
        'Total Work = LCM(12, 24) = 24 units.',
        "A's 1-day work rate = 24 / 12 = 2 units/day.",
        "B's 1-day work rate = 24 / 24 = 1 unit/day.",
        'Combined 1-day work rate = 2 + 1 = 3 units/day.',
        'Time taken together = Total units / Combined rate = 24 / 3 = 8 days.',
      ],
      formula: 'Combined Time = (A × B) / (A + B) = (12 × 24) / (12 + 24) = 288 / 36 = 8 days',
    },
  },

  // 2. Time and Work - Medium
  {
    id: 'tw-2',
    topicId: 'time-work',
    topicName: 'Time and Work',
    category: 'Quantitative',
    difficulty: 'Medium',
    question: 'A and B can do a work in 15 days and 20 days respectively. They began the work together, but after 4 days A left. How many more days will B take to complete the remaining work alone?',
    options: [
      { id: 'A', text: '10 days' },
      { id: 'B', text: '10.67 days' },
      { id: 'C', text: '11.33 days' },
      { id: 'D', text: '12 days' },
    ],
    correctOptionId: 'B',
    explanation: {
      summary: 'Determine work completed in the first 4 days, then divide remaining work by B’s efficiency.',
      steps: [
        'Total Work = LCM(15, 20) = 60 units.',
        "A's efficiency = 60 / 15 = 4 units/day.",
        "B's efficiency = 60 / 20 = 3 units/day.",
        'Combined efficiency = 4 + 3 = 7 units/day.',
        'Work done in initial 4 days = 4 × 7 = 28 units.',
        'Remaining work = 60 - 28 = 32 units.',
        "Time for B alone to complete remainder = 32 / 3 = 10 2/3 days (approx 10.67 days).",
      ],
      formula: 'Remaining Time = (Total Work - Work Done) / Efficiency_B',
    },
  },

  // 3. Time and Work - Hard
  {
    id: 'tw-3',
    topicId: 'time-work',
    topicName: 'Time and Work',
    category: 'Quantitative',
    difficulty: 'Hard',
    question: 'Pipe A can fill a tank in 10 hours, Pipe B in 15 hours, while Pipe C can empty the full tank in 20 hours. All three pipes are opened simultaneously. How long will it take to fill the tank completely?',
    options: [
      { id: 'A', text: '7 hours 12 minutes' },
      { id: 'B', text: '8 hours 34 minutes' },
      { id: 'C', text: '9 hours 15 minutes' },
      { id: 'D', text: '8 hours 40 minutes' },
    ],
    correctOptionId: 'D',
    explanation: {
      summary: 'Pipes A and B are positive filling rates, whereas emptying Pipe C is negative rate.',
      steps: [
        'Total capacity = LCM(10, 15, 20) = 60 liters.',
        'Pipe A fills = 60 / 10 = +6 liters/hour.',
        'Pipe B fills = 60 / 15 = +4 liters/hour.',
        'Pipe C empties = 60 / 20 = -3 liters/hour.',
        'Net filling rate per hour = 6 + 4 - 3 = 7 liters/hour.',
        'Total time required = 60 / 7 hours = 8.5714 hours = 8 hours and (4/7 × 60) min ≈ 8 hours 34 minutes (exact: 8 hours 34 min 17 sec).',
      ],
      formula: 'Net Rate = (1/A) + (1/B) - (1/C) = 1/10 + 1/15 - 1/20 = 7/60 tank/hour',
    },
  },

  // 4. Speed, Time and Distance - Medium
  {
    id: 'spd-1',
    topicId: 'speed-distance',
    topicName: 'Speed, Time and Distance',
    category: 'Quantitative',
    difficulty: 'Medium',
    question: 'A train 180 meters long is traveling at a constant speed of 54 km/h. How many seconds will it take to cross a railway platform that is 270 meters long?',
    options: [
      { id: 'A', text: '24 seconds' },
      { id: 'B', text: '30 seconds' },
      { id: 'C', text: '36 seconds' },
      { id: 'D', text: '42 seconds' },
    ],
    correctOptionId: 'B',
    explanation: {
      summary: 'Total distance to cover is length of the train plus length of the platform. Convert speed from km/h to m/s.',
      steps: [
        'Speed in m/s = 54 × (5 / 18) = 15 m/s.',
        'Total distance = Train length + Platform length = 180 m + 270 m = 450 meters.',
        'Time = Distance / Speed = 450 / 15 = 30 seconds.',
      ],
      formula: 'Speed (m/s) = Speed (km/h) × 5/18; Time = Total Distance / Speed',
    },
  },

  // 5. Percentages and Profit & Loss - Easy
  {
    id: 'pl-1',
    topicId: 'percentages-profit',
    topicName: 'Percentages and Profit & Loss',
    category: 'Quantitative',
    difficulty: 'Easy',
    question: 'An item is purchased for ₹800 and marked 25% above cost. If a discount of 10% is offered on the marked price, what is the profit percentage earned by the merchant?',
    options: [
      { id: 'A', text: '12.5%' },
      { id: 'B', text: '15.0%' },
      { id: 'C', text: '17.5%' },
      { id: 'D', text: '10.0%' },
    ],
    correctOptionId: 'A',
    explanation: {
      summary: 'Compute the marked price after 25% markup, then deduct 10% discount to find effective selling price.',
      steps: [
        'Cost Price (CP) = ₹800.',
        'Marked Price (MP) = 800 × 1.25 = ₹1000.',
        'Selling Price (SP) after 10% discount = 1000 - (0.10 × 1000) = ₹900.',
        'Profit = SP - CP = 900 - 800 = ₹100.',
        'Profit % = (Profit / CP) × 100 = (100 / 800) × 100 = 12.5%.',
      ],
      formula: 'Effective Profit % = Markup% - Discount% - (Markup × Discount)/100 = 25 - 10 - 2.5 = 12.5%',
    },
  },

  // 6. Syllogisms - Medium
  {
    id: 'syl-1',
    topicId: 'syllogisms',
    topicName: 'Syllogisms and Venn Deductions',
    category: 'Logical Reasoning',
    difficulty: 'Medium',
    question: 'Statements:\n1. All engineers are innovators.\n2. Some innovators are leaders.\n\nConclusions:\nI. Some engineers are leaders.\nII. Some innovators are engineers.',
    options: [
      { id: 'A', text: 'Only Conclusion I follows' },
      { id: 'B', text: 'Only Conclusion II follows' },
      { id: 'C', text: 'Both I and II follow' },
      { id: 'D', text: 'Neither I nor II follows' },
    ],
    correctOptionId: 'B',
    explanation: {
      summary: 'Analyze the Euler circles for universal affirmative and particular affirmative statements.',
      steps: [
        'From statement 1: The set "Engineers" is a subset of "Innovators". Since Engineers ⊆ Innovators, any member of Engineers is also an Innovator. Therefore, the intersection of Innovators and Engineers is non-empty. Conclusion II ("Some innovators are engineers") unconditionally holds true.',
        'From statement 2: "Innovators" intersects with "Leaders". This intersection does not necessarily overlap with the sub-circle "Engineers". Thus, Conclusion I cannot be asserted with certainty.',
        'Therefore, only conclusion II strictly follows.',
      ],
      formula: 'Universal affirmative "All A are B" guarantees conversion to "Some B are A".',
    },
  },

  // 7. Blood Relations - Easy
  {
    id: 'br-1',
    topicId: 'blood-relations',
    topicName: 'Blood Relations and Family Trees',
    category: 'Logical Reasoning',
    difficulty: 'Easy',
    question: 'Pointing to a photograph, Rohan said, "She is the only daughter of my paternal grandfather\'s only son." How is the person in the photograph related to Rohan?',
    options: [
      { id: 'A', text: 'Mother' },
      { id: 'B', text: 'Aunt' },
      { id: 'C', text: 'Sister' },
      { id: 'D', text: 'Daughter' },
    ],
    correctOptionId: 'C',
    explanation: {
      summary: 'Deconstruct the relation statement step-by-step from the reference person outwards.',
      steps: [
        "Rohan's paternal grandfather's only son is Rohan's father.",
        "The person in the photograph is the 'only daughter of Rohan's father'.",
        "The daughter of Rohan's father is Rohan's sister.",
      ],
      formula: 'Paternal grandfather’s only son = Father; Daughter of Father = Sister.',
    },
  },

  // 8. Sentence Correction - Medium
  {
    id: 'sc-1',
    topicId: 'sentence-correction',
    topicName: 'Sentence Correction & Grammar',
    category: 'Verbal Ability',
    difficulty: 'Medium',
    question: 'Choose the grammatically correct sentence that observes proper subject-verb agreement and modifier placement:',
    options: [
      { id: 'A', text: 'Neither the team captain nor the players was ready to concede the defeat.' },
      { id: 'B', text: 'Neither the team captain nor the players were ready to concede the defeat.' },
      { id: 'C', text: 'Neither the team captain nor the players was ready for conceding defeat.' },
      { id: 'D', text: 'Neither the team captain or the players were ready to concede defeat.' },
    ],
    correctOptionId: 'B',
    explanation: {
      summary: 'In "neither... nor" compound constructions, the verb agrees in number with the subject closest to it (proximity rule).',
      steps: [
        'The subjects are "the team captain" (singular) and "the players" (plural).',
        'The subject closest to the auxiliary verb is "the players" (plural).',
        'Therefore, the verb must be the plural "were", not "was".',
        'Option B correctly uses the correlative conjunction "neither... nor" and the plural verb "were".',
      ],
      formula: 'Subject-Verb Proximity Rule: Neither [A] nor [B] + verb agreeing with [B]',
    },
  },
];
