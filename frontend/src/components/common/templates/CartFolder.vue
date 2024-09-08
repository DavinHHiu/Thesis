<template>
  <div class="cart-folder-wp">
    <div class="cart-folder flex flex-col w-full">
      <div class="cart-folder-header w-full flex justify-between">
        <p class="cart-title">Shopping Cart</p>
        <span
          class="material-symbols-outlined"
          @click="$emit('close:cart-folder')"
        >
          close
        </span>
      </div>
      <div class="cart-folder-body flex-1">
        <cart-folder-item />
      </div>
      <div class="cart-folder-footer">
        <custom-button class="btn-view" intent="primary"
          >View cart</custom-button
        >
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CustomButton from '../atomic/CustomButton.vue';
import CartFolderItem from '../molecules/CartFolderItem.vue';

export default defineComponent({
  name: 'CartFolder',
  components: {
    CustomButton,
    CartFolderItem,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.cart-folder-wp {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: $--black-alpha-40;
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
  z-index: 999;
  transition: all 0.3s ease-in-out;
  .cart-folder {
    position: absolute;
    right: -35%;
    height: 100%;
    width: 35%;
    background-color: $--second-color;
    transition: all 0.3s ease-in-out;
    .cart-folder-header {
      padding: 2rem;
      border-bottom: 1px solid $--color-border;
      .cart-title {
        font-weight: $--font-semibold;
        font-size: $--font-base;
      }
    }
    .cart-folder-footer {
      padding: 2.2rem;
      .btn-view {
        width: 100%;
        padding: 1.5rem;
        text-transform: uppercase;
        font-weight: $--font-bold;
      }
    }
  }
}
</style>
