<template>
  <label class="input-wp">
    <input type="radio" :name="name" :checked="check" @change="changeInput" />
    <span for="">{{ label }}</span>
  </label>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RadioField",
  emits: ["update:input"],
  props: {
    label: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    check: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    changeInput() {
      this.$emit("update:input");
    },
  },
});
</script>

<style lang="scss" scoped>
.input-wp {
  display: flex;
  align-items: center;
  gap: 2rem;
}
</style>
