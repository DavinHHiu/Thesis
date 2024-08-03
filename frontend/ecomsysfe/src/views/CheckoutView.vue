<template>
  <default-layout>
    <div class="title-cont py-[50px]"><span class="title">Checkout</span></div>
    <div class="content-cont">
      <div class="content">
        <router-view></router-view>
      </div>
    </div>
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';

export default defineComponent({
  name: 'CheckoutView',
  components: {
    DefaultLayout,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.title-cont {
  .title {
    margin: auto;
    width: 120rem;
    max-width: 100%;
    display: block;
    padding: 1rem;
    font-size: $--font-8xl;
    font-weight: $--font-bold;
    text-align: center;
  }
}
.content-cont {
  margin: auto;
  width: 120rem;
  max-width: 100%;
  padding-bottom: 8rem;
  .content {
    padding: 1rem;
  }
}
</style>
