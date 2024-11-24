<template>
  <div class="side-best-sellers">
    <h2 class="section-title mb-[2rem]">Our Best Sellers</h2>
    <ul>
      <li v-for="product in topProducts"><top-item :product="product" /></li>
    </ul>
  </div>
</template>

<script lang="ts">
import TopItem from "@/components/common/molecules/TopItem.vue";
import { useProductStore } from "@/stores/product";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SideBestSellers",
  components: {
    TopItem,
  },
  methods: {
    ...mapActions(useProductStore, ["listProducts"]),
  },
  computed: {
    ...mapState(useProductStore, ["products"]),
    topProducts() {
      return _.take(this.products, 5);
    },
  },
  mounted() {
    this.listProducts();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.side-best-sellers {
  li {
    border-bottom: 1px solid $--color-border;
  }
  li:last-child {
    border-bottom: none;
  }
}
</style>
