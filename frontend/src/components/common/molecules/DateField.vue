<template>
  <div class="input-wp" :class="{ 'has-input': value !== undefined }">
    <custom-label v-if="label" v-t="label" />
    <custom-input type="date" :value="value" @input="handleInput" />
  </div>
</template>

<script lang="ts">
import CustomInput from "@/components/common/atomic/CustomInput.vue";
import CustomLabel from "@/components/common/atomic/CustomLabel.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "DateField",
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
      type: Date,
      default: new Date(),
    },
  },
  methods: {
    handleInput(event: Event) {
      const target = event.target as HTMLInputElement;
      this.$emit("update:modelValue", target.value);
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";
</style>
