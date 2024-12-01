<template>
  <div class="nav-header-container" :class="intent">
    <div class="w-[20rem]">
      <app-logo :intent="intent" />
    </div>
    <div class="flex gap-[5rem]">
      <div class="container">
        <span class="material-symbols-outlined" v-text="'language'" />
        <p class="header-items" v-text="'en'" />
      </div>
      <div class="container" @click="navigateToOrders">
        <span class="material-symbols-outlined" v-text="'receipt_long'" />
        <p class="header-items" v-text="'orders'" />
      </div>
      <div class="container" @click="navigateToSearch">
        <span class="material-symbols-outlined" v-text="'search'" />
      </div>
      <div class="container" @click="openCartFolder">
        <icon-cart :intent="intent" />
      </div>
      <div
        v-if="isAuthenticated"
        class="container flex items-center f-full"
        @click="navigateToProfile"
      >
        <div class="w-[3rem]">
          <avatar :src="String(user.avatar)" />
        </div>
        <p class="header-items" v-text="user.username" />
      </div>
      <div v-else class="container">
        <span class="material-symbols-outlined" v-text="'person'" />
        <p class="header-items" v-text="'account'" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Avatar from "@/components/common/atomic/Avatar.vue";
import AppLogo from "@/components/common/molecules/AppLogo.vue";
import IconCart from "@/components/icons/IconCart.vue";
import IconUser from "@/components/icons/IconUser.vue";
import { useCartStore } from "@/stores/cart";
import { useSessionStore } from "@/stores/session";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "NavHeader",
  emits: ["open:cart-folder"],
  components: {
    AppLogo,
    IconCart,
    IconUser,
    Avatar,
  },
  props: {
    intent: {
      type: String,
      default: "primary",
      validator: (val: string) => {
        return ["primary", "second"].includes(val);
      },
    },
  },
  computed: {
    ...mapState(useSessionStore, ["isAuthenticated", "user"]),
  },
  methods: {
    openCartFolder() {
      if (this.$route.name !== "cartPage") {
        this.$emit("open:cart-folder");
      }
    },
    navigateToOrders() {
      this.$router.push({ name: "orderPage" });
    },
    navigateToSearch() {
      this.$router.push({ name: "search" });
    },
    navigateToProfile() {
      this.$router.push({ name: "profile.details" });
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.nav-header-container {
  position: relative;
  height: 10.3rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.6rem 7rem 1.6rem 3rem;
  z-index: 99;

  .container {
    display: flex;
    align-items: center;
    width: auto;
    cursor: pointer;
    gap: 1rem;

    .header-items {
      text-transform: uppercase;
      font-size: $--font-base;
      font-weight: $--font-semibold;
    }
  }
}

.primary {
  background-color: $--second-color;
  color: $--primary-color;
}

.second {
  background-color: $--black-alpha-10;
  color: $--second-color;
}
</style>
