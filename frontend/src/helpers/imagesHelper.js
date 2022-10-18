import { API_URL } from "./constants";

export const getImageUrl = (path) => {
  return `${API_URL}${path}`;
};
