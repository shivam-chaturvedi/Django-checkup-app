import React from "react";
import NavBar from "./NavBar";
import SideBar from "./SideBar";
import "./Home.css";
import AppointmentsList from "./AppointmentsList";
import PatientDetails from './PatientDetail';
// import Page from './Page';
const Home = () => {
  return (
    <>
    <NavBar/> 
    <div className="PATIENT-DETAILS">
    <SideBar/>
    <PatientDetails/>
    {/* <AppointmentsList/> */}
    </div>
    
    </>

  );
};
export default Home;
