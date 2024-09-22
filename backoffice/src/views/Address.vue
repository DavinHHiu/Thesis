<template>
  <page-title :title="$t('addressPage.list.title')" />
  <page-body>
    <header-action :current-route="$t('addressPage.add.name')" />
    <table class="w-full mt-[2rem] overflow-hidden">
      <thead>
        <tr>
          <th>No.</th>
          <th>Title</th>
          <th>Address_1</th>
          <th>Address_2</th>
          <th>Zipcode</th>
          <th>Tel</th>
          <th>User</th>
        </tr>
      </thead>
      <tbody>
        <template v-for="(address, index) in addresses" :key="index">
          <tr :class="{ odd: index % 2 == 0 }">
            <td>{{ index + 1 }}</td>
            <td v-text="address.title" />
            <td v-text="address.address_1" />
            <td v-text="address.address_2" />
            <td v-text="address.zipcode" />
            <td v-text="address.tel" />
            <td>
              <div class="flex justify-center">
                <img
                  :src="address.user.avatar as string"
                  :alt="address.user.email"
                  class="w-[4rem] h-[4rem] rounded-full object-cover"
                />
              </div>
            </td>
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
    <span v-text="$t('addressPage.modalDelete.title')" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import EllipsisDropdown from "@/components/common/molecules/EllipsisDropdown.vue";
import HeaderAction from "@/components/common/molecules/HeaderAction.vue";
import Modal from "@/components/common/molecules/Modal.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useAddressStore } from "@/stores/address";
import { Address } from "@/types/worker";
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
  },
  data() {
    return {
      currentAction: "" as string,
      currentIndex: 0 as number,
    };
  },
  methods: {
    ...mapActions(useAddressStore, ["listAddresses", "destroyAddress"]),
    handleActions(obj: any) {
      const address = this.addresses[obj.currentIndex];
      if (obj.action === "Update") {
        this.$router.push({
          name: "address.update",
          params: { id: address.id },
        });
      }
      this.currentAction = obj.action;
      this.currentIndex = obj.currentIndex;
    },
    async submitAction() {
      const action = this.currentAction;
      if (action === "Delete") {
        const address = this.addresses[this.currentIndex] as Address;
        if (address.id) {
          this.destroyAddress(address.id);
        }
      }
    },
  },
  computed: {
    ...mapState(useAddressStore, ["addresses"]),
  },
  async mounted() {
    await this.listAddresses();
  },
});
</script>
