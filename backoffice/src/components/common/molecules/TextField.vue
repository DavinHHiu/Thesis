<template>
  <div class="input-wp">
    <custom-label v-if="label">{{ label }}</custom-label>
    <custom-input />
  </div>
</template>

<script lang="ts">
import CustomInput from "../atomic/CustomInput.vue";
import CustomLabel from "../atomic/CustomLabel.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "TextField",
  components: {
    CustomLabel,
    CustomInput,
  },
  props: {
    label: {
      type: String,
      required: false,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables.scss";

.input-wp {
  position: relative;
  &:focus-within {
    label {
      top: -1rem;
      left: 0.2rem;
      color: $--text-color;
      font-size: $--font-xs;
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
