<template>
  <div :class="['nav-item', { active }]" tabindex="none">
    <span class="nav-title" v-text="title" />
    <div class="nav-qty-cont">
      <span class="nav-qty" v-text="quantity" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "NavPillItem",
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
@import "@/assets/scss/variables";

.nav-item {
  display: flex;
  align-items: center;
  justify-content: center;
  color: $--primary;
  padding: 0.7rem 0;
  padding-left: 2rem;
  padding-right: 1rem;
  border-radius: 2rem;
  user-select: none;
  gap: 0.5rem;
  transition: all 0.2s ease-out;
  cursor: pointer;

  span {
    font-weight: $--font-bold;
    line-height: 1;
  }

  .nav-title {
    text-transform: capitalize;
  }

  .nav-qty-cont {
    padding: 0 0.7rem;
    border-radius: 2rem;
    border: 1px solid $--gray-color-900;
    text-align: center;
    min-width: 2.5rem;
  }

  &.active {
    color: $--white;
    background-color: $--primary;

    .nav-qty-cont {
      background-color: $--primary;
      border: none;
      span {
        line-height: 1;
      }
    }
  }
}
</style>
