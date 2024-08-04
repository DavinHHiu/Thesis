<template>
  <default-layout>
    <div class="body">
      <div class="side-filter">
        <div class="search-input-wp">
          <search-bar class="search-input" />
        </div>
        <div class="filter-price-cont">
          <h2 class="filter-title">Filter by price</h2>
          <div class="filter-by-price-wp">
            <div class="price-input">
              <div class="field">
                <span>Min</span>
                <text-field
                  ref="inputMin"
                  type="number"
                  min="0"
                  max="10000"
                  class="input-min"
                  :value="minPrice"
                  @input="handleChangeMin"
                />
              </div>
              <div class="separator">-</div>
              <div class="field">
                <span>Max</span>
                <text-field
                  ref="inputMax"
                  type="number"
                  min="0"
                  max="10000"
                  class="input-max"
                  :value="maxPrice"
                  @input="handleChangeMax"
                />
              </div>
            </div>
            <div class="price-slider">
              <div
                class="progress"
                :style="{
                  left: progressLeft,
                  right: progressRight,
                }"
              ></div>
            </div>
            <div class="range-input">
              <range-field
                ref="rangeMin"
                type="range"
                class="range-min"
                min="0"
                max="10000"
                :value="minPrice"
                @input="handleChangeMin"
              />
              <range-field
                ref="rangeMax"
                type="range"
                class="range-max"
                min="0"
                max="10000"
                :value="maxPrice"
                @input="handleChangeMax"
              />
            </div>
          </div>
          <div
            class="filter-price-action mt-[25px] flex items-center justify-between"
          >
            <custom-button
              class="rounded-none px-[18px] uppercase"
              intent="primary"
              >Fitler</custom-button
            >
            <div class="filter-price-value">
              <span
                >Price:
                <span class="price-value"
                  >${{ this.minPrice }} - ${{ this.maxPrice }}</span
                ></span
              >
            </div>
          </div>
        </div>
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
        <div class="side-best-sellers"></div>
      </div>
      <div class="list-products">
        <grid-layout :columns="3" :gap="20">
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
  </default-layout>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DefaultLayout from '../layouts/DefaultLayout.vue';
import SearchBar from '../components/common/SearchBar.vue';
import GridLayout from '../layouts/GridLayout.vue';
import ProductItem from '../components/common/ProductItem.vue';
import TextField from '../components/common/molecules/TextField.vue';
import CustomButton from '../components/common/atomic/CustomButton.vue';
import RangeField from '../components/common/RangeField.vue';

export default defineComponent({
  name: 'SearchView',
  components: {
    DefaultLayout,
    SearchBar,
    GridLayout,
    ProductItem,
    TextField,
    CustomButton,
    RangeField,
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
  setup() {},
  methods: {
    handleChangeMin(e: any) {
      let minPrice = 0;
      if (e.target.classList.value === 'input-min') {
        minPrice =
          !e.target.value && e.target.value === ''
            ? 2500
            : parseInt(this.$refs.inputMin.getInputRef().value);
      } else {
        minPrice = parseInt(this.$refs.rangeMin.getInputRef().value);
      }
      this.maxPrice = parseInt(this.$refs.rangeMax.getInputRef().value);
      if (this.maxPrice - minPrice < this.priceGap) {
        minPrice = this.maxPrice - this.priceGap;
      }
      minPrice = Math.max(minPrice, e.target.min);
      this.$refs.rangeMin.getInputRef().value =
        this.$refs.inputMin.getInputRef().value =
        this.minPrice =
          minPrice;
      this.progressLeft = (this.minPrice / e.target.max) * 100 + '%';
    },
    handleChangeMax(e: any) {
      let maxPrice = 0;
      if (e.target.classList.value === 'input-max') {
        maxPrice =
          !e.target.value && e.target.value === ''
            ? 7500
            : parseInt(this.$refs.inputMax.getInputRef().value);
      } else {
        maxPrice = parseInt(this.$refs.rangeMax.getInputRef().value);
      }
      this.minPrice = parseInt(this.$refs.rangeMin.getInputRef().value);
      if (maxPrice - this.minPrice < this.priceGap) {
        maxPrice = this.minPrice + this.priceGap;
      }
      maxPrice = Math.min(maxPrice, e.target.max);
      this.$refs.rangeMax.getInputRef().value =
        this.$refs.inputMax.getInputRef().value =
        this.maxPrice =
          maxPrice;
      this.progressRight = 100 - (this.maxPrice / e.target.max) * 100 + '%';
    },
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
    padding-right: 6rem;
    max-width: 33rem;
    display: flex;
    flex-direction: column;
    gap: 5rem;
    .search-input-wp {
      height: 4.2rem;
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
}
</style>
