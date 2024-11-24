<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <Toast />
    <app-logo />
    <card class="w-[40rem] h-[48rem]">
      <div class="h-full p-[1rem] flex flex-col justify-between">
        <p class="text-[28px] font-bold" v-t="'loginPage.title'" />
        <div class="flex flex-col gap-[4rem]">
          <text-field
            class="h-[5rem]"
            label="inputLabel.user.email"
            :value="loginItem?.email"
            @update:model-value="(newValue) => (loginItem.email = newValue)"
          ></text-field>
          <password-field
            class="h-[5rem]"
            label="inputLabel.user.password"
            :value="loginItem?.password"
            @update:model-value="(newValue) => (loginItem.password = newValue)"
          ></password-field>
        </div>
        <div class="flex flex-col gap-[2rem]">
          <custom-button
            class="h-[5rem]"
            intent="primary"
            :disabled="loading"
            v-t="'buttonLabel.login'"
            @click="handleLogin"
          />
          <divider-break :title="'dividerBreak.login'" />
          <custom-button
            class="h-[5rem]"
            intent="p-outline"
            :disabled="loading"
            v-t="'buttonLabel.register'"
            @click="routeRegister"
          />
        </div>
      </div>
    </card>
  </div>
</template>
<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import AppLogo from "@/components/common/molecules/AppLogo.vue";
import Card from "@/components/common/molecules/Card.vue";
import DividerBreak from "@/components/common/molecules/DividerBreak.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import { useSessionStore } from "@/stores/session";
import { useToastStore } from "@/stores/toast";
import { LoginItem } from "@/types/frontend";
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
      loading: false,
    };
  },
  methods: {
    ...mapActions(useSessionStore, ["login"]),
    ...mapActions(useToastStore, ["toast"]),
    async handleLogin() {
      try {
        this.loading = true;
        const response = await this.login(this.loginItem);
        if (response && response.status === 200) {
          this.loading = false;
          this.$router.push({ name: "home" });
        }
      } catch (e) {
        this.loading = false;
        this.toast({
          theme: "danger",
          message: "loginPage.message.fail",
        });
      }
    },
    routeRegister() {
      this.$router.push({ name: "register" });
    },
  },
  computed: {
    ...mapState(useSessionStore, ["isAuthenticated"]),
  },
});
</script>
