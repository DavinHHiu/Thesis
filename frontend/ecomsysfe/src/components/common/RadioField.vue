<template>
  <div class="input-wp">
    <input type="radio" :name="name" />
    <label for="">{{ label }}</label>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'RadioField',
  props: {
    label: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.input-wp {
  display: flex;
  align-items: center;
  gap: 20px;
}
</style>
