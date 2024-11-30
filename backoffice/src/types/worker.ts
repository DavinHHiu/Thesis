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
  category_id: number;
}

interface User {
  id?: string;
  avatar?: File | string;
  username?: string;
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
}

export {
  Address,
  Province,
  District,
  Ward,
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
