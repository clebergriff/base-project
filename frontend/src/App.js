import "./App.css";
import { Route, Routes } from "react-router-dom";
import Main from "./pages/Main";
import Navigation from "./components/Navigation";
import Login from "./pages/Login";
import { RecoilRoot } from "recoil";
import Account from "./pages/Account";
import RecoilNexus from "recoil-nexus";

function App() {
  return (
    <RecoilRoot>
      <RecoilNexus />
      <Navigation />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="about" element={<div />} />
        <Route path="login" element={<Login />} />
        <Route path="account" element={<Account />} />
      </Routes>
    </RecoilRoot>
  );
}

export default App;
