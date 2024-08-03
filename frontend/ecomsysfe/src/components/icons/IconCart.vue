<template>
  <div class="wrapper">
    <svg
      viewBox="0 0 24 24"
      xmlns="http://www.w3.org/2000/svg"
      id="cart"
      :class="intent"
      fill="#000000"
    >
      <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
      <g
        id="SVGRepo_tracerCarrier"
        stroke-linecap="round"
        stroke-linejoin="round"
      ></g>
      <g id="SVGRepo_iconCarrier">
        <path
          d="M22,7.24l-2,8a1,1,0,0,1-.88.76l-11,1H8a1,1,0,0,1-1-.85l-1.38-9v0L5.14,4H3A1,1,0,0,1,3,2H5.14a2,2,0,0,1,2,1.69L7.48,6H21a1,1,0,0,1,.79.38A1,1,0,0,1,22,7.24ZM16.5,19A1.5,1.5,0,1,0,18,20.5,1.5,1.5,0,0,0,16.5,19Zm-6,0A1.5,1.5,0,1,0,12,20.5,1.5,1.5,0,0,0,10.5,19Z"
        ></path>
      </g>
    </svg>
    <div class="cart-quantity-wrapper">
      <p class="cart-quantity">1</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IconCart',
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

.wrapper {
  position: relative;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  justify-content: center;
  align-items: center;

  .cart-quantity-wrapper {
    position: absolute;
    top: -0.5rem;
    right: -0.7rem;
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;

    .cart-quantity {
      font-size: $--font-3xs;
      font-weight: bold;
    }
  }
}

.primary {
  .cart-quantity-wrapper {
    background-color: $--primary-color;
    .cart-quantity {
      color: $--second-color;
    }
  }
  svg path {
    fill: $--primary-color;
  }
}

.second {
  .cart-quantity-wrapper {
    background-color: $--second-color;
    .cart-quantity {
      color: $--primary-color;
    }
  }
  svg path {
    fill: $--second-color;
  }
}
</style>
