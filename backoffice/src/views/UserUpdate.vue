<template>
  <page-title v-if="new" :title="pageTitle" />
  <page-body>
    <card class="flex">
      <section class="upload-wp">
        <avatar-preview
          :modelValue="user.avatar"
          @update:model-value="(newValue) => (user.avatar = newValue)"
        />
      </section>
      <section class="info-wp flex flex-col gap-[4rem]">
        <text-field
          :label="$t('inputLabel.user.firstName')"
          :value="user.first_name"
          @update:model-value="(newValue) => (user.first_name = newValue)"
        />
        <text-field
          :label="$t('inputLabel.user.lastName')"
          :value="user.last_name"
          @update:model-value="(newValue) => (user.last_name = newValue)"
        />
        <text-field
          :label="$t('inputLabel.user.email')"
          :value="user.email"
          @update:model-value="(newValue) => (user.email = newValue)"
        />
        <password-field
          :label="$t('inputLabel.user.password')"
          :value="user.password"
          @update:model-value="(newValue) => (user.password = newValue)"
        />
        <date-field
          :label="$t('inputLabel.user.dob')"
          :value="user.birth_of_date"
          @update:model-value="(newValue) => (user.birth_of_date = newValue)"
        />
        <text-field
          :label="$t('inputLabel.user.tel')"
          :value="user.tel"
          @update:model-value="(newValue) => (user.tel = newValue)"
        />
        <div class="flex gap-[2rem]">
          <custom-button
            class="w-[15rem]"
            @click="handleUpdate"
            v-text="textButton"
          />
          <custom-button
            class="w-[15rem]"
            intent="second"
            @click="handleBack"
            v-text="$t('buttonLabel.back')"
          />
        </div>
      </section>
    </card>
  </page-body>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import AvatarPreview from "@/components/common/molecules/AvatarPreview.vue";
import DateField from "@/components/common/molecules/DateField.vue";
import PasswordField from "@/components/common/molecules/PasswordField.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import TabLayout from "@/components/common/molecules/TabLayout.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import Card from "@/components/common/templates/Card.vue";
import PageBody from "@/components/common/templates/PageBody.vue";
import PageTitle from "@/components/common/templates/PageTitle.vue";
import { useUserStore } from "@/stores/user";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "UserUpdateView",
  components: {
    AvatarPreview,
    Card,
    CustomButton,
    DateField,
    PageBody,
    PageTitle,
    PasswordField,
    SelectField,
    TabLayout,
    TextField,
  },
  data() {
    return {
      new: true as boolean,
    };
  },
  methods: {
    ...mapActions(useUserStore, [
      "createUser",
      "retrieveUser",
      "updateUser",
      "resetUser",
    ]),
    handleUpdate() {
      if (this.new) {
        this.createUser(this.user);
      } else {
        this.updateUser(this.user);
      }
      this.$router.push({ name: "user.list" });
    },
    handleBack() {
      this.$router.push({ name: "user.list" });
    },
  },
  computed: {
    ...mapState(useUserStore, ["user"]),
    textButton() {
      return this.new
        ? this.$t("buttonLabel.add")
        : this.$t("buttonLabel.update");
    },
    pageTitle() {
      return this.new
        ? this.$t("userPage.add.title")
        : this.$t("userPage.update.title");
    },
  },
  async mounted() {
    const id = this.$router.currentRoute.value.params.id;
    if (id) {
      await this.retrieveUser(id as string);
      this.new = false;
    }
  },
  beforeRouteLeave() {
    this.resetUser();
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
  width: 100%;
  padding: 4rem 4rem 2rem;
}
</style>
