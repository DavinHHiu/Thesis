<template>
  <div class="title-wrap">
    <span class="title" v-t="title" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageTitle",
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.title-wrap {
  padding: 0.5rem 0;
  border-bottom: 1px solid $--primary;
  .title {
    font-size: $--font-4xl;
    font-weight: $--font-bold;
  }
}
</style>
