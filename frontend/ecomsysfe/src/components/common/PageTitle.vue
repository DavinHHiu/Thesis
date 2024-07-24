<template>
  <div class="title-cont">
    <div class="title-wp">
      <span class="title">{{ title }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'PageTitle',
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.title-cont {
  padding: 50px 0;
  .title-wp {
    margin: auto;
    max-width: 1200px;
    padding: 10px;
    text-align: center;
    .title {
      color: #54595f;
      font-size: 59px;
      font-weight: 600;
    }
  }
}
</style>
