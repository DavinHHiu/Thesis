<template>
  <default-layout>
    <page-body class="content">
      <div class="product">
        <div class="product-image">
          <img
            src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2021/03/sports-shoe3.jpg"
            class="zoomImg"
          />
        </div>
        <div class="product-desc">
          <nav class="breadcrumb">
            <a href="">Home</a>&nbsp;/&nbsp;<a href="">Men</a>&nbsp;/&nbsp;DNK
            Yellow Shoes
          </nav>
          <span class="single-product-category mb-[16px] block"
            ><a href="" rel="tag">Men</a></span
          >
          <h1 class="product-title mb-[15px]">DNK Yellow Shoes</h1>
          <p class="price">
            <del aria-hidden="true" class="mr-[10px] text-slate-400"
              >$150.00</del
            >
            <span class="screen-reader-text">$120.00</span>
            <span class="ast-shipping-text">+ Free Shipping</span>
          </p>
          <div class="my-[16px]">
            <p>
              Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non
              mauris vitae erat consequat auctor eu in elit. Class aptent taciti
              sociosqu ad litora torquent per conubia nostra, per inceptos
              himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus
              condimentum sit amet a augue. Sed non neque elit sed.
            </p>
          </div>
          <div class="action-wrapper flex gap-[20px] mb-[20px]">
            <text-field inputType="number" class="input-quantity" />
            <custom-button class="btn-add" intent="primary"
              >ADD TO CART</custom-button
            >
          </div>
          <div class="product_meta border-t">
            <span class="posted_in block pt-[10px] mb-[20px]"
              >Category: <a href="">Men</a></span
            >
          </div>
        </div>
      </div>
      <div class="product-details-wrapper">
        <ul class="tabs">
          <li
            v-for="(x, index) in ['Description', 'Reviews (0)']"
            :key="index"
            :class="{ active: index === currentTabIndex }"
            @click="handleChangeTab(index)"
          >
            {{ x }}
          </li>
        </ul>
        <div class="product-details">
          <div class="pb-[20px]">
            <div>
              <h3 class="product-details-title font-bold">
                Product description
              </h3>
            </div>
            <div class="mb-[20px]">
              <p>
                Since it’s creation lorem ipsum dolor sit amet, consectetur
                adipisicing elit, sed do eiusmod tempor incididunt ut labore et
                dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                exercitation ullamco laboris nisi ut aliquip ex ea commodo
                consequat. Duis aute irure dolor in reprehenderit in voluptate
                velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
                sint occaecat cupidatat non proident, sunt in culpa qui officia
                deserunt mollit anim id est laborum.
              </p>
            </div>
            <div class="mt-[20px]">
              <div class="mb-[20px]">
                <p>
                  Duis aute irure dolor in reprehenderit in voluptate velit esse
                  cillum dolore eu fugiat nulla pariatur. Excepteur sint
                  occaecat cupidatat non proident.
                </p>
              </div>
            </div>
          </div>
          <div class="elementor-container elementor-column-gap-no flex">
            <div class="">
              <img
                src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-about-01.jpg"
              />
            </div>
            <div class="">
              <img
                src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-about-04.jpg"
              />
            </div>
          </div>
          <div class="elementor-container elementor-column-gap-no flex">
            <div class="image-widget-container">
              <img
                src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-about-02.jpg"
              />
            </div>
            <div class="elementor-widget-container">
              <div>
                <h3 class="elementor-widget-title">Ut enim ad minim</h3>
                <span class="elementor-widget-body"
                  >Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
                  do eiusmod tempor incididunt.</span
                >
              </div>
              <div>
                <h3 class="elementor-widget-title">Quis nostrud</h3>
                <span class="elementor-widget-body"
                  >Sed do eiusmod tempor incididunt ut labore.</span
                >
              </div>
              <div>
                <h3 class="elementor-widget-title">Duis aute irure</h3>
                <span class="elementor-widget-body"
                  >Dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                  tempor incididunt ut labore.</span
                >
              </div>
            </div>
          </div>
          <div class="elementor-container elementor-column-gap-no flex w-full">
            <div class="elementor-widget-container">
              <h3 class="elementor-widget-title">More about the product</h3>
              <span class="elementor-widget-body"
                >Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
                do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                Ut enim ad minim veniam, quis nostrud exercitation ullamco
                laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
                dolor in.</span
              >
            </div>
            <div class="image-widget-container">
              <img
                src="https://websitedemos.net/brandstore-02/wp-content/uploads/sites/150/2017/12/product-about-03.jpg"
              />
            </div>
          </div>
        </div>
      </div>
    </page-body>
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import TextField from '../components/common/molecules/TextField.vue';
import CustomButton from '../components/common/atomic/CustomButton.vue';
import PageBody from '../components/common/PageBody.vue';

export default defineComponent({
  name: 'ProductDetail',
  components: {
    DefaultLayout,
    TextField,
    CustomButton,
    PageBody,
  },
  data() {
    return {
      currentTabIndex: 0,
    };
  },
  methods: {
    handleChangeTab(index: Number) {
      this.currentTabIndex = index;
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.content {
  display: flex;
  flex-direction: column;
  padding: 6rem 0;
  .product {
    display: flex;
    width: 100%;
    padding: 0 2rem;
    justify-content: space-between;
    .product-image {
      width: 50%;
      .zoomImg {
        width: 100%;
        height: 100%;
      }
    }
    .product-desc {
      width: 46%;
      .single-product-category {
        font-size: $--font-base;
      }
      .product-title {
        font-size: $--font-4xl;
      }
      .breadcrumb {
        color: $--gray-color-900;
        margin-bottom: 1.5rem;
      }
      .price {
        font-size: $--font-2xl;
        font-weight: $--font-semibold;
      }
      .ast-shipping-text {
        font-size: $--font-base;
      }
      .action-wrapper {
        width: 100%;
        .input-quantity {
          width: 15%;
          height: 4rem;
        }
        .btn-add {
          width: 50%;
        }
      }
    }
  }
  .product-details-wrapper {
    width: 100%;
    padding: 3.2rem 2rem 0;
    margin-top: 3.2rem;
    .tabs {
      display: flex;
      border-top: 1px solid $--color-border;
      li {
        margin-right: 1.6rem;
        font-size: $--font-base;
        font-weight: $--font-bold;
        padding: 1.5rem 0;
        cursor: default;
      }
      .active {
        position: relative;
        &::before {
          position: absolute;
          top: 0;
          content: '';
          width: 100%;
          border-top: 3px solid $--black-color-800;
        }
      }
    }
    .product-details {
      padding: 5rem 0 7rem;
      .product-details-title {
        font-size: 2.6rem;
        margin-bottom: 2rem;
      }
      .image-widget-container {
        width: 50%;
        img {
          width: 100%;
          width: 100%;
        }
      }
      .elementor-widget-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 7rem 10rem 7rem;
        width: 50%;
        gap: 2rem;
        .elementor-widget-title {
          font-size: $--font-xl;
          font-weight: $--font-bold;
          line-height: 5rem;
        }
        .elementor-widget-body {
          font-size: $--font-base;
          line-height: 3rem;
        }
      }
    }
  }
}
</style>
