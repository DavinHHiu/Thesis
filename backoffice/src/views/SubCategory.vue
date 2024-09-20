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
            <td>{{ index + 1 }}</td>
            <td v-text="subcategory.name" />
            <td v-text="subcategory.category.name" />
            <td v-text="subcategory.description" />
            <td class="action-wrap">
              <ellipsis-dropdown
                @action="handleActions"
                :current-index="index"
                :dropdown-list="[
                  { title: 'Update', action: '' },
                  { title: 'Delete', action: '#deleteModal' },
                ]"
              />
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </page-body>
  <modal id="deleteModal" title="Delete attribute" @confirm="submitAction">
    <span v-text="$t('subcategoryPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import { useSubCategoryStore } from "@/stores/subcategory";
import { SubCategory } from "@/types/worker";
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
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useSubCategoryStore, [
      "listByCategory",
      "destroySubCategory",
    ]),
    handleActions(obj: any) {
      const subcategory = this.subcategories[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "subcategory.update",
          params: { subcategoryId: subcategory.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const subcategory = this.subcategories[
          this.currentIndex
        ] as SubCategory;
        if (subcategory.id) {
          this.destroySubCategory(subcategory.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useSubCategoryStore, ["subcategories"]),
  },
  async mounted() {
    const category_id = this.$router.currentRoute.value.params.categoryId;
    await this.listByCategory(Number(category_id));
  },
});
</script>
