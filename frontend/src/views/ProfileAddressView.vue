<template>
  <div class="address-form-cont">
    <h2 class="sub-title" v-t="'checkoutPage.subtitle.address'" />
    <div v-if="addresses.length > 0">
      <address-select
        :open-add-btn="!openAddressForm"
        @add:address="addAddress"
        @edit:address="editAddress"
      />
    </div>
    <div
      v-if="addresses.length === 0 || openAddressForm"
      class="bill-form flex flex-col gap-[4rem] mt-[4rem]"
    >
      <div>
        <select-field
          :label="'inputLabel.checkout.city'"
          :options="[
            { displayValue: 'Ha Noi', value: 'Ha Noi' },
            { displayValue: 'Hai Phong', value: 'Hai Phong' },
          ]"
          :value="address?.city"
          @update:model-value="(newValue) => (address.city = newValue)"
        />
      </div>
      <div>
        <select-field
          :label="'inputLabel.checkout.district'"
          :options="[
            { displayValue: 'Ba Dinh', value: 'Ba Dinh' },
            { displayValue: 'Tay Ho', value: 'Tay Ho' },
          ]"
          :value="address?.district"
          @update:model-value="(newValue) => (address.district = newValue)"
        />
      </div>
      <div>
        <select-field
          :label="'inputLabel.checkout.ward'"
          :options="[
            { displayValue: 'Phuc Xa', value: 'Phuc Xa' },
            { displayValue: 'Quan Thanh', value: 'Quan Thanh' },
          ]"
          :value="address?.ward"
          @update:model-value="(newValue) => (address.ward = newValue)"
        />
      </div>
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.address1'"
          :required="true"
          :value="address?.address_1"
          @update:model-value="(newValue) => (address.address_1 = newValue)"
        />
      </div>
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.address2'"
          :required="true"
          :value="address?.address_2 as string"
          @update:model-value="(newValue) => (address.address_2 = newValue)"
        />
      </div>
    </div>
  </div>
  <div
    v-if="addresses.length === 0 || openAddressForm"
    class="contact-form-cont"
  >
    <h2 class="sub-title" v-t="'checkoutPage.subtitle.contact'" />
    <div class="bill-form flex flex-col gap-[4rem] mt-[4rem]">
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.phone'"
          :required="true"
          :value="address?.tel"
          @update:model-value="(newValue) => (address.tel = newValue)"
        />
      </div>
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.representative'"
          :required="true"
          :value="address?.representative"
          @update:model-value="
            (newValue) => (address.representative = newValue)
          "
        />
      </div>
    </div>
    <div class="flex flex-col mt-[4rem]">
      <div class="flex w-full gap-[2rem] justify-end">
        <custom-button
          v-if="addresses.length > 0"
          class="btn w-1/2 py-[1.4rem] px-[2.8rem]"
          intent="p-outline"
          v-html="$t('buttonLabel.cancel')"
          @click="cancelAdd"
        />
        <custom-button
          class="btn w-1/2 py-[1.4rem] px-[2.8rem]"
          intent="primary"
          v-html="$t('buttonLabel.save')"
          @click="addNewAddress"
        />
      </div>
      <custom-button
        v-if="editing"
        class="btn w-full py-[1.4rem] px-[2.8rem]"
        intent="danger"
        data-bs-toggle="modal"
        data-bs-target="#deleteModal"
        v-html="$t('buttonLabel.delete')"
      />
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import Card from "@/components/common/molecules/Card.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import AddressSelect from "@/components/common/organisms/AddressSelect.vue";
import { useAddressStore } from "@/stores/address";
import { Address, isAddressValid, User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProfileAddressView",
  components: {
    AddressSelect,
    Card,
    CustomButton,
    SelectField,
    TextField,
  },
  data() {
    return {
      openAddressForm: false,
      editing: false,
    };
  },
  computed: {
    ...mapState(useAddressStore, ["addresses", "address"]),
  },
  methods: {
    ...mapActions(useAddressStore, [
      "setAddress",
      "listAddressesByUser",
      "createAddress",
    ]),
    addAddress() {
      this.setAddress({} as Address);
      this.openAddressForm = true;
    },
    editAddress(id: number) {
      const address = this.addresses.find((addr) => addr.id === id) as Address;
      this.setAddress(address);
      this.editing = true;
      this.openAddressForm = true;
    },
    async addNewAddress() {
      if (!this.address.user_id) {
        const user = localStore.get("user") as User;
        if (user && user.id) {
          this.address.user_id = user.id;
        }
      }
      if (isAddressValid(this.address)) {
        if (this.address.id) {
          const response = await this.updateAddress(this.address);
          if (response && response.status === 200) {
            this.openAddressForm = false;
          }
        } else {
          const response = await this.createAddress(this.address);
          if (response && response.status === 201) {
            this.openAddressForm = false;
          }
        }
      } else {
        alert("Please fill all the required fields");
      }
    },
    cancelAdd() {
      this.openAddressForm = false;
      this.editing = false;
      this.setAddress({} as Address);
    },
  },
  async mounted() {
    await this.listAddressesByUser();
  },
});
</script>
<style lang="scss" scoped>
@import "@/assets/variables";

.sub-title {
  padding: 2rem 0 1.4rem;
  margin-bottom: 2rem;
  border-bottom: 1px solid $--color-border;
}
</style>
