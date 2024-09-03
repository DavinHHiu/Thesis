<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <app-logo />
    <card class="w-[40rem] h-[48rem]">
      <div class="h-full p-[1rem] flex flex-col justify-between">
        <p class="text-[28px] font-bold">Sign in</p>
        <div class="flex flex-col gap-[4rem]">
          <text-field
            :value="loginItem.email"
            label="Email"
            class="h-[5rem]"
            @update:model-value="(newValue) => (loginItem.email = newValue)"
          ></text-field>
          <password-field
            :value="loginItem.password"
            label="Password"
            class="h-[5rem]"
            @update:model-value="(newValue) => (loginItem.password = newValue)"
          ></password-field>
        </div>
        <div class="flex flex-col gap-[2rem]">
          <custom-button class="h-[5rem]" intent="primary" @click="handleLogin"
            >Login</custom-button
          >
          <divider-break title="New to Price Tag?" />
          <custom-button class="h-[5rem]" intent="p-outline"
            >Register</custom-button
          >
        </div>
      </div>
    </card>
  </div>
</template>
<script lang="ts">
import CustomButton from "../components/common/atomic/CustomButton.vue";
import AppLogo from "../components/common/molecules/AppLogo.vue";
import TextField from "../components/common/molecules/TextField.vue";
import DividerBreak from "@/components/common/molecules/DividerBreak.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import Card from "@/components/common/templates/Card.vue";
import { useAuthStore } from "@/stores/auth";
import { LoginItem } from "@/types/backoffice";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "LoginView",
  components: {
    AppLogo,
    Card,
    CustomButton,
    DividerBreak,
    PasswordField,
    TextField,
  },
  data() {
    return {
      loginItem: {} as LoginItem,
    };
  },

  methods: {
    ...mapActions(useAuthStore, ["login"]),
    async handleLogin() {
      await this.login(this.loginItem);
      if (this.isAuthenticated) {
        this.$router.push("/");
      }
    },
  },
  computed: {
    ...mapState(useAuthStore, ["isAuthenticated"]),
  },
});
</script>
