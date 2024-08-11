<template>
  <div class="content-wp">
    <slot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageBody",
});
</script>

<style lang="scss" scoped>
.content-wp {
  padding: 2rem 0;
}
</style>
