<template>
  <div class="title-cont">
    <div class="title-wp">
      <span class="title">{{ title }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageTitle',
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.title-cont {
  padding: 5rem 0;
  .title-wp {
    margin: auto;
    width: 120rem;
    max-width: 100%;
    padding: 1rem;
    text-align: center;
    .title {
      color: $--title-color-text;
      font-size: $--font-8xl;
      font-weight: $--font-bold;
    }
  }
}
</style>
