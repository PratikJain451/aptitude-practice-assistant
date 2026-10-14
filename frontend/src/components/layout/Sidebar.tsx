import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  BookOpenCheck,
  Timer,
  MessageSquareQuote,
  FileText,
  TrendingUp,
  GraduationCap,
  X,
} from 'lucide-react';

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
  backendOnline: boolean | null;
}

export const Sidebar: React.FC<SidebarProps> = ({
  isOpen,
  onClose,
  backendOnline,
}) => {
  const navigationItems = [
    {
      to: '/',
      name: 'Overview',
      icon: LayoutDashboard,
      description: 'Dashboard & Quick Start',
    },
    {
      to: '/practice',
      name: 'Practice',
      icon: BookOpenCheck,
      description: 'Topic & Difficulty Drills',
    },
    {
      to: '/mock-tests',
      name: 'Mock Tests',
      icon: Timer,
      description: 'Timed Placement Simulations',
    },
    {
      to: '/doubt-solver',
      name: 'AI Doubt Solver',
      icon: MessageSquareQuote,
      description: 'Concept Clarification',
      badge: 'Assisted',
    },
    {
      to: '/pdf-study',
      name: 'PDF Study',
      icon: FileText,
      description: 'Material Extraction',
    },
    {
      to: '/performance',
      name: 'Performance',
      icon: TrendingUp,
      description: 'Accuracy & Real Metrics',
    },
  ];

  return (
    <>
      {/* Mobile backdrop */}
      {isOpen && (
        <div
          className="fixed inset-0 z-40 bg-slate-900/40 backdrop-blur-xs lg:hidden transition-opacity"
          onClick={onClose}
        />
      )}

      {/* Sidebar container */}
      <aside
        className={`fixed top-0 bottom-0 left-0 z-50 w-64 bg-white border-r border-slate-200 flex flex-col transition-transform duration-200 ease-in-out lg:translate-x-0 ${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        {/* Brand header */}
        <div className="h-16 px-5 border-b border-slate-200 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-md bg-indigo-600 text-white flex items-center justify-center font-bold shadow-xs">
              <GraduationCap className="w-5 h-5" />
            </div>
            <div>
              <span className="text-sm font-semibold tracking-tight text-slate-900 block leading-tight">
                AptitudePrep
              </span>
              <span className="text-[11px] font-medium text-slate-400 block tracking-normal">
                Campus Placement Edition
              </span>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-md text-slate-400 hover:text-slate-600 hover:bg-slate-100 lg:hidden"
            aria-label="Close sidebar"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Navigation list */}
        <div className="flex-1 py-4 px-3 overflow-y-auto space-y-1">
          <div className="px-3 pb-2 text-[11px] font-semibold tracking-wider text-slate-400 uppercase">
            Main Modules
          </div>
          {navigationItems.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink
                key={item.to}
                to={item.to}
                onClick={onClose}
                className={({ isActive }) =>
                  `flex items-center justify-between px-3 py-2.5 rounded-md text-xs sm:text-sm font-medium transition-colors ${
                    isActive
                      ? 'bg-indigo-50 text-indigo-700 font-semibold'
                      : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
                  }`
                }
              >
                <div className="flex items-center gap-3">
                  <Icon className="w-4 h-4 shrink-0" />
                  <span>{item.name}</span>
                </div>
                {item.badge && (
                  <span className="text-[10px] font-semibold px-1.5 py-0.5 rounded bg-indigo-100/70 text-indigo-700">
                    {item.badge}
                  </span>
                )}
              </NavLink>
            );
          })}
        </div>

        {/* System & status footer */}
        <div className="p-3 border-t border-slate-200 bg-slate-50/60">
          <div className="p-3 rounded-md border border-slate-200/80 bg-white">
            <div className="flex items-center justify-between mb-1.5">
              <span className="text-[11px] font-semibold text-slate-700">System API</span>
              <div className="flex items-center gap-1.5">
                <span
                  className={`w-2 h-2 rounded-full ${
                    backendOnline === true
                      ? 'bg-emerald-500'
                      : backendOnline === false
                      ? 'bg-rose-500'
                      : 'bg-amber-400'
                  }`}
                />
                <span className="text-[10px] font-medium text-slate-500">
                  {backendOnline === true
                    ? 'Connected (8000)'
                    : backendOnline === false
                    ? 'API Offline'
                    : 'Checking...'}
                </span>
              </div>
            </div>
            <p className="text-[11px] text-slate-400 leading-normal">
              Placement Aptitude Engine v0.1.0
            </p>
          </div>
        </div>
      </aside>
    </>
  );
};
