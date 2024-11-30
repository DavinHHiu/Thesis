<template>
  <span
    class="material-symbols-outlined elipsis-dropdown"
    data-bs-toggle="dropdown"
    v-text="'more_vert'"
  />
  <ul class="dropdown-menu">
    <li
      v-for="(x, index) in dropdownList"
      class="dropdown-item"
      @click="$emit('action', { action: x.action, currentIndex })"
      :key="index"
      v-text="x.title"
    ></li>
  </ul>
</template>

<script lang="ts">
import { DropdownItem } from "@/types/backoffice";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "EllipsisDropdown",
  emits: ["action"],
  props: {
    dropdownList: {
      type: Array as PropType<DropdownItem[]>,
      required: true,
    },
    currentIndex: {
      type: Number,
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
