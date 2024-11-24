<template>
  <div
    :id="id"
    class="modal fade"
    tabindex="-1"
    aria-labelledby="modalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalLabel" v-t="title" />
          <span
            class="material-symbols-outlined btn-close"
            data-bs-dismiss="modal"
            aria-label="Cancel"
            v-text="'close'"
          />
        </div>
        <div class="modal-body"><slot /></div>
        <div class="modal-footer">
          <custom-button
            class="py-[1rem] px-[2rem]"
            intent="p-outline"
            data-bs-dismiss="modal"
            v-text="$t('buttonLabel.cancel')"
          />
          <custom-button
            class="py-[1rem] px-[2rem]"
            @click="handleSubmit"
            data-bs-dismiss="modal"
            intent="primary"
            v-text="$t('buttonLabel.confirm')"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
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
  methods: {
    handleSubmit() {
      this.$emit("submit");
    },
  },
});
</script>
