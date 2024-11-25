<template>
  <h2 class="sub-title mb-[2rem]" v-t="'profilePage.subtitle.passwordChange'" />
  <card class="profile-form rounded" intent="form">
    <div class="user-form flex flex-col gap-[2rem]">
      <password-field
        class="h-[4.5rem]"
        label="inputLabel.user.oldPassword"
        :value="password?.old_password"
        @update:model-value="(value) => (password.old_password = value)"
      />
      <password-field
        class="h-[4.5rem]"
        label="inputLabel.user.newPassword"
        :value="password?.new_password"
        @update:model-value="(value) => (password.new_password = value)"
      />
      <password-field
        class="h-[4.5rem]"
        label="inputLabel.user.retypePassword"
        :value="password?.retype_password"
        @update:model-value="(value) => (password.retype_password = value)"
      />
      <custom-button
        class="w-[20rem] h-[5rem]"
        intent="primary"
        v-text="$t('buttonLabel.update')"
        @click="changePassword"
      />
    </div>
  </card>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import Card from "@/components/common/molecules/Card.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import { useSessionStore } from "@/stores/session";
import { useToastStore } from "@/stores/toast";
import { Toast } from "@/types/frontend";
import { Password } from "@/types/worker";
import { mapActions } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProfileChangePasswordView",
  components: {
    Card,
    CustomButton,
    PasswordField,
    TextField,
  },
  data() {
    return {
      password: {} as Password,
    };
  },
  methods: {
    ...mapActions(useSessionStore, ["resetPassword"]),
    ...mapActions(useToastStore, ["toast"]),
    isValidPassword(password: Password) {
      const fields: (keyof Password)[] = [
        "old_password",
        "new_password",
        "retype_password",
      ];
      return fields.every(
        (field) => field in password && Boolean(password[field].trim())
      );
    },
    changePassword() {
      if (this.isValidPassword(this.password)) {
        this.resetPassword(this.password)
          .then(() => {
            this.toast({
              theme: "success",
              message: "changePasswordPage.messages.success",
            });
            this.password = {} as Password;
          })
          .catch(() => {
            this.toast({
              theme: "danger",
              message: "changePasswordPage.messages.fail",
            });
            this.password = {} as Password;
          });
      } else {
        this.toast({
          theme: "danger",
          message: "changePasswordPage.messages.error",
        });
      }
    },
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.profile-form {
  border-radius: 1rem;
  padding: 4rem 2rem;
  .user-form {
    display: flex;
    flex-direction: column;
    gap: 3em;
  }
}

.sub-title {
  border-bottom: 1px solid $--color-border;
  padding: 2rem 0;
}
</style>
