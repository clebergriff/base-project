import "./App.css";
import { Route, Routes } from "react-router-dom";
import Main from "./pages/Main";
import Navigation from "./components/Navigation";

function App() {
  return (
    <div>
      <Navigation />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="about" element={<div />} />
      </Routes>
    </div>
  );
}

export default App;
