import { configureStore } from "@reduxjs/toolkit";

import interactionReducer from "./slices/interactionSlice";
import chatReducer from "./slices/chatSlice";
import plannerReducer from "./slices/plannerSlice";

export const store = configureStore({
  reducer: {
    interaction: interactionReducer,
    chat: chatReducer,
    planner: plannerReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;