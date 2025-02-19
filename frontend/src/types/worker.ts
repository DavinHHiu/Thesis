interface User {
  id?: string;
  avatar?: File | string;
  email: string;
  username?: string;
  first_name?: string;
  last_name?: string;
  password?: string;
  dob?: Date;
  tel?: string;
}

interface Password {
  old_password: string;
  new_password: string;
  retype_password: string;
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
  display_address1?: string;
}

function isAddressValid(address: Address): boolean {
  const requiredFields: (keyof Address)[] = [
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

interface Province {
  code: number;
  name: string;
  division_type: string;
  codename: string;
  phone_code: number;
  is_active: boolean;
}

interface District {
  code: number;
  name: string;
  division_type: string;
  codename: string;
  province_code: number;
  is_active: boolean;
}

interface Ward {
  code: number;
  name: string;
  division_type: string;
  codename: string;
  district_code: number;
  is_active: boolean;
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
  colors: string[];
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
  Province,
  District,
  Ward,
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
  Password,
  PaymentMethod,
  Payment,
  ShipmentMethod,
  Shipment,
  isAddressValid,
};
