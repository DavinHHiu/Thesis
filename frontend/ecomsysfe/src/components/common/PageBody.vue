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
  max-width: 1200px;
  padding-bottom: 80px;
  .body-wp {
    padding: 10px;
  }
}
</style>
