<script lang="ts">
  import type { QuizData } from '$lib/types';
  import { Button } from '$lib/components/ui/button';
  import { Card } from '$lib/components/ui/card';
  import CheckCircle from '@lucide/svelte/icons/check-circle';
  import XCircle from '@lucide/svelte/icons/x-circle';
  import RotateCcw from '@lucide/svelte/icons/rotate-ccw';
  import ArrowLeft from '@lucide/svelte/icons/arrow-left';

  interface Props {
    quizData: QuizData;
    onnewquiz: () => void;
  }
  
  let { quizData, onnewquiz }: Props = $props();

  let currentQuestionIndex = $state(0);
  let userAnswers = $state<number[]>([]);
  let showResults = $state(false);
  let selectedAnswer = $state<number | null>(null);

  let currentQuestion = $derived(quizData.questions[currentQuestionIndex]);
  let isLastQuestion = $derived(currentQuestionIndex === quizData.questions.length - 1);
  let score = $derived(userAnswers.reduce((acc, answer, index) => {
    return answer === quizData.questions[index].correctAnswer ? acc + 1 : acc;
  }, 0));

  function selectAnswer(optionIndex: number) {
    selectedAnswer = optionIndex;
  }

  function nextQuestion() {
    if (selectedAnswer !== null) {
      userAnswers[currentQuestionIndex] = selectedAnswer;
      
      if (isLastQuestion) {
        showResults = true;
      } else {
        currentQuestionIndex++;
        selectedAnswer = null;
      }
    }
  }

  function restartQuiz() {
    currentQuestionIndex = 0;
    userAnswers = [];
    showResults = false;
    selectedAnswer = null;
  }

  function newQuiz() {
    onnewquiz();
  }
</script>

<div class="w-full max-w-3xl mx-auto space-y-6">
  <div class="text-center">
    <h2 class="text-2xl font-bold text-gray-800 mb-2">{quizData.title}</h2>
    {#if !showResults}
      <p class="text-gray-600">
        Question {currentQuestionIndex + 1} of {quizData.questions.length}
      </p>
      <div class="w-full bg-gray-200 rounded-full h-2 mt-4">
        <div class="bg-emerald-600 h-2 rounded-full transition-all duration-300" 
             style="width: {((currentQuestionIndex + 1) / quizData.questions.length) * 100}%"></div>
      </div>
    {/if}
  </div>

  {#if showResults}
    <Card class="p-8 text-center">
      <div class="space-y-6">
        <div class="text-4xl font-bold text-emerald-600">
          {score}/{quizData.questions.length}
        </div>
        <div>
          <h3 class="text-xl font-semibold mb-2">Quiz Complete!</h3>
          <p class="text-gray-600">
            You scored {Math.round((score / quizData.questions.length) * 100)}%
          </p>
        </div>
        
        <div class="space-y-4">
          {#each quizData.questions as question, index}
            <div class="text-left p-4 rounded-lg border bg-white">
              <div class="flex items-start space-x-2 mb-2">
                {#if userAnswers[index] === question.correctAnswer}
                  <CheckCircle class="h-5 w-5 text-green-500 mt-0.5 flex-shrink-0" />
                {:else}
                  <XCircle class="h-5 w-5 text-red-500 mt-0.5 flex-shrink-0" />
                {/if}
                <div class="flex-1">
                  <p class="font-medium mb-2">{question.question}</p>
                  <p class="text-sm text-gray-600 mb-1">
                    Your answer: <span class={userAnswers[index] === question.correctAnswer ? 'text-green-600' : 'text-red-600'}>
                      {question.options[userAnswers[index]]}
                    </span>
                  </p>
                  {#if userAnswers[index] !== question.correctAnswer}
                    <p class="text-sm text-green-600 mb-2">
                      Correct answer: {question.options[question.correctAnswer]}
                    </p>
                  {/if}
                  {#if question.explanation}
                    <p class="text-sm text-gray-500 italic bg-gray-50 p-2 rounded">
                      {question.explanation}
                    </p>
                  {/if}
                </div>
              </div>
            </div>
          {/each}
        </div>
        
        <div class="flex gap-4 justify-center">
          <Button variant="outline" onclick={restartQuiz}>
            <RotateCcw class="h-4 w-4 mr-2" />
            Retake Quiz
          </Button>
          <Button onclick={newQuiz} class="bg-emerald-600 hover:bg-emerald-700">
            Create New Quiz
          </Button>
        </div>
      </div>
    </Card>
  {:else}
    <Card class="p-6">
      <div class="space-y-6">
        <h3 class="text-xl font-semibold">{currentQuestion.question}</h3>
        
        <div class="space-y-3">
          {#each currentQuestion.options as option, index}
            <button
              class="w-full p-4 text-left rounded-lg border transition-all duration-200 hover:bg-gray-50 hover:border-emerald-300 {selectedAnswer === index ? 'border-emerald-500 bg-emerald-50' : 'border-gray-200'}"
              onclick={() => selectAnswer(index)}
            >
              <div class="flex items-center space-x-3">
                <div class="w-5 h-5 rounded-full border-2 flex items-center justify-center {selectedAnswer === index ? 'border-emerald-500 bg-emerald-500' : 'border-gray-300'}">
                  {#if selectedAnswer === index}
                    <div class="w-2 h-2 bg-white rounded-full"></div>
                  {/if}
                </div>
                <span class="flex-1">{option}</span>
              </div>
            </button>
          {/each}
        </div>
        
        <div class="flex justify-between items-center pt-4">
          <Button variant="outline" onclick={newQuiz}>
            <ArrowLeft class="h-4 w-4 mr-2" />
            Back to Upload
          </Button>
          <Button 
            onclick={nextQuestion}
            disabled={selectedAnswer === null}
            class="bg-emerald-600 hover:bg-emerald-700"
          >
            {isLastQuestion ? 'Finish Quiz' : 'Next Question'}
          </Button>
        </div>
      </div>
    </Card>
  {/if}
</div>
