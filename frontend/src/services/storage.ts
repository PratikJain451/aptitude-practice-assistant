import type { PracticeAttempt, TopicPerformance } from '../types';
import { TOPICS } from '../data/topics';

const ATTEMPTS_STORAGE_KEY = 'aptitude_practice_attempts_v1';

export const storageService = {
  getAttempts(): PracticeAttempt[] {
    try {
      const data = localStorage.getItem(ATTEMPTS_STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch {
      return [];
    }
  },

  saveAttempt(attempt: PracticeAttempt): void {
    try {
      const attempts = this.getAttempts();
      const updated = [attempt, ...attempts].slice(0, 100); // keep last 100
      localStorage.setItem(ATTEMPTS_STORAGE_KEY, JSON.stringify(updated));
    } catch (e) {
      console.error('Failed to save attempt to localStorage', e);
    }
  },

  clearAttempts(): void {
    try {
      localStorage.removeItem(ATTEMPTS_STORAGE_KEY);
    } catch (e) {
      console.error('Failed to clear attempts', e);
    }
  },

  getTopicPerformance(): TopicPerformance[] {
    const attempts = this.getAttempts();
    if (attempts.length === 0) return [];

    return TOPICS.map((topic) => {
      const topicAttempts = attempts.filter((a) => a.topicId === topic.id);
      const attempted = topicAttempts.length;
      const correct = topicAttempts.filter((a) => a.isCorrect).length;
      const accuracy = attempted > 0 ? Math.round((correct / attempted) * 100) : 0;
      const totalTime = topicAttempts.reduce((acc, a) => acc + (a.timeSpentSeconds || 0), 0);
      const avgTimeSeconds = attempted > 0 ? Math.round(totalTime / attempted) : 0;

      return {
        topicName: topic.name,
        category: topic.category,
        attempted,
        correct,
        accuracy,
        avgTimeSeconds,
      };
    }).filter((t) => t.attempted > 0);
  },

  getOverallSummary() {
    const attempts = this.getAttempts();
    const totalAttempted = attempts.length;
    const totalCorrect = attempts.filter((a) => a.isCorrect).length;
    const accuracy = totalAttempted > 0 ? Math.round((totalCorrect / totalAttempted) * 100) : 0;
    const uniqueTopicsPracticed = new Set(attempts.map((a) => a.topicId)).size;

    return {
      totalAttempted,
      totalCorrect,
      accuracy,
      uniqueTopicsPracticed,
      totalTopicsAvailable: TOPICS.length,
    };
  },
};
