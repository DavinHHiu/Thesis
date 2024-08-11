<template>
  <div class="body-wrap">
    <nav-header />
    <div class="body">
      <sidebar />
      <div class="content-wrap p-[3.2rem] flex-1">
        <slot />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import NavHeader from "@/components/common/organisms/NavHeader.vue";
import Sidebar from "@/components/common/organisms/Sidebar.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "MainLayout",
  components: {
    NavHeader,
    Sidebar,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.body {
  display: flex;
  .content-wrap {
    margin-top: $--header-height;
  }
}
</style>
