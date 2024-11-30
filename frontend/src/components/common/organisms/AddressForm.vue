<template>
  <div class="address-form-cont">
    <h2 class="sub-title" v-t="'checkoutPage.subtitle.address'" />
    <loading-content v-if="loading" />
    <div v-if="!loading && addresses.length > 0">
      <address-select
        :open-add-btn="!openAddressForm"
        @add:address="addAddress"
        @edit:address="editAddress"
        @choose:address="chooseAddress"
      />
    </div>
    <div
      v-if="!loading && (addresses.length === 0 || openAddressForm)"
      class="bill-form"
    >
      <div>
        <select-field
          :label="'inputLabel.checkout.city'"
          :options="provinceOptions"
          :value="formAddress.city"
          @update:model-value="changeProvince"
        />
      </div>
      <div>
        <select-field
          :label="'inputLabel.checkout.district'"
          :options="districtOptions"
          :value="formAddress.district"
          :disabled="!formAddress.city"
          @update:model-value="changeDistrict"
        />
      </div>
      <div>
        <select-field
          :label="'inputLabel.checkout.ward'"
          :options="wardOptions"
          :value="formAddress.ward"
          :disabled="!formAddress.city || !formAddress.district"
          @update:model-value="
            (newValue) => {
              formAddress.ward = newValue;
              $emit('update:modelValue', formAddress);
            }
          "
        />
      </div>
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.address1'"
          :required="true"
          :value="formAddress.address_1"
          @update:model-value="
            (newValue) => {
              formAddress.address_1 = newValue;
              $emit('update:modelValue', formAddress);
            }
          "
        />
      </div>
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.address2'"
          :required="true"
          :value="formAddress.address_2"
          @update:model-value="
            (newValue) => {
              formAddress.address_2 = newValue;
              $emit('update:modelValue', formAddress);
            }
          "
        />
      </div>
    </div>
  </div>
  <div
    v-if="!loading && (addresses.length === 0 || openAddressForm)"
    class="contact-form-cont"
  >
    <h2 class="sub-title" v-t="'checkoutPage.subtitle.contact'" />
    <div class="bill-form">
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.phone'"
          :required="true"
          :value="formAddress?.tel"
          @update:model-value="
            (newValue) => {
              formAddress.tel = newValue;
              $emit('update:modelValue', formAddress);
            }
          "
        />
      </div>
      <div>
        <text-field
          class="h-[4.5rem]"
          :label="'inputLabel.checkout.representative'"
          :required="true"
          :value="formAddress?.representative"
          @update:model-value="
            (newValue) => {
              formAddress.representative = newValue;
              $emit('update:modelValue', formAddress);
            }
          "
        />
      </div>
    </div>
    <div class="flex flex-col">
      <div class="flex w-full gap-[2rem] justify-end">
        <custom-button
          v-if="addresses.length > 0"
          class="btn w-1/2 py-[1.4rem] px-[2.8rem]"
          intent="p-outline"
          :disabled="loading"
          v-html="$t('buttonLabel.cancel')"
          @click="cancelAdd"
        />
        <custom-button
          class="btn w-1/2 py-[1.4rem] px-[2.8rem]"
          intent="primary"
          :disabled="loading"
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
  <modal
    id="deleteModal"
    :title="'addressPage.deleteModel.title'"
    @submit="deleteAddress"
  >
    <span v-t="'addressPage.deleteModel.content'" />
  </modal>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import AddressSelect from "@/components/common/organisms/AddressSelect.vue";
