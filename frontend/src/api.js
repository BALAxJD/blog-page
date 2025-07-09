import axios from "axios";

const API_BASE_URL = "https://jamesdon.pythonanywhere.com/api";

export const getPosts = async () => {
  return axios.get(`${API_BASE_URL}/posts/`);
};

export const createPost = async (postData) => {
  return axios.post(`${API_BASE_URL}/posts/`, postData);
};

export const updatePostasync = async (id, postData) => {
  return axios.put(`${API_BASE_URL}/posts/${id}/`, postData);
};

export const deletePost = async (id) => {
  return axios.delete(`${API_BASE_URL}/posts/${id}/`);
};