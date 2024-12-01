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
  value: string;
  displayValue: string;
}

interface Period {
  start_date: String;
  end_date: String;
}

interface LoginItem {
  email: string;
  password: string;
}

interface SidebarItem {
  title: string;
  path: string;
  icon: string;
}

interface TabItem {
  title: string;
  name?: string;
  path?: string;
}

interface Toast {
  id?: number;
  message: string;
  theme: string;
  autohide?: boolean;
  delay?: number;
}
interface NavPillItem {
  title: string;
  quantity: number;
}

export {
  AuthToken,
  DropdownItem,
  OptionItem,
  Period,
  LoginItem,
  SidebarItem,
  TabItem,
  Toast,
  NavPillItem,
};
