<template>
  <page-body class="page-wp flex justify-between py-[6rem]">
    <section class="user-sidebar">
      <editable-avatar
        class="w-[20rem] h-[20rem]"
        src="/images/avatars/6.jpg"
      />
    </section>
    <section class="user-profile w-3/4">
      <h2 class="sub-title mb-[2rem]">Profile Details</h2>
      <card class="rounded" intent="form">
        <div class="user-form flex flex-col gap-[2rem]">
          <div class="input-name-wp flex gap-[4.5rem]">
            <div class="w-full">
              <custom-label :required="true">First name</custom-label>
              <text-field class="h-[4.5rem]" :required="true" />
            </div>
            <div class="w-full">
              <custom-label :required="true">Last name</custom-label>
              <text-field class="h-[4.5rem]" :required="true" />
            </div>
          </div>
          <div>
            <custom-label>Company name (optional)</custom-label>
            <text-field class="h-[4.5rem]" :required="false" />
          </div>
          <div>
            <custom-label :required="true">Country / Region</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <div>
            <custom-label :required="true">Street address</custom-label>
            <text-field
              class="h-[4.5rem]"
              :required="true"
              placeholder="House number and street name"
            />
          </div>
          <div>
            <custom-label>Postcode / ZIP (optional)</custom-label>
            <text-field class="h-[4.5rem]" :required="false" />
          </div>
          <div>
            <custom-label :required="true">Town / City</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <div>
            <custom-label :required="true">Phone</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <div>
            <custom-label :required="true">Email address</custom-label>
            <text-field class="h-[4.5rem]" :required="true" />
          </div>
          <custom-button class="w-[20rem] h-[5rem] mt-[2rem]" intent="primary"
            >Update profile</custom-button
          >
        </div>
      </card>
    </section>
  </page-body>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import CustomButton from "../components/common/atomic/CustomButton.vue";
import CustomLabel from "../components/common/atomic/CustomLabel.vue";
import Card from "../components/common/molecules/Card.vue";
import EditableAvatar from "../components/common/molecules/EditableAvatar.vue";
import TextField from "../components/common/molecules/TextField.vue";
import PageBody from "../components/common/templates/PageBody.vue";

export default defineComponent({
  name: "ProfileView",
  components: {
    CustomLabel,
    EditableAvatar,
    PageBody,
    TextField,
    CustomButton,
    Card,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.sub-title {
  border-bottom: 1px solid $--color-border;
  padding: 2rem 0;
}
.user-form {
  margin: 0 auto;
}
</style>
