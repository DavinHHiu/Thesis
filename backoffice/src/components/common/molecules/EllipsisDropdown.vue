<template>
  <span
    class="material-symbols-outlined elipsis-dropdown"
    data-bs-toggle="dropdown"
    >more_vert</span
  >
  <ul class="dropdown-menu">
    <li
      v-for="(x, index) in dropdownList"
      class="dropdown-item"
      @click="$emit('action', { action: x.title, currentIndex })"
      data-bs-toggle="modal"
      :data-bs-target="x.action"
      :key="index"
      v-t="x.title"
    ></li>
  </ul>
</template>

<script lang="ts">
import { DropdownItems } from "@/types/backoffice";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "EllipsisDropdown",
  emits: ["action"],
  props: {
    dropdownList: {
      type: Array as PropType<DropdownItems[]>,
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
