<template>
  <aside
    :class="{ 'is-expanded': is_expanded }"
    class="flex flex-col overflow-hidden p-[1.6rem]"
  >
    <div class="menu-toggle-wrap flex justify-end relative top-0 mb-[1.6rem]">
      <button class="menu-toggle" @click="toggleMenu">
        <span
          class="material-symbols-outlined"
          v-text="'keyboard_double_arrow_right'"
        />
      </button>
    </div>

    <div class="menu">
      <router-link
        v-for="(x, index) in 8"
        class="button"
        :class="{ active: activeRoute($t(`backofficeSidebar[${index}].path`)) }"
        :to="$t(`backofficeSidebar[${index}].path`)"
      >
        <span class="material-symbols-outlined">{{
          $t(`backofficeSidebar[${index}].icon`)
        }}</span>
        <span class="text">{{ $t(`backofficeSidebar[${index}].title`) }}</span>
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
    activeRoute(path: string) {
      return path === "/"
        ? this.$route.path === "/"
        : this.$route.path.includes(path);
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
      .material-symbols-outlined {
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
      height: 4.5rem;

      padding: 0.8rem 1.6rem;
      transition: 0.2s ease-out;
      border-radius: 0.4rem;

      .material-symbols-outlined {
        font-size: 2.5rem;
        color: $--gray-color-500;
        transition: 0.2s ease-out;
      }

      .text {
        color: $--gray-color-500;
      }

      &:hover,
      &.active {
        .material-symbols-outlined,
        .text {
          color: $--primary;
        }
      }
      &.active {
        border-right: 5px solid $--primary;
        background-color: rgba($--gray-color-200, 0.8);
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
      .material-symbols-outlined {
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
