import axios from "axios";

const fetchExchangeRate = async (fromCurrency: string, toCurrency: string) => {
  const response = await axios.get(
    `https://api.exchangerate-api.com/v4/latest/${fromCurrency}`
  );
  if (response.status === 200) {
    return response.data.rates[toCurrency];
  } else {
    throw new Error("Failed to fetch exchange rate");
  }
};

export const formatCurrency = async (locale: string, amount: number) => {
  let defaultLocale = "en-US";
  let currency = "USD";
  if (locale === "vi") {
    const rate = await fetchExchangeRate("USD", "VND");
    defaultLocale = "vi-VN";
    currency = "VND";
    amount *= rate;
  }
  return Intl.NumberFormat(defaultLocale, {
    style: "currency",
    currency: currency,
  }).format(amount);
};
