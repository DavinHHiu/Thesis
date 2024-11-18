<template>
  <h2 class="sub-title mb-[2rem]" v-t="'profilePage.subtitle.detail'" />
  <card class="profile-form rounded" intent="form">
    <div class="user-form flex flex-col gap-[2rem]">
      <div class="input-name-wp flex gap-[2rem]">
        <text-field
          class="h-[4.5rem] w-full"
          label="inputLabel.user.firstName"
          :value="user?.first_name as string"
          @update:model-value="(value) => (user.first_name = value)"
        />
        <text-field
          class="h-[4.5rem] w-full"
          label="inputLabel.user.lastName"
          :value="user?.last_name as string"
          @update:model-value="(value) => (user.last_name = value)"
        />
      </div>
      <text-field
        class="h-[4.5rem]"
        label="inputLabel.user.username"
        :value="user?.username as string"
        @update:model-value="(value) => (user.username = value)"
      />
      <text-field
        class="h-[4.5rem]"
        label="inputLabel.user.email"
        :value="user?.email"
        @update:model-value="(value) => (user.email = value)"
      />
      <date-field
        class="h-[4.5rem]"
        label="inputLabel.user.dob"
        :value="user?.dob"
        @update:model-value="(value) => (user.dob = value)"
      />
      <text-field
        class="h-[4.5rem]"
        label="inputLabel.user.tel"
        :value="user?.tel as string"
        @update:model-value="(value) => (user.tel = value)"
      />
      <custom-button
        class="w-[20rem] h-[5rem]"
        intent="primary"
        v-text="$t('buttonLabel.update')"
        @click="updateProfile"
      />
    </div>
  </card>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import Card from "@/components/common/molecules/Card.vue";
import DateField from "@/components/common/molecules/DateField.vue";
import TextField from "@/components/common/molecules/TextField.vue";
import { useSessionStore } from "@/stores/session";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProfileDetailView",
  components: {
    Card,
    CustomButton,
    DateField,
    TextField,
  },
  computed: {
    ...mapState(useSessionStore, ["user"]),
  },
  methods: {
    ...mapActions(useSessionStore, ["refresh", "updateUser"]),
    async updateProfile() {
      const response = await this.updateUser(this.user);
      console.log(response);
    },
  },
  async mounted() {
    // await this.refresh();
    console.log(this.user);
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
