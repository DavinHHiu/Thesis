<template>
  <page-title :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :label="$t('inputLabel.address.title')"
          :value="address.title"
          @update:model-value="(newValue) => (address.title = newValue)"
        />
        <text-field
          :label="$t('inputLabel.address.zipcode')"
          :value="address.zipcode"
          @update:model-value="(newValue) => (address.zipcode = newValue)"
        />
        <text-field
          :label="$t('inputLabel.address.address1')"
          :value="address.address_1"
          @update:model-value="(newValue) => (address.address_1 = newValue)"
        />
        <text-field
          :label="$t('inputLabel.address.address2')"
          :value="address.address_2"
          @update:model-value="(newValue) => (address.address_2 = newValue)"
        />
        <text-field
          :label="$t('inputLabel.address.tel')"
          :value="address.tel"
          @update:model-value="(newValue) => (address.tel = newValue)"
        />
        <select-field
          :label="$t('inputLabel.address.user')"
          :value="address.user?.id"
          :options="options"
          @update:model-value="selectUser"
        />
        <custom-button
          class="w-[15rem]"
          @click="handleUpdate"
          v-text="textButton"
        />
        >
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useAddressStore } from "@/stores/address";
import { useUserStore } from "@/stores/user";
import { OptionItem } from "@/types/backoffice";
import { User } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserUpdateView",
  components: {
    Card,
    CustomButton,
    PageBody,
    PageTitle,
    TextField,
    SelectField,
    UploadPreview,
  },
  data() {
    return {
      new: true as boolean,
    };
  },
  methods: {
    ...mapActions(useUserStore, ["listUsers"]),
    ...mapActions(useAddressStore, [
      "createAddress",
      "retrieveAddress",
      "updateAddress",
    ]),
    selectUser(value: string) {
      const user = _.find(this.users, (user) => (user.id = value)) as User;
      this.address.user = user;
    },
    async handleUpdate() {
      if (this.new) {
        this.createAddress(this.address);
      } else {
        await this.updateAddress(this.address);
      }
      this.$router.push("/addresses");
    },
  },
  computed: {
    ...mapState(useAddressStore, ["address"]),
    ...mapState(useUserStore, ["users"]),
    options(): OptionItem[] {
      return _.map(this.users, (user) => {
        return {
          value: String(user.id),
          displayValue: `${user.first_name} ${user.last_name}`,
        };
      });
    },
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
    pageTitle() {
      return this.new
        ? this.$t("addressPage.addAddress.title")
        : this.$t("addressPage.updateAddress.title");
    },
  },
  mounted() {
    this.listUsers();
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      this.retrieveAddress(id);
      this.new = false;
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  width: 100%;
  padding: 2rem 4rem;
}
</style>
