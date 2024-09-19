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
  images: File[];
  sku: string;
  price: number;
  quantity: number;
  product_id?: string;
}

interface ProductImage {
  image: File[];
}

export {
  Address,
  Category,
  Product,
  ProductImage,
  ProductSku,
  ProductAttribute,
  SubCategory,
  User,
};
