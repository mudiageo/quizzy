<script lang="ts">
	import '../app.css';
	
	let { children } = $props();
</script>

<main class="min-h-screen bg-gradient-to-br from-white to-emerald-50">
  {@render children()}
</main>
