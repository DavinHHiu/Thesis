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
  user_id: string;
  title?: string;
  city: string;
  district: string;
  ward: string;
  address_1: string;
  address_2?: string;
  tel: string;
  representative: string;
}

function isAddressValid(address: Address): boolean {
  const requiredFields: (keyof Address)[] = [
    "user_id",
    "city",
    "district",
    "ward",
    "address_1",
    "tel",
    "representative",
  ];

  return requiredFields.every(
    (field) => field in address && Boolean(address[field])
  );
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

interface PaymentMethod {
  id?: number;
  icon?: string;
  name: string;
  value: string;
  description: string;
  is_active?: boolean;
}

interface Payment {
  id?: number;
  order_id?: string;
  payment_method: PaymentMethod;
  status: string;
  total_amount: number;
}

interface ShipmentMethod {
  id?: number;
  name: string;
  value: string;
  description: string;
  estimated_shipping_days: number;
  shipping_fee: number;
  is_active?: boolean;
}

interface Shipment {
  id?: number;
  order_id?: string;
  receive_address: Address;
  shipment_method: ShipmentMethod;
  shipping_date: Date;
  status: string;
}

interface Order {
  id?: string;
  user_id: string;
  shipment: Shipment;
  payment: Payment;
  total_quantity: number;
  status: string;
}

interface OrderItem {
  id?: string;
  order_id: string;
  product_sku: ProductSkuDetail;
  product: Product;
  quantity: number;
  subtotal: number;
}

export {
  Address,
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
  Order,
  OrderItem,
  User,
  PaymentMethod,
  Payment,
  ShipmentMethod,
  Shipment,
  isAddressValid,
};
