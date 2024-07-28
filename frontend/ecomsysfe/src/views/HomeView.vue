<script lang="ts">
import { defineComponent } from 'vue';
import CategoryItem from '../components/common/CategoryItem.vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import ItemSlider from '../components/common/ItemSlider.vue';
import GridLayout from '../layouts/GridLayout.vue';
import MainBackground from '../components/common/MainBackground.vue';

export default defineComponent({
  name: 'HomeView',
  components: {
    DefaultLayout,
    GridLayout,
    CategoryItem,
    ItemSlider,
    MainBackground,
  },
  data() {
    return {
      slides: [
        { src: '/images/1.jpg' },
        { src: '/images/2.jpg' },
        { src: '/images/3.jpg' },
      ],
    };
  },
});
</script>

<template>
  <default-layout class="w-screen" headerIntent="transparent">
    <main-background class="mt-[-103px]" />
    <div class="wrapper w-screen flex justify-center">
      <div class="w-[75%] my-[70px]">
        <grid-layout class="w-full" :gap="20">
          <category-item
            v-for="(x, index) in 4"
            :key="index"
            :grid-columns="1"
            title="Deals for PC"
            class="p-10px"
          >
            <img
              class="image"
              src="https://images-na.ssl-images-amazon.com/images/G/01/AmazonExports/Events/2023/EBF23/Fuji_Desktop_Single_image_EBF_1x_v1._SY304_CB573698005_.jpg"
            />
          </category-item>
        </grid-layout>
        <grid-layout class="w-full mt-[20px]" :gap="20">
          <category-item
            v-for="(x, index) in 4"
            :key="index"
            :grid-columns="2"
            title="Shop deals in Fashion"
          >
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_BOTTOMS_1x._SY116_CB624172947_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_TOPS_1x._SY116_CB623353881_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_DRESSES_1x._SY116_CB623353881_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_DRESSES_1x._SY116_CB623353881_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
          </category-item>
        </grid-layout>
        <item-slider title="Best Sellers in Sports & Outdoors"></item-slider>
        <item-slider title="Best Sellers in Sports & Outdoors"></item-slider>
        <grid-layout class="w-full mt-[20px]" :gap="20">
          <category-item
            v-for="(x, index) in 4"
            :key="index"
            :grid-columns="2"
            title="Shop deals in Fashion"
          >
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_BOTTOMS_1x._SY116_CB624172947_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_TOPS_1x._SY116_CB623353881_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_DRESSES_1x._SY116_CB623353881_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
            <div>
              <img
                class="image1"
                src="https://images-na.ssl-images-amazon.com/images/G/01/AMAZON_FASHION/2022/SITE_FLIPS/SPR_22/GW/DQC/DQC_APR_TBYB_W_DRESSES_1x._SY116_CB623353881_.jpg"
              />
              <p class="subtitle">Quan ao</p>
            </div>
          </category-item>
        </grid-layout>
        <grid-layout class="w-full" :gap="20">
          <category-item
            v-for="(x, index) in 4"
            :key="index"
            :grid-columns="1"
            title="Deals for PC"
            class="p-10px"
          >
            <img
              class="image"
              src="https://images-na.ssl-images-amazon.com/images/G/01/AmazonExports/Events/2023/EBF23/Fuji_Desktop_Single_image_EBF_1x_v1._SY304_CB573698005_.jpg"
            />
          </category-item>
        </grid-layout>
      </div>
    </div>
  </default-layout>
</template>

<style lang="scss" scoped>
@import '@/assets/variables';

.wrapper {
  background-color: $--second-color;
  position: relative;
}
</style>
