<template>
  <page-title :title="$t('productAttributePage.list.title')" />
  <page-body>
    <header-action :current-route="$t('productAttributePage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Type</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(attribute, index) in productAttributes" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>{{ attribute.type }}</td>
            <td>{{ attribute.value }}</td>
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Update', action: 'update' },
                  { title: 'Delete', action: 'openModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <paging-number
    :paging="paging"
    :cur-page="currentPage"
    @change-page="changePage"
  />
  <modal
    ref="deleteModal"
    id="deleteModal"
    title="Delete attribute"
    @confirm="handleDelete"
  >
    <span v-text="$t('productAttributePage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductAttributeStore } from "@/stores/productAttribute";
import { ProductAttribute } from "@/types/worker";
import { getPaginationRange } from "@/utils/utils";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductAttributeView",
  components: {
    CustomButton,
    EllipsisDropdown,
    Modal,
    HeaderAction,
    PageBody,
    PageTitle,
    PagingNumber,
  },
  data() {
    return {
      currentIndex: 0 as number,
      resultsCount: 0,
      limit: 50,
      offset: 0,
      currentPage: 1,
    };
  },
  methods: {
    ...mapActions(useProductAttributeStore, [
      "listProductAttributes",
      "destroyProductAttribute",
    ]),
    handleActions(obj: any) {
      const attribute = this.productAttributes[obj.currentIndex];
      if (obj.action === "update") {
        this.$router.push({
          name: "product.attribute.update",
          params: { id: attribute.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    handleDelete() {
      const attribute = this.productAttributes[
        this.currentIndex
      ] as ProductAttribute;
      if (attribute.id) {
        this.destroyProductAttribute(attribute.id);
      }
    },
    async changePage(page: number) {
      this.currentPage = page;
      this.offset = (page - 1) * this.limit;
      this.loadingPage = true;
      const params = {
        limit: this.limit,
        offset: this.offset,
      };
      await this.listProductAttributes(params);
      this.loadingPage = false;
    },
  },
  computed: {
    ...mapState(useProductAttributeStore, ["productAttributes"]),
    paging() {
      return getPaginationRange(
        Math.floor(this.resultsCount / this.limit) + 1,
        this.currentPage,
        1
      );
    },
  },
  async mounted() {
    const params = {
      limit: this.limit,
      offset: this.offset,
    };
    const response = await this.listProductAttributes(params);
    this.resultsCount = response.count;
  },
});
</script>

<style lang="scss" scoped></style>
