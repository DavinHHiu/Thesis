<template>
  <div class="tab-wp flex">
    <div class="tab-item">User</div>
    <div class="tab-item active">Addresses</div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "TabLayout",
  data() {},
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.tab-wp {
  margin: 2rem 0;
  border-bottom: 1px solid $--gray-color-200;
  .tab-item {
    padding: 1.5rem 1rem;
    &.active {
      position: relative;
      &::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 0.3rem;
        background-color: black;
      }
    }
  }
}
</style>
