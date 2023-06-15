import React, { useState } from "react";
import NavBar from "../NavBar";
import SideBar from "../SideBar";
import "./Home.css";
import AppointmentsList from "../AppointmentsList";
import PatientDetails from "../PatientDetail";

const Home = () => {
  const [AppointmentPage, setAppointmentPage] = useState(true);
  const handleAppointmentButton = () => {
    setAppointmentPage(true);
  };
  const handleDetailsButton = () => {
    setAppointmentPage(false);
  };

  return (
    <>
      <NavBar />
      <div className="PATIENT-DETAILS">
        <SideBar
          onAppointmentButton={handleAppointmentButton}
          onDetailsButton={handleDetailsButton}
        />
        {AppointmentPage ? <AppointmentsList /> : <PatientDetails />}
      </div>
    </>
  );
};
export default Home;
