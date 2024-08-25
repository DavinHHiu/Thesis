<template>
  <div class="alert alert-warning alert-dismissible fade show" role="alert">
    <slot />
    <button
      class="btn-close material-symbols-outlined"
      data-bs-dismiss="alert"
      aria-label="Close"
    >
      close
    </button>
  </div>
</template>

<script lang="ts">
import CustomButton from "../atomic/CustomButton.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Alert",
  components: {
    CustomButton,
  },
});
</script>
