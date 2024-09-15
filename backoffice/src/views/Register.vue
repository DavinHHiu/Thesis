<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <app-logo />
    <card class="w-[40rem] h-[55rem]">
      <div class="h-full p-[1rem] flex flex-col justify-between">
        <p class="text-[28px] font-bold" v-text="$t('buttonLabel.register')" />
        <div class="flex flex-col gap-[3rem]">
          <text-field
            class="h-[5rem]"
            :label="$t('inputLabel.user.email')"
          ></text-field>
          <text-field
            class="h-[5rem]"
            :label="$t('inputLabel.user.password')"
          ></text-field>
          <text-field
            class="h-[5rem]"
            :label="$t('inputLabel.user.retypePassword')"
          ></text-field>
        </div>
        <div class="flex flex-col gap-[2rem]">
          <custom-button
            class="h-[5rem]"
            intent="primary"
            v-text="$t('buttonLabel.register')"
          />
          <divider-break :title="$t('dividerBreak.register')" />
          <custom-button
            class="h-[5rem]"
            intent="p-outline"
            v-text="$t('buttonLabel.login')"
          />
        </div>
      </div>
    </card>
  </div>
</template>
<script lang="ts">
import CustomButton from "../components/common/atomic/CustomButton.vue";
import CustomLabel from "../components/common/atomic/CustomLabel.vue";
import AppLogo from "../components/common/molecules/AppLogo.vue";
import TextField from "../components/common/molecules/TextField.vue";
import DividerBreak from "@/components/common/molecules/DividerBreak.vue";
import Card from "@/components/common/templates/Card.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegisterView",
  components: {
    Card,
    TextField,
    CustomButton,
    AppLogo,
    DividerBreak,
    CustomLabel,
  },
});
</script>
