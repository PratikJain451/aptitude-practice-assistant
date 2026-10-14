import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Menu, BookOpen, MessageSquare, RefreshCw } from 'lucide-react';
import { Button } from '../common/Button';

interface TopBarProps {
  onOpenSidebar: () => void;
  backendOnline: boolean | null;
  onRefreshHealth: () => void;
}

const pageTitles: Record<string, { title: string; subtitle: string }> = {
  '/': {
    title: 'Workspace Overview',
    subtitle: 'Placement aptitude preparation status and rapid action modules',
  },
  '/practice': {
    title: 'Practice Drills',
    subtitle: 'Targeted topic questions with immediate step-by-step solutions',
  },
  '/mock-tests': {
    title: 'Mock Placement Tests',
    subtitle: 'Standard timed aptitude examination simulation environments',
  },
  '/doubt-solver': {
    title: 'Aptitude Concept & Doubt Solver',
    subtitle: 'Structured question walkthroughs and mathematical shortcuts',
  },
  '/pdf-study': {
    title: 'PDF Study Material Assistant',
    subtitle: 'Upload and parse campus aptitude guides and formulas',
  },
  '/performance': {
    title: 'Performance & Accuracy Analytics',
    subtitle: 'Verifiable practice statistics based on your completed sessions',
  },
};

export const TopBar: React.FC<TopBarProps> = ({
  onOpenSidebar,
  backendOnline,
  onRefreshHealth,
}) => {
  const location = useLocation();
  const navigate = useNavigate();
  const currentInfo = pageTitles[location.pathname] || {
    title: 'Aptitude Practice Assistant',
    subtitle: 'College placement evaluation preparation',
  };

  return (
    <header className="sticky top-0 z-30 h-16 bg-white/95 backdrop-blur-xs border-b border-slate-200 px-4 sm:px-6 flex items-center justify-between">
      <div className="flex items-center gap-3">
        <button
          onClick={onOpenSidebar}
          className="p-1.5 -ml-1.5 rounded-md text-slate-500 hover:text-slate-900 hover:bg-slate-100 lg:hidden focus:outline-none"
          aria-label="Open navigation menu"
        >
          <Menu className="w-5 h-5" />
        </button>

        <div>
          <h1 className="text-base sm:text-lg font-semibold text-slate-900 tracking-tight leading-tight">
            {currentInfo.title}
          </h1>
          <p className="hidden sm:block text-xs text-slate-500 font-normal truncate max-w-md">
            {currentInfo.subtitle}
          </p>
        </div>
      </div>

      <div className="flex items-center gap-2 sm:gap-3">
        {/* Backend health status badge */}
        <div
          onClick={onRefreshHealth}
          title="Click to re-check FastAPI backend health (http://127.0.0.1:8000/api/health)"
          className="hidden md:flex items-center gap-2 px-2.5 py-1 rounded-md text-xs font-medium border border-slate-200 bg-slate-50 hover:bg-slate-100 transition-colors cursor-pointer text-slate-600"
        >
          <span
            className={`w-2 h-2 rounded-full shrink-0 ${
              backendOnline === true
                ? 'bg-emerald-500'
                : backendOnline === false
                ? 'bg-rose-500'
                : 'bg-amber-400'
            }`}
          />
          <span>
            {backendOnline === true
              ? 'FastAPI Online'
              : backendOnline === false
              ? 'FastAPI Offline'
              : 'Checking API...'}
          </span>
          <RefreshCw className="w-3 h-3 text-slate-400 hover:text-slate-600 ml-0.5" />
        </div>

        {/* Quick Navigation Actions */}
        {location.pathname !== '/practice' && (
          <Button
            size="sm"
            variant="outline"
            icon={<BookOpen className="w-3.5 h-3.5" />}
            onClick={() => navigate('/practice')}
            className="hidden sm:inline-flex"
          >
            Practice
          </Button>
        )}

        {location.pathname !== '/doubt-solver' && (
          <Button
            size="sm"
            variant="primary"
            icon={<MessageSquare className="w-3.5 h-3.5" />}
            onClick={() => navigate('/doubt-solver')}
          >
            Ask Doubt
          </Button>
        )}
      </div>
    </header>
  );
};
