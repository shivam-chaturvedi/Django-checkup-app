import React from "react";
import NavBar from'./NavBar'
import SideBar from "./SideBar";
import './Home.css';
import History from "./History";
import Details from "./Details";
// import AppointmentsList from "./AppointmentsList";
const Home=()=>{
return (
    <div>
        <NavBar/>
        <div className="middle-section">
        <SideBar />
        <History/>
        <Details/>
        <History/>
        {/* <AppointmentsList/> */}
        </div>
    </div>
);
}
export default Home;