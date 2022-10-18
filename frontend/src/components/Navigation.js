import { useEffect } from "react";
import { Link } from "react-router-dom";
import { checkUserProfileByToken } from "../api/helpers";
import AccountButton from "./AccountButton";

const Navigation = () => {
  const imgSrc = "https://via.placeholder.com/150";

  useEffect(() => {
    // check if token is in local storage and load profile
    const token = localStorage.getItem("token");
    if (token) checkUserProfileByToken();
  }, []);

  return (
    <div className="flex flex-col mx-auto flex-wrap p-5 md:flex-row items-center">
      <div className="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <img
          alt="logo"
          className="object-contain h-16 rounded-full border-2 border-gray-300"
          src={imgSrc}
        />
        <span className="ml-3 text-xl">Redelícia</span>
      </div>
      <nav className="md:ml-auto flex flex-wrap items-center text-base justify-center">
        <Link className="mr-5 hover:text-gray-900" to="/">
          Home
        </Link>
        <Link className="mr-5 hover:text-gray-900" to="/about">
          Sobre
        </Link>
        <AccountButton />
      </nav>
    </div>
  );
};

export default Navigation;
