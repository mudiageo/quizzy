<script lang="ts">
  import Upload from '@lucide/svelte/icons/upload';
  import FileText from '@lucide/svelte/icons/file-text';
  import File from '@lucide/svelte/icons/file';
  import { Button } from '$lib/components/ui/button';
  import { cn } from '$lib/utils';
  
  interface Props {
    onquizgenerated: (quiz: import('$lib/types').QuizData) => void;
  }
  
  let { onquizgenerated }: Props = $props();

  let dragActive = $state(false);
  let fileInput = $state<HTMLInputElement>();
  let uploading = $state(false);

  const acceptedTypes = {
    'application/pdf': '.pdf',
    'text/plain': '.txt',
    'text/markdown': '.md'
  };

  function handleDrop(e: DragEvent) {
    e.preventDefault();
    dragActive = false;
    
    const files = e.dataTransfer?.files;
    if (files && files.length > 0) {
      handleFile(files[0]);
    }
  }

  function handleFileSelect(e: Event) {
    const input = e.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      handleFile(input.files[0]);
    }
  }

  async function handleFile(file: File) {
    if (!Object.keys(acceptedTypes).includes(file.type) && !file.name.endsWith('.txt')) {
      alert('Please upload a PDF or text file only.');
      return;
    }

    uploading = true;
    
    try {
      // Simulate API call - replace with actual API endpoint
      const formData = new FormData();
      formData.append('file', file);
      
      // Mock API response - replace with actual API call
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Mock response data
      const mockQuizData = {
        title: `Quiz from ${file.name}`,
        questions: [
          {
            id: '1',
            question: 'What is the main topic discussed in the document?',
            options: ['Option A', 'Option B', 'Option C', 'Option D'],
            correctAnswer: 0,
            explanation: 'Based on the content analysis of the uploaded document.'
          },
          {
            id: '2',
            question: 'Which concept is most emphasized in the text?',
            options: ['Concept 1', 'Concept 2', 'Concept 3', 'Concept 4'],
            correctAnswer: 1,
            explanation: 'This concept appears multiple times throughout the document.'
          },
          {
            id: '3',
            question: 'What conclusion can be drawn from the document?',
            options: ['Conclusion A', 'Conclusion B', 'Conclusion C', 'Conclusion D'],
            correctAnswer: 2,
            explanation: 'This conclusion is supported by the evidence presented.'
          }
        ]
      };
      
      onquizgenerated(mockQuizData);
    } catch (error) {
      console.error('Upload failed:', error);
      alert('Failed to generate quiz. Please try again.');
    } finally {
      uploading = false;
    }
  }

  function openFileDialog() {
    fileInput?.click();
  }
</script>

<div class="w-full max-w-2xl mx-auto">
  <div
    class={cn(
      "relative border-2 border-dashed rounded-lg p-8 text-center transition-colors",
      dragActive ? "border-emerald-500 bg-emerald-50" : "border-gray-300 hover:border-emerald-400",
      uploading && "pointer-events-none opacity-50"
    )}
    ondragover={(e) => { e.preventDefault(); dragActive = true; }}
    ondragleave={(e) => { e.preventDefault(); dragActive = false; }}
    ondrop={handleDrop}
    role="button"
    tabindex="0"
  >
    <input
      bind:this={fileInput}
      type="file"
      accept=".pdf,.txt,.md"
      class="hidden"
      onchange={handleFileSelect}
    />
    
    <div class="flex flex-col items-center space-y-4">
      {#if uploading}
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-500"></div>
        <p class="text-lg font-medium">Generating quiz...</p>
        <p class="text-sm text-gray-600">Please wait while we analyze your document</p>
      {:else}
        <div class="p-3 rounded-full bg-emerald-100">
          <Upload class="h-8 w-8 text-emerald-600" />
        </div>
        <div>
          <h3 class="text-lg font-semibold mb-2">Upload your document</h3>
          <p class="text-gray-600 mb-4">
            Drop your PDF or text file here, or click to browse
          </p>
        </div>
        
        <Button onclick={openFileDialog} class="px-6 bg-emerald-600 hover:bg-emerald-700">
          Choose File
        </Button>
        
        <div class="flex items-center space-x-4 text-sm text-gray-500">
          <div class="flex items-center space-x-1">
            <File class="h-4 w-4" />
            <span>PDF</span>
          </div>
          <div class="flex items-center space-x-1">
            <FileText class="h-4 w-4" />
            <span>TXT</span>
          </div>
        </div>
      {/if}
    </div>
  </div>
</div>