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

interface Category {
  id?: number;
  name: string;
  description: string;
  created_at?: Date;
  updated_at?: Date;
}

interface ColorDisplay {
  color: string;
  image: string;
  totalQuantity: number;
}

interface SizeDisplay {
  size: string;
  disabled: boolean;
}

interface SubCategory {
  id?: number;
  name: string;
  description: string;
  category: Category;
}

interface ProductAttribute {
  id?: number;
  type: string;
  value: string;
}

interface Product {
  id?: string;
  name: string;
  rating?: number;
  categories: string[];
  prices: number[];
  images: string[];
}

interface ProductSkuDetail {
  id?: string;
  size: string;
  color: string;
  price: number;
  quantity: number;
  images: string[];
}

interface ProductDetail {
  id?: string;
  name: string;
  rating?: number;
  description?: string;
  summary?: string;
  categories: string[];
  skus: ProductSkuDetail[];
}

interface ProductSku {
  id?: string;
  size: ProductAttribute;
  color: ProductAttribute;
  images: ProductImage[];
  sku: string;
  price: number;
  quantity: number;
  product_id?: string;
}

interface ProductImage {
  id?: number;
  image: string;
}

interface Cart {
  id?: string;
  user: User;
  total_quantity: number;
  total_amount: number;
}

interface NewCartItem {
  cart_id: string;
  product_sku_id: string;
  quantity: number;
}

interface CartItem {
  id?: number;
  cart_id: string;
  product_sku: ProductSkuDetail;
  product: Product;
  quantity: number;
  subtotal: number;
}

export {
  Cart,
  CartItem,
  NewCartItem,
  Category,
  ColorDisplay,
  Product,
  ProductDetail,
  ProductImage,
  ProductSku,
  ProductSkuDetail,
  ProductAttribute,
  SizeDisplay,
  SubCategory,
  User,
};
