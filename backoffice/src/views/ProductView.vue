<template>
  <page-title title="Products" />
  <page-body>
    <div class="action-wrap flex justify-between">
      <custom-button intent="p-outline">
        <span class="material-symbols-outlined">filter_alt</span>
        Filter
      </custom-button>
      <custom-button :rounded="true">
        <span class="material-symbols-outlined">add</span>
        Add
      </custom-button>
    </div>

    <table class="w-full mt-[2rem] overflow-hidden">
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
        <template v-for="(index, x) in 16" :key="index">
          <tr :class="{ odd: index % 2 == 1 }">
            <td>{{ index }}</td>
            <td>Brown T-shirt</td>
            <td>15.00$</td>
            <td>22-08-2024</td>
            <td>Processing</td>
            <td class="action-wrap">
              <ellipsis-dropdown :dropdown-list="[]" />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
    <paging-number :paging="paging" :cur-page="curPage" />
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import Alert from "@/components/common/molecules/Alert.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { computePaging } from "@/utils/utils";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductView",
  components: {
    Card,
    CustomButton,
    PageBody,
    PagingNumber,
    PageTitle,
    Modal,
    Alert,
    EllipsisDropdown,
  },
  data() {
    return {
      curPage: 5,
    };
  },
  methods: {
    handleAction() {
      console.log("Action clicked");
    },
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
</style>
