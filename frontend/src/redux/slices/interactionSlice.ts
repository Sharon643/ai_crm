import { createSlice } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";

export interface InteractionState {
  hcpName: string;
  hospital: string;
  interactionType: string;
  date: string;
  time: string;
  attendees: string;
  topics: string;
  materials: string;
  sentiment: string;
  outcome: string;
  followUp: string;

  loading: boolean;
  error: string | null;
}

const initialState: InteractionState = {
  hcpName: "",
  hospital: "",
  interactionType: "",
  date: "",
  time: "",
  attendees: "",
  topics: "",
  materials: "",
  sentiment: "",
  outcome: "",
  followUp: "",

  loading: false,
  error: null,
};

export type FormField =
  | "hcpName"
  | "hospital"
  | "interactionType"
  | "date"
  | "time"
  | "attendees"
  | "topics"
  | "materials"
  | "sentiment"
  | "outcome"
  | "followUp";

const interactionSlice = createSlice({
  name: "interaction",

  initialState,

  reducers: {
    updateField: (
      state,
      action: PayloadAction<{
        field: FormField;
        value: string;
      }>
    ) => {
      state[action.payload.field] = action.payload.value;
    },

    updateSingleField: (
      state,
      action: PayloadAction<{
        field: FormField;
        value: string;
      }>
    ) => {
      state[action.payload.field] = action.payload.value;
    },

    setForm: (
      state,
      action: PayloadAction<
        Pick<
          InteractionState,
          | "hcpName"
          | "hospital"
          | "interactionType"
          | "date"
          | "time"
          | "attendees"
          | "topics"
          | "materials"
          | "sentiment"
          | "outcome"
          | "followUp"
        >
      >
    ) => {
      Object.assign(state, action.payload);
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

    resetForm: (state) => {
      Object.assign(state, initialState);
    },
  },
});

export const {
  updateField,
  updateSingleField,
  setForm,
  setLoading,
  setError,
  resetForm,
} = interactionSlice.actions;

export default interactionSlice.reducer;