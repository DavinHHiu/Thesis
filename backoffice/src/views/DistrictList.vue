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
      <template v-for="(district, index) in districts" :key="index">
        <tr :class="{ odd: !(index % 2) }">
          <td v-text="fmt(district.code)" />
          <td v-text="fmt(district.name)" />
          <td v-text="fmt(district.division_type)" />
          <td v-text="fmt(district.codename)" />
          <td v-text="fmt(district.province_code)" />
          <td v-text="fmt(district.is_active)" />
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
import { District, Province } from "@/types/worker";
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
      "listDistricts",
    ]),
    handleActions(obj: any) {
      const province = this.districts[obj.currentIndex];
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
        const district = this.districts[this.currentIndex] as District;
        if (district.code) {
          this.destroyAddress(district.code);
        }
      }
    },
    fmt,
  },
  computed: {
    ...mapState(useAddressStore, ["districts"]),
  },
  async mounted() {
    await this.listDistricts();
  },
});
</script>
