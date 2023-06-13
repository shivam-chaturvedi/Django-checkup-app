import React from "react";
import "./SideBar.css";
import calendar from '../calendar.png';
import person from '../person.png';

const SideBar = () => {
  return (
    <div className="sidebar">
      <div className="appointments">
        <img id="calendar" src={calendar} alt="img"></img>
        <p>Appointments</p>
      </div>
      <div className="patient-details">
        <img id="person" src={person} alt="img"/>
        <p>Patient Details</p>
      </div>
    </div>
  );
};

export default SideBar;
