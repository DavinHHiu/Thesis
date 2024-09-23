import { createRouter, createWebHistory } from "vue-router";

const Address = () => import("@/views/Address.vue");
const AddressUpdate = () => import("@/views/AddressUpdate.vue");
const Base = () => import("@/views/Base.vue");
const Cart = () => import("@/views/Cart.vue");
const CartDetail = () => import("@/views/CartDetail.vue");
const CartUpdate = () => import("@/views/CartUpdate.vue");
const CartItem = () => import("@/views/CartItem.vue");
const CartItemUpdate = () => import("@/views/CartItemUpdate.vue");
const Category = () => import("@/views/Category.vue");
const CategoryDetail = () => import("@/views/CategoryDetail.vue");
const CategoryUpdate = () => import("@/views/CategoryUpdate.vue");
const Home = () => import("@/views/Home.vue");
const Login = () => import("@/views/Login.vue");
const Register = () => import("@/views/Register.vue");
const Order = () => import("@/views/Order.vue");
const OrderDetail = () => import("@/views/OrderDetail.vue");
const OrderItem = () => import("@/views/OrderItem.vue");
const OrderItemUpdate = () => import("@/views/OrderItemUpdate.vue");
const OrderUpdate = () => import("@/views/OrderUpdate.vue");
const Product = () => import("@/views/Product.vue");
const ProductDetail = () => import("@/views/ProductDetail.vue");
const ProductUpdate = () => import("@/views/ProductUpdate.vue");
const ProductSku = () => import("@/views/ProductSku.vue");
const ProductSkuUpdate = () => import("@/views/ProductSkuUpdate.vue");
const ProductAttribute = () => import("@/views/ProductAttribute.vue");
const ProductAttributeUpdate = () =>
  import("@/views/ProductAttributeUpdate.vue");
const SubCategory = () => import("@/views/SubCategory.vue");
const SubCategoryUpdate = () => import("@/views/SubCategoryUpdate.vue");
const UserDetail = () => import("@/views/UserDetail.vue");
const UserAddresses = () => import("@/views/UserAddresses.vue");
const User = () => import("@/views/User.vue");
const UserUpdate = () => import("@/views/UserUpdate.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      name: "base",
      path: "/",
      component: Base,
      children: [
        {
          name: "home",
          path: "dashboard",
          component: Home,
        },
        {
          path: "products",
          children: [
            {
              name: "product.list",
              path: "",
              component: Product,
            },
            {
              name: "product.add",
              path: "add",
              component: ProductUpdate,
            },
            {
              name: "product.detail",
              path: ":productId",
              component: ProductDetail,
              children: [
                {
                  name: "product.update",
                  path: "detail",
                  component: ProductUpdate,
                },
                {
                  name: "product.skus.in.product",
                  path: "product-skus",
                  children: [
                    {
                      name: "product.skus.list",
                      path: "",
                      component: ProductSku,
                    },
                    {
                      name: "product.sku.add",
                      path: "add",
                      component: ProductSkuUpdate,
                    },
                    {
                      name: "product.sku.update",
                      path: "update/:productSkuId",
                      component: ProductSkuUpdate,
                    },
                  ],
                },
              ],
            },
          ],
        },
        {
          path: "product-attributes",
          children: [
            {
              name: "product.attribute.list",
              path: "",
              component: ProductAttribute,
            },
            {
              name: "product.attribute.add",
              path: "add",
              component: ProductAttributeUpdate,
            },
            {
              name: "product.attribute.update",
              path: "update/:id",
              component: ProductAttributeUpdate,
            },
          ],
        },
        {
          path: "categories",
          children: [
            {
              name: "category.list",
              path: "",
              component: Category,
            },
            {
              name: "category.add",
              path: "add",
              component: CategoryUpdate,
            },
            {
              name: "category.detail",
              path: ":categoryId",
              component: CategoryDetail,
              children: [
                {
                  name: "category.update",
                  path: "detail",
                  component: CategoryUpdate,
                },
                {
                  path: "sub-categories",
                  children: [
                    {
                      name: "subcategory.list",
                      path: "",
                      component: SubCategory,
                    },
                    {
                      name: "subcategory.add",
                      path: "add",
                      component: SubCategoryUpdate,
                    },
                    {
                      name: "subcategory.update",
                      path: "update/:subcategoryId",
                      component: SubCategoryUpdate,
                    },
                  ],
                },
              ],
            },
          ],
        },
        {
          path: "users",
          children: [
            {
              name: "user.list",
              path: "",
              component: User,
            },
            {
              name: "user.add",
              path: "add",
              component: UserUpdate,
            },
            {
              name: "user.detail",
              path: "detail",
              component: UserDetail,
              children: [
                {
                  name: "user.update",
                  path: "update/:id",
                  component: UserUpdate,
                },
                {
                  name: "user.addresses",
                  path: "addresses",
                  component: UserAddresses,
                },
              ],
            },
          ],
        },
        {
          path: "addresses",
          children: [
            {
              name: "address.list",
              path: "",
              component: Address,
            },
            {
              name: "address.add",
              path: "add",
              component: AddressUpdate,
            },
            {
              name: "address.update",
              path: "update/:id",
              component: AddressUpdate,
            },
          ],
        },
        {
          path: "carts",
          children: [
            {
              name: "cart.list",
              path: "",
              component: Cart,
            },
            {
              name: "cart.add",
              path: "add",
              component: CartUpdate,
            },
            {
              name: "cart.detail",
              path: ":cartId",
              component: CartDetail,
              children: [
                {
                  name: "cart.update",
                  path: "detail",
                  component: CartUpdate,
                },
                {
                  name: "cart.items",
                  path: "cart-items",
                  children: [
                    {
                      name: "cart.items.list",
                      path: "",
                      component: CartItem,
                    },
                    {
                      name: "cart.item.add",
                      path: "add",
                      component: CartItemUpdate,
                    },
                    {
                      name: "cart.item.update",
                      path: "update/:cartItemId",
                      component: CartItemUpdate,
                    },
                  ],
                },
              ],
            },
          ],
        },
        {
          path: "orders",
          children: [
            {
              name: "order.list",
              path: "",
              component: Order,
            },
            {
              name: "order.add",
              path: "add",
              component: OrderUpdate,
            },
            {
              name: "order.detail",
              path: ":orderId",
              component: OrderDetail,
              children: [
                {
                  name: "order.update",
                  path: "detail",
                  component: OrderDetail,
                },
                {
                  name: "order.items",
                  path: "order-items",
                  children: [
                    {
                      name: "order.items.list",
                      path: "",
                      component: OrderItem,
                    },
                    {
                      name: "order.item.add",
                      path: "add",
                      component: OrderItemUpdate,
                    },
                    {
                      name: "order.item.update",
                      path: "update/:orderItemId",
                      component: OrderItemUpdate,
                    },
                  ],
                },
              ],
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
          component: Login,
        },
        {
          name: "register",
          path: "register",
          component: Register,
        },
      ],
    },
  ],
});

router.beforeEach((to, from) => {
  const isAuthenticated = localStorage.getItem("token");
  if (!isAuthenticated && !["login", "register"].includes(to.name as string)) {
    return { name: "login" };
  }
});

export default router;
