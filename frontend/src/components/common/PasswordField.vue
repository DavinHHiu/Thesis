<template>
  <div class="input-wp">
    <input ref="inputRef" :type="type" class="password-input" />
    <div class="icon-eye-wp">
      <icon-eye-on
        v-if="!show"
        class="icon-eye"
        width="20px"
        height="20px"
        color="#ccc"
        @click="toggleShow"
      />
      <icon-eye-off
        v-if="show"
        class="icon-eye"
        width="20px"
        height="20px"
        color="#ccc"
        @click="toggleHidden"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import IconEyeOn from '../icons/IconEyeOn.vue';
import IconEyeOff from '../icons/IconEyeOff.vue';

export default defineComponent({
  name: 'PasswordField',
  components: {
    IconEyeOn,
    IconEyeOff,
  },
  data() {
    return {
      show: false,
    };
  },
  props: {
    type: {
      type: String,
      default: 'password',
    },
  },
  computed: {
    showPass() {
      return this?.$refs?.inputRef?.type === 'password';
    },
  },
  methods: {
    toggleHidden() {
      this.$refs.inputRef.type = 'password';
      this.show = false;
    },
    toggleShow() {
      this.$refs.inputRef.type = 'text';
      this.show = true;
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/_variables.scss';

.input-wp {
  position: relative;
  width: 100%;
  height: 100%;
  .password-input {
    width: 100%;
    height: 100%;
    padding: 15px 12px;
    padding-right: 50px;
    border: 1px solid $--color-border;
    &::after {
      content: '';
    }
  }
  .icon-eye-wp {
    position: absolute;
    top: 0;
    right: 0;
    width: 50px;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
