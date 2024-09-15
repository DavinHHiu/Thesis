<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <app-logo />
    <card class="w-[40rem] h-[55rem]">
      <div class="h-full p-[1rem] flex flex-col justify-between">
        <p class="text-[28px] font-bold" v-text="$t('buttonLabel.register')" />
        <div class="flex flex-col gap-[4rem]">
          <text-field
            class="h-[5rem]"
            :label="$t('inputLabel.user.email')"
            :value="registerItem.email"
            @update:model-value="(newValue) => (registerItem.email = newValue)"
          ></text-field>
          <password-field
            class="h-[5rem]"
            :label="$t('inputLabel.user.password')"
            :value="registerItem.password"
            @update:model-value="
              (newValue) => (registerItem.password = newValue)
            "
          ></password-field>
          <password-field
            class="h-[5rem]"
            :label="$t('inputLabel.user.retypePassword')"
            :value="registerItem.retypePassword"
            @update:model-value="
              (newValue) => (registerItem.retypePassword = newValue)
            "
          ></password-field>
        </div>
        <div class="flex flex-col gap-[2rem]">
          <custom-button
            class="h-[5rem]"
            intent="primary"
            v-text="$t('buttonLabel.register')"
            @click="handleRegister"
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
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import CustomLabel from "@/components/common/atomic/CustomLabel.vue";
import AppLogo from "@/components/common/molecules/AppLogo.vue";
import Card from "@/components/common/molecules/Card.vue";
import DividerBreak from "@/components/common/molecules/DividerBreak.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import { useSessionStore } from "@/stores/session";
import { RegisterItem } from "@/types/frontend";
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
        retypePassword: "",
      } as RegisterItem,
    };
  },
  methods: {
    ...mapActions(useSessionStore, ["register"]),
    handleRegister() {
      // Check fields not empty
      if (
        !_.every(
          this.registerItem,
          (field) => !_.isNil(field) && !_.isEmpty(field)
        )
      ) {
        alert("Please fill out all the required fields");
      }

      //Register the user
      this.register(this.registerItem).then((response) => {
        if (response && response.status === 201) {
          alert("User registered successfully");
          this.$router.push("/login");
        } else {
          alert("Failed to register user");
        }
      });
    },
  },
  computed: {
    ...mapState(useSessionStore, ["user"]),
  },
});
</script>
