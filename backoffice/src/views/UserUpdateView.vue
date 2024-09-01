<template>
  <page-title title="Add category" />
  <page-body>
    <card class="flex">
      <section class="upload-wp">
        <upload-preview
          intent="avatar"
          :modelValue="user.avatar"
          @update:model-value="(newValue) => (user.avatar = newValue)"
        />
      </section>
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :value="user.first_name"
          label="First name"
          @update:model-value="(newValue) => (user.first_name = newValue)"
        />
        <text-field
          :value="user.last_name"
          label="Last name"
          @update:model-value="(newValue) => (user.last_name = newValue)"
        />
        <text-field
          :value="user.email"
          label="Email"
          @update:model-value="(newValue) => (user.email = newValue)"
        />
        <password-field
          :value="user.password"
          label="Password"
          @update:model-value="(newValue) => (user.password = newValue)"
        />
        <date-field
          :value="user.birth_of_date"
          label="Birth of date"
          @update:model-value="(newValue) => (user.birth_of_date = newValue)"
        />
        <text-field
          :value="user.tel"
          label="Tel"
          @update:model-value="(newValue) => (user.tel = newValue)"
        />
        <custom-button class="w-[15rem]" @click="handleUpdate"
          >Update</custom-button
        >
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import DateField from "@/components/common/molecules/DateField.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import UploadPreview from "@/components/common/molecules/UploadPreview.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useUserStore } from "@/stores/user";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserUpdateView",
  components: {
    Card,
    CustomButton,
    DateField,
    PageBody,
    PageTitle,
    PasswordField,
    TextField,
    UploadPreview,
    SelectField,
  },
  data() {
    return {
      new: true as boolean,
    };
  },
  methods: {
    ...mapActions(useUserStore, ["createUser", "retrieveUser", "updateUser"]),
    handleUpdate() {
      if (this.new) {
        this.createUser(this.user);
      } else {
        this.updateUser(this.user);
      }
      this.$router.push("/users");
    },
  },
  computed: {
    ...mapState(useUserStore, ["user"]),
  },
  async mounted() {
    const id = this.$router.currentRoute._value.params.id;
    if (id) {
      await this.retrieveUser(id);
      this.new = false;
    }
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/scss/variables";

.upload-wp {
  padding: 2rem 4rem;
  color: $--gray-color-700;
}

.info-wp {
  flex: 1;
  padding: 2rem 4rem;
}
</style>
