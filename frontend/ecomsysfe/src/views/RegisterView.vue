<template>
  <div class="flex flex-col items-center gap-[3rem] mt-[5rem]">
    <app-logo />
    <card-view
      class="w-[50rem] h-[60rem] p-[2rem] rounded flex flex-col gap-[3rem]"
    >
      <p class="text-[28px] font-bold">Register</p>
      <div>
        <custom-label>Username or Email Address</custom-label>
        <text-field type="email" class="h-[5rem]"></text-field>
      </div>
      <div>
        <custom-label>Password</custom-label>
        <text-field type="password" class="h-[5rem]"></text-field>
      </div>
      <div>
        <custom-label>Re-enter password</custom-label>
        <text-field type="password" class="h-[5rem]"></text-field>
      </div>
      <custom-button class="h-[5rem]" intent="primary">Register</custom-button>
      <divider-break title="Already have an account?" />
      <custom-button class="h-[5rem]" intent="outline">Login</custom-button>
    </card-view>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import CardView from '../components/common/CardView.vue';
import TextField from '../components/common/molecules/TextField.vue';
import CustomButton from '../components/common/atomic/CustomButton.vue';
import AppLogo from '../components/common/molecules/AppLogo.vue';
import DividerBreak from '../components/common/DividerBreak.vue';
import CustomLabel from '../components/common/atomic/CustomLabel.vue';

export default defineComponent({
  name: 'RegisterView',
  components: {
    CardView,
    TextField,
    CustomButton,
    AppLogo,
    DividerBreak,
    CustomLabel,
  },
});
</script>
