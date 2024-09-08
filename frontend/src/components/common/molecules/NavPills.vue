<template>
  <nav class="nav-pills-wp">
    <template v-for="(item, index) in items" :key="index">
      <nav-pill-item
        :title="item.title"
        :quantity="item.quantity"
        :active="index === current"
        @click="handleTab(index)"
      />
    </template>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import NavPillItem from './NavPillItem.vue';
import { NavPillItem as iNavPill } from '../../../types/common';

export default defineComponent({
  name: 'NavPills',
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
    handleTab(index: number) {
      this.current = index;
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
