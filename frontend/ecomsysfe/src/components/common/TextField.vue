<template>
  <input
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
});
</script>

<style scoped>
input {
  padding: 10px 15px;
  outline: none;
  color: #000;
}
</style>
