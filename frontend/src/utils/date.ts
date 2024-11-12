export const formatDate = (dateString: Date) => {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat("en-GB", {
    year: "numeric",
    month: "long",
    day: "numeric",
  }).format(date);
};
