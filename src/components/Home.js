import React from "react";
import NavBar from'./NavBar'
import SideBar from "./SideBar";
import './Home.css'
import AppointmentsList from "./AppointmentsList";
const Home=()=>{
return (
    <div>
        <NavBar/>
        <div className="middle-section">
        <SideBar />
        <AppointmentsList/>
        </div>
    </div>
);
}
export default Home;