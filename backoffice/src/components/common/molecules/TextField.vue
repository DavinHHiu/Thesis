<template>
  <div
    class="input-wp"
    :class="{ 'has-input': (inputValue != '') | (value != '') }"
  >
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
      type: String,
      default: "",
    },
  },
  data() {
    return {
      inputValue: "",
    };
  },
  methods: {
    handleInput(event: any) {
      const value = event.target.value;
      this.inputValue = value;
      this.$emit("update:modelValue", this.inputValue);
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables.scss";

.input-wp {
  position: relative;
  &.has-input,
  &:focus-within {
    label {
      top: -1.25rem;
      left: 0.2rem;
      color: $--text-color;
      font-size: $--font-sm;
      font-weight: $--font-semibold;
    }
  }
}
label {
  top: 50%;
  left: 1rem;
  color: $--gray-color-700;
  transform: translateY(-50%);
  position: absolute;
  transition: 0.2s all ease-out;
}
</style>
