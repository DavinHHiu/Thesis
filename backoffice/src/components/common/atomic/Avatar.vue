<template>
  <img class="avatar w-[3.2rem]" :src="src" />
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Avatar",
  props: {
    src: {
      type: String,
      required: true,
    },
  },
  mounted() {},
});
</script>

<style lang="scss" scoped>
.avatar {
  border-radius: 50%;
}
</style>
