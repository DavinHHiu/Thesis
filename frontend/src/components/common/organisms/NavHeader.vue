<template>
  <div class="nav-header-container" :class="intent">
    <div class="w-[20rem]">
      <app-logo :intent="intent" />
    </div>
    <div class="flex gap-[7rem]">
      <div class="container">
        <p class="header-items">en</p>
      </div>
      <div class="container">
        <p class="header-items">orders</p>
      </div>
      <div class="container" @click="$emit('open:cart-folder')">
        <icon-cart :intent="intent" />
      </div>
      <div v-if="isAuthenticated" class="container flex items-center f-full">
        <!-- <avatar
          :src="`http://localhost:8000/${user.avatar}`"
          class="w-[3.2rem]"
        /> -->
        <p
          class="dropdown-toggle header-items"
          data-bs-toggle="dropdown"
          @click="handleClick"
        >
          Hong Hieu
        </p>
        <!-- <ul class="dropdown-menu">
          <li class="dropdown-item" @click="handleLogout">Logout</li>
        </ul> -->
      </div>
      <div v-else class="container">
        <icon-user width="2rem" :intent="intent" />
        <p class="header-items">account</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { useSessionStore } from "@/stores/session";
import { mapState } from "pinia";
import { defineComponent } from "vue";

import IconCart from "../../icons/IconCart.vue";
import IconUser from "../../icons/IconUser.vue";
import Avatar from "../atomic/Avatar.vue";
import AppLogo from "../molecules/AppLogo.vue";

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
    handleClick() {
      console.log("Dropdown clicked");
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
