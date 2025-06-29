<script lang="ts">
  import Brain from '@lucide/svelte/icons/brain';
  import Sparkles from '@lucide/svelte/icons/sparkles';
  import BookOpen from '@lucide/svelte/icons/book-open';
  import FileUpload from '$lib/components/FileUpload.svelte';
  import TextInput from '$lib/components/TextInput.svelte';
  import Quiz from '$lib/components/Quiz.svelte';
  import { Button } from '$lib/components/ui/button';
  import type { QuizData } from '$lib/types';

  let currentQuiz = $state<QuizData | null>(null);
  let activeTab = $state<'upload' | 'text'>('upload');

  function handleQuizGenerated(quiz: QuizData) {
    currentQuiz = quiz;
  }

  function handleNewQuiz() {
    currentQuiz = null;
    activeTab = 'upload';
  }
</script>

<svelte:head>
  <title>Quiizzy - Generate Quizzes from Documents</title>
  <meta name="description" content="Transform your documents into interactive quizzes with AI" />
</svelte:head>

<div class="min-h-screen">
  {#if currentQuiz}
    <div class="container mx-auto px-4 py-8">
      <Quiz quizData={currentQuiz} onnewquiz={handleNewQuiz} />
    </div>
  {:else}
    <!-- Header -->
    <header class="bg-white/90 backdrop-blur-sm border-b sticky top-0 z-10">
      <div class="container mx-auto px-4 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="p-2 rounded-lg bg-emerald-100">
              <Brain class="h-6 w-6 text-emerald-600" />
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-800">Quiizzy</h1>
              <p class="text-sm text-gray-600">AI-powered quiz generator</p>
            </div>
          </div>
          <div class="flex items-center space-x-2 text-emerald-600">
            <Sparkles class="h-5 w-5" />
            <span class="text-sm font-medium">Powered by AI</span>
          </div>
        </div>
      </div>
    </header>

    <!-- Hero Section -->
    <section class="py-16 px-4">
      <div class="container mx-auto text-center max-w-4xl">
        <div class="flex justify-center mb-6">
          <div class="p-4 rounded-full bg-emerald-100">
            <BookOpen class="h-12 w-12 text-emerald-600" />
          </div>
        </div>
        <h2 class="text-4xl md:text-5xl font-bold text-gray-800 mb-4">
          Transform Documents into 
          <span class="text-emerald-600">Interactive Quizzes</span>
        </h2>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Upload your PDFs or paste text content, and let our AI generate engaging quiz questions 
          to test comprehension and knowledge retention.
        </p>
        
        <!-- Tab Navigation -->
        <div class="flex justify-center mb-8">
          <div class="bg-white rounded-lg p-1 border shadow-sm">
            <Button
              variant={activeTab === 'upload' ? 'default' : 'ghost'}
              onclick={() => activeTab = 'upload'}
              class={activeTab === 'upload' ? 'bg-emerald-600 hover:bg-emerald-700' : ''}
            >
              Upload File
            </Button>
            <Button
              variant={activeTab === 'text' ? 'default' : 'ghost'}
              onclick={() => activeTab = 'text'}
              class={activeTab === 'text' ? 'bg-emerald-600 hover:bg-emerald-700' : ''}
            >
              Paste Text
            </Button>
          </div>
        </div>

        <!-- Content -->
        <div class="max-w-3xl mx-auto">
          {#if activeTab === 'upload'}
            <FileUpload onquizgenerated={handleQuizGenerated} />
          {:else}
            <TextInput onquizgenerated={handleQuizGenerated} />
          {/if}
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="py-16 px-4 bg-white/50">
      <div class="container mx-auto max-w-4xl">
        <h3 class="text-2xl font-bold text-center mb-12 text-gray-800">Why Choose Quiizzy?</h3>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center">
            <div class="p-3 rounded-full bg-emerald-100 w-fit mx-auto mb-4">
              <Brain class="h-6 w-6 text-emerald-600" />
            </div>
            <h4 class="font-semibold mb-2">AI-Powered</h4>
            <p class="text-gray-600 text-sm">Advanced AI analyzes your content to generate relevant, thoughtful questions.</p>
          </div>
          <div class="text-center">
            <div class="p-3 rounded-full bg-emerald-100 w-fit mx-auto mb-4">
              <Sparkles class="h-6 w-6 text-emerald-600" />
            </div>
            <h4 class="font-semibold mb-2">Instant Results</h4>
            <p class="text-gray-600 text-sm">Get your quiz in seconds. No waiting, no complex setup required.</p>
          </div>
          <div class="text-center">
            <div class="p-3 rounded-full bg-emerald-100 w-fit mx-auto mb-4">
              <BookOpen class="h-6 w-6 text-emerald-600" />
            </div>
            <h4 class="font-semibold mb-2">Multiple Formats</h4>
            <p class="text-gray-600 text-sm">Support for PDFs, text files, and direct text input for maximum flexibility.</p>
          </div>
        </div>
      </div>
    </section>
  {/if}
</div>