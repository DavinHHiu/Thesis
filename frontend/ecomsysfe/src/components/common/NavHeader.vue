<template>
  <div class="nav-header-container" :class="intent">
    <div class="w-[200px]">
      <app-logo :intent="intent" />
    </div>
    <div class="flex gap-[100px]">
      <div class="container language-container">
        <icon-image src="/icons/flags/usa.svg" />
        <h2 class="header-items font-bold">en</h2>
      </div>
      <div class="container avatar-container">
        <h2 class="header-items font-bold">account</h2>
      </div>
      <div class="container orders-container">
        <h2 class="header-items font-bold">orders</h2>
      </div>
      <div class="container cart-container">
        <icon-cart :color="intent == 'primary' ? '#000' : '#fff'" />
        <h2 class="header-items font-bold py-0.5">cart</h2>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppLogo from '../common/AppLogo.vue';
import IconCart from '../icons/IconCart.vue';
import IconImage from './IconImage.vue';

export default defineComponent({
  name: 'NavHeader',
  components: {
    AppLogo,
    IconCart,
    IconImage,
  },
  props: {
    intent: {
      type: String,
      default: 'primary',
      validator: (val: string) => {
        return ['primary', 'transparent'].includes(val);
      },
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.nav-header-container {
  position: relative;
  height: 10.3rem;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.6rem 5rem 1.6rem 3rem;
  z-index: 99;

  .container {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 1rem;

    .header-items {
      text-transform: uppercase;
    }
  }
}

.primary {
  background-color: $--second-color;
  color: $--primary-color;
}

.transparent {
  background-color: $--black-alpha-10;
  color: $--second-color;
}
</style>
