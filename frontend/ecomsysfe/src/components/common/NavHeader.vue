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

<style scoped>
.nav-header-container {
  position: relative;
  height: 103px;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 50px 16px 30px;
  z-index: 99;

  .container {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 10px;

    .header-items {
      text-transform: uppercase;
    }
  }
}

.primary {
  background-color: #fff;
  color: #000;
}

.transparent {
  background-color: rgb(0, 0, 0, 0.1);
  color: #fff;
}
</style>
