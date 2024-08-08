module.exports = {
  extends: [
    "eslint:recommend",
    "plugin:vue/vue3-recommended",
    "@vue/eslint-config-prettier",
    "@vue/eslint-config-typescript",
    "plugin:prettier/recommended",
    "prettier",
  ],
  parser: "vue-eslint-parser",
  parserOptions: {
    parser: "@typescript-eslint/parser",
  },
  rules: {
    "vue/multi-word-component-names": off,
    "vue/attribute-hyphenation": ["warn"],
    "vue/max-len": [
      "warn",
      {
        code: 80,
        template: 80,
        tabWidth: 2,
        comments: 80,
        ignorePattern: "",
        ignoreComments: false,
        ignoreTrailingComments: false,
        ignoreUrls: false,
        ignoreStrings: false,
        ignoreTemplateLiterals: false,
        ignoreRegExpLiterals: false,
        ignoreHTMLAttributeValues: false,
        ignoreHTMLTextContents: false,
      },
    ],
  },
};
