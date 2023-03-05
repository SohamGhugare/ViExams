import { useState } from "react";

import { search, hamburger } from "../assets";

const Navbar = () => {

  return (
    <nav className="w-full flex flex-row py-6 justify-between items-center navbar">

      <ul className="list-none flex flex-row justify-between gap-[35vw]">
        <li>
          <img src={search} alt="search" className="w-[124px] h-[32px] cursor-pointer" />
        </li>
        <li>
          <h1 className="font-poppins font-bold cursor-pointer text-[30px] text-white">
            ViExams
          </h1>
        </li>
        <li>
          <img src={hamburger} alt="hamburger" className="w-[124px] h-[32px] cursor-pointer" />
        </li>
      </ul>

      </nav>
  );
};

export default Navbar;
