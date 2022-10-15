import "./App.css";
import { Route, Routes } from "react-router-dom";
import Main from "./pages/Main";
import Navigation from "./components/Navigation";
import Login from "./pages/Login";
import { RecoilRoot } from "recoil";

function App() {
  return (
    <RecoilRoot>
      <Navigation />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="about" element={<div />} />
        <Route path="login" element={<Login />} />
      </Routes>
    </RecoilRoot>
  );
}

export default App;
