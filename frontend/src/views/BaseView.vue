<template>
  <div class="body-wp" :class="{ 'h-screen': openCart }">
    <nav-header :intent="headerIntent" @open:cart-folder="toogleCartFolder" />
    <div class="body">
      <router-view class="overflow" />
    </div>
    <custom-footer />
    <cart-folder
      :class="{ active: openCart }"
      @close:cart-folder="toogleCartFolder"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import NavHeader from '../components/common/organisms/NavHeader.vue';
import CustomFooter from '../components/common/organisms/CustomFooter.vue';
import CartFolder from '@/components/common/templates/CartFolder.vue';

export default defineComponent({
  name: 'BaseView',
  components: {
    CartFolder,
    CustomFooter,
    NavHeader,
  },
  data() {
    return {
      openCart: false,
    };
  },
  methods: {
    toogleCartFolder() {
      this.openCart = !this.openCart;
    },
  },
  computed: {
    headerIntent() {
      return this.$router.currentRoute._value.meta.intent;
    },
  },
});
</script>

<style lang="scss" scoped>
.body-wp {
  width: 100%;
  overflow-x: hidden;
}

:deep(.cart-folder-wp) {
  &.active {
    opacity: 1;
    visibility: visible;
    .cart-folder {
      right: 0;
    }
  }
}
</style>
