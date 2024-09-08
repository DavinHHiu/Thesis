<template>
  <div class="item-wp flex items-center gap-[1.5rem]">
    <div class="item-image">
      <img
        src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-w-jeans4-300x300.jpg"
        alt="Item Image"
      />
    </div>
    <div class="item-info flex-1">
      <p class="item-name">Basic Gray Jeans</p>
      <div class="item-price">
        <span>{{ 1 }}</span>
        <span>{{ ' x ' }}</span>
        <span>$150.000</span>
      </div>
    </div>
    <div class="item-actions">
      <span class="material-symbols-outlined"> cancel </span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CartFolderItem',
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.item-wp {
  padding: 2.2rem;
  .item-image {
    width: 6rem;
    height: 6rem;
  }
  .item-info {
    padding: 2rem;
    .item-name {
      font-weight: $--font-semibold;
      font-size: $--font-base;
      margin-bottom: 0.5rem;
    }
    .item-price {
      font-size: $--font-base;
    }
  }
  .item-actions {
    color: $--gray-color-300;
  }
}
</style>
