import type {
  ApiQuestion,
  SubmitAnswerResult,
  BackendAttempt,
  PerformanceSummary,
  TopicCountItem,
  DocumentItem,
  DocumentListResult,
  DocumentAskResult,
  GenerateQuestionsResult,
} from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

export interface HealthResponse {
  status: string;
  service: string;
  timestamp: string;
  version: string;
}

export const apiService = {
  async checkHealth(): Promise<{ ok: boolean; data?: HealthResponse; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/health`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        return { ok: false, error: `HTTP ${response.status}: ${response.statusText}` };
      }

      const data: HealthResponse = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Backend unreachable on port 8000',
      };
    }
  },

  async getTopics(): Promise<{ ok: boolean; data?: TopicCountItem[]; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/questions/topics`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to fetch topics (HTTP ${response.status})` };
      }

      const data: TopicCountItem[] = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while fetching topics',
      };
    }
  },

  async getQuestions(params: {
    topic?: string;
    difficulty?: string;
    limit?: number;
  }): Promise<{ ok: boolean; data?: ApiQuestion[]; error?: string }> {
    try {
      const queryParams = new URLSearchParams();
      if (params.topic && params.topic !== 'all') {
        queryParams.append('topic', params.topic);
      }
      if (params.difficulty && params.difficulty !== 'all') {
        queryParams.append('difficulty', params.difficulty);
      }
      if (params.limit) {
        queryParams.append('limit', params.limit.toString());
      }

      const url = `${API_BASE_URL}/api/questions?${queryParams.toString()}`;
      const response = await fetch(url, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to fetch questions (HTTP ${response.status})` };
      }

      const data: ApiQuestion[] = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while fetching questions',
      };
    }
  },

  async submitAnswer(
    questionId: string,
    selectedAnswer: string
  ): Promise<{ ok: boolean; data?: SubmitAnswerResult; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/questions/${questionId}/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ selected_answer: selectedAnswer }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to submit answer (HTTP ${response.status})` };
      }

      const data: SubmitAnswerResult = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while evaluating answer',
      };
    }
  },

  async createAttempt(attempt: {
    question_id: string;
    topic: string;
    difficulty: string;
    selected_answer: string;
    is_correct: boolean;
    time_spent_seconds?: number;
  }): Promise<{ ok: boolean; data?: BackendAttempt; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/attempts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(attempt),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to save attempt (HTTP ${response.status})` };
      }

      const data: BackendAttempt = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while saving attempt',
      };
    }
  },

  async getAttempts(): Promise<{ ok: boolean; data?: BackendAttempt[]; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/attempts`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to fetch attempts (HTTP ${response.status})` };
      }

      const data: BackendAttempt[] = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while fetching attempts',
      };
    }
  },

  async getPerformanceSummary(): Promise<{ ok: boolean; data?: PerformanceSummary; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/performance/summary`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to fetch performance (HTTP ${response.status})` };
      }

      const data: PerformanceSummary = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while fetching performance',
      };
    }
  },

  async deleteAttempts(): Promise<{ ok: boolean; message?: string; error?: string }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/attempts`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return { ok: false, error: errorData.detail || `Failed to reset attempts (HTTP ${response.status})` };
      }

      const data = await response.json();
      return { ok: true, message: data.message };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while resetting attempts',
      };
    }
  },

  async askDoubt(params: {
    question: string;
    topic?: string;
    conversation_history?: Array<{ role: 'user' | 'assistant'; content: string }>;
  }): Promise<{
    ok: boolean;
    data?: { answer: string; topic?: string; model: string };
    error?: string;
    isConfigError?: boolean;
  }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/ai/doubt`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const isConfig = response.status === 503 || (typeof errorData.detail === 'string' && errorData.detail.includes('GROQ_API_KEY'));
        return {
          ok: false,
          error: errorData.detail || `AI service returned error (HTTP ${response.status})`,
          isConfigError: isConfig,
        };
      }

      const data = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error while contacting AI service',
      };
    }
  },

  // Document RAG API Methods
  async uploadDocument(file: File): Promise<{
    ok: boolean;
    data?: DocumentItem;
    error?: string;
  }> {
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch(`${API_BASE_URL}/api/documents/upload`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        return {
          ok: false,
          error: errData.detail || `Upload failed with status ${response.status}`,
        };
      }

      const data: DocumentItem = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error during file upload',
      };
    }
  },

  async getDocuments(): Promise<{
    ok: boolean;
    data?: DocumentListResult;
    error?: string;
  }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/documents`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        return {
          ok: false,
          error: errData.detail || `Failed to fetch documents (HTTP ${response.status})`,
        };
      }

      const data: DocumentListResult = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error fetching documents',
      };
    }
  },

  async getDocument(documentId: string): Promise<{
    ok: boolean;
    data?: DocumentItem;
    error?: string;
  }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/documents/${documentId}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        return {
          ok: false,
          error: errData.detail || `Failed to fetch document (HTTP ${response.status})`,
        };
      }

      const data: DocumentItem = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error fetching document',
      };
    }
  },

  async deleteDocument(documentId: string): Promise<{
    ok: boolean;
    message?: string;
    error?: string;
  }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/documents/${documentId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        return {
          ok: false,
          error: errData.detail || `Failed to delete document (HTTP ${response.status})`,
        };
      }

      const data = await response.json();
      return { ok: true, message: data.message };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error deleting document',
      };
    }
  },

  async askDocumentDoubt(
    documentId: string,
    question: string
  ): Promise<{
    ok: boolean;
    data?: DocumentAskResult;
    error?: string;
    isConfigError?: boolean;
  }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/documents/${documentId}/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        const isConfig = response.status === 503 || (typeof errData.detail === 'string' && errData.detail.includes('GROQ_API_KEY'));
        return {
          ok: false,
          error: errData.detail || `AI query failed (HTTP ${response.status})`,
          isConfigError: isConfig,
        };
      }

      const data: DocumentAskResult = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error querying document',
      };
    }
  },

  async generateDocumentQuestions(
    documentId: string,
    params: { topic?: string; difficulty?: string; count?: number }
  ): Promise<{
    ok: boolean;
    data?: GenerateQuestionsResult;
    error?: string;
    isConfigError?: boolean;
  }> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/documents/${documentId}/generate-questions`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(params),
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        const isConfig = response.status === 503 || (typeof errData.detail === 'string' && errData.detail.includes('GROQ_API_KEY'));
        return {
          ok: false,
          error: errData.detail || `Question generation failed (HTTP ${response.status})`,
          isConfigError: isConfig,
        };
      }

      const data: GenerateQuestionsResult = await response.json();
      return { ok: true, data };
    } catch (err) {
      return {
        ok: false,
        error: err instanceof Error ? err.message : 'Network error during question generation',
      };
    }
  },
};

