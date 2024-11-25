<template>
  <address-form />
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import Card from "@/components/common/molecules/Card.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import AddressForm from "@/components/common/organisms/AddressForm.vue";
import AddressSelect from "@/components/common/organisms/AddressSelect.vue";
import LoadingContent from "@/components/common/organisms/LoadingContent.vue";
import { useAddressStore } from "@/stores/address";
import { useToastStore } from "@/stores/toast";
import { Address, isAddressValid, User } from "@/types/worker";
import localStore from "@/utils/localStorage";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProfileAddressView",
  components: {
    AddressSelect,
    AddressForm,
    Card,
    CustomButton,
    SelectField,
    TextField,
    LoadingContent,
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
    ...mapActions(useToastStore, ["toast"]),
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
      if (isAddressValid(this.address)) {
        if (this.address.id) {
          await this.updateAddress(this.address)
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
