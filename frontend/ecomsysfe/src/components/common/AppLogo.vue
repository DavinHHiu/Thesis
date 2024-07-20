<template>
  <div class="logo-container w-full flex items-center justify-center">
    <icon-price-tag :intent="intent" />
    <h2
      class="app-name mt-[-12px] ml-[10px] text-[22px] font-bold flex items-center"
      :class="{
        'text-black': intent == 'primary',
        'text-white': intent == 'transparent',
      }"
    >
      price tag
    </h2>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import IconPriceTag from '../icons/IconPriceTag.vue';

export default defineComponent({
  name: 'AppLogo',
  props: {
    intent: {
      type: String,
      default: 'primary',
    },
  },
  components: {
    IconPriceTag,
  },
});
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik+Glitch&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap');

.app-name {
  font-family: 'Playwrite CU', cursive;
  font-size: 30px;
}
</style>
