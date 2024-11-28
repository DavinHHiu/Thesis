import en from "@/locales/en.yaml";
import vi from "@/locales/vi.yaml";
import { createI18n } from "vue-i18n";

const i18n = createI18n({
  legacy: true,
  locale: "en",
  fallbackLocale: "en",
  messages: {
    en,
    vi,
  },
  globalInjection: true,
  strictMessage: true,
});

export default i18n;
