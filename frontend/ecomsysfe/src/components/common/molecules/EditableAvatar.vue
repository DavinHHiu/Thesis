<template>
  <div class="user-avatar-wp">
    <avatar class="user-avatar" :src="src" />
    <custom-button intent="second" class="btn-edit px-[1rem] py-[0.5rem]">
      <icon-pen width="1.5rem" />
      Edit
    </custom-button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Avatar from '../atomic/Avatar.vue';
import CustomButton from '../atomic/CustomButton.vue';
import IconPen from '../../icons/IconPen.vue';

export default defineComponent({
  name: 'EditableAvatar',
  components: {
    Avatar,
    CustomButton,
    IconPen,
  },
  props: {
    src: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

.user-avatar-wp {
  position: relative;
  .btn-edit {
    position: absolute;
    bottom: 0;
    right: 0;
    border-radius: 0.4rem;
    border: 1px solid $--color-border;
  }
}
</style>
