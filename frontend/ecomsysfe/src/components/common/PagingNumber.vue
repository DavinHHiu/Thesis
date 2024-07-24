<template>
  <ul class="pagination">
    <li class="page-item"><span class="page-link">&laquo;</span></li>
    <li class="page-item"><span class="page-link">&lsaquo;</span></li>
    <template v-for="(page, index) in paging" :key="index">
      <li :class="['page-item', { active: page === curPage }]">
        <span class="page-link">{{ page }}</span>
      </li>
    </template>
    <li class="page-item"><span class="page-link">&rsaquo;</span></li>
    <li class="page-item"><span class="page-link">&raquo;</span></li>
  </ul>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PagingNumber',
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
  methods: {},
});
</script>

<style scoped>
.pagination {
  display: flex;
  gap: 5px;
  width: 100%;
  justify-content: end;
  margin-top: 70px;
  .page-item {
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid #000;
    min-width: 40px;
    min-height: 40px;
    transition: all 0.3s ease-out;
    cursor: pointer;
    .page-link {
      color: #000;
      font-size: 16px;
      font-weight: 500;
    }
    &:hover {
      background-color: #000;
      .page-link {
        color: #fff;
      }
    }
  }
  .active {
    background-color: #000;
    .page-link {
      color: #fff;
    }
  }
}
</style>
