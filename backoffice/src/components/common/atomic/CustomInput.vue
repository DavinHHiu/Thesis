<template>
  <input class="w-full h-[5rem]" :class="intent" />
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "CustomInput",
  props: {
    intent: {
      type: String,
      default: "primary",
      validator: (value) => {
        return ["primary"].includes(value);
      },
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

input {
  transition: all 0.2s linear;
}

.validated {
  border: 1px solid $--color-valid;
}
.invalidated {
  border: 1px solid $--color-invalid;
}

.primary {
  border: 1px solid $--dark-alt;
  padding: 0 1.5rem;
  &:focus {
    border: 1px dotted $--black-color-900;
  }
}
</style>
