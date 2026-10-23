<!-- Counter.svelte — try it at https://svelte.dev/playground -->
<script>
  let count = $state(0);
  let double = $derived(count * 2);
</script>

<h1>Svelte Counter</h1>
<p>{count} (double: {double})</p>
<button onclick={() => count--} disabled={count === 0}>−</button>
<button onclick={() => count++}>+</button>
