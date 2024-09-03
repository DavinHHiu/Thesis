<template>
  <nav
    class="header-wrap w-full relative flex items-center justify-between px-[3.2rem]"
  >
    <app-logo />
    <div class="avatar-wrap flex items-center f-full">
      <avatar src="/images/avatars/6.jpg" class="mr-[0.8rem]" />
      <button class="dropdown-toggle" data-bs-toggle="dropdown">
        Hong Hieu
      </button>
      <ul class="dropdown-menu">
        <li class="dropdown-item" @click="handleLogout">Logout</li>
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
import Avatar from "@/components/common/atomic/Avatar.vue";
import AppLogo from "@/components/common/molecules/AppLogo.vue";
import { useAuthStore } from "@/stores/auth";
import { mapActions } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Header",
  components: {
    AppLogo,
    Avatar,
  },
  methods: {
    ...mapActions(useAuthStore, ["logout"]),
    handleLogout() {
      this.logout();
      this.$router.push("/login");
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

nav {
  position: fixed;
  height: $--header-height;
  background-color: $--white;
  box-shadow: $--shadow-x;
  z-index: 100;
  .dropdown-toggle,
  .dropdown-item {
    user-select: none;
  }
}
</style>
