<template>
  <component :is="as" :class="buttonClass">
    <svg
      v-if="loading"
      class="animate-spin h-5 w-5"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle
        class="opacity-25"
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        stroke-width="4"
      ></circle>
      <path
        class="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      ></path>
    </svg>
    <component v-if="!loading" :is="leftIcon" />
    <slot></slot>
    <component v-if="!loading" :is="rightIcon" />
  </component>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CustomButton',
  props: {
    btnType: {
      type: String,
      default: 'button',
      required: false,
    },
    disabled: {
      type: Boolean,
      required: false,
    },
    loading: {
      type: Boolean,
      default: false,
      required: false,
    },
    leftIcon: {
      type: Object,
      required: false,
    },
    rightIcon: {
      type: Object,
      required: false,
    },
    as: {
      type: [String, Object],
      default: 'button',
    },
    intent: {
      type: String,
      validator: (val: string) =>
        ['primary', 'second', 'outline', 'text', 'danger'].includes(val),
      default: 'secondary',
      required: false,
    },
  },
  computed: {
    buttonClass() {
      const classes = ['btn'];
      const variants = {
        intent: {
          primary: 'bg-black text-white',
          second: 'bg-white text-black',
          outline: [
            'text-black bg-transparent',
            'hover:text-white hover:bg-black',
            'outlinePrimary',
          ],
          outlineSecond: 'outlineSecond',
        },
      };
      if (this.intent) {
        classes.push(variants.intent[this.intent]);
      }
      return classes;
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.btn {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  min-width: 3.2rem;
  font-weight: $--font-semibold;
  font-size: $--font-sm;
  transition: all 0.2s linear;
  gap: 0.5rem;
}

.outlinePrimary {
  border: 1px solid $--primary-color;
}

.outlineSecond {
  color: $--second-color-text;
  border: 1px solid $--second-color;
}
</style>
