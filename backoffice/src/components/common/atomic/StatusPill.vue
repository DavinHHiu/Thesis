<template>
  <div class="wrapper" :style="statusColor">
    <span v-text="status" />
  </div>
</template>

<script lang="ts">
import consts, { StatusType } from "@/consts/consts";
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "StatusPill",
  props: {
    status: {
      type: String as PropType<StatusType>,
      required: true,
    },
  },
  computed: {
    statusColor() {
      const color = consts.ORDER_STATUS_MAP_COLOR[this.status];
      return {
        border: `1px solid ${color}`,
        color,
      };
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.wrapper {
  padding: 0.5rem 1rem;
  width: fit-content;
  border-radius: 50rem;
  font-size: $--font-3xs;
}
</style>
