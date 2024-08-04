<template>
  <div class="wrapper">
    <img class="icon" :src="imageSrc" />
    <h3 class="title">{{ title }}</h3>
    <span class="desc">{{ desc }}</span>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CriteraItem',
  props: {
    title: {
      type: String,
      required: true,
    },
    desc: {
      type: String,
      required: true,
    },
    imageSrc: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 26.5rem;
  gap: 2rem;
  .icon {
    width: 5.2rem;
    height: 5.2rem;
  }
  .title {
    font-size: $--font-lg;
    font-weight: $--font-bold;
  }
  .desc {
    text-align: center;
    line-height: 2;
    color: $--black-alpha-70;
  }
}
</style>
