<script lang="ts">
  import { Button } from '$lib/components/ui/button';
  import { Textarea } from '$lib/components/ui/textarea';
  import Send from '@lucide/svelte/icons/send';

  interface Props {
    onquizgenerated: (quiz: import('$lib/types').QuizData) => void;
  }
  
  let { onquizgenerated }: Props = $props();

  let textContent = $state('');
  let generating = $state(false);

  async function handleSubmit() {
    if (!textContent.trim()) return;
    
    generating = true;
    
    try {
      // Simulate API call - replace with actual API endpoint
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Mock response data
      const mockQuizData = {
        title: 'Quiz from Text Input',
        questions: [
          {
            id: '1',
            question: 'What is the main theme of the provided text?',
            options: ['Theme A', 'Theme B', 'Theme C', 'Theme D'],
            correctAnswer: 0,
            explanation: 'Based on the analysis of your text content.'
          },
          {
            id: '2',
            question: 'Which key point is highlighted in the text?',
            options: ['Point 1', 'Point 2', 'Point 3', 'Point 4'],
            correctAnswer: 2,
            explanation: 'This point is central to the text narrative.'
          },
          {
            id: '3',
            question: 'What can be inferred from the text?',
            options: ['Inference A', 'Inference B', 'Inference C', 'Inference D'],
            correctAnswer: 1,
            explanation: 'This inference follows logically from the text content.'
          }
        ]
      };
      
      onquizgenerated(mockQuizData);
      textContent = '';
    } catch (error) {
      console.error('Generation failed:', error);
      alert('Failed to generate quiz. Please try again.');
    } finally {
      generating = false;
    }
  }
</script>

<div class="w-full max-w-2xl mx-auto space-y-4">
  <div>
    <h3 class="text-lg font-semibold mb-2">Or paste your text</h3>
    <p class="text-gray-600 text-sm mb-4">
      Enter your text content below to generate quiz questions
    </p>
  </div>
  
  <Textarea
    bind:value={textContent}
    placeholder="Paste your text content here..."
    rows={8}
    disabled={generating}
    class="resize-none"
  />
  
  <Button 
    onclick={handleSubmit}
    disabled={!textContent.trim() || generating}
    class="w-full bg-emerald-600 hover:bg-emerald-700"
  >
    {#if generating}
      <div class="animate-spin rounded-full h-4 w-4 border-b-2 border-current mr-2"></div>
      Generating Quiz...
    {:else}
      <Send class="h-4 w-4 mr-2" />
      Generate Quiz
    {/if}
  </Button>
</div>
