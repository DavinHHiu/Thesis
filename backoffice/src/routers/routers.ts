import { createRouter, createWebHistory } from "vue-router";

const AddressView = () => import("@/views/AddressView.vue");
const AddressUpdateView = () => import("@/views/AddressUpdateView.vue");
const BaseView = () => import("@/views/BaseView.vue");
const CategoryView = () => import("@/views/CategoryView.vue");
const CategoryUpdateView = () => import("@/views/CategoryUpdateView.vue");
const HomeView = () => import("@/views/Home.vue");
const LoginView = () => import("@/views/LoginView.vue");
const RegisterView = () => import("@/views/RegisterView.vue");
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
      name: "base",
      path: "/",
      component: BaseView,
      children: [
        {
          name: "home",
          path: "",
          component: HomeView,
        },
        {
          path: "products",
          children: [
            {
              name: "product.list",
              path: "",
              component: ProductView,
            },
            {
              name: "product.add",
              path: "add",
              component: ProductUpdateView,
            },
            {
              name: "product.update",
              path: "update/:id",
              component: ProductUpdateView,
            },
          ],
        },
        {
          path: "product-attributes",
          children: [
            {
              name: "product.attribute.list",
              path: "",
              component: ProductAttributeView,
            },
            {
              name: "product.attribute.add",
              path: "add",
              component: ProductAttributeUpdateView,
            },
            {
              name: "product.attribute.update",
              path: "update/:id",
              component: ProductAttributeUpdateView,
            },
          ],
        },
        {
          path: "categories",
          children: [
            {
              name: "category.list",
              path: "",
              component: CategoryView,
            },
            {
              name: "category.add",
              path: "add",
              component: CategoryUpdateView,
            },
            {
              name: "category.update",
              path: "update/:id",
              component: CategoryUpdateView,
            },
          ],
        },
        {
          path: "sub-categories",
          children: [
            {
              name: "subcategory.list",
              path: "",
              component: SubCategoryView,
            },
            {
              name: "subcategory.add",
              path: "add",
              component: SubCategoryUpdateView,
            },
            {
              name: "subcategory.update",
              path: "update/:id",
              component: SubCategoryUpdateView,
            },
          ],
        },
        {
          path: "users",
          children: [
            {
              name: "user.list",
              path: "",
              component: UserView,
            },
            {
              name: "user.add",
              path: "add",
              component: UserUpdateView,
            },
            {
              name: "user.update",
              path: "update/:id",
              component: UserUpdateView,
            },
          ],
        },
        {
          path: "addresses",
          children: [
            {
              name: "address.list",
              path: "",
              component: AddressView,
            },
            {
              name: "address.add",
              path: "add",
              component: AddressUpdateView,
            },
            {
              name: "address.update",
              path: "update/:id",
              component: AddressUpdateView,
            },
          ],
        },
      ],
    },
    {
      path: "/",
      children: [
        {
          name: "login",
          path: "login",
          component: LoginView,
        },
        {
          name: "register",
          path: "register",
          component: RegisterView,
        },
      ],
    },
  ],
});

router.beforeEach((to, from) => {
  const isAuthenticated = localStorage.getItem("authTokens");
  if (!isAuthenticated && !["login", "register"].includes(to.name as string)) {
    return { name: "login" };
  }
});

export default router;
