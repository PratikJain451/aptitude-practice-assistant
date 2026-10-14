import { useState, useEffect, useRef } from 'react';
import {
  FileText,
  Upload,
  Trash2,
  AlertCircle,
  CheckCircle2,
  Loader2,
  HelpCircle,
  Sparkles,
  BookOpen,
  ChevronDown,
  ChevronUp,
  MessageSquare,
  Send,
  Layers,
  FileCheck,
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { apiService } from '../services/api';
import type {
  DocumentItem,
  DocumentAskResult,
  GeneratedQuestionItem,
  Difficulty,
} from '../types';

export const PdfStudyPage: React.FC = () => {
  // Document management state
  const [documents, setDocuments] = useState<DocumentItem[]>([]);
  const [selectedDocId, setSelectedDocId] = useState<string | null>(null);
  const [isLoadingDocs, setIsLoadingDocs] = useState<boolean>(true);
  const [isUploading, setIsUploading] = useState<boolean>(false);
  const [uploadError, setUploadError] = useState<string | null>(null);

  // Active Tab: 'qa' | 'generate'
  const [activeTab, setActiveTab] = useState<'qa' | 'generate'>('qa');

  // PDF Doubt Solver state
  const [qaQuestion, setQaQuestion] = useState<string>('');
  const [isAsking, setIsAsking] = useState<boolean>(false);
  const [qaError, setQaError] = useState<string | null>(null);
  const [qaHistory, setQaHistory] = useState<
    Array<{
      id: string;
      question: string;
      answer: string;
      sources: DocumentAskResult['sources'];
      timestamp: string;
    }>
  >([]);
  const [expandedSources, setExpandedSources] = useState<Record<string, boolean>>({});

  // Question Generator state
  const [genTopic, setGenTopic] = useState<string>('');
  const [genDifficulty, setGenDifficulty] = useState<Difficulty>('Medium');
  const [genCount, setGenCount] = useState<number>(3);
  const [isGenerating, setIsGenerating] = useState<boolean>(false);
  const [genError, setGenError] = useState<string | null>(null);
  const [generatedQuestions, setGeneratedQuestions] = useState<GeneratedQuestionItem[]>([]);
  const [revealedAnswers, setRevealedAnswers] = useState<Record<string, boolean>>({});
  const [userSelectedAnswers, setUserSelectedAnswers] = useState<Record<string, string>>({});

  const fileInputRef = useRef<HTMLInputElement>(null);

  // Load documents on mount
  useEffect(() => {
    fetchDocuments();
  }, []);

  const fetchDocuments = async () => {
    setIsLoadingDocs(true);
    const result = await apiService.getDocuments();
    setIsLoadingDocs(false);

    if (result.ok && result.data) {
      setDocuments(result.data.documents);
      // Auto-select first ready document if none selected
      if (!selectedDocId && result.data.documents.length > 0) {
        const readyDoc = result.data.documents.find((d) => d.status === 'ready');
        if (readyDoc) {
          setSelectedDocId(readyDoc.id);
        } else {
          setSelectedDocId(result.data.documents[0].id);
        }
      }
    }
  };

  const selectedDocument = documents.find((d) => d.id === selectedDocId);

  const formatFileSize = (bytes: number) => {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
  };

  // Upload handler
  const handleFileUpload = async (file: File) => {
    setUploadError(null);

    // Extension check
    if (!file.name.toLowerCase().endsWith('.pdf') && file.type !== 'application/pdf') {
      setUploadError('Only PDF files (.pdf) are supported.');
      return;
    }

    // 15 MB limit
    if (file.size > 15 * 1024 * 1024) {
      setUploadError(`File exceeds the 15 MB limit (${formatFileSize(file.size)}). Please select a smaller document.`);
      return;
    }

    setIsUploading(true);
    const result = await apiService.uploadDocument(file);
    setIsUploading(false);

    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }

    if (result.ok && result.data) {
      setDocuments((prev) => [result.data!, ...prev]);
      setSelectedDocId(result.data.id);
      setUploadError(null);
    } else {
      setUploadError(result.error || 'Failed to process and index PDF document.');
    }
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      handleFileUpload(files[0]);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleFileUpload(e.dataTransfer.files[0]);
    }
  };

  const handleDeleteDocument = async (docId: string, e: React.MouseEvent) => {
    e.stopPropagation();
    if (!window.confirm('Are you sure you want to delete this document and remove its indexed vector embeddings?')) {
      return;
    }

    const result = await apiService.deleteDocument(docId);
    if (result.ok) {
      setDocuments((prev) => prev.filter((d) => d.id !== docId));
      if (selectedDocId === docId) {
        const remaining = documents.filter((d) => d.id !== docId);
        setSelectedDocId(remaining.length > 0 ? remaining[0].id : null);
      }
    } else {
      alert(result.error || 'Could not delete document.');
    }
  };

  // Q&A submission
  const handleAskQuestion = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!qaQuestion.trim() || !selectedDocId || isAsking) return;

    if (selectedDocument?.status !== 'ready') {
      setQaError('This document is not ready yet. Please wait for indexing to complete or upload a valid document.');
      return;
    }

    const promptText = qaQuestion.trim();
    setIsAsking(true);
    setQaError(null);

    const result = await apiService.askDocumentDoubt(selectedDocId, promptText);
    setIsAsking(false);

    if (result.ok && result.data) {
      setQaHistory((prev) => [
        {
          id: `qa_${Date.now()}`,
          question: promptText,
          answer: result.data!.answer,
          sources: result.data!.sources,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
        ...prev,
      ]);
      setQaQuestion('');
    } else {
      setQaError(result.error || 'Failed to get an answer for this question.');
    }
  };

  // Question generator submission
  const handleGenerateQuestions = async () => {
    if (!selectedDocId || isGenerating) return;

    if (selectedDocument?.status !== 'ready') {
      setGenError('Selected document is not indexed. Please select a ready document.');
      return;
    }

    setIsGenerating(true);
    setGenError(null);

    const result = await apiService.generateDocumentQuestions(selectedDocId, {
      topic: genTopic.trim() || undefined,
      difficulty: genDifficulty,
      count: genCount,
    });
    setIsGenerating(false);

    if (result.ok && result.data) {
      setGeneratedQuestions(result.data.questions);
      setRevealedAnswers({});
      setUserSelectedAnswers({});
    } else {
      setGenError(result.error || 'Failed to generate questions from document content.');
    }
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      {/* Page Header */}
      <div>
        <div className="flex items-center gap-2 text-indigo-600 mb-1">
          <FileText className="w-5 h-5" />
          <span className="text-xs font-semibold uppercase tracking-wider">
            Document RAG Engine
          </span>
        </div>
        <h1 className="text-2xl font-bold text-slate-900 tracking-tight">
          PDF Study Material & Grounded AI Assistant
        </h1>
        <p className="mt-1 text-sm text-slate-500 max-w-3xl">
          Upload aptitude formula handbooks, lecture notes, or company test sheets. The system extracts page text using PyMuPDF, chunks and embeds passages via <code className="text-xs bg-slate-100 text-slate-700 px-1 py-0.5 rounded font-mono">bge-small-en-v1.5</code> into persistent ChromaDB, and generates strictly grounded answers and practice questions.
        </p>
      </div>

      {/* Main Grid: Left Column Documents / Upload, Right Column RAG Workspace */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Left Column: Upload & Document Library (5 cols) */}
        <div className="lg:col-span-5 space-y-5">
          {/* Upload Card */}
          <Card className="p-5">
            <h2 className="text-sm font-bold text-slate-900 mb-1 flex items-center justify-between">
              <span>Upload Document</span>
              <span className="text-xs font-normal text-slate-400">Max 15 MB</span>
            </h2>

            {/* Drop Zone */}
            <div
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              onClick={() => fileInputRef.current?.click()}
              className={`mt-3 border-2 border-dashed rounded-lg p-5 text-center transition-all cursor-pointer group ${
                isUploading
                  ? 'border-indigo-300 bg-indigo-50/40 pointer-events-none'
                  : 'border-slate-300 hover:border-indigo-400 bg-slate-50/70 hover:bg-slate-50'
              }`}
            >
              <input
                type="file"
                ref={fileInputRef}
                onChange={handleFileInputChange}
                accept=".pdf,application/pdf"
                className="hidden"
                disabled={isUploading}
              />

              <div className="w-10 h-10 rounded-full bg-white border border-slate-200 shadow-xs flex items-center justify-center text-slate-500 group-hover:text-indigo-600 group-hover:border-indigo-200 transition-colors mx-auto mb-2">
                {isUploading ? (
                  <Loader2 className="w-5 h-5 animate-spin text-indigo-600" />
                ) : (
                  <Upload className="w-5 h-5" />
                )}
              </div>

              {isUploading ? (
                <div className="space-y-1">
                  <p className="text-xs font-semibold text-indigo-700">
                    Extracting text, chunking & indexing...
                  </p>
                  <p className="text-[11px] text-slate-400">
                    Computing sentence embeddings into ChromaDB
                  </p>
                </div>
              ) : (
                <>
                  <p className="text-xs font-semibold text-slate-800">
                    Click to browse or drop PDF here
                  </p>
                  <p className="text-[11px] text-slate-400 mt-0.5">
                    Selectable text PDFs only (scanned OCR not supported)
                  </p>
                </>
              )}
            </div>

            {/* Upload Error Alert */}
            {uploadError && (
              <div className="mt-3 p-3 bg-rose-50 border border-rose-200 rounded-md flex items-start gap-2 text-xs text-rose-800">
                <AlertCircle className="w-4 h-4 text-rose-600 shrink-0 mt-0.5" />
                <div className="flex-1 leading-relaxed">
                  <span className="font-semibold block">Upload Failed</span>
                  {uploadError}
                </div>
              </div>
            )}
          </Card>

          {/* Document Library List */}
          <Card className="p-5">
            <div className="flex items-center justify-between mb-3">
              <h2 className="text-sm font-bold text-slate-900 flex items-center gap-1.5">
                <BookOpen className="w-4 h-4 text-slate-500" />
                <span>Uploaded Documents</span>
              </h2>
              <span className="text-xs text-slate-400 font-medium">
                {documents.length} {documents.length === 1 ? 'file' : 'files'}
              </span>
            </div>

            {isLoadingDocs ? (
              <div className="py-8 text-center text-slate-400 text-xs flex items-center justify-center gap-2">
                <Loader2 className="w-4 h-4 animate-spin text-slate-400" />
                <span>Loading documents...</span>
              </div>
            ) : documents.length === 0 ? (
              <div className="py-8 text-center border border-dashed border-slate-200 rounded-lg p-4 bg-slate-50/40">
                <FileText className="w-8 h-8 text-slate-300 mx-auto mb-1.5" />
                <p className="text-xs font-medium text-slate-600">No documents indexed</p>
                <p className="text-[11px] text-slate-400 mt-0.5">
                  Upload an aptitude PDF to start grounded RAG practice.
                </p>
              </div>
            ) : (
              <div className="space-y-2 max-h-[460px] overflow-y-auto pr-1">
                {documents.map((doc) => {
                  const isSelected = doc.id === selectedDocId;
                  const isReady = doc.status === 'ready';

                  return (
                    <div
                      key={doc.id}
                      onClick={() => setSelectedDocId(doc.id)}
                      className={`p-3 rounded-lg border text-left transition-all cursor-pointer relative group ${
                        isSelected
                          ? 'border-indigo-500 bg-indigo-50/40 shadow-xs ring-1 ring-indigo-500/20'
                          : 'border-slate-200 hover:border-slate-300 bg-white hover:bg-slate-50/50'
                      }`}
                    >
                      <div className="flex items-start justify-between gap-2">
                        <div className="min-w-0 flex-1">
                          <div className="flex items-center gap-1.5">
                            <span className="text-xs font-bold text-rose-600 bg-rose-50 px-1.5 py-0.5 rounded border border-rose-100">
                              PDF
                            </span>
                            <h3 className="text-xs font-semibold text-slate-900 truncate" title={doc.original_name}>
                              {doc.original_name}
                            </h3>
                          </div>

                          <div className="flex items-center gap-2 mt-1 text-[11px] text-slate-500">
                            <span>{formatFileSize(doc.file_size)}</span>
                            {isReady && (
                              <>
                                <span>•</span>
                                <span>{doc.page_count} {doc.page_count === 1 ? 'page' : 'pages'}</span>
                                <span>•</span>
                                <span>{doc.chunk_count} chunks</span>
                              </>
                            )}
                          </div>
                        </div>

                        <div className="flex items-center gap-1 shrink-0">
                          {doc.status === 'ready' && (
                            <Badge variant="success" size="sm">
                              Ready
                            </Badge>
                          )}
                          {doc.status === 'processing' && (
                            <Badge variant="warning" size="sm">
                              Indexing
                            </Badge>
                          )}
                          {doc.status === 'failed' && (
                            <Badge variant="error" size="sm" title={doc.error_message || 'Indexing failed'}>
                              Failed
                            </Badge>
                          )}

                          <button
                            type="button"
                            onClick={(e) => handleDeleteDocument(doc.id, e)}
                            className="p-1 text-slate-400 hover:text-rose-600 rounded hover:bg-white transition-colors ml-1"
                            title="Delete document and remove Chroma vectors"
                          >
                            <Trash2 className="w-3.5 h-3.5" />
                          </button>
                        </div>
                      </div>

                      {doc.status === 'failed' && doc.error_message && (
                        <p className="mt-1.5 text-[11px] text-rose-600 bg-rose-50/80 p-1.5 rounded border border-rose-100 leading-tight">
                          {doc.error_message}
                        </p>
                      )}
                    </div>
                  );
                })}
              </div>
            )}
          </Card>
        </div>

        {/* Right Column: RAG Workspace (7 cols) */}
        <div className="lg:col-span-7 space-y-5">
          {/* Document Context Header Card */}
          <Card className="p-4 bg-slate-50/80 border-slate-200">
            {selectedDocument ? (
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div className="min-w-0">
                  <div className="flex items-center gap-2">
                    <span className="text-[11px] font-semibold uppercase text-indigo-700 tracking-wider">
                      Active Material Context
                    </span>
                    <Badge
                      variant={selectedDocument.status === 'ready' ? 'success' : 'neutral'}
                      size="sm"
                    >
                      {selectedDocument.status}
                    </Badge>
                  </div>
                  <h3 className="text-sm font-bold text-slate-900 truncate mt-0.5">
                    {selectedDocument.original_name}
                  </h3>
                  <p className="text-xs text-slate-500">
                    {selectedDocument.page_count} pages • {selectedDocument.chunk_count} semantic vector chunks in ChromaDB
                  </p>
                </div>

                {/* Tabs Switcher */}
                <div className="flex items-center bg-slate-200/70 p-0.5 rounded-lg shrink-0 self-start sm:self-auto">
                  <button
                    onClick={() => setActiveTab('qa')}
                    className={`px-3 py-1.5 text-xs font-semibold rounded-md transition-all flex items-center gap-1.5 ${
                      activeTab === 'qa'
                        ? 'bg-white text-slate-900 shadow-xs'
                        : 'text-slate-600 hover:text-slate-900'
                    }`}
                  >
                    <MessageSquare className="w-3.5 h-3.5 text-indigo-600" />
                    <span>Doubt Solver</span>
                  </button>
                  <button
                    onClick={() => setActiveTab('generate')}
                    className={`px-3 py-1.5 text-xs font-semibold rounded-md transition-all flex items-center gap-1.5 ${
                      activeTab === 'generate'
                        ? 'bg-white text-slate-900 shadow-xs'
                        : 'text-slate-600 hover:text-slate-900'
                    }`}
                  >
                    <Sparkles className="w-3.5 h-3.5 text-amber-600" />
                    <span>Drill Generator</span>
                  </button>
                </div>
              </div>
            ) : (
              <div className="text-center py-4 text-xs text-slate-500">
                Please select or upload a document to begin grounded RAG interactions.
              </div>
            )}
          </Card>

          {/* TAB 1: Grounded PDF Doubt Solver */}
          {activeTab === 'qa' && (
            <Card className="p-5 sm:p-6 space-y-5">
              <div>
                <h3 className="text-base font-bold text-slate-900">
                  Ask Document Questions (PDF Grounded)
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  Queries are matched against Chroma embeddings strictly for this PDF. Answers cite source pages and will explicitly decline if the PDF lacks sufficient context.
                </p>
              </div>

              {/* Question Input Form */}
              <form onSubmit={handleAskQuestion} className="space-y-3">
                <div className="relative">
                  <textarea
                    value={qaQuestion}
                    onChange={(e) => setQaQuestion(e.target.value)}
                    placeholder={
                      selectedDocument?.status === 'ready'
                        ? 'e.g., What is the formula for net work efficiency? Explain the derivation on page 2.'
                        : 'Please select a ready document first...'
                    }
                    disabled={selectedDocument?.status !== 'ready' || isAsking}
                    rows={3}
                    className="w-full text-xs sm:text-sm p-3 rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 bg-white resize-none disabled:bg-slate-50 disabled:text-slate-400"
                  />
                </div>

                {qaError && (
                  <div className="p-3 bg-rose-50 border border-rose-200 rounded-md flex items-start gap-2 text-xs text-rose-800">
                    <AlertCircle className="w-4 h-4 text-rose-600 shrink-0 mt-0.5" />
                    <span>{qaError}</span>
                  </div>
                )}

                <div className="flex justify-between items-center pt-1">
                  <span className="text-[11px] text-slate-400">
                    Grounded with BGE-small embeddings & Groq LLM
                  </span>
                  <Button
                    type="submit"
                    variant="primary"
                    size="sm"
                    disabled={!qaQuestion.trim() || selectedDocument?.status !== 'ready' || isAsking}
                    icon={isAsking ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Send className="w-3.5 h-3.5" />}
                  >
                    {isAsking ? 'Retrieving & Answering...' : 'Ask Document'}
                  </Button>
                </div>
              </form>

              {/* Q&A Answer History */}
              <div className="space-y-4 pt-2 border-t border-slate-100">
                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                  Recent Document Answers
                </h4>

                {qaHistory.length === 0 ? (
                  <div className="py-8 text-center text-xs text-slate-400">
                    No questions asked yet for this session. Submit a doubt above to inspect grounded answers with page citations.
                  </div>
                ) : (
                  qaHistory.map((item) => {
                    const isExpanded = expandedSources[item.id] ?? false;

                    return (
                      <div
                        key={item.id}
                        className="p-4 rounded-lg border border-slate-200 bg-white space-y-3 shadow-xs"
                      >
                        {/* Student Question */}
                        <div className="flex items-start gap-2.5">
                          <div className="w-5 h-5 rounded-full bg-slate-100 text-slate-600 flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">
                            Q
                          </div>
                          <div className="flex-1">
                            <p className="text-xs font-semibold text-slate-900 leading-snug">
                              {item.question}
                            </p>
                            <span className="text-[10px] text-slate-400">{item.timestamp}</span>
                          </div>
                        </div>

                        {/* Grounded AI Answer */}
                        <div className="flex items-start gap-2.5 pl-1 border-l-2 border-indigo-200">
                          <div className="flex-1 space-y-2">
                            <p className="text-xs text-slate-800 leading-relaxed whitespace-pre-wrap">
                              {item.answer}
                            </p>

                            {/* Source References Pills */}
                            {item.sources && item.sources.length > 0 && (
                              <div className="pt-2">
                                <div className="flex flex-wrap items-center gap-1.5">
                                  <span className="text-[11px] font-semibold text-slate-500 mr-1">
                                    Retrieved Sources:
                                  </span>
                                  {item.sources.map((src, sIdx) => (
                                    <span
                                      key={sIdx}
                                      className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200"
                                    >
                                      <FileCheck className="w-3 h-3 text-indigo-500" />
                                      Page {src.page}
                                      {src.relevance_score !== null && src.relevance_score !== undefined && (
                                        <span className="text-indigo-400 font-normal">
                                          ({Math.round(src.relevance_score * 100)}% match)
                                        </span>
                                      )}
                                    </span>
                                  ))}

                                  <button
                                    type="button"
                                    onClick={() =>
                                      setExpandedSources((prev) => ({
                                        ...prev,
                                        [item.id]: !isExpanded,
                                      }))
                                    }
                                    className="text-[11px] text-indigo-600 hover:text-indigo-800 font-medium ml-1 inline-flex items-center gap-0.5"
                                  >
                                    {isExpanded ? (
                                      <>
                                        Hide Passages <ChevronUp className="w-3 h-3" />
                                      </>
                                    ) : (
                                      <>
                                        View Passages <ChevronDown className="w-3 h-3" />
                                      </>
                                    )}
                                  </button>
                                </div>

                                {/* Expanded Snippets Box */}
                                {isExpanded && (
                                  <div className="mt-2.5 space-y-2 p-3 bg-slate-50 rounded-md border border-slate-200 text-xs text-slate-600">
                                    {item.sources.map((src, sIdx) => (
                                      <div key={sIdx} className="space-y-1">
                                        <div className="flex items-center justify-between text-[11px] font-semibold text-slate-700">
                                          <span>Page {src.page} (Chunk {src.chunk_index})</span>
                                          {src.relevance_score !== null && src.relevance_score !== undefined && (
                                            <span className="text-slate-400 font-normal">
                                              Score: {src.relevance_score}
                                            </span>
                                          )}
                                        </div>
                                        <p className="text-[11px] text-slate-600 bg-white p-2 rounded border border-slate-200 font-mono leading-relaxed">
                                          {src.text}
                                        </p>
                                      </div>
                                    ))}
                                  </div>
                                )}
                              </div>
                            )}
                          </div>
                        </div>
                      </div>
                    );
                  })
                )}
              </div>
            </Card>
          )}

          {/* TAB 2: Grounded Question Generator */}
          {activeTab === 'generate' && (
            <Card className="p-5 sm:p-6 space-y-5">
              <div>
                <h3 className="text-base font-bold text-slate-900">
                  Generate PDF-Grounded Practice Questions
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  Synthesize structured multiple-choice aptitude drill questions grounded strictly in the concepts from this PDF document.
                </p>
              </div>

              {/* Controls Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 p-4 bg-slate-50/70 border border-slate-200 rounded-lg">
                <div>
                  <label className="block text-[11px] font-bold text-slate-700 uppercase mb-1">
                    Topic Focus (Optional)
                  </label>
                  <input
                    type="text"
                    value={genTopic}
                    onChange={(e) => setGenTopic(e.target.value)}
                    placeholder="e.g. Ratio, Work, Vocab"
                    className="w-full text-xs p-2 rounded-md border border-slate-300 focus:outline-none focus:ring-1 focus:ring-indigo-500 bg-white"
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-bold text-slate-700 uppercase mb-1">
                    Difficulty Level
                  </label>
                  <select
                    value={genDifficulty}
                    onChange={(e) => setGenDifficulty(e.target.value as Difficulty)}
                    className="w-full text-xs p-2 rounded-md border border-slate-300 focus:outline-none focus:ring-1 focus:ring-indigo-500 bg-white"
                  >
                    <option value="Easy">Easy (Conceptual)</option>
                    <option value="Medium">Medium (Standard)</option>
                    <option value="Hard">Hard (Multi-step)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-[11px] font-bold text-slate-700 uppercase mb-1">
                    Number of Questions
                  </label>
                  <select
                    value={genCount}
                    onChange={(e) => setGenCount(parseInt(e.target.value))}
                    className="w-full text-xs p-2 rounded-md border border-slate-300 focus:outline-none focus:ring-1 focus:ring-indigo-500 bg-white"
                  >
                    <option value={1}>1 Question</option>
                    <option value={3}>3 Questions</option>
                    <option value={5}>5 Questions</option>
                    <option value={8}>8 Questions</option>
                  </select>
                </div>
              </div>

              {genError && (
                <div className="p-3 bg-rose-50 border border-rose-200 rounded-md flex items-start gap-2 text-xs text-rose-800">
                  <AlertCircle className="w-4 h-4 text-rose-600 shrink-0 mt-0.5" />
                  <span>{genError}</span>
                </div>
              )}

              <div className="flex justify-end">
                <Button
                  variant="primary"
                  size="sm"
                  onClick={handleGenerateQuestions}
                  disabled={selectedDocument?.status !== 'ready' || isGenerating}
                  icon={isGenerating ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Sparkles className="w-3.5 h-3.5" />}
                >
                  {isGenerating ? 'Generating Grounded Drills...' : 'Generate Questions from PDF'}
                </Button>
              </div>

              {/* Generated Questions List */}
              <div className="space-y-4 pt-2 border-t border-slate-100">
                <div className="flex items-center justify-between">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                    Generated Drill Set ({generatedQuestions.length})
                  </h4>
                  {generatedQuestions.length > 0 && (
                    <Badge variant="neutral" size="sm">
                      Distinguished from Repository Question Bank
                    </Badge>
                  )}
                </div>

                {generatedQuestions.length === 0 ? (
                  <div className="py-8 text-center text-xs text-slate-400 border border-dashed border-slate-200 rounded-lg bg-slate-50/40 p-6">
                    <Layers className="w-8 h-8 text-slate-300 mx-auto mb-1.5" />
                    <p className="font-medium text-slate-600">No generated questions yet</p>
                    <p className="text-[11px] text-slate-400 mt-0.5">
                      Click the generate button above to extract relevant concepts from this document and create test questions.
                    </p>
                  </div>
                ) : (
                  <div className="space-y-4">
                    {generatedQuestions.map((q, idx) => {
                      const userChoice = userSelectedAnswers[q.id];
                      const isRevealed = revealedAnswers[q.id] || false;

                      return (
                        <div
                          key={q.id}
                          className="p-4 rounded-lg border border-slate-200 bg-white space-y-3 shadow-xs"
                        >
                          {/* Question Header & Tags */}
                          <div className="flex items-start justify-between gap-2">
                            <span className="text-xs font-bold text-slate-800">
                              Question {idx + 1}
                            </span>
                            <div className="flex items-center gap-1.5">
                              {q.source_pages && q.source_pages.length > 0 && (
                                <Badge variant="neutral" size="sm">
                                  Source: Page {q.source_pages.join(', ')}
                                </Badge>
                              )}
                              {q.verified ? (
                                <Badge variant="success" size="sm">
                                  Verified Structure
                                </Badge>
                              ) : (
                                <Badge variant="neutral" size="sm">
                                  Generated
                                </Badge>
                              )}
                            </div>
                          </div>

                          <p className="text-xs sm:text-sm font-medium text-slate-900 leading-relaxed">
                            {q.question}
                          </p>

                          {/* Options */}
                          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                            {q.options.map((opt) => {
                              const isSelected = userChoice === opt.id;
                              const isCorrect = opt.id === q.correct_option;

                              let optClass = 'border-slate-200 hover:border-slate-300 bg-white text-slate-700';
                              if (isRevealed) {
                                if (isCorrect) {
                                  optClass = 'border-emerald-300 bg-emerald-50 text-emerald-900 font-semibold ring-1 ring-emerald-400';
                                } else if (isSelected && !isCorrect) {
                                  optClass = 'border-rose-300 bg-rose-50 text-rose-900';
                                }
                              } else if (isSelected) {
                                optClass = 'border-indigo-400 bg-indigo-50 text-indigo-900 font-semibold';
                              }

                              return (
                                <button
                                  key={opt.id}
                                  type="button"
                                  onClick={() => {
                                    if (!isRevealed) {
                                      setUserSelectedAnswers((prev) => ({
                                        ...prev,
                                        [q.id]: opt.id,
                                      }));
                                    }
                                  }}
                                  className={`p-2.5 rounded-md border text-left text-xs transition-all flex items-center gap-2 ${optClass}`}
                                >
                                  <span className="w-5 h-5 rounded flex items-center justify-center font-bold text-[11px] bg-slate-100 text-slate-700 shrink-0">
                                    {opt.id}
                                  </span>
                                  <span className="leading-snug">{opt.text}</span>
                                </button>
                              );
                            })}
                          </div>

                          {/* Reveal Answer & Explanation */}
                          <div className="pt-2 border-t border-slate-100 flex items-center justify-between">
                            <button
                              type="button"
                              onClick={() =>
                                setRevealedAnswers((prev) => ({
                                  ...prev,
                                  [q.id]: !isRevealed,
                                }))
                              }
                              className="text-xs font-semibold text-indigo-600 hover:text-indigo-800 flex items-center gap-1"
                            >
                              <HelpCircle className="w-3.5 h-3.5" />
                              <span>{isRevealed ? 'Hide Explanation' : 'Check Answer & Explanation'}</span>
                            </button>

                            {isRevealed && (
                              <span className="text-xs font-bold text-emerald-700 flex items-center gap-1">
                                <CheckCircle2 className="w-3.5 h-3.5" />
                                Correct: Option {q.correct_option}
                              </span>
                            )}
                          </div>

                          {isRevealed && (
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md text-xs text-slate-700 leading-relaxed">
                              <span className="font-bold text-slate-900 block mb-1">
                                Grounded Explanation:
                              </span>
                              {q.explanation}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
};
