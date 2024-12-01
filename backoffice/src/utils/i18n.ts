import en from "@/locales/en.yaml";
import vi from "@/locales/vi.yaml";
import { createI18n } from "vue-i18n";

const i18n = createI18n({
  legacy: true,
  globalInjection: true,
  locale: "en",
  fallbackLocale: "en",
  strictMessage: true,
  messages: {
    en,
    vi,
  },
});

export default i18n;
