<template>
  <div>
    <nav-header :intent="headerIntent" />
    <slot></slot>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/common/organisms/Footer.vue";
import NavHeader from "@/components/common/organisms/NavHeader.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "DefaultLayout",
  components: {
    NavHeader,
    Footer,
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
