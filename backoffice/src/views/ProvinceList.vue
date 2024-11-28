<template>
  <table class="w-full mt-[2rem] overflow-hidden">
    <thead>
      <tr>
        <th v-text="'Code'" />
        <th v-text="'Name'" />
        <th v-text="'Divistion type'" />
        <th v-text="'Codename'" />
        <th v-text="'Phone code'" />
        <th v-text="'Status'" />
      </tr>
    </thead>
    <tbody>
      <template v-for="(province, index) in provinces" :key="index">
        <tr :class="{ odd: !(index % 2) }">
          <td v-text="fmt(province.code)" />
          <td v-text="fmt(province.name)" />
          <td v-text="fmt(province.division_type)" />
          <td v-text="fmt(province.codename)" />
          <td v-text="fmt(province.phone_code)" />
          <td v-text="fmt(province.is_active)" />
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
import { Address, Province } from "@/types/worker";
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
    ...mapActions(useAddressStore, [
      "listAddresses",
      "destroyAddress",
      "listProvinces",
    ]),
    handleActions(obj: any) {
      const province = this.provinces[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "address.update",
          params: { id: province.code },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const province = this.provinces[this.currentIndex] as Province;
        if (province.code) {
          this.destroyAddress(province.code);
        }
      }
    },
    fmt,
  },
  computed: {
    ...mapState(useAddressStore, ["provinces"]),
  },
  async mounted() {
    await this.listProvinces();
  },
});
</script>
