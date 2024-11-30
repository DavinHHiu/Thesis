<template>
  <div
    :id="id"
    ref="modal"
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
            v-text="'close'"
          />
        </div>
        <div class="modal-body"><slot /></div>
        <div class="modal-footer">
          <custom-button
            intent="p-outline"
            data-bs-dismiss="modal"
            v-text="'Close'"
          />
          <custom-button
            @click="$emit('confirm')"
            data-bs-dismiss="modal"
            intent="primary"
            v-text="'Confirm'"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "../atomic/CustomButton.vue";
import { Modal } from "bootstrap";
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
  data() {
    return {
      modal: {} as Modal,
    };
  },
  methods: {
    init() {
      const modalElement = this.$refs.modal as HTMLDivElement;
      this.modal = Modal.getOrCreateInstance(modalElement);
    },
    open() {
      this.modal.show();
    },
    close() {
      this.modal.hide();
    },
    dispose() {
      this.modal.dispose();
    },
  },
  mounted() {
    this.init();
  },
});
</script>
