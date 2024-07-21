<template>
  <input
    ref="inputRef"
    :type="inputType"
    :placeholder="placeholder"
    :disabled="disabled"
    :maxlength="maxLength"
  />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'TextField',
  props: {
    inputType: {
      type: String,
      required: false,
    },
    placeholder: {
      type: String,
      required: false,
    },
    disabled: {
      type: Boolean,
      required: false,
    },
    maxLength: {
      type: Number,
      required: false,
    },
  },
  methods: {
    getInputRef() {
      return this.$refs.inputRef;
    },
  },
});
</script>

<style scoped>
input {
  padding: 10px 15px;
  outline: none;
  color: #000;
  border: 1px solid #ddd;
}
</style>
