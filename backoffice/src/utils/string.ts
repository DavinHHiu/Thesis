export const fmt = (value: any) => {
  if (Array.isArray(value)) {
    value = value.join(", ").trim();
  }
  return typeof value === "number" || value ? value : "_";
};
