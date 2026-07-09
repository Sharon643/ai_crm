import api from "./api";

export const getActionItems = () =>
  api.get("/action-items");

export const updateActionItem = (
  id: number,
  status: "Pending" | "Completed"
) =>
  api.patch(`/action-items/${id}`, {
    status,
  });