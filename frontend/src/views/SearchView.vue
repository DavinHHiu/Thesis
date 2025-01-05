<template>
  <div class="body flex">
    <loadingPage v-if="loadingPage" />
    <div class="side-filter">
      <search-bar v-model="queryInput" @submit="submitSearch" />
      <filter-price
        @update:min="updateFilterPrice"
        @update:max="updateFilterPrice"
      />
      <side-best-sellers />
    </div>
    <div class="list-products">
      <LoadingContent v-if="loadingContent" />
      <div v-else>
        <grid-layout
          wrap="wrap"
          :row-gap="2"
          :column-gap="1"
          justify-conent="flex-start"
        >
          <product-item v-for="item in products" :product="item" />
        </grid-layout>
        <paging-number
          :paging="paging"
          :cur-page="currentPage"
          @change-page="changePage"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import NumberField from "@/components/common/molecules/NumberField.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import ProductItem from "@/components/common/molecules/ProductItem.vue";
import RangeField from "@/components/common/molecules/RangeField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import TopItem from "@/components/common/molecules/TopItem.vue";
import FilterPrice from "@/components/common/organisms/FilterPrice.vue";
import LoadingContent from "@/components/common/organisms/LoadingContent.vue";
import SearchBar from "@/components/common/organisms/SearchBar.vue";
import SideBestSellers from "@/components/common/organisms/SideBestSellers.vue";
import SideCategory from "@/components/common/organisms/SideCategory.vue";
import GridLayout from "@/layouts/GridLayout.vue";
import { useSearchStore } from "@/stores/search";
import { Product } from "@/types/worker";
import { readFileAsDataURL } from "@/utils/files";
import { getPaginationRange } from "@/utils/utils";
import { mapActions } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SearchView",
  components: {
    CustomButton,
    FilterPrice,
    GridLayout,
    NumberField,
    PagingNumber,
    ProductItem,
    RangeField,
    SearchBar,
    SideCategory,
    SideBestSellers,
    TextField,
    TopItem,
  },
  data() {
    return {
      queryInput: "" as String | File,
      filterPrice: {
        min: 0,
        max: 500,
      },
      products: [] as Product[],
      resultsCount: 0,
      limit: 50,
      offset: 0,
      currentPage: 1,
      loadingContent: false,
      loadingPage: false,
    };
  },
  computed: {
    paging() {
      return getPaginationRange(
        Math.floor(this.resultsCount / this.limit) + 1,
        this.currentPage,
        1
      );
    },
  },
  methods: {
    ...mapActions(useSearchStore, ["searchByImage", "searchByText"]),
    async search() {
      this.loadingContent = true;
      let queryPayload = {
        query:
          this.queryInput instanceof File
            ? await readFileAsDataURL(this.queryInput)
            : this.queryInput,
        filter_price: this.filterPrice,
      };

      const searchMethod =
        this.queryInput instanceof File
          ? this.searchByImage
          : this.searchByText;

      const response = await searchMethod(queryPayload, {
        limit: this.limit,
        offset: this.offset,
      });
      if (response && response.status == 200 && response.data) {
        this.products = response.data.results as Product[];
        this.resultsCount = response.data.count;
      }
      this.loadingContent = false;
      window.scrollTo({ top: 0 });
    },
    submitSearch() {
      this.currentPage = 1;
      this.offset = 0;
      this.search();
    },
    async changePage(page: number) {
      this.currentPage = page;
      this.offset = (page - 1) * this.limit;
      this.loadingPage = true;
      await this.search();
      this.loadingPage = false;
    },
    updateFilterPrice(newValue: Object) {
      this.filterPrice = { ...this.filterPrice, ...newValue };
    },
  },
  mounted() {
    this.search();
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
