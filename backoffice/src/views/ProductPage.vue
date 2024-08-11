<template>
  <main-layout>
    <page-title title="Product page" />
    <page-body>
      <div class="action-wrap flex justify-between">
        <custom-button intent="p-outline">
          <span class="material-icons">filter_alt</span>
          Filter
        </custom-button>
        <custom-button :rounded="true">
          <span class="material-icons">add</span>
          Add
        </custom-button>
      </div>

      <table class="w-full mt-[2rem]">
        <thead>
          <tr>
            <th>No.</th>
            <th>Name</th>
            <th>Price</th>
            <th>Delivery date</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(index, x) in 7" :key="index">
            <tr :class="{ odd: index % 2 == 1 }">
              <td>{{ index }}</td>
              <td>Brown T-shirt</td>
              <td>15.00$</td>
              <td>22-08-2024</td>
              <td>Processing</td>
            </tr>
          </template>
        </tbody>
      </table>
      <paging-number :paging="paging" :cur-page="curPage" />
    </page-body>
  </main-layout>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import MainLayout from "@/layouts/MainLayout.vue";
import { computePaging } from "@/utils/utils";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductPage",
  components: {
    Card,
    CustomButton,
    MainLayout,
    PageBody,
    PagingNumber,
    PageTitle,
  },
  data() {
    return {
      curPage: 5,
    };
  },
  computed: {
    paging() {
      return computePaging(10, 7, this.curPage, 1);
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

table {
  background-color: $--white;
  border-radius: 0.4rem;
  overflow: hidden;

  th,
  td {
    padding: 2rem 1rem;
  }

  .odd {
    background-color: $--gray-color-200;
  }

  tbody {
    tr {
      transition: 0.2s ease-out;

      &:hover {
        cursor: pointer;
        color: $--white;
        background-color: $--dark-gray;
      }
    }
    td {
      text-align: center;
      border-top: 1px solid $--gray-color-400;
    }
  }
}
</style>
