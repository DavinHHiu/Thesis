<template>
  <div class="tab-wp flex">
    <div
      v-for="(item, index) in tabs"
      class="tab-item"
      :class="{ active: activeTab(item) }"
      v-text="item.title"
      @click="changeTab(index)"
    />
  </div>
</template>

<script lang="ts">
import { TabItem } from "@/types/backoffice";
import _ from "lodash";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "TabLayout",
  props: {
    curPathName: {
      type: String,
      required: false,
    },
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
    },
    activeTab(item: TabItem) {
      return this.$router.currentRoute.value.path.includes(item.path as string);
    },
  },
  watch: {
    curPathName() {
      const index = _.findIndex(
        this.tabs,
        (tab) => tab.name === this.curPathName
      );
      this.currentIndex = index !== -1 ? index : 0;
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
