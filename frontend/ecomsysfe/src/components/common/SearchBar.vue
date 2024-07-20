<template>
  <div class="container">
    <div class="item-left-container"></div>
    <div class="search-input-container flex-1 h-full">
      <text-field
        type="text"
        class="input-search w-full h-full"
        placeholder="Search Price Tag"
      />
    </div>
    <div class="item-right-container">
      <icon-search class="icon" />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import TextField from './TextField.vue';
import IconSearch from '../icons/IconSearch.vue';

export default defineComponent({
  name: 'SearchBar',
  components: {
    TextField,
    IconSearch,
  },
});
</script>

<style lang="scss" scoped>
.container {
  flex: 1;
  display: flex;
  align-items: center;
  height: 70px;
  width: 100%;
  overflow: hidden;

  .input-search {
    line-height: 3rem;
    font-size: 16px;
  }

  .item-right-container {
    background-color: #000;
    width: 150px;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;

    &:hover {
      .icon {
        width: 35px;
        height: 35px;
      }
    }
  }
}
</style>
