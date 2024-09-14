<template>
  <div class="body">
    <div class="side-filter">
      <search-bar />
      <filter-price />
      <div class="fitler-category-cont">
        <div class="filter-title">Categories</div>
        <div class="category-list">
          <div class="category-item flex justify-between text-black">
            <div class="category-name">Book</div>
            <div class="category-quantity">(243)</div>
          </div>
          <div class="category-item flex justify-between font-base">
            <div class="category-name">Cloth</div>
            <div class="category-quantity">(1423)</div>
          </div>
          <div class="category-item flex justify-between font-base">
            <div class="category-name">PC</div>
            <div class="category-quantity">(134)</div>
          </div>
        </div>
      </div>
      <div class="side-best-sellers">
        <h2>Our Best Sellers</h2>
        <ul>
          <li><top-item /></li>
          <li><top-item /></li>
          <li><top-item /></li>
          <li><top-item /></li>
          <li><top-item /></li>
        </ul>
      </div>
    </div>
    <div class="list-products">
      <grid-layout wrap="wrap" align="start">
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
        <product-item />
      </grid-layout>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SearchBar from '../components/common/organisms/SearchBar.vue';
import GridLayout from '../layouts/GridLayout.vue';
import ProductItem from '../components/common/molecules/ProductItem.vue';
import TextField from '../components/common/molecules/TextField.vue';
import CustomButton from '../components/common/atomic/CustomButton.vue';
import RangeField from '../components/common/molecules/RangeField.vue';
import TopItem from '@/components/common/molecules/TopItem.vue';
import NumberField from '@/components/common/molecules/NumberField.vue';
import FilterPrice from '@/components/common/organisms/FilterPrice.vue';

export default defineComponent({
  name: 'SearchView',
  components: {
    CustomButton,
    FilterPrice,
    GridLayout,
    NumberField,
    ProductItem,
    RangeField,
    SearchBar,
    TextField,
    TopItem,
  },
  data() {
    return {
      minPrice: 2500,
      maxPrice: 7500,
      progressLeft: '25%',
      progressRight: '25%',
      priceGap: 1000,
    };
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';
.body {
  margin: auto;
  display: flex;
  min-height: 100vh;
  max-width: 136rem;
  padding: 0 2rem;
  .side-filter {
    margin: 6.4rem 0 4rem;
    width: 50rem;
    display: flex;
    flex-direction: column;
    gap: 5rem;
    .search-input-wp {
      height: 5rem;
      width: 100%;
    }
    .filter-price-cont {
      .filter-by-price-wp {
        width: 100%;
        .price-input {
          width: 100%;
          display: flex;
          justify-content: space-between;
          margin-bottom: 2rem;
          .field {
            height: 4.5rem;
            display: flex;
            align-items: center;

            input {
              width: 100%;
              height: 100%;
              margin-left: 1.2rem;
              -moz-appearance: textfield;
            }
            input[type='number']::-webkit-outer-spin-button,
            input[type='number']::-webkit-inner-spin-button {
              -webkit-appearance: none;
            }
          }
          .separator {
            display: flex;
            padding: 0 1rem;
            font-size: 2rem;
            align-items: center;
            justify-content: center;
          }
        }
        .price-slider {
          position: relative;
          height: 0.3rem;
          border-radius: 0.3rem;
          background-color: $--gray-color-300;

          .progress {
            position: absolute;
            height: 0.3rem;
            border-radius: 0.3rem;
            left: 25%;
            right: 25%;
            background-color: $--primary-color;
          }
        }

        .range-input {
          position: relative;
          input {
            position: absolute;
            top: -0.3rem;
            padding: 0 0;
            height: 0.3rem;
            width: 100%;
            pointer-events: none;
            background: none;
            border: none;
            -webkit-appearance: none;
          }
          input[type='range']::-webkit-slider-thumb {
            -webkit-appearance: none;
            height: 1.7rem;
            width: 1.7rem;
            pointer-events: auto;
            background-color: $--primary-color;
            border-radius: 50%;
          }
          input[type='range']::-moz-slider-thumb {
            -moz-appearance: none;
            height: 1.7rem;
            width: 1.7rem;
            pointer-events: auto;
            background-color: $--primary-color;
            border-radius: 50%;
          }
        }
      }
      .filter-price-action {
        .filter-price-value {
          .price-value {
            font-weight: $--font-semibold;
            color: $--primary-color-text;
          }
        }
      }
    }
    .fitler-category-cont {
      .category-list {
        display: flex;
        flex-direction: column;
        gap: 2rem;
        font-size: $--font-base;
      }
    }
    .filter-title {
      font-size: $--font-xl;
      font-weight: $--font-semibold;
      margin-bottom: 2rem;
    }
  }
  .list-products {
    padding: 8.5rem 10.5rem;
  }
  .side-best-sellers {
    li {
      border-bottom: 1px solid $--color-border;
    }
    li:last-child {
      border-bottom: none;
    }
  }
}
</style>
