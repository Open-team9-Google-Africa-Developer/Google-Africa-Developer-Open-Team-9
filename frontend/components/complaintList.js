import React from "react";
import Complaint from "./complaint";

const ComplaintList = ({ complaints }) => {
  return (
    <div className="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
      {complaints.map((complaint) => (
        <Complaint complaint={complaint} />
      ))}
    </div>
  );
};

export default ComplaintList;
