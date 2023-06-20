import React, { useEffect,useState } from "react";
import "./SideBar.css";
import calendar from "../components/images/calendar.png";
import person from "../components/images/person.png";

const SideBar = ({ onAppointmentButton, onDetailsButton ,setDetailButtonState}) => {
  const [activeButton, setactiveButton] = useState(true);

  useEffect(()=>{
    setDetailButtonState(setactiveButton);

  },[setDetailButtonState]);

  const handleAppointmentButton = () => {
    setactiveButton(true);
    onAppointmentButton();
  };
  const handleDetailsButton = () => {
    setactiveButton(false);
    onDetailsButton();
  };
  return (
    <div className="sidebar">
      <div
        style={
          activeButton
            ? { backgroundColor: "white", boxShadow: "0px 0px 10px" }
            : null
        }
        onClick={handleAppointmentButton}
        className="appointments"
      >
        <img id="calendar" src={calendar} alt="img"></img>
        <p>Appointments</p>
      </div>
      <div
      
        style={
          !(activeButton)
            ? { backgroundColor: "white", boxShadow: "0px 0px 10px" }
            : null
        }
        onClick={handleDetailsButton}
        className="patient-details"
      >
        <img id="person" src={person} alt="img" />
        <p>Patient Details</p>
      </div>
    </div>
  );
};

export default SideBar;
