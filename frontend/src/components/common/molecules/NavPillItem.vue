<template>
  <div :class="['nav-item', { active: active }]" tabindex="none">
    <span class="nav-title">{{ title }}</span>
    <div class="nav-qty-cont">
      <span class="nav-qty">{{ quantity }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavPillItem',
  props: {
    title: {
      type: String,
      required: true,
    },
    quantity: {
      type: Number,
      required: false,
    },
    active: {
      type: Boolean,
      default: false,
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.nav-item {
  display: flex;
  align-items: center;
  justify-content: center;
  color: $--primary-color;
  padding: 0.7rem 0;
  padding-left: 2rem;
  padding-right: 1rem;
  border-radius: 2rem;
  user-select: none;
  gap: 0.5rem;
  transition: all 0.2s ease-out;

  span {
    font-weight: $--font-bold;
  }

  .nav-qty-cont {
    padding: 0 0.7rem;
    border-radius: 2rem;
    border: 1px solid $--gray-color-900;
  }
}
.active {
  color: $--second-color;
  background-color: $--primary-color;

  .nav-qty-cont {
    background-color: $--primary-color;
    border: none;
  }
}
</style>
