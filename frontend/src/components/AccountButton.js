import React, { useState } from "react";
import { CgProfile } from "react-icons/cg";
import { Link } from "react-router-dom";
import { useRecoilState } from "recoil";
import { profileAtom } from "../states/user";

const AccountButton = () => {
  // create a login button for the navigation bar
  // this button shows a VscAccount icon
  // when clicked, it shows options: login, register, my account, logout
  // when logged in, it shows options: my account, logout
  const [open, setOpen] = useState(false);
  const [profile, setProfile] = useRecoilState(profileAtom);

  return (
    <div className="relative">
      <button
        className="flex items-center focus:outline-none"
        onClick={() => setOpen(!open)}
      >
        <CgProfile className="text-2xl" />
      </button>
      {open && (
        <div className="flex flex-col space-y-2 absolute right-0 w-40 py-2 px-2 mt-2 bg-gray-100 rounded-md shadow-xl">
          {!profile && (
            <Link className="mr-5 hover:text-gray-900" to="/login">
              Login
            </Link>
          )}
          <Link className="mr-5 hover:text-gray-900" to="/account">
            Minha conta
          </Link>

          <div
            onClick={() => {
              localStorage.removeItem("token");
              setProfile(null);
            }}
          >
            Logout
          </div>
        </div>
      )}
    </div>
  );
};

export default AccountButton;
