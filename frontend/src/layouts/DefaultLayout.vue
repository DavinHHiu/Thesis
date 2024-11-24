<template>
  <div>
    <nav-header :intent="headerIntent" />
    <slot></slot>
    <custom-footer />
  </div>
</template>

<script>
import CustomFooter from "@/components/common/organisms/CustomFooter.vue";
import NavHeader from "@/components/common/organisms/NavHeader.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "DefaultLayout",
  components: {
    NavHeader,
    CustomFooter,
  },
  props: {
    headerIntent: {
      type: String,
      default: "primary",
    },
  },
});
</script>

<style lang="scss" scoped></style>
