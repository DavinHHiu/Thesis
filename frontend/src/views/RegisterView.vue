<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <Toast />
    <app-logo />
    <card class="w-[40rem] h-[55rem]">
      <div class="h-full p-[1rem] flex flex-col justify-between">
        <p class="text-[28px] font-bold" v-t="'buttonLabel.register'" />
        <div class="flex flex-col gap-[4rem]">
          <text-field
            class="h-[5rem]"
            :label="'inputLabel.user.email'"
            :value="registerItem.email"
            @update:model-value="(newValue) => (registerItem.email = newValue)"
          ></text-field>
          <password-field
            class="h-[5rem]"
            :label="'inputLabel.user.password'"
            :value="registerItem.password"
            @update:model-value="
              (newValue) => (registerItem.password = newValue)
            "
          ></password-field>
          <password-field
            class="h-[5rem]"
            :label="'inputLabel.user.retypePassword'"
            :value="registerItem.retype_password"
            @update:model-value="
              (newValue) => (registerItem.retype_password = newValue)
            "
          ></password-field>
        </div>
        <div class="flex flex-col gap-[2rem]">
          <custom-button
            class="h-[5rem]"
            intent="primary"
            :disabled="loading"
            v-text="$t('buttonLabel.register')"
            @click="handleRegister"
          />
          <divider-break :title="'dividerBreak.register'" />
          <custom-button
            class="h-[5rem]"
            intent="p-outline"
            :disabled="loading"
            v-t="'buttonLabel.login'"
            @click="routeLogin"
          />
        </div>
      </div>
    </card>
  </div>
</template>
<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomLabel from "@/components/common/atomic/CustomLabel.vue";
import AppLogo from "@/components/common/molecules/AppLogo.vue";
import Card from "@/components/common/molecules/Card.vue";
import DividerBreak from "@/components/common/molecules/DividerBreak.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import { useSessionStore } from "@/stores/session";
import { useToastStore } from "@/stores/toast";
import { RegisterItem } from "@/types/frontend";
import { AxiosError } from "axios";
import _ from "lodash";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegisterView",
  components: {
    AppLogo,
    Card,
    CustomButton,
    CustomLabel,
    DividerBreak,
    PasswordField,
    TextField,
  },
  data() {
    return {
      registerItem: {
        email: "",
        password: "",
        retype_password: "",
      } as RegisterItem,
      loading: false,
    };
  },
  methods: {
    ...mapActions(useSessionStore, ["register"]),
    ...mapActions(useToastStore, ["toast"]),
    async handleRegister() {
      this.loading = true;
      if (
        !_.every(
          this.registerItem,
          (field) => !_.isNil(field) && !_.isEmpty(field)
        )
      ) {
        this.toast({
          theme: "danger",
          message: "registerPage.message.warn",
        });
        this.loading = false;
        return;
      }

      this.register(this.registerItem)
        .then(() => {
          this.toast({
            theme: "success",
            message: "registerPage.message.success",
          });
          setTimeout(() => this.$router.push({ name: "login" }), 1000);
        })
        .catch((err) => {
          const message = err.response.data.non_field_errors[0];
          this.loading = false;
          this.toast({
            theme: "danger",
            message: message,
          });
        });
    },
    routeLogin() {
      this.$router.push({ name: "login" });
    },
  },
  computed: {
    ...mapState(useSessionStore, ["user"]),
  },
});
</script>
