<template>
  <page-body class="page-wp flex justify-between py-[6rem]">
    <Toast />
    <section class="user-sidebar">
      <editable-avatar
        class="w-[20rem] h-[20rem]"
        src="/images/avatars/6.jpg"
      />
      <div class="side-tab flex flex-col gap-[2rem] mt-[4rem]">
        <nav class="side-tab-upper flex flex-col items-center gap-[2rem]">
          <router-link class="side-tab-item" :to="{ name: 'profile.details' }">
            <span class="material-symbols-outlined" v-text="'person'" />
            <span v-text="'Profile details'" />
          </router-link>
          <router-link
            class="side-tab-item"
            :to="{ name: 'profile.addresses' }"
          >
            <span class="material-symbols-outlined" v-text="'pin_drop'" />
            <span v-text="'My addresses'" />
          </router-link>
          <router-link class="side-tab-item" :to="{ name: 'cartPage' }">
            <span class="material-symbols-outlined" v-text="'shopping_cart'" />
            <span v-text="'My cart'" />
          </router-link>
          <router-link class="side-tab-item" :to="{ name: 'orderPage' }">
            <span class="material-symbols-outlined" v-text="'list_alt'" />
            <span v-text="'My orders'" />
          </router-link>
        </nav>
        <nav class="flex flex-col items-center gap-[2rem]">
          <router-link
            class="side-tab-item"
            :to="{ name: 'profile.change-password' }"
          >
            <span class="material-symbols-outlined" v-text="'lock_open'" />
            <span v-text="'Change password'" />
          </router-link>
          <a class="side-tab-item logout" @click.prevent="handleLogout">
            <span class="material-symbols-outlined" v-text="'logout'" />
            <span v-text="'Logout'" />
          </a>
        </nav>
      </div>
    </section>
    <section class="user-profile w-3/4">
      <router-view />
    </section>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomLabel from "@/components/common/atomic/CustomLabel.vue";
import Card from "@/components/common/molecules/Card.vue";
import DividerBreak from "@/components/common/molecules/DividerBreak.vue";
import EditableAvatar from "@/components/common/molecules/EditableAvatar.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import { useSessionStore } from "@/stores/session";
import { mapActions } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProfileView",
  components: {
    CustomLabel,
    EditableAvatar,
    PageBody,
    TextField,
    DividerBreak,
    CustomButton,
    Card,
  },
  methods: {
    ...mapActions(useSessionStore, ["logout"]),
    handleLogout() {
      this.logout();
      this.$router.push({ name: "login" });
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.user-sidebar {
  display: flex;
  flex-direction: column;
}

.side-tab {
  font-size: $--font-xs;
  .side-tab-item {
    display: flex;
    align-items: center;
    width: 100%;
    color: $--gray-color-800;
    cursor: pointer;
    gap: 0.5rem;
    transition: all 0.2s ease-in-out;
    .material-symbols-outlined {
      font-size: $--font-lg;
    }
    &:active {
      transform: scale(0.85);
    }
  }
  .side-tab-upper {
    padding: 2rem 0;
    border-top: 1px solid $--color-border;
    border-bottom: 1px solid $--color-border;
  }
  .logout {
    color: $--color-danger;
  }
}

.router-link-exact-active {
  span {
    font-weight: $--font-bold;
    color: $--primary-color;
  }
}
</style>
