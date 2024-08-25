<template>
  <span
    class="material-symbols-outlined elipsis-dropdown"
    data-bs-toggle="dropdown"
    >more_vert</span
  >
  <ul class="dropdown-menu">
    <li
      class="dropdown-item"
      v-for="(x, index) in dropdownList"
      :key="index"
      v-t="x"
    ></li>
  </ul>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "EllipsisDropdown",
  props: {
    dropdownList: {
      type: Array,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
.elipsis-dropdown {
  font-size: $--font-base;
}
</style>
