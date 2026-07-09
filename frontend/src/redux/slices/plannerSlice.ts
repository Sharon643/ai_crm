import { createSlice, type PayloadAction } from "@reduxjs/toolkit";

export interface Visit {
  hcp_id: number;
  hcp_name: string;
  hospital: string;
  score: number;
  priority: string;
  reason: string;
}

interface PlannerState {
  visits: Visit[];
}

const initialState: PlannerState = {
  visits: [],
};

const plannerSlice = createSlice({
  name: "planner",
  initialState,

  reducers: {
    setVisitPlan(
      state,
      action: PayloadAction<Visit[]>
    ) {
      state.visits = action.payload;
    },
  },
});

export const { setVisitPlan } =
  plannerSlice.actions;

export default plannerSlice.reducer;