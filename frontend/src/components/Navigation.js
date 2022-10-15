import { Link } from "react-router-dom";

const Navigation = () => {
  const imgSrc = "https://via.placeholder.com/150";

  return (
    <div className="flex flex-col mx-auto flex-wrap p-5 md:flex-row items-center">
      <div className="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <img
          alt="logo"
          className="object-contain h-16 rounded-full border-2 border-gray-300"
          src={imgSrc}
        />
        <span className="ml-3 text-xl">Project Name</span>
      </div>
      <nav className="md:ml-auto flex flex-wrap items-center text-base justify-center">
        <Link className="mr-5 hover:text-gray-900" to="/">
          Home
        </Link>
        <Link className="mr-5 hover:text-gray-900" to="/about">
          About
        </Link>
      </nav>
    </div>
  );
};

export default Navigation;
