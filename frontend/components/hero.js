import React from "react";
import Link from "next/link";
import Image from "next/image";

const Hero = () => {
  return (
    <section className="mt-24 mx-auto max-w-screen-xl pb-12 px-4 items-center lg:flex md:px-8">
      <div className="space-y-4 flex-1 sm:text-center lg:text-left">
        <h1 className="text-gray-800 font-bold text-4xl xl:text-5xl">
          Convenient and Effective Way for People to Engage with the
          <span className="text-violet-600"> Police</span>
        </h1>

        <p className="text-gray-500 max-w-xl leading-relaxed sm:mx-auto lg:ml-0">
          <span className="font-bold text-2xl text-orange-400">
            Reduce Level of Crimes
          </span>&nbsp;
          Help bring the offender to justice and make sure this doesn't happen
          to anyone else.
        </p>

        
        <p className="text-gray-500 max-w-xl leading-relaxed sm:mx-auto lg:ml-0">
        <span className="font-bold text-2xl text-orange-400">
          Help victims get support
        </span> &nbsp;
          File a crime report by sending your location, description of the crime and a photo as evidence to the police
        </p>

        <div className="pt-10 items-center justify-center space-y-3 sm:space-x-6 sm:space-y-0 sm:flex lg:justify-start">
          <Link
            href="javascript:void(0)"
            className="px-7 py-3 w-full bg-violet-600 text-white text-center rounded-md shadow-md block sm:w-auto"
          >
           Add Report
          </Link>
        </div>
      </div>
      <div className="flex-1 text-center mt-7 lg:mt-0 lg:ml-3">
        <img
          src="https://i.postimg.cc/HxHyt53c/undraw-heatmap-uyye.png"
          className="w-full mx-auto sm:w-10/12  lg:w-full"
        />
      </div>
    </section>
  );
};

export default Hero;
