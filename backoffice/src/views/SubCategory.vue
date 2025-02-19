<template>
  <page-body>
    <header-action :current-route="$t('subcategoryPage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Name</th>
          <th>Category</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(subcategory, index) in subcategories" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td v-text="index + 1" />
            <td v-text="fmt(subcategory.name)" />
            <td v-text="fmt(subcategory.category_id)" />
            <td v-text="fmt(subcategory.description)" />
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
    <span v-t="'subcategoryPage.modalDelete.title'" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PagingNumber from "@/components/common/molecules/PagingNumber.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import { useSubCategoryStore } from "@/stores/subcategory";
import { SubCategory } from "@/types/worker";
import { fmt } from "@/utils/string";
import { getPaginationRange } from "@/utils/utils";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "SubCategoryView",
  components: {
    CustomButton,
    EllipsisDropdown,
    Modal,
    HeaderAction,
    PageBody,
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
    ...mapActions(useSubCategoryStore, [
      "listByCategory",
      "destroySubCategory",
    ]),
    handleActions(obj: any) {
      const subcategory = this.subcategories[obj.currentIndex];
      if (obj.action === "update") {
        this.$router.push({
          name: "subcategory.update",
          params: { subcategoryId: subcategory.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    async handleDelete() {
      const subcategory = this.subcategories[this.currentIndex] as SubCategory;
      if (subcategory.id) {
        this.destroySubCategory(subcategory.id);
      }
    },
    async changePage(page: number) {
      this.currentPage = page;
      this.offset = (page - 1) * this.limit;
      this.loadingPage = true;
      const params = {
        limit: this.limit,
        offset: this.offset,
        category_id: Number(this.$route.params.categoryId),
      };
      await this.listByCategory(params);
      this.loadingPage = false;
    },
    fmt,
  },
  computed: {
    ...mapState(useSubCategoryStore, ["subcategories"]),
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
      category_id: Number(this.$route.params.categoryId),
    };
    const response = await this.listByCategory(params);
    this.resultsCount = response.data.count;
  },
});
</script>
