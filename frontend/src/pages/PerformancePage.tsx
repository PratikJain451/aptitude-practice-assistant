import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  TrendingUp,
  BookOpen,
  BarChart2,
  Trash2,
  RefreshCw,
  Loader2,
  CheckCircle2,
  XCircle,
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Badge } from '../components/common/Badge';
import { Card } from '../components/common/Card';
import { EmptyState } from '../components/common/EmptyState';
import { apiService } from '../services/api';
import { storageService } from '../services/storage';
import type { PerformanceSummary } from '../types';

export const PerformancePage: React.FC = () => {
  const navigate = useNavigate();
  const [summary, setSummary] = useState<PerformanceSummary | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [isDeleting, setIsDeleting] = useState<boolean>(false);
  const [errorNotice, setErrorNotice] = useState<string | null>(null);

  const fetchPerformance = async () => {
    setIsLoading(true);
    setErrorNotice(null);

    const res = await apiService.getPerformanceSummary();
    setIsLoading(false);

    if (res.ok && res.data) {
      setSummary(res.data);
    } else {
      // Fallback to local storage summary if backend is temporarily unreachable
      const localAttempts = storageService.getAttempts();
      const localTopicStats = storageService.getTopicPerformance();
      const localOverall = storageService.getOverallSummary();

      setSummary({
        questions_attempted: localOverall.totalAttempted,
        correct_answers: localOverall.totalCorrect,
        accuracy: localOverall.accuracy,
        topic_wise_performance: localTopicStats.map((t) => ({
          topic: t.topicName,
          attempted: t.attempted,
          correct: t.correct,
          accuracy: t.accuracy,
          avg_time_seconds: t.avgTimeSeconds,
        })),
        recent_attempts: localAttempts.slice(0, 10).map((a, idx) => ({
          id: idx + 1,
          question_id: a.questionId,
          topic: a.topicName,
          difficulty: a.difficulty,
          selected_answer: a.selectedOptionId,
          is_correct: a.isCorrect,
          time_spent_seconds: a.timeSpentSeconds,
          created_at: a.timestamp,
        })),
      });

      if (res.error) {
        setErrorNotice('Showing cached metrics. Connect to backend to sync live attempts.');
      }
    }
  };

  useEffect(() => {
    fetchPerformance();
  }, []);

  const handleClearAttempts = async () => {
    if (
      window.confirm(
        'Are you sure you want to reset all recorded attempt history in the database? This cannot be undone.'
      )
    ) {
      setIsDeleting(true);
      await apiService.deleteAttempts();
      storageService.clearAttempts();
      setIsDeleting(false);
      await fetchPerformance();
    }
  };

  const totalAttempted = summary?.questions_attempted ?? 0;
  const totalCorrect = summary?.correct_answers ?? 0;
  const accuracy = summary?.accuracy ?? 0;
  const topicStats = summary?.topic_wise_performance ?? [];
  const recentAttempts = summary?.recent_attempts ?? [];

  return (
    <div className="space-y-6">
      {/* Top Banner / Metrics Summary */}
      <div className="bg-white border border-slate-200 rounded-lg p-6 sm:p-8 shadow-xs">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-indigo-600 mb-1.5">
              <TrendingUp className="w-4 h-4" />
              <span className="text-xs font-semibold uppercase tracking-wider">
                Verifiable Assessment Analytics
              </span>
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
              Placement Performance Record
            </h2>
            <p className="mt-1 text-xs sm:text-sm text-slate-500 max-w-2xl">
              Real-time accuracy and time statistics computed strictly from your stored SQLite attempts. No fabricated baseline data.
            </p>
          </div>

          <div className="flex items-center gap-2 self-start sm:self-auto">
            <Button
              size="sm"
              variant="outline"
              icon={<RefreshCw className={`w-3.5 h-3.5 ${isLoading ? 'animate-spin' : ''}`} />}
              onClick={fetchPerformance}
              disabled={isLoading}
            >
              Refresh
            </Button>

            {totalAttempted > 0 && (
              <Button
                size="sm"
                variant="outline"
                icon={<Trash2 className="w-3.5 h-3.5 text-rose-500" />}
                onClick={handleClearAttempts}
                disabled={isDeleting}
              >
                {isDeleting ? 'Resetting...' : 'Reset History'}
              </Button>
            )}
          </div>
        </div>

        {errorNotice && (
          <div className="mt-4 p-2.5 rounded bg-amber-50 border border-amber-200 text-xs text-amber-800">
            {errorNotice}
          </div>
        )}

        {/* Real Summary Metrics */}
        <div className="mt-6 pt-6 border-t border-slate-100 grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div className="p-3.5 rounded-md bg-slate-50 border border-slate-200/70">
            <span className="text-xs font-medium text-slate-500 uppercase tracking-wider block mb-1">
              Questions Solved
            </span>
            <div className="text-2xl font-bold text-slate-900">{totalAttempted}</div>
            <span className="text-[11px] text-slate-400 mt-0.5 block">
              {totalAttempted === 0 ? '0 attempted' : `${totalCorrect} correct`}
            </span>
          </div>

          <div className="p-3.5 rounded-md bg-slate-50 border border-slate-200/70">
            <span className="text-xs font-medium text-slate-500 uppercase tracking-wider block mb-1">
              Overall Accuracy
            </span>
            <div className="text-2xl font-bold text-indigo-600">
              {totalAttempted > 0 ? `${accuracy}%` : '—'}
            </div>
            <span className="text-[11px] text-slate-400 mt-0.5 block">
              {totalAttempted > 0 ? 'Verified backend average' : 'Awaiting attempts'}
            </span>
          </div>

          <div className="p-3.5 rounded-md bg-slate-50 border border-slate-200/70">
            <span className="text-xs font-medium text-slate-500 uppercase tracking-wider block mb-1">
              Modules Evaluated
            </span>
            <div className="text-2xl font-bold text-slate-900">
              {topicStats.length}
            </div>
            <span className="text-[11px] text-slate-400 mt-0.5 block">
              topics with recorded attempts
            </span>
          </div>

          <div className="p-3.5 rounded-md bg-slate-50 border border-slate-200/70">
            <span className="text-xs font-medium text-slate-500 uppercase tracking-wider block mb-1">
              Placement Readiness
            </span>
            <div className="text-base font-bold text-slate-800 pt-1">
              {totalAttempted >= 15 ? 'Benchmark Active' : 'Diagnostic Phase'}
            </div>
            <span className="text-[11px] text-slate-400 mt-0.5 block">
              {totalAttempted >= 15 ? 'Sample threshold reached' : 'Requires ≥15 questions'}
            </span>
          </div>
        </div>
      </div>

      {/* Topic-Wise Breakdown Table */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h3 className="text-base font-bold text-slate-900 tracking-tight">
            Topic-Wise Competency Breakdown
          </h3>
          {topicStats.length > 0 && (
            <span className="text-xs text-slate-500">
              {topicStats.length} topics practiced
            </span>
          )}
        </div>

        {isLoading ? (
          <Card className="py-12 text-center">
            <Loader2 className="w-6 h-6 animate-spin text-indigo-600 mx-auto mb-2" />
            <p className="text-xs text-slate-500">Calculating performance metrics...</p>
          </Card>
        ) : topicStats.length === 0 ? (
          <EmptyState
            icon={<BarChart2 className="w-5 h-5 text-slate-400" />}
            title="No topic attempts recorded"
            description="Your accuracy by topic, number of attempts, and average time per question will automatically compute here after your first practice drill."
            action={
              <Button
                size="sm"
                variant="primary"
                icon={<BookOpen className="w-3.5 h-3.5" />}
                onClick={() => navigate('/practice')}
              >
                Go to Practice Drills
              </Button>
            }
          />
        ) : (
          <div className="bg-white border border-slate-200 rounded-lg overflow-hidden shadow-xs">
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs sm:text-sm">
                <thead className="bg-slate-50 text-slate-500 uppercase font-semibold text-[11px] border-b border-slate-200 tracking-wider">
                  <tr>
                    <th className="px-5 py-3">Topic</th>
                    <th className="px-5 py-3">Attempted</th>
                    <th className="px-5 py-3">Correct</th>
                    <th className="px-5 py-3">Accuracy</th>
                    <th className="px-5 py-3">Avg. Speed</th>
                    <th className="px-5 py-3 text-right">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 text-slate-700">
                  {topicStats.map((item, idx) => (
                    <tr key={idx} className="hover:bg-slate-50/50 transition-colors">
                      <td className="px-5 py-4 font-medium text-slate-900">
                        {item.topic}
                      </td>
                      <td className="px-5 py-4 text-slate-600">{item.attempted}</td>
                      <td className="px-5 py-4 text-emerald-700 font-medium">{item.correct}</td>
                      <td className="px-5 py-4">
                        <div className="flex items-center gap-2">
                          <span
                            className={`font-semibold ${
                              item.accuracy >= 70
                                ? 'text-emerald-700'
                                : item.accuracy >= 50
                                ? 'text-amber-700'
                                : 'text-rose-700'
                            }`}
                          >
                            {item.accuracy}%
                          </span>
                          <div className="w-16 bg-slate-100 rounded-full h-1.5 overflow-hidden hidden sm:block">
                            <div
                              className={`h-1.5 rounded-full ${
                                item.accuracy >= 70
                                  ? 'bg-emerald-500'
                                  : item.accuracy >= 50
                                  ? 'bg-amber-500'
                                  : 'bg-rose-500'
                              }`}
                              style={{ width: `${item.accuracy}%` }}
                            />
                          </div>
                        </div>
                      </td>
                      <td className="px-5 py-4 text-slate-500">
                        {item.avg_time_seconds > 0 ? `${item.avg_time_seconds}s / question` : '—'}
                      </td>
                      <td className="px-5 py-4 text-right">
                        <Button
                          size="sm"
                          variant="ghost"
                          onClick={() => navigate(`/practice?topic=${encodeURIComponent(item.topic)}`)}
                        >
                          Practice
                        </Button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </section>

      {/* Recent Attempts History */}
      {recentAttempts.length > 0 && (
        <section className="space-y-3 pt-2">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-slate-900 tracking-tight">
              Recent Stored Attempts
            </h3>
            <span className="text-xs text-slate-500">
              Last {recentAttempts.length} evaluations from SQLite
            </span>
          </div>

          <div className="bg-white border border-slate-200 rounded-lg divide-y divide-slate-100 overflow-hidden shadow-xs">
            {recentAttempts.map((att) => (
              <div
                key={att.id}
                className="p-3.5 sm:p-4 flex items-center justify-between gap-4 text-xs sm:text-sm hover:bg-slate-50/50 transition-colors"
              >
                <div className="flex items-center gap-3 min-w-0">
                  {att.is_correct ? (
                    <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                  ) : (
                    <XCircle className="w-4 h-4 text-rose-600 shrink-0" />
                  )}
                  <div className="min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="font-semibold text-slate-900 truncate">
                        {att.topic}
                      </span>
                      <Badge
                        variant={
                          att.difficulty === 'Easy'
                            ? 'success'
                            : att.difficulty === 'Medium'
                            ? 'warning'
                            : 'error'
                        }
                        size="sm"
                      >
                        {att.difficulty}
                      </Badge>
                    </div>
                    <div className="text-[11px] text-slate-400 mt-0.5 flex items-center gap-2">
                      <span>Selected: {att.selected_answer}</span>
                      <span>•</span>
                      <span>{att.time_spent_seconds}s elapsed</span>
                    </div>
                  </div>
                </div>

                <div className="shrink-0 text-right">
                  <span
                    className={`font-semibold text-xs ${
                      att.is_correct ? 'text-emerald-700' : 'text-rose-700'
                    }`}
                  >
                    {att.is_correct ? 'Correct' : 'Incorrect'}
                  </span>
                  <div className="text-[10px] text-slate-400 mt-0.5">
                    {new Date(att.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
};
