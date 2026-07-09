import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface ChatMessage {
  sender: "user" | "assistant";
  message: string;
}

interface ChatState {
  messages: ChatMessage[];
  loading: boolean;
  error: string | null;
}

const initialState: ChatState = {
  messages: [],
  loading: false,
  error: null,
};

const chatSlice = createSlice({
  name: "chat",

  initialState,

  reducers: {
    addMessage: (
      state,
      action: PayloadAction<ChatMessage>
    ) => {
      state.messages.push(action.payload);
    },

    clearChat: (state) => {
      state.messages = [];
    },

    setLoading: (
      state,
      action: PayloadAction<boolean>
    ) => {
      state.loading = action.payload;
    },

    setError: (
      state,
      action: PayloadAction<string | null>
    ) => {
      state.error = action.payload;
    },
  },
});

export const {
  addMessage,
  clearChat,
  setLoading,
  setError,
} = chatSlice.actions;

export default chatSlice.reducer;