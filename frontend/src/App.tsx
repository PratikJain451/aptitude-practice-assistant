import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AppLayout } from './components/layout/AppLayout';
import { OverviewPage } from './pages/OverviewPage';
import { PracticePage } from './pages/PracticePage';
import { MockTestsPage } from './pages/MockTestsPage';
import { DoubtSolverPage } from './pages/DoubtSolverPage';
import { PdfStudyPage } from './pages/PdfStudyPage';
import { PerformancePage } from './pages/PerformancePage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AppLayout />}>
          <Route index element={<OverviewPage />} />
          <Route path="practice" element={<PracticePage />} />
          <Route path="mock-tests" element={<MockTestsPage />} />
          <Route path="doubt-solver" element={<DoubtSolverPage />} />
          <Route path="pdf-study" element={<PdfStudyPage />} />
          <Route path="performance" element={<PerformancePage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
