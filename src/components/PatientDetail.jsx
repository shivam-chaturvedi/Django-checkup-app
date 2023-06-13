import React from "react";
import "./PatientDetail.css";
import History from "./History";
import Details from "./Details";
import Notes from "./Notes";
import AppointmentHistory from "./AppointmentHistory";

 export default function Page(){
    return (
        <div className="parent">
            <button>Add Prescription</button>
            <div className="two">
                <History/>
                <Details/>
                <Notes/>
            </div>
            <AppointmentHistory/>
        </div>
    );
}