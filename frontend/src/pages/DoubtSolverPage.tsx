import { useState, useRef, useEffect } from 'react';
import {
  Send,
  Bot,
  User,
  Lightbulb,
  Copy,
  Check,
  RotateCcw,
  Loader2,
  AlertCircle,
  KeyRound,
  ExternalLink,
  Sparkles,
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Card } from '../components/common/Card';
import { apiService } from '../services/api';
import { TOPICS } from '../data/topics';
import type { ChatMessage } from '../types';

const SUGGESTED_QUESTIONS = [
  'How do I solve "A can do a work in 10 days and B in 15 days"?',
  'What is the formula for relative speed when two trains travel in opposite directions?',
  'How do I deduce "All cats are dogs, some dogs are mammals" in syllogisms?',
  'What is the shortcut for finding profit % with successive discounts of 20% and 10%?',
  'How do I calculate shortest distance in directional sense problems?',
];

export const DoubtSolverPage: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [selectedTopic, setSelectedTopic] = useState<string>('General Aptitude');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isCopied, setIsCopied] = useState<string | null>(null);
  const [configError, setConfigError] = useState<string | null>(null);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSendMessage = async (textToSend?: string) => {
    const text = (textToSend || inputValue).trim();
    if (!text || isLoading) return;

    setConfigError(null);

    const userMsg: ChatMessage = {
      id: `user-${Date.now()}`,
      sender: 'user',
      content: text,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    // Update conversation state immediately
    const updatedMessages = [...messages, userMsg];
    setMessages(updatedMessages);
    setInputValue('');

    // Prepare conversation history (up to last 6 messages, excluding errors)
    const history = updatedMessages
      .slice(0, -1) // exclude current user message
      .filter((m) => !m.isError)
      .slice(-6)
      .map((m) => ({
        role: m.sender === 'user' ? ('user' as const) : ('assistant' as const),
        content: m.content,
      }));

    setIsLoading(true);

    const res = await apiService.askDoubt({
      question: text,
      topic: selectedTopic !== 'General Aptitude' ? selectedTopic : undefined,
      conversation_history: history.length > 0 ? history : undefined,
    });

    setIsLoading(false);

    if (res.ok && res.data) {
      const assistantMsg: ChatMessage = {
        id: `assist-${Date.now()}`,
        sender: 'assistant',
        content: res.data.answer,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        topic: res.data.topic,
        model: res.data.model,
      };
      setMessages((prev) => [...prev, assistantMsg]);
    } else {
      if (res.isConfigError) {
        setConfigError(res.error || 'GROQ_API_KEY is not configured in backend/.env');
      }

      const errorMsg: ChatMessage = {
        id: `error-${Date.now()}`,
        sender: 'assistant',
        content:
          res.error ||
          'Failed to receive a response from the AI Doubt engine. Please verify backend connectivity.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isError: true,
      };
      setMessages((prev) => [...prev, errorMsg]);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleNewChat = () => {
    setMessages([]);
    setInputValue('');
    setConfigError(null);
  };

  const handleCopy = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setIsCopied(id);
    setTimeout(() => setIsCopied(null), 2000);
  };

  return (
    <div className="space-y-4 max-w-4xl mx-auto">
      {/* Header controls bar */}
      <div className="bg-white border border-slate-200 rounded-lg p-3 sm:p-4 px-4 sm:px-5 flex flex-wrap items-center justify-between gap-3 shadow-xs">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-md bg-indigo-50 border border-indigo-200 text-indigo-600 flex items-center justify-center font-bold">
            <Bot className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-semibold text-slate-900 leading-tight">
              AI Aptitude Doubt Solver
            </h3>
            <p className="text-[11px] text-slate-500">
              Live mathematical step-by-step reasoning via Groq LLM
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {/* Topic Context Selector */}
          <select
            value={selectedTopic}
            onChange={(e) => setSelectedTopic(e.target.value)}
            disabled={isLoading}
            className="text-xs bg-slate-50 border border-slate-200 rounded-md px-2.5 py-1.5 text-slate-700 focus:outline-none focus:ring-1 focus:ring-indigo-500"
          >
            <option value="General Aptitude">General Aptitude (Auto-Detect)</option>
            {TOPICS.map((t) => (
              <option key={t.id} value={t.name}>
                {t.name}
              </option>
            ))}
          </select>

          {messages.length > 0 && (
            <Button
              size="sm"
              variant="outline"
              icon={<RotateCcw className="w-3.5 h-3.5" />}
              onClick={handleNewChat}
              disabled={isLoading}
            >
              New Chat
            </Button>
          )}
        </div>
      </div>

      {/* Configuration Help Banner if Key is Missing */}
      {configError && (
        <div className="bg-amber-50 border border-amber-200 rounded-lg p-4 text-xs sm:text-sm text-amber-900 space-y-2">
          <div className="flex items-center gap-2 font-semibold text-amber-950">
            <KeyRound className="w-4 h-4 text-amber-700 shrink-0" />
            <span>LLM Provider Setup Required (GROQ_API_KEY)</span>
          </div>
          <p className="leading-relaxed text-amber-800">
            {configError}
          </p>
          <div className="p-3 bg-white/80 border border-amber-200/80 rounded-md space-y-1 font-mono text-xs text-slate-800">
            <div className="font-sans font-semibold text-slate-700 mb-1">Configuration Steps:</div>
            <div>1. Get a free API key: <a href="https://console.groq.com/keys" target="_blank" rel="noreferrer" className="text-indigo-600 underline font-sans inline-flex items-center gap-1">console.groq.com/keys <ExternalLink className="w-3 h-3" /></a></div>
            <div>2. Add to <code>backend/.env</code>: <code>GROQ_API_KEY=gsk_your_key_here</code></div>
            <div>3. Restart or reload the FastAPI backend.</div>
          </div>
        </div>
      )}

      {/* Main Chat Box */}
      <Card className="flex flex-col h-[580px] p-0 overflow-hidden">
        {/* Message Stream */}
        <div className="flex-1 p-4 sm:p-6 overflow-y-auto space-y-4 bg-slate-50/50">
          {messages.length === 0 ? (
            /* First-time empty state */
            <div className="h-full flex flex-col items-center justify-center text-center p-6 text-slate-500">
              <div className="w-12 h-12 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-600 flex items-center justify-center mb-3">
                <Sparkles className="w-5 h-5" />
              </div>
              <h4 className="text-sm font-semibold text-slate-900 mb-1">
                Ask Any Aptitude Concept or Question
              </h4>
              <p className="text-xs text-slate-500 max-w-md mb-6 leading-relaxed">
                Receive step-by-step calculations, governing formulas, shortcuts, and beginner-friendly derivations tailored for placement exams.
              </p>

              <div className="w-full max-w-lg space-y-2 text-left">
                <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400 block mb-1">
                  Example Placement Doubts:
                </span>
                <div className="grid grid-cols-1 gap-1.5">
                  {SUGGESTED_QUESTIONS.map((q, idx) => (
                    <button
                      key={idx}
                      onClick={() => handleSendMessage(q)}
                      className="text-left px-3.5 py-2 rounded-md bg-white hover:bg-indigo-50/50 hover:border-indigo-200 border border-slate-200 text-xs text-slate-700 transition-colors cursor-pointer"
                    >
                      {q}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          ) : (
            messages.map((msg) => (
              <div
                key={msg.id}
                className={`flex gap-3 ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                {msg.sender === 'assistant' && (
                  <div
                    className={`w-7 h-7 rounded-md flex items-center justify-center shrink-0 mt-0.5 text-xs font-semibold shadow-xs ${
                      msg.isError
                        ? 'bg-rose-600 text-white'
                        : 'bg-indigo-600 text-white'
                    }`}
                  >
                    {msg.isError ? <AlertCircle className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
                  </div>
                )}

                <div
                  className={`max-w-[88%] sm:max-w-[78%] rounded-lg p-4 text-xs sm:text-sm leading-relaxed ${
                    msg.sender === 'user'
                      ? 'bg-slate-900 text-white rounded-tr-none'
                      : msg.isError
                      ? 'bg-rose-50 border border-rose-200 text-rose-900 rounded-tl-none shadow-xs'
                      : 'bg-white border border-slate-200 text-slate-800 rounded-tl-none shadow-xs'
                  }`}
                >
                  {msg.sender === 'assistant' && !msg.isError && msg.model && (
                    <div className="flex items-center gap-2 pb-2 mb-2 border-b border-slate-100 text-[10px] text-slate-400">
                      <span className="font-semibold text-slate-600">Model: {msg.model}</span>
                      {msg.topic && (
                        <>
                          <span>•</span>
                          <span>{msg.topic}</span>
                        </>
                      )}
                    </div>
                  )}

                  <div className="whitespace-pre-line font-sans space-y-2">
                    {msg.content}
                  </div>

                  <div className="mt-2.5 pt-2 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-400">
                    <span>{msg.timestamp}</span>
                    {msg.sender === 'assistant' && !msg.isError && (
                      <button
                        onClick={() => handleCopy(msg.id, msg.content)}
                        className="inline-flex items-center gap-1 text-slate-400 hover:text-slate-600 cursor-pointer"
                        title="Copy answer"
                      >
                        {isCopied === msg.id ? (
                          <>
                            <Check className="w-3 h-3 text-emerald-600" />
                            <span className="text-emerald-600">Copied</span>
                          </>
                        ) : (
                          <>
                            <Copy className="w-3 h-3" />
                            <span>Copy</span>
                          </>
                        )}
                      </button>
                    )}
                  </div>
                </div>

                {msg.sender === 'user' && (
                  <div className="w-7 h-7 rounded-md bg-slate-200 text-slate-700 flex items-center justify-center shrink-0 mt-0.5 text-xs font-semibold">
                    <User className="w-4 h-4" />
                  </div>
                )}
              </div>
            ))
          )}

          {/* Assistant typing indicator while loading */}
          {isLoading && (
            <div className="flex gap-3 justify-start items-center">
              <div className="w-7 h-7 rounded-md bg-indigo-600 text-white flex items-center justify-center shrink-0 text-xs font-semibold shadow-xs">
                <Bot className="w-4 h-4" />
              </div>
              <div className="bg-white border border-slate-200 rounded-lg rounded-tl-none p-3.5 shadow-xs flex items-center gap-2 text-xs text-slate-500">
                <Loader2 className="w-3.5 h-3.5 animate-spin text-indigo-600" />
                <span>Generating step-by-step reasoning...</span>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>

        {/* Quick Suggestions Bar when messages exist */}
        {messages.length > 0 && (
          <div className="p-2.5 px-4 bg-white border-t border-slate-100 overflow-x-auto">
            <div className="flex items-center gap-2 text-xs">
              <span className="text-slate-400 shrink-0 font-medium flex items-center gap-1">
                <Lightbulb className="w-3.5 h-3.5 text-amber-500" />
                Quick:
              </span>
              <div className="flex gap-2">
                {SUGGESTED_QUESTIONS.slice(0, 3).map((q, idx) => (
                  <button
                    key={idx}
                    onClick={() => handleSendMessage(q)}
                    disabled={isLoading}
                    className="px-2.5 py-1 rounded bg-slate-50 hover:bg-slate-100 text-slate-600 text-xs font-normal whitespace-nowrap shrink-0 transition-colors cursor-pointer border border-slate-200/60 disabled:opacity-50"
                  >
                    {q}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* Multiline Message Input Box */}
        <div className="p-3.5 sm:p-4 bg-white border-t border-slate-200">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSendMessage();
            }}
            className="flex items-end gap-2"
          >
            <div className="flex-1 relative">
              <textarea
                ref={textareaRef}
                rows={2}
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={handleKeyDown}
                disabled={isLoading}
                placeholder="Ask an aptitude doubt... (Press Enter to send, Shift+Enter for newline)"
                className="w-full resize-none bg-slate-50 border border-slate-300 rounded-md px-3.5 py-2.5 text-xs sm:text-sm text-slate-900 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white disabled:opacity-60"
              />
            </div>
            <Button
              type="submit"
              variant="primary"
              disabled={!inputValue.trim() || isLoading}
              icon={isLoading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
              className="h-[46px] px-4"
            >
              {isLoading ? 'Solving...' : 'Send'}
            </Button>
          </form>
          <div className="flex items-center justify-between text-[11px] text-slate-400 mt-1.5 px-1">
            <span>Focused on quantitative formulas, logical derivations, and placement tricks</span>
            <span>{inputValue.length}/2000</span>
          </div>
        </div>
      </Card>
    </div>
  );
};
