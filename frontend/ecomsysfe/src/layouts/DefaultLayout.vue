<template>
  <div>
    <nav-header :intent="headerIntent" />
    <slot></slot>
    <custom-footer />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import NavHeader from '../components/common/organisms/NavHeader.vue';
import CustomFooter from '../components/common/organisms/CustomFooter.vue';

export default defineComponent({
  name: 'DefaultLayout',
  components: {
    NavHeader,
    CustomFooter,
  },
  props: {
    headerIntent: {
      type: String,
      default: 'primary',
    },
  },
});
</script>

<style lang="scss" scoped></style>
