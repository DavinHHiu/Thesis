<template>
  <ul class="pagination flex justify-end gap-[0.5rem] w-full mt-[5rem]">
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
@import "@/assets/scss/variables";

.pagination {
  .page-item {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.4rem;
    background-color: $--white;
    width: 4rem;
    height: 4rem;
    transition: all 0.3s ease-out;
    cursor: pointer;
    .page-link {
      color: $--text-color;
      font-size: $--font-base;
      font-weight: $--font-semibold;
    }
    &:hover {
      background-color: $--primary;
      .page-link {
        color: $--white;
      }
    }
  }
  .active {
    background-color: $--primary;
    .page-link {
      color: $--white;
    }
  }
}
</style>
