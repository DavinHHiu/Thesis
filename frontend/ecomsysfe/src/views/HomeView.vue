<template>
  <default-layout class="w-screen" headerIntent="transparent">
    <div class="main-bg-wp">
      <main-background class="mt-[-103px]" bgImgUrl="'/images/1.jpg'" />
    </div>
    <div class="wrapper w-screen flex flex-col justify-center">
      <page-body>
        <div class="categories-wp">
          <grid-layout class="w-full">
            <category-item
              v-for="(x, index) in slides"
              :key="index"
              :title="x.title"
              class="p-10px"
            >
              <img class="bg-image" :src="x.src" />
            </category-item>
          </grid-layout>
        </div>
      </page-body>
      <div class="list-products">
        <div class="products-title-wp">
          <h1 class="products-title">Featured Products</h1>
        </div>
        <grid-layout wrap="wrap">
          <product-item />
          <product-item />
          <product-item />
          <product-item />
          <product-item />
          <product-item />
          <product-item />
          <product-item />
          <product-item />
          <product-item />
        </grid-layout>
      </div>
      <div class="image-model">
        <main-background bgImgUrl="'/images/5.jpg'" />
      </div>
    </div>
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CategoryItem from '../components/common/CategoryItem.vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import GridLayout from '../layouts/GridLayout.vue';
import MainBackground from '../components/common/MainBackground.vue';
import PageBody from '../components/common/PageBody.vue';
import ProductItem from '../components/common/ProductItem.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    DefaultLayout,
    GridLayout,
    CategoryItem,
    MainBackground,
    PageBody,
    ProductItem,
  },
  data() {
    return {
      slides: [
        { title: '20% Off On Tank Tops', src: '/images/categories/2.jpg' },
        { title: 'Latest Eyewear For You', src: '/images/categories/3.jpg' },
        { title: "Let's Lorem Suit Up!", src: '/images/categories/4.jpg' },
      ],
    };
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.main-bg-wp {
  height: 47vw;
}

.wrapper {
  background-color: $--second-color;
  position: relative;
  .categories-wp {
    margin-top: 10rem;
    display: flex;
    justify-content: center;
    .bg-image {
      height: 100%;
      width: 100%;
      object-fit: cover;
      object-position: top;
    }
  }
  .list-products {
    margin: 5rem auto;
    .products-title-wp {
      width: 100%;
      padding: 5rem;
      text-align: center;
      .products-title {
        position: relative;
        line-height: 1;
        padding: 3rem 0;
        font-size: $--font-6xl;
        font-weight: $--font-bold;
        &::after {
          content: '';
          position: absolute;
          bottom: 0;
          right: 50%;
          width: 10rem;
          border-bottom: 2px solid $--primary-color;
          transform: translateX(50%);
        }
      }
    }
  }
  .image-model {
    width: 75%;
    height: 50rem;
    margin: 0 auto;
  }
}
</style>
