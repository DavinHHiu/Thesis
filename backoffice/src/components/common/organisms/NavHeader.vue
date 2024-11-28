<template>
  <nav
    class="header-wrap w-full relative flex items-center justify-between px-[3.2rem]"
  >
    <app-logo />
    <div class="avatar-wrap flex items-center f-full">
      <avatar :src="String(user?.avatar)" class="mr-[0.8rem]" />
      <button
        class="dropdown-toggle"
        data-bs-toggle="dropdown"
        v-text="String(user?.username)"
      />
      <ul class="dropdown-menu">
        <li
          class="dropdown-item"
          @click="handleLogout"
          v-t="'buttonLabel.logout'"
        />
      </ul>
    </div>
  </nav>
</template>

<script lang="ts">
import Avatar from "@/components/common/atomic/Avatar.vue";
import AppLogo from "@/components/common/molecules/AppLogo.vue";
import { useSessionStore } from "@/stores/session";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Header",
  components: {
    AppLogo,
    Avatar,
  },
  computed: {
    ...mapState(useSessionStore, ["user"]),
  },
  methods: {
    ...mapActions(useSessionStore, ["logout"]),
    handleLogout() {
      this.logout();
      this.$router.push({ name: "login" });
    },
  },
  mounted() {
    console.log(this.user);
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
    font-size: $--font-sm;
  }
}
</style>
