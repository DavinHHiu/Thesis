<template>
  <page-title v-if="new" :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :label="$t('inputLabel.cart.totalQuantity')"
          :value="cart.total_quantity"
          @update:model-value="(newValue) => (cart.total_quantity = newValue)"
        />
        <text-field
          :label="$t('inputLabel.cart.totalAmount')"
          :value="cart.total_amount"
          @update:model-value="(newValue) => (cart.total_amount = newValue)"
        />
        <select-field
          :label="$t('inputLabel.address.user')"
          :value="cart.user?.id"
          :options="options"
          @update:model-value="selectUser"
        />
        <custom-form-button
          :text-button="textButton"
          @update="handleUpdate"
          @back="handleBack"
        />
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomFormButton from "@/components/common/molecules/CustomFormButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useCartStore } from "@/stores/cart";
import { useUserStore } from "@/stores/user";
import { OptionItem } from "@/types/backoffice";
import { User } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "CartUpdateView",
  components: {
    Card,
    CustomButton,
    CustomFormButton,
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
    ...mapActions(useCartStore, [
      "createCart",
      "retrieveCart",
      "updateCart",
      "resetCart",
    ]),
    selectUser(value: string) {
      const user = _.find(this.users, (user) => user.id === value) as User;
      this.cart.user = user;
    },
    async handleUpdate() {
      if (this.new) {
        this.createCart(this.cart);
      } else {
        await this.updateCart(this.cart);
      }
      this.$router.push({ name: "cart.list" });
    },
    handleBack() {
      this.$router.push({ name: "cart.list" });
    },
  },
  computed: {
    ...mapState(useCartStore, ["cart"]),
    ...mapState(useUserStore, ["users"]),
    options(): OptionItem[] {
      const users = _.map(this.users, (user) => {
        return {
          value: String(user.id),
          displayValue: user.email,
        };
      });
      return users;
    },
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
    pageTitle() {
      return this.new
        ? this.$t("cartPage.add.title")
        : this.$t("cartPage.update.title");
    },
  },
  async mounted() {
    await this.listUsers();
    const cartId = this.$router.currentRoute.value.params.cartId;
    if (cartId) {
      this.retrieveCart(cartId as string);
      this.new = false;
    }
  },
  beforeRouteLeave() {
    this.resetCart();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  width: 100%;
  padding: 4rem 4rem 2rem;
}
</style>
