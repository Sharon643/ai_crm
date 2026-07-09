import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Home from "./pages/Home";
import ActionItems from "./pages/ActionItems";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/action-items"
          element={<ActionItems />}
        />
      </Routes>
    </BrowserRouter>
  );
}