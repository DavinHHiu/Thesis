<template>
  <img
    class="avatar w-[3.2rem]"
    :src="src"
    data-bs-toggle="tooltip"
    data-bs-placement="bottom"
    title="Hong Hieu"
  />
</template>

<script lang="ts">
import { Tooltip } from "bootstrap";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Avatar",
  props: {
    src: {
      type: String,
      required: true,
    },
  },
  mounted() {
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach((tooltip) => {
      new Tooltip(tooltip);
    });
  },
});
</script>

<style lang="scss" scoped>
.avatar {
  border-radius: 50%;
}
</style>
