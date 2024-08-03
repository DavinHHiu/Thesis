<template>
  <input class="w-full h-full" :class="intent" />
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CustomInput',
  props: {
    intent: {
      type: String,
      default: 'primary',
      validator: (value) => {
        return ['primary'].includes(value);
      },
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

input {
  transition: all 0.2s linear;

  &::-webkit-input-placeholder {
    color: $--gray-color-700;
  }

  &:-moz-placeholder {
    color: $--gray-color-700;
  }

  &::-moz-placeholder {
    color: $--gray-color-700;
  }

  &:-ms-input-placeholder {
    color: $--gray-color-700;
  }
}

.validated {
  border: 1px solid $--color-valid;
}
.invalidated {
  border: 1px solid $--color-invalid;
}

.primary {
  border: 1px solid $--color-border;
  padding: 0 1.5rem;
  &:focus {
    border: 1px dotted $--black-color-900;
  }
}
</style>
