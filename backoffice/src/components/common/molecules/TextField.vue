<template>
  <div class="input-wp" :class="{ 'has-input': value != '' }">
    <custom-label v-if="label">{{ label }}</custom-label>
    <custom-input :value="value" @input="handleInput" />
  </div>
</template>

<script lang="ts">
import CustomInput from "../atomic/CustomInput.vue";
import CustomLabel from "../atomic/CustomLabel.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "TextField",
  emits: ["update:modelValue"],
  components: {
    CustomLabel,
    CustomInput,
  },
  props: {
    label: {
      type: String,
      required: false,
    },
    value: {
      type: [String, Number],
      default: "",
    },
  },
  methods: {
    handleInput(event: any) {
      const value = event.target.value;
      this.$emit("update:modelValue", value);
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables.scss";
</style>
