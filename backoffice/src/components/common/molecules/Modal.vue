<template>
  <div
    class="modal fade"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <span
            class="material-icons btn-close"
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
          <custom-button intent="primary">Save changes</custom-button>
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
});
</script>
