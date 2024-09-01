import { createRouter, createWebHistory } from "vue-router";

const AddressView = () => import("@/views/AddressView.vue");
const AddressUpdateView = () => import("@/views/AddressUpdateView.vue");
const BaseView = () => import("@/views/BaseView.vue");
const CategoryView = () => import("@/views/CategoryView.vue");
const CategoryUpdateView = () => import("@/views/CategoryUpdateView.vue");
const ProductView = () => import("@/views/ProductView.vue");
const ProductAttributeView = () => import("@/views/ProductAttributeView.vue");
const ProductAttributeUpdateView = () =>
  import("@/views/ProductAttributeUpdateView.vue");
const ProductUpdateView = () => import("@/views/ProductUpdateView.vue");
const SubCategoryView = () => import("@/views/SubCategoryView.vue");
const SubCategoryUpdateView = () => import("@/views/SubCategoryUpdateView.vue");
const UserView = () => import("@/views/UserView.vue");
const UserUpdateView = () => import("@/views/UserUpdateView.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      component: BaseView,
      children: [
        {
          path: "products",
          children: [
            {
              path: "",
              component: ProductView,
            },
            {
              path: "add",
              component: ProductUpdateView,
            },
          ],
        },
        {
          path: "product-attributes",
          children: [
            {
              path: "",
              component: ProductAttributeView,
            },
            {
              path: "add",
              component: ProductAttributeUpdateView,
            },
            {
              path: "update/:id",
              name: "product.attributes.update",
              component: ProductAttributeUpdateView,
            },
          ],
        },
        {
          path: "categories",
          children: [
            {
              path: "",
              component: CategoryView,
            },
            {
              path: "add",
              component: CategoryUpdateView,
            },
            {
              path: "update/:id",
              name: "category.update",
              component: CategoryUpdateView,
            },
          ],
        },
        {
          path: "sub-categories",
          children: [
            {
              path: "",
              component: SubCategoryView,
            },
            {
              path: "add",
              component: SubCategoryUpdateView,
            },
            {
              path: "update/:id",
              name: "subcategory.update",
              component: SubCategoryUpdateView,
            },
          ],
        },
        {
          path: "users",
          children: [
            {
              path: "",
              component: UserView,
            },
            {
              path: "add",
              component: UserUpdateView,
            },
            {
              path: "update/:id",
              name: "user.update",
              component: UserUpdateView,
            },
          ],
        },
        {
          path: "addresses",
          children: [
            {
              path: "",
              component: AddressView,
            },
            {
              path: "add",
              component: AddressUpdateView,
            },
            {
              path: "update/:id",
              name: "address.update",
              component: AddressUpdateView,
            },
          ],
        },
      ],
    },
  ],
});

export default router;
