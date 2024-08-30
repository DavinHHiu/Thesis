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
          <th>Description</th>
          <th>Create at</th>
          <th>Update at</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(category, index) in categories" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td v-text="category.name" />
            <td v-text="category.description" />
            <td v-text="category.created_at" />
            <td v-text="category.updated_at" />
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
  <modal id="deleteModal" title="Delete category" @confirm="submitAction">
    <span>Do you want to delete this category?</span>
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useCategory } from "@/stores/category";
import { Category } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CategoryView",
  components: {
    PageTitle,
    PageBody,
    CustomButton,
    EllipsisDropdown,
    Modal,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useCategory, ["listCategories", "destroyCategory"]),
    handleActions(obj: any) {
      const category = this.categories[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "category.update",
          params: { id: category.id },
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
  },
  computed: {
    ...mapState(useCategory, ["categories"]),
  },
  async mounted() {
    await this.listCategories();
  },
});
</script>
