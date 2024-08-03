<template>
  <div class="logo-wp w-[25rem] flex items-center justify-center gap-[0.5rem]">
    <div class="w-[5rem] h-[5rem]">
      <icon-price-tag :intent="intent" />
    </div>
    <h2
      class="app-name flex items-center"
      :class="{
        'text-black': intent == 'primary',
        'text-white': intent == 'second',
      }"
    >
      price tag
    </h2>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import IconPriceTag from '../../icons/IconPriceTag.vue';

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
@import '@/assets/variables';

.logo-wp {
  margin: 0 auto;
}

.app-name {
  font-family: 'Playwrite CU', cursive;
  font-size: $--font-xl;
  text-transform: uppercase;
}
</style>
