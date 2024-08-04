<template>
  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
    <g
      id="SVGRepo_tracerCarrier"
      stroke-linecap="round"
      stroke-linejoin="round"
    ></g>
    <g id="SVGRepo_iconCarrier">
      <g>
        <path fill="none" d="M0 0h24v24H0z"></path>
        <path
          d="M4 22a8 8 0 1 1 16 0H4zm8-9c-3.315 0-6-2.685-6-6s2.685-6 6-6 6 2.685 6 6-2.685 6-6 6z"
        ></path>
      </g>
    </g>
  </svg>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IconUser',
  props: {
    intent: {
      type: String,
      default: 'primary',
      validator: (value: string) => ['primary', 'second'].includes(value),
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.primary {
  svg {
    fill: $--primary-color;
  }
}

.second {
  svg {
    fill: $--second-color;
  }
}
</style>