import Modal from "@/components/common/organisms/Modal.vue";
import { useAddressStore } from "@/stores/address";
import { useToastStore } from "@/stores/toast";
import { OptionItem } from "@/types/frontend";
import {
  Address,
  District,
  isAddressValid,
  Province,
  Ward,
} from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "AddressForm",
  emits: ["update:modelValue"],
  components: {
    AddressSelect,
    CustomButton,
    Modal,
    SelectField,
    TextField,
  },
  props: {
    modelValue: {
      type: Object as PropType<Address>,
      required: true,
    },
  },
  data() {
    return {
      loading: false,
      formAddress: {} as Address,
      openAddressForm: false,
      editing: false,
      provinces: [] as Province[],
      districts: [] as District[],
      wards: [] as Ward[],
    };
  },
  computed: {
    ...mapState(useAddressStore, ["address", "addresses"]),
    provinceOptions() {
      if (!this.provinces) return [];
      return this.provinces.map((province) => {
        return {
          displayValue: province.name,
          value: String(province.code),
        } as OptionItem;
      });
    },
    districtOptions() {
      if (!this.districts) return [];
      return this.districts.map((district) => {
        return {
          displayValue: district.name,
          value: String(district.code),
        } as OptionItem;
      });
    },
    wardOptions() {
      if (!this.wards) return [];
      return this.wards.map((ward) => {
        return {
          displayValue: ward.name,
          value: String(ward.code),
        } as OptionItem;
      });
    },
  },
  methods: {
    ...mapActions(useAddressStore, [
      "createAddress",
      "updateAddress",
      "listAddressesByUser",
      "destroyAddress",
      "setAddress",
      "listProvinces",
      "listDistrictsByProvince",
      "listWardsByDistrict",
    ]),
    ...mapActions(useToastStore, ["toast"]),
    async addNewAddress() {
      if (isAddressValid(this.formAddress)) {
        if (this.formAddress.id) {
          await this.updateAddress(this.formAddress)
            .then((response) => {
              if (response && response.status === 200) {
                this.openAddressForm = false;
              }
              window.scrollTo({ top: 0, behavior: "smooth" });
              this.toast({
                theme: "success",
                message: "Update added successfully!",
              });
            })
            .catch((err) => {
              window.scrollTo({ top: 0, behavior: "smooth" });
              this.toast({
                theme: "danger",
                message: "Failed to update address!",
              });
            });
        } else {
          await this.createAddress(this.formAddress)
            .then((response) => {
              if (response && response.status === 201) {
                this.openAddressForm = false;
              }
              window.scrollTo({ top: 0, behavior: "smooth" });
              this.toast({
                theme: "success",
                message: "Address added successfully!",
              });
            })
            .catch((err) => {
              window.scrollTo({ top: 0, behavior: "smooth" });
              this.toast({
                theme: "danger",
                message: "Failed to add address!",
              });
            });
        }
      } else {
        alert("Please fill all the required fields");
      }
    },
    cancelAdd() {
      window.scrollTo({ top: 0, behavior: "smooth" });
      this.openAddressForm = false;
      this.editing = false;
      this.formAddress = {} as Address;
    },
    addAddress() {
      this.formAddress = {} as Address;
      this.openAddressForm = true;
    },
    chooseAddress(address: Address) {
      this.listDistricts(address.city);
      this.listWards(address.district);
      this.formAddress = { ...address };
    },
    editAddress(address: Address) {
      this.listDistricts(address.city);
      this.listWards(address.district);
      this.formAddress = { ...address };
      this.editing = true;
      this.openAddressForm = true;
    },
    async deleteAddress() {
      this.destroyAddress(this.formAddress)
        .then((response) => {
          window.scrollTo({ top: 0, behavior: "smooth" });
          this.toast({
            theme: "success",
            message: "Address deleted successfully!",
          });
        })
        .catch((err) => {
          window.scrollTo({ top: 0, behavior: "smooth" });
          this.toast({
            theme: "danger",
            message: "Failed to delete address!",
          });
        });
      this.formAddress = {} as Address;
      this.openAddressForm = false;
      this.editing = false;
    },
    changeProvince(newValue: string) {
      this.formAddress.city = newValue;
      this.formAddress.district = "";
      this.formAddress.ward = "";
      this.listDistricts(newValue);
      this.$emit("update:modelValue", this.formAddress);
    },
    changeDistrict(newValue: string) {
      this.formAddress.district = newValue;
      this.formAddress.ward = "";
      this.listWards(newValue);
      this.$emit("update:modelValue", this.formAddress);
    },
    async listDistricts(province: string) {
      await this.listDistrictsByProvince(Number(province)).then((response) => {
        if (response && response.status === 200 && response.data) {
          this.districts = response.data;
        }
      });
    },
    async listWards(district: string) {
      await this.listWardsByDistrict(Number(district)).then((response) => {
        if (response && response.status === 200 && response.data) {
          this.wards = response.data;
        }
      });
    },
  },
  async mounted() {
    this.loading = true;
    await this.listAddressesByUser();
    await this.listProvinces().then((response) => {
      if (response && response.status === 200 && response.data) {
        this.provinces = response.data.results;
      }
    });
    this.formAddress = this.addresses[0] || {};
    this.$emit("update:modelValue", this.formAddress);
    this.loading = false;
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

.bill-form {
  margin-top: 4rem;
  display: flex;
  flex-direction: column;
  gap: 4rem;
  width: 100%;
  .input-name-cont {
    width: 100%;
    display: flex;
    gap: 4.5rem;
  }
}

.btn {
  margin-top: 3rem;
  text-transform: uppercase;
}
</style>
