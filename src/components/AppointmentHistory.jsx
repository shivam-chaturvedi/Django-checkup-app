import React, { useEffect, useState } from "react";
import "./AppointmentHistory.css";
import AppointmentContentX from "./AppointmentContentX";

export default function AppointmentHistory(props) {
  const [previousAppointments, setpreviousAppointments] = useState([]);
  useEffect(() => {
    if(!props.appointments){
      setpreviousAppointments([]);
    }
    else{
    setpreviousAppointments(props.appointments);
    }
    
    // console.log(previousAppointments);
  }, [props]);

  return (
    <div className="aparent">
      <div className="appointment-history">
        <h4>Appointment History</h4>
        <div className="scrollbar">
          {previousAppointments.map((item, index) => {
            // console.log(item.Date,item.Time);
            return <AppointmentContentX key={index} date={item.Date} time={item.Time}/>;
          })}
        </div>
      </div>
    </div>
  );
}
