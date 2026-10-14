export type Difficulty = 'Easy' | 'Medium' | 'Hard';

export type Category = 'Quantitative' | 'Logical Reasoning' | 'Verbal Ability' | 'Data Interpretation';

export interface Topic {
  id: string;
  name: string;
  category: Category;
  description: string;
  questionCount: number;
}

export interface QuestionOption {
  id: string;
  text: string;
}

export interface ApiQuestion {
  id: string;
  topic: string;
  difficulty: Difficulty;
  question: string;
  options: QuestionOption[];
}

export interface SubmitAnswerResult {
  question_id: string;
  is_correct: boolean;
  correct_answer: string;
  explanation: string;
  formula?: string;
}

export interface BackendAttempt {
  id: number;
  question_id: string;
  topic: string;
  difficulty: string;
  selected_answer: string;
  is_correct: boolean;
  time_spent_seconds: number;
  created_at: string;
}

export interface BackendTopicPerformance {
  topic: string;
  attempted: number;
  correct: number;
  accuracy: number;
  avg_time_seconds: number;
}

export interface PerformanceSummary {
  questions_attempted: number;
  correct_answers: number;
  accuracy: number;
  topic_wise_performance: BackendTopicPerformance[];
  recent_attempts: BackendAttempt[];
}

export interface TopicCountItem {
  topic: string;
  question_count: number;
}

// Legacy / Local fallback compatibility types
export interface Question {
  id: string;
  topicId: string;
  topicName: string;
  category: Category;
  difficulty: Difficulty;
  question: string;
  options: QuestionOption[];
  correctOptionId: string;
  explanation: {
    summary: string;
    steps: string[];
    formula?: string;
  };
}

export interface PracticeAttempt {
  id: string;
  questionId: string;
  topicId: string;
  topicName: string;
  difficulty: Difficulty;
  questionText: string;
  selectedOptionId: string;
  correctOptionId: string;
  isCorrect: boolean;
  timeSpentSeconds: number;
  timestamp: string;
}

export interface MockTestConfig {
  topic: string;
  difficulty: Difficulty | 'Mixed';
  questionCount: number;
  durationMinutes: number;
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  content: string;
  timestamp: string;
  topic?: string;
  model?: string;
  isError?: boolean;
}

export interface TopicPerformance {
  topicName: string;
  category: Category;
  attempted: number;
  correct: number;
  accuracy: number;
  avgTimeSeconds: number;
}

// PDF RAG Document Types
export interface DocumentItem {
  id: string;
  filename: string;
  original_name: string;
  file_size: number;
  page_count: number;
  chunk_count: number;
  status: 'uploaded' | 'processing' | 'ready' | 'failed';
  error_message?: string | null;
  created_at: string;
  updated_at: string;
}

export interface DocumentListResult {
  documents: DocumentItem[];
  total: number;
}

export interface SourceSnippet {
  page: number;
  chunk_index: number;
  text: string;
  relevance_score?: number;
}

export interface DocumentAskResult {
  answer: string;
  document_id: string;
  document_name: string;
  sources: SourceSnippet[];
}

export interface GeneratedQuestionItem {
  id: string;
  question: string;
  options: QuestionOption[];
  correct_option: string;
  explanation: string;
  source_pages: number[];
  is_grounded: boolean;
  verified: boolean;
}

export interface GenerateQuestionsResult {
  document_id: string;
  document_name: string;
  topic?: string;
  difficulty: string;
  questions: GeneratedQuestionItem[];
}
