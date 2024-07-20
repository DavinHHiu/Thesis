<template>
  <div class="divider-wraper flex justify-center">
    <p class="title text-center text-xs font-normal text-slate-400 bg-white">
      {{ title }}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'DividerBreak',
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.divider-wraper {
  position: relative;
  .title {
    position: relative;
    display: inline-block;
    padding: 0 8px 0 7px;
    z-index: 2;
  }
  &::after {
    content: '';
    position: absolute;
    background-color: transparent;
    top: 50%;
    display: block;
    width: 100%;
    border-top: 1px solid #e7e7e7;
    z-index: 1;
  }
}
</style>
