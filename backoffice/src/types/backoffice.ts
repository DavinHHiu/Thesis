interface AuthToken {
  access: string;
  refresh: string;
}

interface DropdownItem {
  title: string;
  action: string;
}

interface OptionItem {
  displayValue: string;
  value: string;
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

export { AuthToken, DropdownItem, OptionItem, LoginItem, SidebarItem, TabItem };
