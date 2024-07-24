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

<style lang="scss">
.nav-item {
  display: flex;
  align-items: center;
  justify-content: center;
  color: #000;
  padding: 7px 0px;
  padding-left: 20px;
  padding-right: 10px;
  border-radius: 20px;
  user-select: none;
  gap: 5px;
  transition: all 0.2s ease-out;

  span {
    font-weight: 600;
  }

  .nav-qty-cont {
    padding: 0 7px;
    border-radius: 20px;
    border: 1px solid #777;
  }
}
.active {
  color: #fff;
  background-color: #000;

  .nav-qty-cont {
    background-color: #000;
    border: none;
  }
}
</style>
