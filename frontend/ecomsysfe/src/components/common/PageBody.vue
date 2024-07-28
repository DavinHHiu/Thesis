<template>
  <div class="body-cont">
    <div class="body-wp">
      <slot></slot>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageBody',
});
</script>

<style lang="scss" scoped>
.body-cont {
  margin: auto;
  width: 120rem;
  max-width: 100%;
  padding-bottom: 8rem;
  .body-wp {
    padding: 1rem;
  }
}
</style>
