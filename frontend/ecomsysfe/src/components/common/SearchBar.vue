<template>
  <div class="container">
    <!-- <div class="item-left-container"></div> -->
    <div class="search-input-container flex-1 h-full">
      <text-field
        type="text"
        :class="['input-search', 'w-full', 'h-full']"
        :style="{
          fontSize: inputFontSize,
        }"
        placeholder="Search Price Tag"
      />
    </div>
    <div class="item-right-container h-full">
      <icon-right-arrow class="icon" />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import TextField from './TextField.vue';
import IconRightArrow from '../icons/IconRightArrow.vue';

export default defineComponent({
  name: 'SearchBar',
  components: {
    TextField,
    IconRightArrow,
  },
  props: {
    inputFontSize: {
      type: String,
      default: '14px',
    },
    intent: {
      type: String,
      required: false,
      validators: (val: string) => {
        return ['dotted'].includes(val);
      },
    },
  },
  methods: {
    computeClass() {
      let classes = ['input-search', 'w-full', 'h-full'];
      if (this.intent) {
        classes.push(this.intent);
      }
      return classes;
    },
  },
});
</script>

<style lang="scss" scoped>
.container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  width: 100%;
  overflow: hidden;
  gap: 7px;

  .input-search {
    line-height: 3rem;
    font-size: 16px;
    border: 1px solid #ddd;

    &:focus {
      border: 1px dotted #333;
    }
  }

  .item-right-container {
    background-color: #000;
    padding: 0 5px;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;

    .icon {
      transition: all 0.2s ease-in;
    }

    &:hover {
      .icon {
        transform: translateX(7px);
      }
    }
  }
}

.dotted {
  border-bottom: 1px dotted #ddd;
}
</style>
