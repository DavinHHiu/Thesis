<template>
  <div class="tab-wp flex">
    <div
      v-for="(item, index) in tabs"
      class="tab-item"
      :class="{ active: index === currentIndex }"
      v-text="item.title"
      @click="changeTab(index)"
    />
  </div>
</template>

<script lang="ts">
import { TabItem } from "@/types/backoffice";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "TabLayout",
  props: {
    tabs: {
      type: Array as PropType<TabItem[]>,
      required: true,
    },
  },
  data() {
    return {
      currentIndex: 0,
    };
  },
  methods: {
    changeTab(index: number): void {
      this.currentIndex = index;
      this.$emit("change:tab", index);
      console.log(this.$router.currentRoute._value);
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.tab-wp {
  margin: 2rem 0;
  border-bottom: 1px solid $--gray-color-200;
  .tab-item {
    padding: 1.5rem 1rem;
    min-width: 10rem;
    user-select: none;
    text-align: center;
    cursor: pointer;
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
