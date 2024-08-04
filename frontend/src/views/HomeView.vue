<template>
  <default-layout class="w-screen" headerIntent="second">
    <div class="main-bg-wp">
      <main-background
        class="mt-[-103px]"
        bgImgUrl="'/images/1.jpg'"
        gradientColor="#f7b5ca"
      >
        <div class="bg-content bg-content-left">
          <div class="content">
            <h1 class="title">Super Offers For<br />Hot Summer!</h1>
            <span class="desc">20% Off On All Products</span>
            <div class="btn-wp">
              <custom-button class="btn" intent="second"
                >SHOP NOW</custom-button
              >
              <custom-button class="btn" intent="outlineSecond"
                >FIND MORE</custom-button
              >
            </div>
          </div>
        </div>
      </main-background>
    </div>
    <div class="wrapper w-screen flex flex-col justify-center">
      <logo-slider />
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
      <div class="image-bg">
        <main-background bgImgUrl="/images/4.jpg" gradientColor="#f58700" />
      </div>
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
        <main-background bgImgUrl="'/images/6.jpg'" gradientColor="#54595f">
          <div class="bg-content bg-content-right">
            <div class="content">
              <h3>Limited Time Offer</h3>
              <h1 class="title">Special Edition</h1>
              <span
                >Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut
                elit tellus,<br />
                luctus nec ullamcorper mattis, pulvinar dapibus leo.</span
              >
              <h3>Buy This T-shirt At 20% Discount, Use Code OFF20</h3>
              <div class="btn-wp">
                <custom-button class="btn" intent="second"
                  >SHOP NOW</custom-button
                >
              </div>
            </div>
          </div>
        </main-background>
      </div>
      <page-body>
        <grid-layout>
          <criteria-item
            image-src="/icons/common/earth.svg"
            title="Worldwide Shipping"
            desc="It elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
          />
          <criteria-item
            image-src="/icons/common/mannerquin.svg"
            title="Best Quality"
            desc="It elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
          />
          <criteria-item
            image-src="/icons/common/tag.svg"
            title="Best Offers"
            desc="It elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
          />
          <criteria-item
            image-src="/icons/common/secure.svg"
            title="Secure Payments"
            desc="It elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
          />
        </grid-layout>
      </page-body>
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
import CustomButton from '../components/common/atomic/CustomButton.vue';
import LogoSlider from '../components/common/LogoSlider.vue';
import CriteriaItem from '../components/common/CriteriaItem.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    DefaultLayout,
    GridLayout,
    CategoryItem,
    MainBackground,
    PageBody,
    ProductItem,
    CustomButton,
    LogoSlider,
    CriteriaItem,
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

.bg-content {
  position: absolute;
  height: 100%;
  width: 65%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: $--second-color-text;
  z-index: 10;
  .content {
    .title {
      font-size: $--font-9xl;
      font-weight: $--font-bold;
      line-height: 1.5;
    }
    .desc {
      font-size: $--font-3xl;
      font-weight: $--font-semibold;
      line-height: 3;
    }
  }
}

.bg-content-right {
  width: 50%;
  right: 0;
  .content {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
  h3 {
    font-size: $--font-xl;
  }
  span {
    font-size: $--font-base;
    line-height: 1.5;
  }
}
.btn-wp {
  margin-top: 3rem;
  display: flex;
  align-items: center;
  width: 100%;
  gap: 2rem;
  .btn {
    padding: 1.5rem 3.5rem;
  }
}

.wrapper {
  background-color: $--second-color;
  position: relative;
  .categories-wp {
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
    margin: 6rem auto;
    margin-bottom: 10rem;
  }
  .image-bg {
    margin-top: 8rem;
    width: 100%;
    height: 100rem;
  }
}
</style>
