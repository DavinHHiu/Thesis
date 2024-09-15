<template>
  <div class="body-wrap">
    <nav-header />
    <div class="body flex">
      <sidebar />
      <div class="content-wrap p-[3.2rem] flex-1 overflow-y-scroll">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import NavHeader from "@/components/common/organisms/NavHeader.vue";
import Sidebar from "@/components/common/organisms/Sidebar.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "BaseView",
  components: {
    NavHeader,
    Sidebar,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.content-wrap {
  height: calc(100vh - $--header-height);
  margin-top: $--header-height;
}
</style>
