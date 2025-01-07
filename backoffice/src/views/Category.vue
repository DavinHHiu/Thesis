<template>
  <page-title :title="$t('categoryPage.list.title')" />
  <page-body>
    <header-action :current-route="$t('categoryPage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Name</th>
          <th>Description</th>
          <th>Create at</th>
          <th>Update at</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(category, index) in categories" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td v-text="index + 1" />
            <td v-text="fmt(category.name)" />
            <td v-text="fmt(category.description)" />
            <td v-text="fmt(category.created_at)" />
            <td v-text="fmt(category.updated_at)" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Detail', action: 'detail' },
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
    <span v-t="'categoryPage.modalDelete.title'" />
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
import { useCategoryStore } from "@/stores/category";
import { Category } from "@/types/worker";
import { fmt } from "@/utils/string";
import { getPaginationRange } from "@/utils/utils";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CategoryView",
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
    ...mapActions(useCategoryStore, ["listCategories", "destroyCategory"]),
    handleActions(obj: any) {
      const category = this.categories[obj.currentIndex];
      if (obj.action === "detail") {
        this.$router.push({
          name: "category.update",
          params: { categoryId: category.id },
        });
      } else if (obj.action === "openModal") {
        const modal = this.$refs.deleteModal as InstanceType<typeof Modal>;
        modal.open();
      }
      this.currentIndex = obj.currentIndex;
    },
    handleDelete() {
      const category = this.categories[this.currentIndex] as Category;
      if (category.id) {
        this.destroyCategory(category.id);
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
      await this.listCategories(params);
      this.loadingPage = false;
    },
    fmt,
  },
  computed: {
    ...mapState(useCategoryStore, ["categories"]),
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
    const response = await this.listCategories(params);
    this.resultsCount = response.data.count;
  },
});
</script>
