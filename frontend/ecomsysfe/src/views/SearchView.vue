<template>
  <default-layout>
    <div class="body">
      <div class="side-filter">
        <search-bar />
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

export default defineComponent({
  name: 'SearchView',
  components: {
    DefaultLayout,
    SearchBar,
    GridLayout,
    ProductItem,
  },
});
</script>

<style lang="scss" scoped>
.body {
  margin: auto;
  display: flex;
  min-height: 100vh;
  max-width: 1360px;
  padding: 0 20px;
  .side-filter {
    margin: 64px 0 40px;
    padding-right: 60px;
    max-width: 330px;
  }
  .list-products {
    padding: 85px 105px;
  }
}
</style>
