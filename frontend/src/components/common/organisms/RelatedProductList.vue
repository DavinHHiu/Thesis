<template>
  <div class="wrapper mb-[3rem]">
    <div class="title flex justify-center">
      <span class="py-[0.5rem]">Related products</span>
    </div>
    <div class="product-list mt-[4rem] flex gap-[1rem]">
      <product-item v-for="item in products" :product="item" />
    </div>
  </div>
</template>

<script lang="ts">
import { useProductStore } from "@/stores/product";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

import ProductItem from "../molecules/ProductItem.vue";

export default defineComponent({
  name: "RelatedProductList",
  components: {
    ProductItem,
  },
  methods: {
    ...mapActions(useProductStore, ["listProducts"]),
  },
  computed: {
    ...mapState(useProductStore, ["products"]),
  },
  mounted() {
    this.listProducts({ limit: 4 });
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.wrapper {
  .title {
    font-size: $--font-3xl;
    span {
      position: relative;
      color: $--title-color-text;
      text-transform: uppercase;
      font-weight: $--font-semibold;
      &::after {
        content: "";
        position: absolute;
        display: block;
        width: 20%;
        bottom: -10%;
        left: 50%;
        transform: translateX(-50%);
        border-top: 2px solid $--primary-color;
      }
    }
  }
}
</style>
