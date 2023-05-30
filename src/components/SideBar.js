import React from "react";
import "./SideBar.css";

const SideBar = () => {
  return (
    <div className="sidebar">
      <div className="appointments">
        <img src="https://images.template.net/wp-content/uploads/2016/04/22060254/Calendra-Icon.jpg" alt="img"></img>
        <p>Appointments</p>
      </div>
      <div className="patient-details">
        <img src="https://www.shutterstock.com/image-vector/person-icon-260nw-282598823.jpg" alt="img"/>
        <p>Patient Details</p>
      </div>
    </div>
  );
};

export default SideBar;
