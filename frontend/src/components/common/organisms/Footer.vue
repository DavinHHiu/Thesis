<template>
  <div class="navLeftFooter nav-sprite-v1" id="navFooter">
    <a id="navBackToTop" aria-label="Back to top">
      <div class="navFooterBackToTop flex items-center justify-center">
        <span
          class="navFooterBackToTopText"
          v-t="'footer.buttonLabel.backToTop'"
          @click="backToTop"
        />
      </div>
    </a>

    <div
      class="navFooterLine navFooterMiddle flex justify-center gap-[15rem]"
      role="navigation"
      aria-label="More on Amazon"
    >
      <div class="app-logo flex flex-col gap-[1.5rem]">
        <span class="app-name" v-t="'app.name'" />
        <span class="app-slogan" v-t="'app.slogan'" />
      </div>
      <div
        v-for="category in categories"
        class="categories flex flex-col gap-[1.5rem]"
      >
        <h2 v-text="category.description" />
        <span
          v-for="subcategory in subcategories[category.id as number]"
          v-text="subcategory.name"
        />
      </div>
      <div class="flex flex-col gap-[1.5rem]">
        <h2 v-t="'footer.subtitle.subscribe'" />
        <text-field :placeholder="$t('footer.placeholder')" />
        <custom-button
          class="w-[15rem] h-[4.5rem] uppercase"
          intent="primary"
          v-text="$t('footer.buttonLabel.subscribe')"
        />
      </div>
    </div>

    <div class="navFooterLine flex justify-center">
      <span v-t="'footer.copyright'" />
    </div>
  </div>
</template>

<script lang="ts">
import { useCategoryStore } from "@/stores/category";
import { SubCategory } from "@/types/worker";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

import CustomButton from "../atomic/CustomButton.vue";
import TextField from "../molecules/TextField.vue";

export default defineComponent({
  name: "Footer",
  components: {
    TextField,
    CustomButton,
  },
  data() {
    return {
      subcategories: {} as { [key: number]: SubCategory[] },
    };
  },
  computed: {
    ...mapState(useCategoryStore, ["categories"]),
  },
  methods: {
    ...mapActions(useCategoryStore, [
      "listCategories",
      "listSubCategoryByCategory",
    ]),
    backToTop() {
      window.scrollTo({ top: 0, behavior: "smooth" });
    },
    async listSubCategory(categoryId: number) {
      await this.listSubCategoryByCategory(categoryId).then(
        (response) => response
      );
    },
  },
  async mounted() {
    await this.listCategories();
    this.categories.forEach((category) => {
      this.listSubCategoryByCategory(category.id as number).then((response) => {
        const listSubCategory = response.data as SubCategory[];
        if (category.id) {
          this.subcategories[category.id] = listSubCategory;
        }
      });
    });
  },
});
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Rubik+Glitch&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Playwrite+CU:wght@100..400&display=swap");
@import "@/assets/variables";

.app-name {
  font-family: "Playwrite CU", cursive;
  font-weight: $--font-bold;
  font-size: $--font-lg;
  text-transform: uppercase;
  color: $--primary-color;
}

.categories {
  span {
    font-size: $--font-base;
  }
}

.app-slogan {
  font-family: "Rubik", cursive;
  font-size: $--font-xl;
  font-weight: $--font-bold;
}

.navLeftFooter {
  position: relative;
  background-color: $--second-color;
  width: 100%;
}

.navFooterBackToTop {
  background-color: $--second-color;
  min-height: 5rem;
  border-top: 1px solid $--color-border;
  cursor: pointer;
  user-select: none;
}

.navFooterLine {
  width: 100%;
  padding: 7rem 0;
  font-size: $--font-xs;
  border-top: 1px solid $--color-border;
  background-color: $--second-color;
}
</style>
