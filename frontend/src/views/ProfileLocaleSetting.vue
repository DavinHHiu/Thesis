<template>
  <h2 class="sub-title mb-[2rem]" v-t="'languageSettingsPage.title'" />
  <div class="settings-wp flex flex-col gap-[5rem]">
    <section class="flex flex-col gap-[3rem]">
      <h2
        class="section-title"
        v-t="'languageSettingsPage.subtitle.language'"
      />
      <select-field
        label="languageSettingsPage.label.language"
        :options="[
          { displayValue: 'English', value: 'en' },
          { displayValue: 'Tieng Viet', value: 'vi' },
        ]"
      />
    </section class="flex flex-col gap-[3rem]">
    <section>
      <h2
        class="section-title"
        v-t="'languageSettingsPage.subtitle.currency'"
      />
      <select-field
        label="languageSettingsPage.label.currency"
        :options="[
          { displayValue: 'USD', value: 'usd' },
          { displayValue: 'Dong', value: 'dong' },
        ]"
      />
    </section>
    <section>
      <custom-button         
        class="w-[20rem] h-[5rem]"
        intent="primary"
        v-text="$t('buttonLabel.update')" 
      />
    </section>
  </div>
</template>

<script lang="ts">
import CustomButton from "@/components/common/atomic/CustomButton.vue";
import SelectField from "@/components/common/molecules/SelectField.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProfileLocaleSetting",
  components: {
    CustomButton,
    SelectField,
  },
});
</script>

<style lang="scss" scoped>
@import "@/assets/variables";

.settings-wp {
  padding: 2rem 0;
  section {
    display: flex;
    flex-direction: column;
    gap: 3em;
  }
}

.sub-title {
  border-bottom: 1px solid $--color-border;
  padding: 2rem 0;
}

.section-title {
  font-size: $--font-base;
}
</style>
