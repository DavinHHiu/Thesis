<template>
  <default-layout>
    <div class="content">
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
            ><a href="" rel="tag" class="text-black text-base">Men</a></span
          >
          <h1 class="product_title entry-title text-black text-3xl mb-[15px]">
            DNK Yellow Shoes
          </h1>
          <p class="price text-2xl">
            <del aria-hidden="true" class="mr-[10px] text-slate-400"
              >$150.00</del
            >
            <span class="screen-reader-text font-semibold text-black"
              >$120.00</span
            >
            <span class="ast-shipping-text text-black text-base"
              >+ Free Shipping</span
            >
          </p>
          <div class="my-[16px] text-black text-base">
            <p>
              Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non
              mauris vitae erat consequat auctor eu in elit. Class aptent taciti
              sociosqu ad litora torquent per conubia nostra, per inceptos
              himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus
              condimentum sit amet a augue. Sed non neque elit sed.
            </p>
          </div>
          <div class="action-wrapper flex gap-[20px] mb-[20px]">
            <text-field
              type="number"
              class="input-quantity w-[60px] border py-[5px]"
              value="1"
              min="0"
            />
            <custom-button
              class="btn-add rounded-none min-w-[280px] px-[20px] py[10px]"
              intent="primary"
              >ADD TO CART</custom-button
            >
          </div>
          <div class="product_meta text-black border-t">
            <span class="posted_in block pt-[10px] mb-[20px] text-black"
              >Category: <a href="" rel="tag" class="text-black">Men</a></span
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
              <div class="">
                <h3 class="product-details-title font-bold">
                  Product description
                </h3>
              </div>
            </div>
            <div>
              <div class="text-black text-base mb-[20px]">
                <p>
                  Since it’s creation lorem ipsum dolor sit amet, consectetur
                  adipisicing elit, sed do eiusmod tempor incididunt ut labore
                  et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                  exercitation ullamco laboris nisi ut aliquip ex ea commodo
                  consequat. Duis aute irure dolor in reprehenderit in voluptate
                  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
                  sint occaecat cupidatat non proident, sunt in culpa qui
                  officia deserunt mollit anim id est laborum.
                </p>
              </div>
            </div>
            <div class="mt-[20px]">
              <div class="text-black text-base mb-[20px]">
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
    </div>
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import TextField from '../components/common/TextField.vue';
import CustomButton from '../components/common/CustomButton.vue';

export default defineComponent({
  name: 'ProductDetail',
  data() {
    return {
      currentTabIndex: 0,
    };
  },
  components: {
    DefaultLayout,
    TextField,
    CustomButton,
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
  margin: auto;
  width: 120rem;
  max-width: 100%;
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
      .breadcrumb {
        color: $--gray-color-900;
        margin-bottom: 1.5rem;
      }
      .input-quantity {
        padding: 0.5rem;
        text-align: center;
        transition: 0.2s linear;
        &:focus {
          border: 1px dotted $--black-color-800;
        }
      }
      .btn-add {
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
          color: $--primary-color-text;
          line-height: 3rem;
        }
      }
    }
  }
}
</style>
