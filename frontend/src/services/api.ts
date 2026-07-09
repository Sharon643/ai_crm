import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export default api;

export const createInteraction = (data: unknown) =>
  api.post("/interaction", data);

export const sendChatMessage = (message: string) =>
  api.post("/chat", {
    message,
  });