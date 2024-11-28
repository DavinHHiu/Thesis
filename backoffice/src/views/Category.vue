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
                  { title: 'Detail', action: '' },
                  { title: 'Delete', action: '#deleteModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <modal id="deleteModal" title="Delete category" @confirm="submitAction">
    <span v-t="'categoryPage.modalDelete.title'" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useCategoryStore } from "@/stores/category";
import { Category } from "@/types/worker";
import { fmt } from "@/utils/string";
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
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useCategoryStore, ["listCategories", "destroyCategory"]),
    handleActions(obj: any) {
      const category = this.categories[obj.currentIndex];
      if (obj.action === "Detail") {
        this.$router.push({
          name: "category.update",
          params: { categoryId: category.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const category = this.categories[this.currentIndex] as Category;
        if (category.id) {
          this.destroyCategory(category.id);
        }
      }
    },
    fmt,
  },
  computed: {
    ...mapState(useCategoryStore, ["categories"]),
  },
  async mounted() {
    await this.listCategories();
  },
});
</script>
