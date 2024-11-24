<template>
  <div class="body flex">
    <div class="side-filter">
      <search-bar />
      <filter-price />
      <side-category />
      <side-best-sellers />
    </div>
    <div class="list-products">
      <grid-layout wrap="wrap" :row-gap="2">
        <product-item v-for="item in products" :product="item" />
      </grid-layout>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import NumberField from "@/components/common/molecules/NumberField.vue";
import ProductItem from "@/components/common/molecules/ProductItem.vue";
import RangeField from "@/components/common/molecules/RangeField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import TopItem from "@/components/common/molecules/TopItem.vue";
import FilterPrice from "@/components/common/organisms/FilterPrice.vue";
import SearchBar from "@/components/common/organisms/SearchBar.vue";
import SideBestSellers from "@/components/common/organisms/SideBestSellers.vue";
import SideCategory from "@/components/common/organisms/SideCategory.vue";
import GridLayout from "@/layouts/GridLayout.vue";
import { useProductStore } from "@/stores/product";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SearchView",
  components: {
    CustomButton,
    FilterPrice,
    GridLayout,
    NumberField,
    ProductItem,
    RangeField,
    SearchBar,
    SideCategory,
    SideBestSellers,
    TextField,
    TopItem,
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions(useProductStore, ["listProducts"]),
  },
  computed: {
    ...mapState(useProductStore, ["products"]),
  },
  mounted() {
    this.listProducts();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";
.body {
  margin: auto;
  min-height: 100vh;
  max-width: 136rem;
  padding: 0 2rem;
  .side-filter {
    flex: 0.38;
    margin: 6.4rem 0 4rem;
    display: flex;
    flex-direction: column;
    gap: 5rem;
  }
  .list-products {
    flex: 1;
    padding: 8.5rem 0 8.5rem 10.5rem;
  }
}
</style>
