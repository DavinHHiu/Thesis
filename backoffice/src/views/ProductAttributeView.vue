<template>
  <page-title title="Product Attributes" />
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
          <th>Type</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(attribute, index) in attributes" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td>{{ attribute.type }}</td>
            <td>{{ attribute.value }}</td>
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
    <span>Do you want to delete this attribute?</span>
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useProductAttributeStore } from "@/stores/useProductAttributeStore";
import { ProductAttribute } from "@/types/backoffice";
import { mapActions } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductAttributeView",
  components: {
    CustomButton,
    PageTitle,
    PageBody,
    EllipsisDropdown,
    Modal,
  },
  data() {
    return {
      attributes: [] as ProductAttribute[],
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useProductAttributeStore, [
      "listProductAttributes",
      "destroyProductAttribute",
    ]),
    handleActions(obj: any) {
      const attribute = this.attributes[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "product.attributes.update",
          params: { id: attribute.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const attribute = this.attributes[
          this.currentIndex
        ] as ProductAttribute;
        if (attribute.id) {
          const response = await this.destroyProductAttribute(attribute.id);
          if (response && response.status === 204) {
            this.attributes.splice(this.currentIndex, 1);
          }
        }
      }
    },
  },
  async mounted() {
    const response = await this.listProductAttributes();
    if (response && response.status === 200) {
      this.attributes = response.data;
    }
  },
});
</script>

<style lang="scss" scoped></style>
