import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  BookOpen,
  MessageSquare,
  Upload,
  ArrowRight,
  Clock,
  CheckCircle2,
  XCircle,
  Compass,
  Layers,
  ChevronRight,
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { EmptyState } from '../components/common/EmptyState';
import { TOPICS } from '../data/topics';
import { apiService } from '../services/api';
import { storageService } from '../services/storage';
import type { BackendAttempt } from '../types';

export const OverviewPage: React.FC = () => {
  const navigate = useNavigate();
  const [recentAttempts, setRecentAttempts] = useState<BackendAttempt[]>([]);
  const [stats, setStats] = useState({
    totalAttempted: 0,
    totalCorrect: 0,
    accuracy: 0,
    uniqueTopicsPracticed: 0,
    totalTopicsAvailable: TOPICS.length,
  });

  useEffect(() => {
    const fetchOverviewStats = async () => {
      const res = await apiService.getPerformanceSummary();
      if (res.ok && res.data) {
        const perf = res.data;
        setRecentAttempts(perf.recent_attempts);
        setStats({
          totalAttempted: perf.questions_attempted,
          totalCorrect: perf.correct_answers,
          accuracy: Math.round(perf.accuracy),
          uniqueTopicsPracticed: perf.topic_wise_performance.length,
          totalTopicsAvailable: TOPICS.length,
        });
      } else {
        // Fallback to local storage
        const localAttempts = storageService.getAttempts();
        const localSummary = storageService.getOverallSummary();
        setRecentAttempts(
          localAttempts.slice(0, 5).map((a, idx) => ({
            id: idx + 1,
            question_id: a.questionId,
            topic: a.topicName,
            difficulty: a.difficulty,
            selected_answer: a.selectedOptionId,
            is_correct: a.isCorrect,
            time_spent_seconds: a.timeSpentSeconds,
            created_at: a.timestamp,
          }))
        );
        setStats({
          totalAttempted: localSummary.totalAttempted,
          totalCorrect: localSummary.totalCorrect,
          accuracy: localSummary.accuracy,
          uniqueTopicsPracticed: localSummary.uniqueTopicsPracticed,
          totalTopicsAvailable: TOPICS.length,
        });
      }
    };

    fetchOverviewStats();
  }, []);

  return (
    <div className="space-y-8">
      {/* 1. Welcome & Primary Actions Banner */}
      <div className="bg-white border border-slate-200/90 rounded-lg p-6 sm:p-8 shadow-xs">
        <div className="max-w-3xl">
          <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-semibold mb-3">
            <span>Engineering & Placement Aptitude</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-bold text-slate-900 tracking-tight leading-tight">
            Welcome to Aptitude Practice Assistant
          </h2>
          <p className="mt-2 text-sm sm:text-base text-slate-600 leading-relaxed">
            Targeted preparation for college placement aptitude rounds. Master quantitative problem-solving, logical deductions, and verbal patterns with clear step-by-step methodologies.
          </p>
        </div>

        {/* 3 Prominent Quick Actions */}
        <div className="mt-6 pt-6 border-t border-slate-100 grid grid-cols-1 sm:grid-cols-3 gap-3">
          <Button
            size="lg"
            variant="primary"
            icon={<BookOpen className="w-4 h-4" />}
            onClick={() => navigate('/practice')}
            className="w-full justify-center"
          >
            Start Practising
          </Button>

          <Button
            size="lg"
            variant="outline"
            icon={<MessageSquare className="w-4 h-4" />}
            onClick={() => navigate('/doubt-solver')}
            className="w-full justify-center"
          >
            Solve a Doubt
          </Button>

          <Button
            size="lg"
            variant="outline"
            icon={<Upload className="w-4 h-4" />}
            onClick={() => navigate('/pdf-study')}
            className="w-full justify-center"
          >
            Upload Study Material
          </Button>
        </div>
      </div>

      {/* 2. Honest Progress Section (No fabricated scores) */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
              Topics Practiced
            </span>
            <Layers className="w-4 h-4 text-slate-400" />
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-2xl font-bold text-slate-900">
              {stats.uniqueTopicsPracticed}
            </span>
            <span className="text-xs text-slate-500">
              of {stats.totalTopicsAvailable} core topics
            </span>
          </div>
          <p className="mt-2 text-xs text-slate-500 leading-normal">
            {stats.uniqueTopicsPracticed === 0
              ? 'No topics completed yet. Select a topic below to begin diagnostic practice.'
              : `${stats.uniqueTopicsPracticed} topic${stats.uniqueTopicsPracticed > 1 ? 's' : ''} actively exercised.`}
          </p>
        </Card>

        <Card>
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
              Questions Answered
            </span>
            <CheckCircle2 className="w-4 h-4 text-slate-400" />
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-2xl font-bold text-slate-900">
              {stats.totalAttempted}
            </span>
            <span className="text-xs text-slate-500">total questions</span>
          </div>
          <p className="mt-2 text-xs text-slate-500 leading-normal">
            {stats.totalAttempted === 0
              ? 'Real session attempts will appear here as you practice.'
              : `${stats.totalCorrect} answered correctly (${stats.accuracy}% accuracy).`}
          </p>
        </Card>

        <Card>
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
              Diagnostic Status
            </span>
            <Compass className="w-4 h-4 text-slate-400" />
          </div>
          <div className="flex items-center gap-2">
            <span className="text-base font-semibold text-slate-800">
              {stats.totalAttempted >= 5 ? 'Active Practice' : 'Readiness Baseline'}
            </span>
          </div>
          <p className="mt-2 text-xs text-slate-500 leading-normal">
            {stats.totalAttempted === 0
              ? 'Untested. Complete at least one practice set to initialize accuracy tracking.'
              : 'Continuous logging active. Full breakdown in Performance view.'}
          </p>
        </Card>
      </div>

      {/* 3. Topic Selection Area */}
      <section className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h3 className="text-lg font-bold text-slate-900 tracking-tight">
              Aptitude Topic Syllabus
            </h3>
            <p className="text-xs sm:text-sm text-slate-500">
              Select a module to practice curated placement question sets with step-by-step explanations.
            </p>
          </div>
          <Button
            size="sm"
            variant="ghost"
            onClick={() => navigate('/practice')}
            icon={<ArrowRight className="w-3.5 h-3.5" />}
            iconPosition="right"
          >
            All Questions
          </Button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {TOPICS.map((topic) => (
            <Card
              key={topic.id}
              hoverable
              onClick={() => navigate(`/practice?topic=${encodeURIComponent(topic.name)}`)}
              className="flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between mb-2">
                  <Badge
                    variant={
                      topic.category === 'Quantitative'
                        ? 'primary'
                        : topic.category === 'Logical Reasoning'
                        ? 'warning'
                        : topic.category === 'Verbal Ability'
                        ? 'success'
                        : 'neutral'
                    }
                    size="sm"
                  >
                    {topic.category}
                  </Badge>
                  <span className="text-xs text-slate-400 font-medium">
                    {topic.questionCount} sample items
                  </span>
                </div>
                <h4 className="text-sm font-semibold text-slate-900 group-hover:text-indigo-600 transition-colors">
                  {topic.name}
                </h4>
                <p className="mt-1 text-xs text-slate-500 leading-relaxed line-clamp-2">
                  {topic.description}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-xs text-indigo-600 font-medium">
                <span>Start Practice Drill</span>
                <ChevronRight className="w-4 h-4 text-indigo-500" />
              </div>
            </Card>
          ))}
        </div>
      </section>

      {/* 4. Recent Activity Section with Honest Empty State */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h3 className="text-base font-bold text-slate-900 tracking-tight">
            Recent Practice Activity
          </h3>
          {recentAttempts.length > 0 && (
            <span className="text-xs text-slate-400">
              Showing last {Math.min(recentAttempts.length, 5)} attempts
            </span>
          )}
        </div>

        {recentAttempts.length === 0 ? (
          <EmptyState
            icon={<Clock className="w-5 h-5 text-slate-400" />}
            title="No practice sessions recorded yet"
            description="Your recent questions, answers, and time per question will appear here as soon as you complete a practice set."
            action={
              <Button
                size="sm"
                variant="primary"
                icon={<BookOpen className="w-3.5 h-3.5" />}
                onClick={() => navigate('/practice')}
              >
                Launch First Practice Session
              </Button>
            }
          />
        ) : (
          <div className="bg-white border border-slate-200/90 rounded-lg divide-y divide-slate-100 overflow-hidden shadow-xs">
            {recentAttempts.slice(0, 5).map((attempt) => (
              <div
                key={attempt.id}
                className="p-4 flex items-center justify-between gap-4 text-xs sm:text-sm hover:bg-slate-50/50 transition-colors"
              >
                <div className="flex items-start gap-3 min-w-0">
                  <div className="mt-0.5 shrink-0">
                    {attempt.is_correct ? (
                      <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                    ) : (
                      <XCircle className="w-4 h-4 text-rose-600" />
                    )}
                  </div>
                  <div className="min-w-0">
                    <div className="flex items-center gap-2">
                      <span className="font-medium text-slate-900 truncate">
                        {attempt.topic}
                      </span>
                      <Badge
                        variant={
                          attempt.difficulty === 'Easy'
                            ? 'success'
                            : attempt.difficulty === 'Medium'
                            ? 'warning'
                            : 'error'
                        }
                        size="sm"
                      >
                        {attempt.difficulty}
                      </Badge>
                    </div>
                    <p className="text-xs text-slate-500 truncate mt-0.5">
                      Selected: {attempt.selected_answer} • Q ID: {attempt.question_id}
                    </p>
                  </div>
                </div>

                <div className="shrink-0 text-right">
                  <span
                    className={`font-semibold ${
                      attempt.is_correct ? 'text-emerald-700' : 'text-rose-700'
                    }`}
                  >
                    {attempt.is_correct ? 'Correct' : 'Incorrect'}
                  </span>
                  <div className="text-[11px] text-slate-400 mt-0.5">
                    {attempt.time_spent_seconds}s elapsed
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
};
