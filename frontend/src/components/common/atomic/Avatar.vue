<template>
  <img class="avatar" :src="src" />
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Avatar",
  props: {
    src: {
      type: String,
      required: true,
      default: "",
    },
  },
});
</script>

<style lang="scss" scoped>
.avatar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
}
</style>
