<template>
  <table class="w-full mt-[2rem] overflow-hidden">
    <thead>
      <tr>
        <th v-text="'Code'" />
        <th v-text="'Name'" />
        <th v-text="'Divistion type'" />
        <th v-text="'Codename'" />
        <th v-text="'Province code'" />
        <th v-text="'Status'" />
      </tr>
    </thead>
    <tbody>
      <template v-for="(ward, index) in wards" :key="index">
        <tr :class="{ odd: !(index % 2) }">
          <td v-text="fmt(ward.code)" />
          <td v-text="fmt(ward.name)" />
          <td v-text="fmt(ward.division_type)" />
          <td v-text="fmt(ward.codename)" />
          <td v-text="fmt(ward.district_code)" />
          <td v-text="fmt(ward.is_active)" />
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
  <modal id="deleteModal" title="Delete attribute" @confirm="submitAction">
    <span v-text="$t('productPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import TabLayout from "@/components/common/molecules/TabLayout.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useAddressStore } from "@/stores/address";
import { TabItem } from "@/types/backoffice";
import { Ward } from "@/types/worker";
import { fmt } from "@/utils/string";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "AddressView",
  components: {
    CustomButton,
    EllipsisDropdown,
    HeaderAction,
    Modal,
    PageTitle,
    PageBody,
    TabLayout,
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
      tabs: [
        { title: "User", name: "user.update", path: "update" },
        { title: "Orders", name: "user.order.list", path: "order" },
      ] as TabItem[],
    };
  },
  methods: {
    ...mapActions(useAddressStore, ["listWards"]),
    handleActions(obj: any) {
      const ward = this.wards[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "address.update",
          params: { id: ward.code },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const ward = this.wards[this.currentIndex] as Ward;
        if (ward.code) {
          this.destroyAddress(ward.code);
        }
      }
    },
    fmt,
  },
  computed: {
    ...mapState(useAddressStore, ["wards"]),
  },
  async mounted() {
    await this.listWards();
  },
});
</script>
