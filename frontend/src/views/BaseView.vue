<template>
  <div class="body-wp" :class="{ 'h-screen': openCart }">
    <nav-header :intent="headerIntent" @open:cart-folder="toogleCartFolder" />
    <div class="body">
      <router-view />
    </div>
    <Footer v-if="hasFooter" />
    <cart-folder
      :class="{ active: openCart }"
      @close:cart-folder="toogleCartFolder"
    />
  </div>
</template>

<script lang="ts">
import Footer from "@/components/common/organisms/Footer.vue";
import NavHeader from "@/components/common/organisms/NavHeader.vue";
import CartFolder from "@/components/common/templates/CartFolder.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "BaseView",
  components: {
    CartFolder,
    Footer,
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
      return this.$route.meta?.intent as string;
    },
    hasFooter() {
      return this.$route.meta?.hasFooter === undefined
        ? true
        : this.$route.meta?.hasFooter;
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
