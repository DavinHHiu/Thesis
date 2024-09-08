<template>
  <div class="container">
    <div class="search-input-container flex-1">
      <text-field label="Search Price Tag" />
    </div>
    <div class="item-right-container flex items-center justify-center">
      <span class="material-symbols-outlined icon"> chevron_right </span>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import IconRightArrow from '@/components/icons/IconRightArrow.vue';
import TextField from '../molecules/TextField.vue';

export default defineComponent({
  name: 'SearchBar',
  components: {
    TextField,
    IconRightArrow,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.container {
  display: flex;
  height: 100%;
  gap: 0.7rem;

  .item-right-container {
    background-color: $--primary-color;
    color: $--second-color-text;
    padding: 0 0.5rem;
    cursor: pointer;

    .icon {
      transition: all 0.2s ease-in;
    }

    &:hover {
      .icon {
        transform: translateX(0.5rem);
      }
    }
  }
}
</style>
