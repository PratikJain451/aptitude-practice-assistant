import { useState, useEffect, useRef } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import {
  CheckCircle2,
  XCircle,
  HelpCircle,
  ArrowRight,
  RotateCcw,
  Filter,
  Award,
  Loader2,
  AlertCircle,
  Server,
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { TOPICS } from '../data/topics';
import { apiService } from '../services/api';
import { storageService } from '../services/storage';
import type { Difficulty, ApiQuestion, SubmitAnswerResult } from '../types';

export const PracticePage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const navigate = useNavigate();

  // Filter states
  const initialTopic = searchParams.get('topic') || 'all';
  const [selectedTopic, setSelectedTopic] = useState<string>(initialTopic);
  const [selectedDifficulty, setSelectedDifficulty] = useState<Difficulty | 'all'>('all');
  const [questionCountLimit, setQuestionCountLimit] = useState<number>(5);

  // Active session states
  const [activeQuestions, setActiveQuestions] = useState<ApiQuestion[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);
  const [submissionResult, setSubmissionResult] = useState<SubmitAnswerResult | null>(null);
  const [sessionCompleted, setSessionCompleted] = useState<boolean>(false);
  const [sessionScore, setSessionScore] = useState<number>(0);

  // Network & loading states
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isBackendConnected, setIsBackendConnected] = useState<boolean>(true);
  const [topicCounts, setTopicCounts] = useState<Record<string, number>>({});

  // Fetch real topic question counts from backend
  useEffect(() => {
    const fetchCounts = async () => {
      const res = await apiService.getTopics();
      if (res.ok && res.data) {
        const map: Record<string, number> = {};
        res.data.forEach((item) => {
          map[item.topic] = item.question_count;
        });
        setTopicCounts(map);
      }
    };
    fetchCounts();
  }, []);

  // Timer for time spent tracking
  const startTimeRef = useRef<number>(Date.now());

  // Function to load questions from backend
  const loadQuestions = async () => {
    setIsLoading(true);
    setErrorMessage(null);
    setCurrentIndex(0);
    setSelectedOption(null);
    setIsSubmitted(false);
    setSubmissionResult(null);
    setSessionCompleted(false);
    setSessionScore(0);

    const res = await apiService.getQuestions({
      topic: selectedTopic !== 'all' ? selectedTopic : undefined,
      difficulty: selectedDifficulty !== 'all' ? selectedDifficulty : undefined,
      limit: questionCountLimit,
    });

    setIsLoading(false);

    if (res.ok && res.data) {
      setActiveQuestions(res.data);
      setIsBackendConnected(true);
      startTimeRef.current = Date.now();
    } else {
      setIsBackendConnected(false);
      setErrorMessage(
        res.error || 'Failed to fetch questions from backend. Please verify your parameter selection or backend connection.'
      );
      setActiveQuestions([]);
    }
  };

  useEffect(() => {
    loadQuestions();
  }, [selectedTopic, selectedDifficulty, questionCountLimit]);

  const currentQuestion: ApiQuestion | undefined = activeQuestions[currentIndex];

  const handleOptionSelect = (optionId: string) => {
    if (!isSubmitted && !isSubmitting) {
      setSelectedOption(optionId);
    }
  };

  const handleSubmitAnswer = async () => {
    if (!selectedOption || !currentQuestion || isSubmitted || isSubmitting) return;

    setIsSubmitting(true);
    const timeSpent = Math.max(1, Math.round((Date.now() - startTimeRef.current) / 1000));

    // 1. Submit answer to backend evaluation endpoint
    const evalRes = await apiService.submitAnswer(currentQuestion.id, selectedOption);

    setIsSubmitting(false);

    if (!evalRes.ok || !evalRes.data) {
      setErrorMessage(evalRes.error || 'Failed to evaluate answer. Please check backend connection.');
      return;
    }

    const result = evalRes.data;
    setSubmissionResult(result);
    setIsSubmitted(true);

    if (result.is_correct) {
      setSessionScore((prev) => prev + 1);
    }

    // 2. Persist attempt to SQLite backend
    await apiService.createAttempt({
      question_id: currentQuestion.id,
      topic: currentQuestion.topic,
      difficulty: currentQuestion.difficulty,
      selected_answer: selectedOption,
      is_correct: result.is_correct,
      time_spent_seconds: timeSpent,
    });

    // Also mirror to storageService for client resilience
    storageService.saveAttempt({
      id: `${currentQuestion.id}-${Date.now()}`,
      questionId: currentQuestion.id,
      topicId: currentQuestion.topic,
      topicName: currentQuestion.topic,
      difficulty: currentQuestion.difficulty,
      questionText: currentQuestion.question,
      selectedOptionId: selectedOption,
      correctOptionId: result.correct_answer,
      isCorrect: result.is_correct,
      timeSpentSeconds: timeSpent,
      timestamp: new Date().toISOString(),
    });
  };

  const handleNextQuestion = () => {
    if (currentIndex + 1 < activeQuestions.length) {
      setCurrentIndex((prev) => prev + 1);
      setSelectedOption(null);
      setIsSubmitted(false);
      setSubmissionResult(null);
      startTimeRef.current = Date.now();
    } else {
      setSessionCompleted(true);
    }
  };

  const handleRestartSession = () => {
    loadQuestions();
  };

  return (
    <div className="space-y-6">
      {/* Backend Engine Status Banner */}
      <div className="bg-slate-100/90 border border-slate-200 rounded-md p-3 px-4 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs text-slate-700">
        <div className="flex items-center gap-2">
          <Server className="w-4 h-4 text-indigo-600 shrink-0" />
          <span>
            <strong>Practice Engine (API Active):</strong> Questions and answer evaluations are verified securely by the FastAPI backend and recorded in SQLite.
          </span>
        </div>
        <div className="flex items-center gap-2 self-end sm:self-auto">
          <span
            className={`w-2 h-2 rounded-full ${isBackendConnected ? 'bg-emerald-500' : 'bg-amber-500'}`}
          />
          <span className="font-mono text-[11px] text-slate-500">
            {activeQuestions.length > 0 ? `${activeQuestions.length} Loaded` : 'Ready'}
          </span>
        </div>
      </div>

      {/* Filter / Configuration Controls */}
      <Card className="p-4 sm:p-5">
        <div className="flex items-center gap-2 mb-3 text-xs font-semibold text-slate-500 uppercase tracking-wider">
          <Filter className="w-3.5 h-3.5" />
          <span>Practice Session Parameters</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-4">
          {/* Topic Select */}
          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1">
              Topic Filter
            </label>
            <select
              value={selectedTopic}
              onChange={(e) => {
                setSelectedTopic(e.target.value);
                setSearchParams(e.target.value !== 'all' ? { topic: e.target.value } : {});
              }}
              className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            >
              <option value="all">All Topics (Full Mix)</option>
              {TOPICS.map((t) => {
                const count = topicCounts[t.name] ?? t.questionCount;
                return (
                  <option key={t.id} value={t.name}>
                    {t.name} ({count} Qs)
                  </option>
                );
              })}
            </select>
          </div>

          {/* Difficulty Select */}
          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1">
              Difficulty Level
            </label>
            <select
              value={selectedDifficulty}
              onChange={(e) => setSelectedDifficulty(e.target.value as Difficulty | 'all')}
              className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            >
              <option value="all">All Difficulties</option>
              <option value="Easy">Easy (Foundational)</option>
              <option value="Medium">Medium (Placement Level)</option>
              <option value="Hard">Hard (Speed / Advanced)</option>
            </select>
          </div>

          {/* Question Count Select */}
          <div>
            <label className="block text-xs font-medium text-slate-700 mb-1">
              Number of Questions
            </label>
            <select
              value={questionCountLimit}
              onChange={(e) => setQuestionCountLimit(Number(e.target.value))}
              className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            >
              <option value={3}>3 Questions (Rapid Drill)</option>
              <option value={5}>5 Questions (Standard)</option>
              <option value={10}>10 Questions (Comprehensive)</option>
            </select>
            {selectedTopic !== 'all' && (
              <span className="text-[11px] text-slate-500 mt-1 block">
                {topicCounts[selectedTopic] ?? 18} questions in bank for this topic.
              </span>
            )}
          </div>
        </div>
      </Card>

      {/* Error alert banner */}
      {errorMessage && (
        <div className="p-4 bg-rose-50 border border-rose-200 rounded-lg flex items-start gap-3 text-xs sm:text-sm text-rose-800">
          <AlertCircle className="w-5 h-5 text-rose-600 shrink-0 mt-0.5" />
          <div className="flex-1">
            <span className="font-semibold block mb-0.5">Notice</span>
            <p className="leading-relaxed">{errorMessage}</p>
          </div>
          <div className="flex items-center gap-2">
            {errorMessage.includes('available') && (() => {
              const match = errorMessage.match(/only (\d+) available/i);
              if (match) {
                const count = parseInt(match[1], 10);
                return (
                  <Button
                    size="sm"
                    variant="primary"
                    onClick={() => {
                      setQuestionCountLimit(count);
                    }}
                  >
                    Load {count} Available
                  </Button>
                );
              }
              return null;
            })()}
            <Button
              size="sm"
              variant="outline"
              onClick={() => {
                setSelectedTopic('all');
                setSelectedDifficulty('all');
                setQuestionCountLimit(5);
              }}
            >
              Reset Filters
            </Button>
          </div>
        </div>
      )}

      {/* Loading indicator */}
      {isLoading ? (
        <Card className="text-center py-16">
          <Loader2 className="w-8 h-8 text-indigo-600 animate-spin mx-auto mb-3" />
          <h3 className="text-sm font-semibold text-slate-900 mb-1">
            Fetching practice questions from backend...
          </h3>
          <p className="text-xs text-slate-500">Preparing sanitized aptitude items.</p>
        </Card>
      ) : activeQuestions.length === 0 && !errorMessage ? (
        <Card className="text-center py-12">
          <HelpCircle className="w-8 h-8 text-slate-400 mx-auto mb-2" />
          <h3 className="text-sm font-semibold text-slate-900 mb-1">
            No questions available for the selected parameters
          </h3>
          <p className="text-xs text-slate-500 mb-4 max-w-sm mx-auto">
            Try adjusting topic, difficulty, or question count to begin your practice drill.
          </p>
          <Button
            size="sm"
            variant="outline"
            onClick={() => {
              setSelectedTopic('all');
              setSelectedDifficulty('all');
              setQuestionCountLimit(5);
            }}
          >
            Reset Filters
          </Button>
        </Card>
      ) : sessionCompleted ? (
        /* Session Completed Review */
        <Card className="p-6 sm:p-8 text-center max-w-xl mx-auto border-indigo-100 shadow-sm">
          <div className="w-12 h-12 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-600 flex items-center justify-center mx-auto mb-3">
            <Award className="w-6 h-6" />
          </div>
          <h3 className="text-xl font-bold text-slate-900 mb-1">Practice Session Complete</h3>
          <p className="text-xs sm:text-sm text-slate-500 mb-6">
            All attempts have been evaluated and recorded in the SQLite database.
          </p>

          <div className="bg-slate-50 border border-slate-200 rounded-lg p-4 grid grid-cols-3 gap-2 mb-6">
            <div>
              <div className="text-xs text-slate-500">Attempted</div>
              <div className="text-lg font-bold text-slate-900">{activeQuestions.length}</div>
            </div>
            <div>
              <div className="text-xs text-slate-500">Correct</div>
              <div className="text-lg font-bold text-emerald-600">{sessionScore}</div>
            </div>
            <div>
              <div className="text-xs text-slate-500">Accuracy</div>
              <div className="text-lg font-bold text-indigo-600">
                {activeQuestions.length > 0
                  ? Math.round((sessionScore / activeQuestions.length) * 100)
                  : 0}
                %
              </div>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row gap-2 justify-center">
            <Button
              variant="primary"
              icon={<RotateCcw className="w-4 h-4" />}
              onClick={handleRestartSession}
            >
              Practice Again
            </Button>
            <Button
              variant="outline"
              onClick={() => navigate('/performance')}
            >
              View Performance Analytics
            </Button>
          </div>
        </Card>
      ) : currentQuestion ? (
        /* Active Question Display */
        <div className="space-y-4">
          <Card className="p-5 sm:p-6">
            {/* Header / Meta Bar */}
            <div className="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-100">
              <div className="flex items-center gap-2">
                <span className="text-xs font-semibold text-slate-500">
                  Question {currentIndex + 1} of {activeQuestions.length}
                </span>
                <span className="text-slate-300">•</span>
                <span className="text-xs font-medium text-slate-700">
                  {currentQuestion.topic}
                </span>
              </div>
              <Badge
                variant={
                  currentQuestion.difficulty === 'Easy'
                    ? 'success'
                    : currentQuestion.difficulty === 'Medium'
                    ? 'warning'
                    : 'error'
                }
                size="sm"
              >
                {currentQuestion.difficulty}
              </Badge>
            </div>

            {/* Question Text */}
            <div className="py-4">
              <p className="text-sm sm:text-base font-medium text-slate-900 leading-relaxed whitespace-pre-line">
                {currentQuestion.question}
              </p>
            </div>

            {/* Options List */}
            <div className="space-y-2.5 pt-2">
              {currentQuestion.options.map((option) => {
                const isSelected = selectedOption === option.id;
                const isCorrectOption = submissionResult?.correct_answer === option.id;

                let optionClass =
                  'border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50/70 text-slate-800';

                if (isSelected && !isSubmitted) {
                  optionClass =
                    'border-indigo-600 bg-indigo-50/50 text-indigo-900 ring-1 ring-indigo-600 font-medium';
                } else if (isSubmitted) {
                  if (isCorrectOption) {
                    optionClass =
                      'border-emerald-500 bg-emerald-50/60 text-emerald-950 ring-1 ring-emerald-500 font-medium';
                  } else if (isSelected && !isCorrectOption) {
                    optionClass =
                      'border-rose-400 bg-rose-50/60 text-rose-950 ring-1 ring-rose-400';
                  } else {
                    optionClass = 'border-slate-200 opacity-60 text-slate-600';
                  }
                }

                return (
                  <button
                    key={option.id}
                    type="button"
                    onClick={() => handleOptionSelect(option.id)}
                    disabled={isSubmitted || isSubmitting}
                    className={`w-full text-left p-3.5 rounded-md border flex items-start gap-3 transition-all duration-150 cursor-pointer ${optionClass}`}
                  >
                    <span
                      className={`w-6 h-6 rounded border flex items-center justify-center text-xs font-semibold shrink-0 mt-0.5 ${
                        isSelected && !isSubmitted
                          ? 'border-indigo-600 bg-indigo-600 text-white'
                          : isSubmitted && isCorrectOption
                          ? 'border-emerald-600 bg-emerald-600 text-white'
                          : isSubmitted && isSelected && !isCorrectOption
                          ? 'border-rose-600 bg-rose-600 text-white'
                          : 'border-slate-300 text-slate-600 bg-slate-50'
                      }`}
                    >
                      {option.id}
                    </span>
                    <span className="text-xs sm:text-sm pt-0.5 leading-normal">
                      {option.text}
                    </span>
                  </button>
                );
              })}
            </div>

            {/* Actions: Submit or Next */}
            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
              <span className="text-xs text-slate-400">
                {!isSubmitted
                  ? selectedOption
                    ? 'Option chosen. Click Submit to verify on backend.'
                    : 'Select an option to enable submission'
                  : 'Answer verified by backend engine'}
              </span>

              {!isSubmitted ? (
                <Button
                  variant="primary"
                  size="md"
                  disabled={!selectedOption || isSubmitting}
                  onClick={handleSubmitAnswer}
                  icon={isSubmitting ? <Loader2 className="w-4 h-4 animate-spin" /> : undefined}
                >
                  {isSubmitting ? 'Evaluating...' : 'Submit Answer'}
                </Button>
              ) : (
                <Button
                  variant="primary"
                  size="md"
                  icon={<ArrowRight className="w-4 h-4" />}
                  iconPosition="right"
                  onClick={handleNextQuestion}
                >
                  {currentIndex + 1 < activeQuestions.length ? 'Next Question' : 'Complete Session'}
                </Button>
              )}
            </div>
          </Card>

          {/* Backend Evaluated Solution & Explanation Area */}
          {isSubmitted && submissionResult && (
            <div className="bg-white border border-slate-200 rounded-lg p-5 sm:p-6 space-y-4 shadow-xs animate-in fade-in duration-200">
              <div className="flex items-center gap-2 text-sm font-semibold text-slate-900 pb-3 border-b border-slate-100">
                {submissionResult.is_correct ? (
                  <>
                    <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
                    <span className="text-emerald-800">
                      Correct Answer (Option {submissionResult.correct_answer})
                    </span>
                  </>
                ) : (
                  <>
                    <XCircle className="w-5 h-5 text-rose-600 shrink-0" />
                    <span className="text-rose-800">
                      Incorrect — Correct option is {submissionResult.correct_answer}
                    </span>
                  </>
                )}
              </div>

              <div>
                <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-500 mb-1">
                  Explanation
                </h4>
                <p className="text-xs sm:text-sm text-slate-700 leading-relaxed whitespace-pre-line">
                  {submissionResult.explanation}
                </p>
              </div>

              {submissionResult.formula && (
                <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                  <span className="text-xs font-semibold text-indigo-900 block mb-1">
                    Standard Formula / Governing Principle:
                  </span>
                  <code className="text-xs text-slate-800 font-mono">
                    {submissionResult.formula}
                  </code>
                </div>
              )}
            </div>
          )}
        </div>
      ) : null}
    </div>
  );
};
