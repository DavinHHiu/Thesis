<template>
  <nav class="nav-pills-wp">
    <template v-for="(item, index) in items" :key="index">
      <nav-pill-item
        :title="item.title"
        :quantity="item.quantity"
        :active="index === current"
        @click="changeTab(index)"
      />
    </template>
  </nav>
</template>

<script lang="ts">
import NavPillItem from "@/components/common/molecules/NavPillItem.vue";
import { NavPillItem as iNavPill } from "@/types/common";
import { defineComponent } from "vue";

export default defineComponent({
  name: "NavPills",
  emits: ["update:changeStatus"],
  props: {
    items: {
      type: Array as () => iNavPill[],
      required: true,
    },
  },
  components: {
    NavPillItem,
  },
  data() {
    return {
      current: 0,
    };
  },
  methods: {
    changeTab(index: number) {
      this.current = index;
      this.$emit("update:changeStatus", this.items[index]);
    },
  },
});
</script>

<style scoped>
.nav-pills-wp {
  width: 100%;
  display: flex;
  gap: 0.5rem;
}
</style>
