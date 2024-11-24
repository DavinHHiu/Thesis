<template>
  <div class="fitler-category-cont">
    <div class="filter-title">Categories</div>
    <div class="category-list flex flex-col">
      <div class="category-item flex justify-between text-black">
        <div class="category-name">Men</div>
        <div class="category-quantity">(243)</div>
      </div>
      <div class="category-item flex justify-between font-base">
        <div class="category-name">Woman</div>
        <div class="category-quantity">(1423)</div>
      </div>
      <div class="category-item flex justify-between font-base">
        <div class="category-name">Children</div>
        <div class="category-quantity">(134)</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import TopItem from "@/components/common/molecules/TopItem.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SideBestSellers",
  components: {
    TopItem,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.fitler-category-cont {
  .category-list {
    gap: 2rem;
    font-size: $--font-base;
  }
}
.filter-title {
  font-size: $--font-xl;
  font-weight: $--font-semibold;
  margin-bottom: 2rem;
}
</style>
