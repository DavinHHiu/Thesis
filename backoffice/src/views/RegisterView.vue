<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <app-logo />
    <card class="w-[40rem] h-[55rem]">
      <div class="h-full p-[1rem] flex flex-col justify-between">
        <p class="text-[28px] font-bold">Register</p>
        <div class="flex flex-col gap-[3rem]">
          <text-field label="Email" class="h-[5rem]"></text-field>
          <text-field label="Password" class="h-[5rem]"></text-field>
          <text-field label="Re-type password" class="h-[5rem]"></text-field>
        </div>
        <div class="flex flex-col gap-[2rem]">
          <custom-button class="h-[5rem]" intent="primary"
            >Register</custom-button
          >
          <divider-break title="Already have an account?" />
          <custom-button class="h-[5rem]" intent="p-outline"
            >Login</custom-button
          >
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
