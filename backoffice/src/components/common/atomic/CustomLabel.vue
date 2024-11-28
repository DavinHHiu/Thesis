<template>
  <label class="custom-label" :class="{ required: required }" v-t="label" />
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "CustomLabel",
  props: {
    label: {
      type: String,
      required: false,
    },
    required: {
      type: Boolean,
      default: false,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.required {
  &::after {
    content: "*";
    margin-left: 0.3rem;
    color: $--color-red;
  }
}
</style>
