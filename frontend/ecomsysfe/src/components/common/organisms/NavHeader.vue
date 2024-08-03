<template>
  <div class="nav-header-container" :class="intent">
    <div class="w-[20rem]">
      <app-logo :intent="intent" />
    </div>
    <div class="flex gap-[7rem]">
      <div class="container">
        <p class="header-items">en</p>
      </div>
      <div class="container">
        <p class="header-items">orders</p>
      </div>
      <div class="container">
        <icon-cart :intent="intent" />
        <p class="header-items py-0.5">cart</p>
      </div>
      <div class="container">
        <icon-user width="2rem" :intent="intent" />
        <p class="header-items">account</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AppLogo from '../molecules/AppLogo.vue';
import IconCart from '../../icons/IconCart.vue';
import IconUser from '../../icons/IconUser.vue';

export default defineComponent({
  name: 'NavHeader',
  components: {
    AppLogo,
    IconCart,
    IconUser,
  },
  props: {
    intent: {
      type: String,
      default: 'primary',
      validator: (val: string) => {
        return ['primary', 'second'].includes(val);
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
  padding: 1.6rem 7rem 1.6rem 3rem;
  z-index: 99;

  .container {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 1rem;

    .header-items {
      text-transform: uppercase;
      font-size: $--font-base;
      font-weight: $--font-semibold;
    }
  }
}

.primary {
  background-color: $--second-color;
  color: $--primary-color;
}

.second {
  background-color: $--black-alpha-10;
  color: $--second-color;
}
</style>
