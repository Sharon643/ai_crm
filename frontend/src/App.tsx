import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages/Home";
import ActionItems from "./pages/ActionItems";
import VisitPlanner from "./pages/VisitPlanner";
import { Toaster } from "react-hot-toast";

export default function App() {
  return (
    <BrowserRouter>
      <Toaster
          position="top-right"
          toastOptions={{
              duration: 3000,
          }}
      />
      <Routes>
        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/action-items"
          element={<ActionItems />}
        />
        <Route
            path="/visit-planner"
            element={<VisitPlanner/>}
        />
      </Routes>
    </BrowserRouter>
  );
}