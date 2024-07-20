<template>
  <div class="body">
    <product-item></product-item>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import ProductItem from '../components/common/ProductItem.vue';

export default defineComponent({
  name: 'AboutView',
  components: {
    ProductItem,
  },
});
</script>
<style scoped>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

.body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
