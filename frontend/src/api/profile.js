import axios from "axios";
import { API_ENDPOINT, API_URL } from "../helpers/constants";

const METHODS = {
  GET: "GET",
  POST: "POST",
  PATCH: "PATCH",
};

export const communicateAPI = async (endpoint, method, data, extraHeaders) => {
  let response = {};
  try {
    const url = `${API_URL}${API_ENDPOINT}${endpoint}`;
    const headers = {
      "Content-Type": "application/json",
      ...extraHeaders,
    };

    const resp = await axios({
      method,
      url,
      data,
      headers,
    });

    response = {
      status: resp.status,
      data: resp.data,
      error: resp.error,
    };
  } catch (error) {
    console.log(error);
    response = {
      status: error?.response?.status || 500,
      data: null,
      error: error?.response?.data?.error || "Unknown error",
    };
  }

  return response;
};

export const postToken = async (login) => {
  const response = await communicateAPI("/token/", METHODS.POST, login);
  return response;
};

export const getUser = async (username = null) => {
  const url = username ? `/profile/${username}/` : "/profile/";
  const response = await communicateAPI(
    url,
    METHODS.GET,
    {},
    {
      Authorization: `Token ${localStorage.getItem("token")}`,
    }
  );
  return response;
};

export const createUser = async (login) => {
  const response = await communicateAPI("/profile/", METHODS.POST, login);
  return response;
};

export const updateProfile = async (profile) => {
  const response = await communicateAPI("/profile/", METHODS.PATCH, profile, {
    Authorization: `Token ${localStorage.getItem("token")}`,
  });
  return response;
};
