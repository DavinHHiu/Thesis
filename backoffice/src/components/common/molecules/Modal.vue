<template>
  <div
    :id="id"
    class="modal fade"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">{{ title }}</h5>
          <span
            class="material-symbols-outlined btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            >close
          </span>
        </div>
        <div class="modal-body"><slot /></div>
        <div class="modal-footer">
          <custom-button intent="p-outline" data-bs-dismiss="modal">
            Close
          </custom-button>
          <custom-button
            @click="$emit('confirm')"
            data-bs-dismiss="modal"
            intent="primary"
            >Confirm</custom-button
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "../atomic/CustomButton.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Modal",
  components: {
    CustomButton,
  },
  props: {
    id: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
  },
});
</script>
