interface Category {
  id?: number;
  name: string;
  description: string;
  created_at?: Date;
  updated_at?: Date;
}

interface SubCategory {
  id?: number;
  name: string;
  description: string;
  category: Category;
}

interface User {
  id?: string;
  avatar?: File | string;
  email: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  birth_of_date?: Date;
  tel?: string;
}

interface Address {
  id?: number;
  user: User;
  title: string;
  address_1: string;
  address_2?: string;
  zipcode?: string;
  tel: string;
}

interface ProductAttribute {
  id?: number;
  type: string;
  value: string;
}

interface Product {
  id?: string;
  name: string;
  description?: string;
  summary?: string;
  rating?: number;
  categories: SubCategory[];
}

interface ProductSku {
  id?: string;
  size: ProductAttribute;
  color: ProductAttribute;
  images?: File[];
  sku: string;
  price: number;
  quantity: number;
  product_id?: string;
}

interface ProductImage {
  id?: number;
  image: string;
}

interface ProductSkuDetail {
  id?: string;
  size: ProductAttribute;
  color: ProductAttribute;
  images?: ProductImage[];
  sku: string;
  price: number;
  quantity: number;
  product: Product;
}

interface ProductDetails {
  id?: string;
  name: string;
  description?: string;
  summary?: string;
  rating?: number;
  categories: SubCategory[];
  skus: ProductSkuDetail[];
}

interface Cart {
  id?: string;
  total_quantity?: number;
  total_amount?: number;
  user: User;
}

interface CartItem {
  id?: number;
  cart_id: string;
  product_sku: ProductSkuDetail;
  quantity: number;
  subtotal?: number;
}

interface Order {
  id?: string;
  total_amount?: number;
  status?: string;
  user: User;
}

interface OrderItem {
  id?: string;
  order_id: string;
  product_sku: ProductSkuDetail;
  quantity: number;
  subtotal?: number;
}

export {
  Address,
  Cart,
  CartItem,
  Category,
  Order,
  OrderItem,
  Product,
  ProductImage,
  ProductDetails,
  ProductSkuDetail,
  ProductSku,
  ProductAttribute,
  SubCategory,
  User,
};
