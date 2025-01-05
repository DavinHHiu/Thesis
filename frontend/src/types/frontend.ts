interface AuthToken {
  access: string;
  refresh: string;
}

interface DropdownItem {
  title: string;
  action: string;
}

interface OptionItem {
  image?: string;
  displayValue: string;
  value: string;
}

interface LoginItem {
  email: string;
  password: string;
}

interface RegisterItem {
  email: string;
  password: string;
  retype_password: string;
}

interface SidebarItem {
  title: string;
  path: string;
  icon: string;
}

interface TabItem {
  title: string;
  path: string;
}

interface Toast {
  id?: number;
  message: string;
  theme: string;
  autohide?: boolean;
  delay?: number;
}

interface FilterPrice {
  min: number;
  max: number;
}

export {
  AuthToken,
  DropdownItem,
  FilterPrice,
  OptionItem,
  LoginItem,
  RegisterItem,
  SidebarItem,
  TabItem,
  Toast,
};
