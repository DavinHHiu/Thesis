<template>
  <ul class="pagination">
    <li class="page-item"><span class="page-link">&laquo;</span></li>
    <li class="page-item"><span class="page-link">&lsaquo;</span></li>
    <template v-for="(page, index) in paging" :key="index">
      <li
        :class="['page-item', { active: page === curPage }]"
        @click="changePage(page as any)"
      >
        <span class="page-link">{{ page }}</span>
      </li>
    </template>
    <li class="page-item"><span class="page-link">&rsaquo;</span></li>
    <li class="page-item"><span class="page-link">&raquo;</span></li>
  </ul>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PagingNumber",
  emits: ["change-page"],
  props: {
    paging: {
      type: Array,
      required: true,
    },
    curPage: {
      type: Number,
      default: 1,
    },
  },
  methods: {
    changePage(page: number | string) {
      if (typeof page === "string") return;
      this.$emit("change-page", page);
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.pagination {
  display: flex;
  gap: 0.5rem;
  width: 100%;
  justify-content: end;
  margin-top: 7rem;
  .page-item {
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid $--primary-color;
    min-width: 4rem;
    min-height: 4rem;
    transition: all 0.3s ease-out;
    cursor: pointer;
    .page-link {
      color: $--primary-color-text;
      font-size: $--font-base;
      font-weight: $--font-semibold;
    }
    &:hover {
      background-color: $--primary-color;
      .page-link {
        color: $--second-color-text;
      }
    }
  }
  .active {
    background-color: $--primary-color;
    .page-link {
      color: $--second-color-text;
    }
  }
}
</style>
