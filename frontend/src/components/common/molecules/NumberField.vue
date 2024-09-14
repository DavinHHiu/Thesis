<template>
  <div class="input-wp" :class="{ 'has-input': value != '' }">
    <custom-label v-if="label">{{ label }}</custom-label>
    <custom-input
      ref="inputRef"
      type="number"
      :value="value"
      @input="handleInput"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CustomInput from '../atomic/CustomInput.vue';
import CustomLabel from '../atomic/CustomLabel.vue';

export default defineComponent({
  name: 'TextField',
  components: {
    CustomInput,
    CustomLabel,
  },
  props: {
    label: {
      type: String,
      required: false,
    },
    value: {
      type: [String, Number],
      default: '',
    },
  },
  data() {
    return {
      validated: false,
    };
  },
  methods: {
    getInputRef() {
      return this.$refs.inputRef;
    },
    handleValidation(event: any) {
      this.validated = event.target.value.trim() ? true : false;
      console.log(this.validated);
    },
    handleInput(event: any) {
      const value = event.target.value;
      this.$emit('update:modelValue', value);
    },
  },
});
</script>

<style lang="scss" scoped>
input {
  text-align: center;
}
</style>
