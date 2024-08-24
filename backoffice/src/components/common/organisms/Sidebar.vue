<template>
  <aside
    :class="{ 'is-expanded': is_expanded }"
    class="flex flex-col overflow-hidden p-[1.6rem]"
  >
    <div class="menu-toggle-wrap flex justify-end relative top-0 mb-[1.6rem]">
      <button class="menu-toggle" @click="toggleMenu">
        <span class="material-icons">keyboard_double_arrow_right</span>
      </button>
    </div>

    <div class="menu">
      <router-link class="button" to="/">
        <span class="material-icons">home</span>
        <span class="text">Home</span>
      </router-link>
      <router-link class="button" to="/products">
        <span class="material-icons">inventory_2</span>
        <span class="text">Product</span>
      </router-link>
      <router-link class="button" to="/users">
        <span class="material-icons">group</span>
        <span class="text">User</span>
      </router-link>
      <router-link class="button" to="/orders">
        <span class="material-icons">description</span>
        <span class="text">Order</span>
      </router-link>
    </div>

    <div class="flex-1"></div>

    <div class="menu">
      <router-link class="button" to="/settings">
        <span class="material-icons">settings</span>
        <span class="text">Settings</span>
      </router-link>
    </div>
  </aside>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Sidebar",
  data() {
    return {
      is_expanded: localStorage.getItem("is_expanded") === "true",
    };
  },
  methods: {
    toggleMenu() {
      this.is_expanded = !this.is_expanded;

      localStorage.setItem("is_expanded", this.is_expanded.toString());
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

aside {
  width: calc(3.2rem + 32px);
  height: calc(100vh - $--header-height);
  margin-top: $--header-height;
  background-color: $--white;
  color: $--primary;
  transition: 0.2s ease-out;

  .menu-toggle-wrap {
    transition: 0.2s ease-out;

    .menu-toggle {
      transition: 0.2 ease-out;
      .material-icons {
        font-size: 3.2rem;
        color: $--gray-color-300;
        transition: 0.2s ease-out;

        &:hover {
          color: $--primary;
          transform: translateX(0.8rem);
        }
      }
    }
  }

  .button .text,
  .app-name {
    opacity: 0;
    transition: 0.3s ease-out;
  }

  .menu {
    margin: 0 -1.6rem;
    .button {
      display: flex;
      align-items: center;
      text-decoration: none;

      padding: 0.8rem 1.6rem;
      transition: 0.2s ease-out;

      .material-icons {
        font-size: 3.2rem;
        color: $--gray-color-500;
        transition: 0.2s ease-out;
      }

      .text {
        color: $--gray-color-500;
      }

      &:hover,
      &.router-link-exact-active {
        .material-icons,
        .text {
          color: $--primary;
        }
      }
      &.router-link-exact-active {
        border-right: 5px solid $--primary;
        background-color: $--gray-color-200;
      }
    }
  }

  &.is-expanded {
    width: $--sidebar-width;
    .menu-toggle-wrap {
      .menu-toggle {
        transform: rotate(-180deg);
      }
    }

    .button .text,
    .app-name {
      opacity: 1;
    }

    .button {
      .material-icons {
        margin-right: 1.6rem;
      }
    }
    .logo {
      margin-right: 1.6rem;
    }
  }

  @media (max-width: 768px) {
    position: fixed;
    z-index: 99;
  }
}
</style>
