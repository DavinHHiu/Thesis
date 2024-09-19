<template>
  <div class="action-wrap flex justify-between">
    <custom-button intent="p-outline">
      <span class="material-symbols-outlined" v-text="'filter_alt'" />
      <span v-text="$t('buttonLabel.filter')" />
    </custom-button>
    <custom-button class="btn" :rounded="true" @click="routeAdd">
      <span class="material-symbols-outlined" v-text="'add'" />
      <span v-text="$t('buttonLabel.add')" />
    </custom-button>
  </div>
</template>

<script lang="ts">
import CustomButton from "../atomic/CustomButton.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "HeaderAction",
  components: {
    CustomButton,
  },
  props: {
    currentRoute: {
      type: String,
      required: true,
    },
  },
  methods: {
    routeAdd() {
      this.$router.push({ name: this.currentRoute });
    },
  },
});
</script>

<style lang="scss" scoped></style>
