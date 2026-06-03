import { Navigate, Route, Routes } from "react-router-dom";
import { paths } from "./routes";
import { DashboardPage } from "../pages/DashboardPage";
import { ModulesPage } from "../pages/ModulesPage";
import { Module0OrientationPage } from "../pages/Module0OrientationPage";
import { Module1OverviewPage } from "../pages/Module1OverviewPage";
import { LessonPlayerPage } from "../pages/LessonPlayerPage";
import { ModuleAssessmentSplashPage } from "../pages/ModuleAssessmentSplashPage";
import { ModuleAssessmentQuizPage } from "../pages/ModuleAssessmentQuizPage";
import { FinalAssessmentSplashPage } from "../pages/FinalAssessmentSplashPage";
import { FinalAssessmentQuizPage } from "../pages/FinalAssessmentQuizPage";
import { FinalResultPage } from "../pages/FinalResultPage";
import { CertificateGatePage } from "../pages/CertificateGatePage";
import { ClinicalHubPage } from "../pages/ClinicalHubPage";
import { NotFoundPage } from "../pages/NotFoundPage";

export function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to={paths.dashboard} replace />} />
      <Route path={paths.dashboard} element={<DashboardPage />} />
      <Route path={paths.modules} element={<ModulesPage />} />
      <Route path={paths.module0} element={<Module0OrientationPage />} />
      <Route path={paths.moduleRoute} element={<Module1OverviewPage />} />
      <Route path={paths.lessonRoute} element={<LessonPlayerPage />} />
      <Route path={paths.moduleAssessmentRoute} element={<ModuleAssessmentSplashPage />} />
      <Route path={paths.moduleAssessmentQuizRoute} element={<ModuleAssessmentQuizPage />} />
      <Route path={paths.finalSplash} element={<FinalAssessmentSplashPage />} />
      <Route path={paths.finalQuiz} element={<FinalAssessmentQuizPage />} />
      <Route path={paths.finalResult} element={<FinalResultPage />} />
      <Route path={paths.certificate} element={<CertificateGatePage />} />
      <Route path={paths.clinicalHub} element={<ClinicalHubPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
