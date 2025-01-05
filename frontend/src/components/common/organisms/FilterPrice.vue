<template>
  <div class="filter-price-wp">
    <h2 class="section-title mb-[2rem]" v-t="'searchPage.filter.title'" />
    <div class="filter-by-price-wp w-full">
      <div class="price-input flex justify-center mb-[2rem]">
        <div class="field flex items-center gap-[1rem]">
          <span v-t="'searchPage.filter.min'" />
          <number-field
            ref="inputMin"
            :value="minPrice"
            @input="handleChangeMin"
          />
        </div>
        <div class="separator flex items-center justify-center">-</div>
        <div class="field flex items-center gap-[1rem]">
          <span v-t="'searchPage.filter.max'" />
          <number-field
            ref="inputMax"
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
          class="range-min"
          :min="min"
          :max="max"
          :value="minPrice"
          @input="handleChangeMin"
        />
        <range-field
          ref="rangeMax"
          class="range-max"
          :min="min"
          :max="max"
          :value="maxPrice"
          @input="handleChangeMax"
        />
      </div>
    </div>
    <div
      class="filter-price-action mt-[25px] flex items-center justify-between"
    >
      <div class="filter-price-value w-full flex justify-end">
        <span class="block">
          <span v-t="'searchPage.filter.price'" />:
          <span class="price-value" v-text="`${minPrice}$ - ${maxPrice}$`" />
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import NumberField from "@/components/common/molecules/NumberField.vue";
import RangeField from "@/components/common/molecules/RangeField.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "FilterPrice",
  emits: ["update:min", "update:max"],
  components: {
    NumberField,
    RangeField,
    CustomButton,
  },
  props: {
    min: {
      type: Number,
      default: 0,
    },
    max: {
      type: Number,
      default: 500,
    },
  },
  data() {
    return {
      minPrice: this.min,
      maxPrice: this.max,
      progressLeft: "0%",
      progressRight: "0%",
      priceGap: 20,
    };
  },
  methods: {
    handleChangeMin(e: any) {
      let minPrice = 0;
      if (e.target.type === "number") {
        minPrice =
          !e.target.value && e.target.value === ""
            ? this.minPrice
            : parseInt(e.target.value);
      } else {
        minPrice = parseInt(this.rangeMin.getInputRef().value);
      }
      this.maxPrice = parseInt(this.rangeMax.getInputRef().value);
      if (this.maxPrice - minPrice < this.priceGap) {
        minPrice = this.maxPrice - this.priceGap;
      }
      minPrice = Math.max(minPrice, this.min);
      this.rangeMin.getInputRef().value = this.minPrice = minPrice;
      this.progressLeft = (this.minPrice / this.max) * 100 + "%";
      this.$emit("update:min", { min: this.minPrice });
    },
    handleChangeMax(e: any) {
      let maxPrice = 0;
      if (e.target.type === "number") {
        maxPrice =
          !e.target.value && e.target.value === ""
            ? this.maxPrice
            : parseInt(e.target.value);
      } else {
        maxPrice = parseInt(this.rangeMax.getInputRef().value);
      }
      this.minPrice = parseInt(this.rangeMin.getInputRef().value);
      if (maxPrice - this.minPrice < this.priceGap) {
        maxPrice = this.minPrice + this.priceGap;
      }
      maxPrice = Math.min(maxPrice, this.max);
      this.rangeMax.getInputRef().value = this.maxPrice = maxPrice;
      this.progressRight = 100 - (this.maxPrice / this.max) * 100 + "%";
      this.$emit("update:max", { max: this.maxPrice });
    },
  },
  computed: {
    inputMin(): typeof NumberField {
      return this.$refs.inputMin as typeof NumberField;
    },
    inputMax(): typeof NumberField {
      return this.$refs.inputMax as typeof NumberField;
    },
    rangeMin(): typeof RangeField {
      return this.$refs.rangeMin as typeof RangeField;
    },
    rangeMax(): typeof RangeField {
      return this.$refs.rangeMax as typeof RangeField;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.filter-price-wp {
  .filter-by-price-wp {
    .price-input {
      margin-bottom: 2rem;
      .field {
        height: 4.5rem;
      }
      .separator {
        padding: 0 1rem;
        font-size: $--font-xl;
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
</style>
