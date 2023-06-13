import React from "react";
import './AppointmentHistory.css';
import AppointmentContentX from "./AppointmentContentX";

export default function AppointmentHistory() {

  return (
    <div className="aparent">
    <div className="appointment-history">
      <h4>Appointment History</h4>
      <div className="scrollbar">
        <AppointmentContentX/>
        <AppointmentContentX/>
        <AppointmentContentX/>
        <AppointmentContentX/>
        <AppointmentContentX/>
        <AppointmentContentX/>
      </div>
    </div>
    </div> 
  );
}

