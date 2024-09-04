<template>
  <component :is="as" :disable="disable" :class="btnClass">
    <slot />
  </component>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "CustomButton",
  props: {
    as: {
      type: String,
      default: "button",
    },
    disable: {
      type: Boolean,
      default: false,
    },
    rounded: {
      type: Boolean,
      default: false,
    },
    intent: {
      type: String,
      default: "primary",
      validator: (val: string) =>
        ["primary", "second", "p-outline"].includes(val),
      required: false,
    },
  },
  computed: {
    btnClass() {
      const classList = ["btn"];
      if (this.rounded) {
        classList.push("rounded");
      }
      if (this.intent) {
        classList.push(this.intent);
      }
      return classList;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.btn {
  display: flex;
  justify-content: center;
  align-items: center;
  transition: 0.2s ease-out;
  font-weight: $--font-bold;
  border-radius: 0.4rem;
  padding: 0.8rem 1.2rem;
  border: 1px solid $--primary;
  gap: 0.3rem;
}

.primary {
  background-color: $--primary;
  color: $--white;
}

.second {
  background-color: $--white;
  color: $--primary;
}

.p-outline {
  border: 1px solid $--dark-gray;
  color: $--dark-gray;
  background-color: $--white;
}

.none {
  border: none;
  background-color: transparent;
  color: inherit;
}

.rounded {
  border-radius: 5rem;
}
</style>
