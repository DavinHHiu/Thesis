<template>
  <page-title v-if="new" :title="pageTitle" />
  <page-body class="flex flex-col gap-[2rem]">
    <card class="flex">
      <section class="info-wp">
        <select-field
          :label="$t('inputLabel.address.user')"
          :value="order.user?.id"
          :options="options"
          @update:model-value="selectUser"
        />
      </section>
    </card>
    <card v-if="cartItems.length > 0" class="flex">
      <section class="info-wp flex flex-col gap-[2rem]">
        <h2>Order Items</h2>
        <div class="item-wp">
          <label
            v-for="(item, index) in cartItems"
            class="item flex"
            :for="String(item.id)"
          >
            <input
              type="checkbox"
              :id="String(item.id)"
              @change="checkItem($event, item)"
            />
            <span>
              <img
                :src="item.product_sku.images?.[0].image"
                class="w-[4rem] h-[5rem]"
              />
            </span>
            <span v-text="item.product_sku.product.name" />
            <span v-text="item.product_sku.sku" />
            <span v-text="`Size: ${item.product_sku.size.value}`" />
            <span v-text="`Color: ${item.product_sku.color.value}`" />
            <span v-text="`Price: $${item.product_sku.price}`" />
            <span v-text="`Quantity: ${item.quantity}`" />
            <span v-text="`Subtotal: $${item.subtotal}`" />
          </label>
        </div>
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
import { useCartItemStore } from "@/stores/cartItem";
import { useOrderStore } from "@/stores/order";
import { useUserStore } from "@/stores/user";
import { OptionItem } from "@/types/backoffice";
import { User } from "@/types/worker";
import { CartItem } from "@/types/worker";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "OrderUpdateView",
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
      pickedCartItems: [] as CartItem[],
    };
  },
  methods: {
    ...mapActions(useUserStore, ["listUsers"]),
    ...mapActions(useCartItemStore, ["listCartItemsByUser", "resetCartItem"]),
    ...mapActions(useOrderStore, [
      "createOrder",
      "retrieveOrder",
      "updateOrder",
      "resetOrder",
    ]),
    selectUser(value: string) {
      const user = _.find(this.users, (user) => user.id === value) as User;
      this.order.user = user;
      this.listCartItemsByUser(user.id as string);
      console.log(this.cartItems);
    },
    async handleUpdate() {
      if (this.new) {
        this.createOrder(this.order);
      } else {
        await this.updateOrder(this.order);
      }
      this.$router.push({ name: "order.list" });
    },
    handleBack() {
      this.$router.push({ name: "order.list" });
    },
    checkItem(event: Event, cartItem: CartItem) {
      const input = event.target as HTMLInputElement;
      if (input.checked) {
        this.pickedCartItems.push(cartItem);
      } else {
        this.pickedCartItems = _.filter(
          this.pickedCartItems,
          (item) => item !== cartItem
        );
      }
      console.log(this.pickedCartItems);
    },
  },
  computed: {
    ...mapState(useOrderStore, ["order"]),
    ...mapState(useCartItemStore, ["cartItems"]),
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
        ? this.$t("orderPage.add.title")
        : this.$t("orderPage.update.title");
    },
  },
  async mounted() {
    await this.listUsers();
    const orderId = this.$router.currentRoute.value.params.orderId;
    if (orderId) {
      this.retrieveOrder(orderId as string);
      this.new = false;
    }
  },
  beforeRouteLeave() {
    this.resetOrder();
    this.resetCartItem();
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.info-wp {
  width: 100%;
  padding: 2rem;
}

.item-wp {
  max-height: 40rem;
  overflow-y: auto;

  .item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 2rem 4rem;
    border-top: 1px solid $--gray-color-200;
    border-bottom: 1px solid $--gray-color-200;
    user-select: none;
  }
}
</style>
