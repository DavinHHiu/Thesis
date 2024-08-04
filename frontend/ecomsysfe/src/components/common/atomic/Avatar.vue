<template>
  <img class="avatar" :src="src" />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Avatar',
  props: {
    src: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.avatar {
  width: 100%;
  height: auto;
  border-radius: 50%;
}
</style>
