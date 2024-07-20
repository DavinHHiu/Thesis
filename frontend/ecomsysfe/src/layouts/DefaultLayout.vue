<template>
  <div>
    <nav-header :intent="headerIntent" />
    <slot></slot>
    <custom-footer />
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import NavHeader from '../components/common/NavHeader.vue';
import CustomFooter from '../components/common/CustomFooter.vue';

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

<style scoped>
.image {
  width: 300px;
  height: 300px;
  object-fit: cover;
  object-position: center;
}

.image1 {
  width: 150px;
  height: 115px;
  object-fit: cover;
  object-position: center;
}

.subtitle {
  font-size: 12px;
}
</style>
