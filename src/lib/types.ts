export interface Question {
  id: string;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation?: string;
}

export interface QuizData {
  title: string;
  questions: Question[];
}

export interface UploadResponse {
  success: boolean;
  data?: QuizData;
  error?: string;
}