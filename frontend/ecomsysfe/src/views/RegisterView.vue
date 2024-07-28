<template>
  <div>
    <div></div>
    <div class="flex flex-col items-center gap-[30px] mt-[50px]">
      <app-logo />
      <card-view
        class="w-[400px] h-[600px] p-[20px] rounded flex flex-col gap-[30px]"
      >
        <p class="text-[28px] font-bold">Sign in</p>
        <div>
          <label class="font-bold">Username or Email Address</label>
          <text-field
            class="w-full h-[50px] rounded border border-slate-400"
            type="email"
          ></text-field>
        </div>
        <div>
          <label class="font-bold">Password</label>
          <text-field
            typp="password"
            class="w-full h-[50px] rounded border border-slate-400"
          ></text-field>
        </div>
        <div>
          <label class="font-bold">Re-enter password</label>
          <text-field
            typp="password"
            class="w-full h-[50px] rounded border border-slate-400"
          ></text-field>
        </div>
        <custom-button class="w-full h-[50px]" intent="primary"
          >Register</custom-button
        >
        <divider-break title="Already have an account?" />
        <custom-button class="w-full h-[50px]" intent="outline"
          >Login</custom-button
        >
      </card-view>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import CardView from '../components/common/CardView.vue';
import TextField from '../components/common/TextField.vue';
import CustomButton from '../components/common/CustomButton.vue';
import AppLogo from '../components/common/AppLogo.vue';
import DividerBreak from '../components/common/DividerBreak.vue';

export default defineComponent({
  name: 'RegisterView',
  components: {
    CardView,
    TextField,
    CustomButton,
    AppLogo,
    DividerBreak,
  },
});
</script>

<style lang="scss" scoped>
@import '@/assets/variables';

label {
  font-size: $--font-sm;
}
</style>
