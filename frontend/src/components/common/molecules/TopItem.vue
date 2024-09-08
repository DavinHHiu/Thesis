<template>
  <div class="item-wp">
    <a class="image-wp">
      <img
        src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-m-jeans2-300x300.jpg"
      />
    </a>
    <div class="item-info-wp flex flex-col justify-center">
      <a>
        <span>Dark Blue Denim Jeans</span>
      </a>
      <span class="star"></span>
      <span>$150.00</span>
    </div>
  </div>
</template>

<script lang="ts"></script>

<style lang="scss" scoped>
@import '@/assets/variables';

.item-wp {
  display: flex;
  padding: 1.2rem 0;
  margin-bottom: 0.5rem;
  gap: 1rem;
  .image-wp {
    display: block;
    width: 6rem;
    height: 6rem;
  }
  .item-info-wp {
    height: 100%;
    line-height: 1.2;
    font-size: $--font-base;
    .star {
      &::after {
        content: '\2606\2606\2606\2606\2606';
        font-size: $--font-2xl;
      }
    }
  }
}
</style>
