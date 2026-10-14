import { useState, useEffect } from 'react';
import {
  Timer,
  Clock,
  Play,
  RotateCcw,
  AlertTriangle,
  Award,
  ChevronRight,
  ChevronLeft,
  Flag,
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { TOPICS } from '../data/topics';
import { SAMPLE_QUESTIONS } from '../data/sampleQuestions';
import type { Difficulty, Question } from '../types';

export const MockTestsPage: React.FC = () => {
  // Setup configuration state
  const [selectedTopic, setSelectedTopic] = useState<string>('all');
  const [selectedDifficulty, setSelectedDifficulty] = useState<Difficulty | 'Mixed'>('Mixed');
  const [selectedQuestionCount, setSelectedQuestionCount] = useState<number>(5);
  const [selectedDuration, setSelectedDuration] = useState<number>(10); // minutes

  // Active Test State
  const [isTestActive, setIsTestActive] = useState<boolean>(false);
  const [testQuestions, setTestQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [userAnswers, setUserAnswers] = useState<Record<string, string>>({});
  const [flaggedQuestions, setFlaggedQuestions] = useState<Record<string, boolean>>({});
  const [secondsRemaining, setSecondsRemaining] = useState<number>(0);
  const [testSubmitted, setTestSubmitted] = useState<boolean>(false);
  const [showConfirmSubmit, setShowConfirmSubmit] = useState<boolean>(false);

  // Timer effect during active test
  useEffect(() => {
    if (!isTestActive || testSubmitted) return;

    if (secondsRemaining <= 0) {
      // Auto submit when time runs out
      handleSubmitTest();
      return;
    }

    const interval = setInterval(() => {
      setSecondsRemaining((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [isTestActive, testSubmitted, secondsRemaining]);

  const handleStartTest = () => {
    let pool = [...SAMPLE_QUESTIONS];
    if (selectedTopic !== 'all') {
      pool = pool.filter((q) => q.topicId === selectedTopic || q.topicName === selectedTopic);
    }
    if (selectedDifficulty !== 'Mixed') {
      pool = pool.filter((q) => q.difficulty === selectedDifficulty);
    }

    // Pick questions up to selected count
    const questions = pool.slice(0, selectedQuestionCount);
    setTestQuestions(questions);
    setCurrentIndex(0);
    setUserAnswers({});
    setFlaggedQuestions({});
    setSecondsRemaining(selectedDuration * 60);
    setTestSubmitted(false);
    setShowConfirmSubmit(false);
    setIsTestActive(true);
  };

  const handleSelectAnswer = (optionId: string) => {
    if (testSubmitted) return;
    const currentQ = testQuestions[currentIndex];
    if (!currentQ) return;
    setUserAnswers((prev) => ({
      ...prev,
      [currentQ.id]: optionId,
    }));
  };

  const toggleFlag = () => {
    const currentQ = testQuestions[currentIndex];
    if (!currentQ) return;
    setFlaggedQuestions((prev) => ({
      ...prev,
      [currentQ.id]: !prev[currentQ.id],
    }));
  };

  const handleSubmitTest = () => {
    setShowConfirmSubmit(false);
    setTestSubmitted(true);
  };

  const handleResetToSetup = () => {
    setIsTestActive(false);
    setTestSubmitted(false);
    setTestQuestions([]);
    setUserAnswers({});
  };

  const formatTimer = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Score calculations
  const calculateScore = () => {
    let correct = 0;
    testQuestions.forEach((q) => {
      if (userAnswers[q.id] === q.correctOptionId) {
        correct++;
      }
    });
    return {
      total: testQuestions.length,
      correct,
      attempted: Object.keys(userAnswers).length,
      scorePercentage: testQuestions.length > 0 ? Math.round((correct / testQuestions.length) * 100) : 0,
    };
  };

  return (
    <div className="space-y-6">
      {!isTestActive ? (
        /* Test Configuration Setup Page */
        <div className="space-y-6 max-w-4xl mx-auto">
          <div className="bg-white border border-slate-200 rounded-lg p-6 sm:p-8 shadow-xs">
            <div className="flex items-center gap-2 text-indigo-600 mb-2">
              <Timer className="w-5 h-5" />
              <span className="text-xs font-semibold uppercase tracking-wider">
                Exam Mode Configuration
              </span>
            </div>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">
              Placement Mock Aptitude Test
            </h2>
            <p className="mt-1 text-xs sm:text-sm text-slate-500 leading-relaxed">
              Simulate actual placement exam conditions with time-bound constraints. Question navigation, review flags, and detailed score breakdown are enabled.
            </p>

            {/* Test Configuration Form */}
            <div className="mt-6 pt-6 border-t border-slate-100 grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                  Assessment Topic
                </label>
                <select
                  value={selectedTopic}
                  onChange={(e) => setSelectedTopic(e.target.value)}
                  className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md p-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                >
                  <option value="all">Full Placement Assessment (Comprehensive Mix)</option>
                  {TOPICS.map((t) => (
                    <option key={t.id} value={t.id}>
                      {t.name} ({t.category})
                    </option>
                  ))}
                </select>
                <span className="text-[11px] text-slate-400 mt-1 block">
                  Select a targeted module or comprehensive placement exam mix.
                </span>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                  Difficulty Tier
                </label>
                <select
                  value={selectedDifficulty}
                  onChange={(e) => setSelectedDifficulty(e.target.value as Difficulty | 'Mixed')}
                  className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md p-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                >
                  <option value="Mixed">Mixed (Standard Campus Ratio: 40% E, 40% M, 20% H)</option>
                  <option value="Easy">Standard Level (Foundational Screening)</option>
                  <option value="Medium">Moderate Level (Company Round 1 Standard)</option>
                  <option value="Hard">Advanced Level (Product Companies & Speed Round)</option>
                </select>
                <span className="text-[11px] text-slate-400 mt-1 block">
                  Calibrated to standard company placement cutoff patterns.
                </span>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                  Question Count
                </label>
                <select
                  value={selectedQuestionCount}
                  onChange={(e) => setSelectedQuestionCount(Number(e.target.value))}
                  className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md p-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                >
                  <option value={3}>3 Questions (Micro Diagnostic)</option>
                  <option value={5}>5 Questions (Standard Section)</option>
                  <option value={8}>8 Questions (Full Section Simulation)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                  Duration (Minutes)
                </label>
                <select
                  value={selectedDuration}
                  onChange={(e) => setSelectedDuration(Number(e.target.value))}
                  className="w-full text-xs sm:text-sm bg-white border border-slate-300 rounded-md p-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                >
                  <option value={5}>5 Minutes (Speed Drill: 1 min/question)</option>
                  <option value={10}>10 Minutes (Standard: 2 min/question)</option>
                  <option value={15}>15 Minutes (Comprehensive)</option>
                </select>
              </div>
            </div>

            {/* Test Guidelines & Action */}
            <div className="mt-6 pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="text-xs text-slate-500 space-y-1">
                <div className="flex items-center gap-1.5 text-slate-700 font-medium">
                  <Clock className="w-3.5 h-3.5 text-slate-500" />
                  <span>Exam conditions: Timer will auto-submit upon expiry.</span>
                </div>
                <p>Ensure an uninterrupted environment before beginning the test.</p>
              </div>

              <Button
                variant="primary"
                size="lg"
                icon={<Play className="w-4 h-4 fill-white" />}
                onClick={handleStartTest}
                className="w-full sm:w-auto"
              >
                Start Mock Test
              </Button>
            </div>
          </div>
        </div>
      ) : testSubmitted ? (
        /* Test Results & Performance Review */
        <Card className="p-6 sm:p-8 max-w-2xl mx-auto border-indigo-100 shadow-sm text-center">
          <div className="w-12 h-12 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-600 flex items-center justify-center mx-auto mb-3">
            <Award className="w-6 h-6" />
          </div>
          <h3 className="text-xl font-bold text-slate-900 mb-1">Mock Examination Finished</h3>
          <p className="text-xs sm:text-sm text-slate-500 mb-6">
            Detailed scorecard for your placement evaluation session.
          </p>

          {(() => {
            const result = calculateScore();
            return (
              <div className="space-y-6">
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 border border-slate-200 rounded-lg p-4 text-left">
                  <div>
                    <span className="text-[11px] text-slate-400 font-medium uppercase">Questions</span>
                    <div className="text-lg font-bold text-slate-900">{result.total}</div>
                  </div>
                  <div>
                    <span className="text-[11px] text-slate-400 font-medium uppercase">Attempted</span>
                    <div className="text-lg font-bold text-slate-900">{result.attempted}</div>
                  </div>
                  <div>
                    <span className="text-[11px] text-slate-400 font-medium uppercase">Correct</span>
                    <div className="text-lg font-bold text-emerald-600">{result.correct}</div>
                  </div>
                  <div>
                    <span className="text-[11px] text-slate-400 font-medium uppercase">Score</span>
                    <div className="text-lg font-bold text-indigo-600">{result.scorePercentage}%</div>
                  </div>
                </div>

                {/* Question by question summary */}
                <div className="text-left space-y-2">
                  <h4 className="text-xs font-semibold uppercase text-slate-500 tracking-wider">
                    Question-by-Question Audit
                  </h4>
                  <div className="border border-slate-200 rounded-md divide-y divide-slate-100 text-xs">
                    {testQuestions.map((q, idx) => {
                      const userAns = userAnswers[q.id];
                      const isCorrect = userAns === q.correctOptionId;
                      return (
                        <div key={q.id} className="p-3 flex items-center justify-between gap-3">
                          <div className="flex items-center gap-2 min-w-0">
                            <span className="font-semibold text-slate-600">Q{idx + 1}</span>
                            <span className="text-slate-800 truncate">{q.topicName}</span>
                          </div>
                          <div className="flex items-center gap-2 shrink-0">
                            {userAns ? (
                              isCorrect ? (
                                <Badge variant="success" size="sm">
                                  Correct ({userAns})
                                </Badge>
                              ) : (
                                <Badge variant="error" size="sm">
                                  Your: {userAns} | Right: {q.correctOptionId}
                                </Badge>
                              )
                            ) : (
                              <Badge variant="neutral" size="sm">
                                Unanswered
                              </Badge>
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>

                <div className="flex justify-center gap-3 pt-2">
                  <Button
                    variant="primary"
                    icon={<RotateCcw className="w-4 h-4" />}
                    onClick={handleResetToSetup}
                  >
                    Setup New Mock Test
                  </Button>
                </div>
              </div>
            );
          })()}
        </Card>
      ) : (
        /* Active Test Simulation Runner */
        <div className="space-y-4 max-w-4xl mx-auto">
          {/* Header Bar with Countdown Timer */}
          <div className="bg-white border border-slate-200 rounded-lg p-4 px-5 flex items-center justify-between shadow-xs">
            <div className="flex items-center gap-3">
              <Badge variant="primary" size="md">
                Live Mock Test
              </Badge>
              <span className="text-xs font-medium text-slate-600 hidden sm:inline">
                {selectedTopic === 'all' ? 'Comprehensive Assessment' : 'Sectional Assessment'}
              </span>
            </div>

            {/* Timer Display */}
            <div className="flex items-center gap-2 bg-slate-900 text-white px-3.5 py-1.5 rounded-md font-mono text-sm font-semibold tracking-wider shadow-xs">
              <Clock className="w-4 h-4 text-amber-400 animate-pulse" />
              <span>{formatTimer(secondsRemaining)}</span>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-4 gap-4">
            {/* Question Panel */}
            <div className="lg:col-span-3 space-y-4">
              {testQuestions[currentIndex] && (
                <Card className="p-5 sm:p-6">
                  <div className="flex items-center justify-between pb-3 border-b border-slate-100 mb-4">
                    <span className="text-xs font-semibold text-slate-500">
                      Question {currentIndex + 1} of {testQuestions.length}
                    </span>
                    <button
                      onClick={toggleFlag}
                      className={`inline-flex items-center gap-1.5 text-xs font-medium px-2 py-1 rounded border transition-colors ${
                        flaggedQuestions[testQuestions[currentIndex].id]
                          ? 'border-amber-300 bg-amber-50 text-amber-800 font-semibold'
                          : 'border-slate-200 text-slate-500 hover:text-slate-800'
                      }`}
                    >
                      <Flag className="w-3.5 h-3.5" />
                      <span>{flaggedQuestions[testQuestions[currentIndex].id] ? 'Flagged for Review' : 'Flag Question'}</span>
                    </button>
                  </div>

                  <p className="text-sm sm:text-base font-medium text-slate-900 leading-relaxed whitespace-pre-line mb-6">
                    {testQuestions[currentIndex].question}
                  </p>

                  <div className="space-y-2.5">
                    {testQuestions[currentIndex].options.map((opt) => {
                      const isSelected = userAnswers[testQuestions[currentIndex].id] === opt.id;
                      return (
                        <button
                          key={opt.id}
                          type="button"
                          onClick={() => handleSelectAnswer(opt.id)}
                          className={`w-full text-left p-3.5 rounded-md border flex items-start gap-3 transition-colors cursor-pointer ${
                            isSelected
                              ? 'border-indigo-600 bg-indigo-50/50 text-indigo-900 ring-1 ring-indigo-600 font-medium'
                              : 'border-slate-200 bg-white hover:border-slate-300 hover:bg-slate-50/60 text-slate-800'
                          }`}
                        >
                          <span
                            className={`w-6 h-6 rounded border flex items-center justify-center text-xs font-semibold shrink-0 mt-0.5 ${
                              isSelected
                                ? 'border-indigo-600 bg-indigo-600 text-white'
                                : 'border-slate-300 text-slate-600 bg-slate-50'
                            }`}
                          >
                            {opt.id}
                          </span>
                          <span className="text-xs sm:text-sm pt-0.5">{opt.text}</span>
                        </button>
                      );
                    })}
                  </div>

                  {/* Navigation controls */}
                  <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
                    <Button
                      variant="outline"
                      size="sm"
                      icon={<ChevronLeft className="w-4 h-4" />}
                      disabled={currentIndex === 0}
                      onClick={() => setCurrentIndex((prev) => prev - 1)}
                    >
                      Previous
                    </Button>

                    <div className="flex gap-2">
                      {currentIndex + 1 < testQuestions.length ? (
                        <Button
                          variant="primary"
                          size="sm"
                          icon={<ChevronRight className="w-4 h-4" />}
                          iconPosition="right"
                          onClick={() => setCurrentIndex((prev) => prev + 1)}
                        >
                          Next
                        </Button>
                      ) : (
                        <Button
                          variant="primary"
                          size="sm"
                          onClick={() => setShowConfirmSubmit(true)}
                        >
                          Finish & Submit
                        </Button>
                      )}
                    </div>
                  </div>
                </Card>
              )}
            </div>

            {/* Question Palette Sidebar */}
            <div className="space-y-3">
              <Card className="p-4">
                <h4 className="text-xs font-semibold uppercase text-slate-500 tracking-wider mb-3">
                  Question Palette
                </h4>
                <div className="grid grid-cols-5 gap-2">
                  {testQuestions.map((q, idx) => {
                    const answered = Boolean(userAnswers[q.id]);
                    const flagged = Boolean(flaggedQuestions[q.id]);
                    const isCurrent = idx === currentIndex;

                    let btnClass = 'border-slate-200 bg-slate-50 text-slate-600';
                    if (answered) {
                      btnClass = 'border-emerald-600 bg-emerald-600 text-white font-semibold';
                    }
                    if (flagged) {
                      btnClass = 'border-amber-500 bg-amber-500 text-white font-semibold';
                    }
                    if (isCurrent) {
                      btnClass += ' ring-2 ring-indigo-500 ring-offset-1';
                    }

                    return (
                      <button
                        key={q.id}
                        onClick={() => setCurrentIndex(idx)}
                        className={`h-8 rounded text-xs border font-medium flex items-center justify-center transition-all ${btnClass}`}
                      >
                        {idx + 1}
                      </button>
                    );
                  })}
                </div>

                <div className="mt-4 pt-3 border-t border-slate-100 space-y-1.5 text-[11px] text-slate-500">
                  <div className="flex items-center gap-2">
                    <span className="w-3 h-3 rounded bg-emerald-600 inline-block" />
                    <span>Answered ({Object.keys(userAnswers).length})</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="w-3 h-3 rounded bg-amber-500 inline-block" />
                    <span>Flagged ({Object.keys(flaggedQuestions).filter((k) => flaggedQuestions[k]).length})</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <span className="w-3 h-3 rounded bg-slate-100 border border-slate-200 inline-block" />
                    <span>Unanswered ({testQuestions.length - Object.keys(userAnswers).length})</span>
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-slate-100">
                  <Button
                    variant="secondary"
                    size="sm"
                    className="w-full"
                    onClick={() => setShowConfirmSubmit(true)}
                  >
                    Submit Test
                  </Button>
                </div>
              </Card>
            </div>
          </div>

          {/* Submit Confirmation Modal */}
          {showConfirmSubmit && (
            <div className="fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-xs flex items-center justify-center p-4">
              <div className="bg-white rounded-lg border border-slate-200 p-6 max-w-md w-full shadow-lg">
                <div className="flex items-center gap-2 text-amber-600 mb-2">
                  <AlertTriangle className="w-5 h-5" />
                  <h3 className="text-base font-bold text-slate-900">Confirm Submission</h3>
                </div>
                <p className="text-xs sm:text-sm text-slate-600 mb-4 leading-relaxed">
                  You have answered <strong>{Object.keys(userAnswers).length}</strong> out of{' '}
                  <strong>{testQuestions.length}</strong> questions. Are you sure you wish to conclude this session?
                </p>
                <div className="flex justify-end gap-2">
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => setShowConfirmSubmit(false)}
                  >
                    Cancel & Resume
                  </Button>
                  <Button
                    variant="primary"
                    size="sm"
                    onClick={handleSubmitTest}
                  >
                    Yes, Submit Now
                  </Button>
                </div>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
