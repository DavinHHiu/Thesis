<template>
  <div class="input-wp">
    <input :type="type" class="password-input" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PasswordField',
  props: {
    type: {
      type: String,
      default: 'password',
    },
  },
});
</script>

<style lang="scss" scoped>
.input-wp {
  width: 100%;
  height: 100%;
  .password-input {
    &::after {
      content: '';
    }
  }
}
</style>
