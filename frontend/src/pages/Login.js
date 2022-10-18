import React, { useEffect, useState } from "react";
import { useRecoilState, useRecoilValue } from "recoil";
import { checkUserProfileByToken, showAPIResponse } from "../api/helpers";
import { createUser, getUser, postToken } from "../api/profile";
import { profileAtom } from "../states/user";
import "./Login.css";

const MODES = {
  LOGIN: "login",
  REGISTER: "register",
};

const Login = () => {
  // create a login screen with sign up and login buttons
  // sign up takes to a modal asking for username and password
  //   create a state that changes between login and sign up
  const [mode, setMode] = useState(MODES.LOGIN);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [profile, setProfile] = useRecoilState(profileAtom);
  const isLoginMode = mode === MODES.LOGIN;

  const checkUserProfileByName = async (username) => {
    const response = await postToken(username);

    if (response.status === 200) {
      localStorage.setItem("token", response.data.token);
      checkUserProfileByToken();
    } else {
      showAPIResponse(response.error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const login = {
      username: username,
      password: password,
    };

    if (mode === MODES.LOGIN) {
      checkUserProfileByName(login);
    } else {
      const resp = await createUser(login);
      if (!!resp.error) showAPIResponse(resp.error);
      else showAPIResponse(resp.data);
    }
  };

  return (
    <div>
      <div className="flex flex-col items-center">
        {profile ? (
          <div>
            <h1>Usuário logado</h1>
            <p>Nome: {profile.username}</p>
            <p>Id: {profile.id}</p>
          </div>
        ) : (
          <>
            <input
              type="text"
              placeholder="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <input
              type="password"
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={async (e) => await handleSubmit(e)}>
              {isLoginMode ? "Login" : "Registrar"}
            </button>
            <button
              onClick={() =>
                setMode(isLoginMode ? MODES.REGISTER : MODES.LOGIN)
              }
            >
              {isLoginMode
                ? "Não possui login? Cadastre-se aqui!"
                : "Já possui cadastro? Entre aqui!"}
            </button>
          </>
        )}
      </div>
    </div>
  );
};

export default Login;
