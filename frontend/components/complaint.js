import React from "react";

const Complaint = ({complaint}) => {
  return (
    <div key={complaint.id} className="group relative">
      <div className="min-h-80 aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-md bg-gray-200 group-hover:opacity-75 lg:aspect-none lg:h-80">
        <img
          src="https://source.unsplash.com/random"
          alt={complaint.title}
          className="h-full w-full object-cover object-center lg:h-full lg:w-full"
        />
      </div>
      <div className="mt-4  justify-between">
        <div>
          <h3 className="text-sm text-gray-900">
            <a href={complaint.location}>
              <span aria-hidden="true" className="absolute inset-0" />
              {complaint.title}
            </a>
          </h3>
          <p className="mt-1 text-sm text-gray-500">{complaint.description}</p>
        </div>
        <p className="text-sm font-medium text-gray-900">{complaint.status}</p>
      </div>
    </div>
  );
};

export default Complaint;
