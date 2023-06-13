import React from "react";
import Content from "./Content";
import "./AppointmentsList.css";
import search_image from '../search_image.png'

function AppointmentsList() {
  
  const details={
    time:'9:30Am',
    date:'23-04-2023',
    name:'Sanjeev Kumar',
    id:'SP006',
    condition:'Fever'
  };
  
  let list=[];
  for (let i=0;i<30;i++){
    list[i]=details;
  }
  return (
    <div>
    <div className="search-bar">
        <img
          src={search_image}
          alt="search"
        />
        <input spellCheck="false" type="search" placeholder="Search by Patient's name..." />
      </div>
      <div className="titles">
        <span>Time</span>
        <span>Date</span>
        <span>Patient Name</span>
        <span>ID</span>
        <span>Condition</span>
      </div>
      
      
    <div className="container">
      {list.map(()=><Content name={details.name} time={details.time} date={details.date} id={details.id} condition={details.condition}/>)}
      {/* <Content name={details.name} time={details.time} date={details.date} id={details.id} condition={details.condition}/> */}
    </div>
    </div>
  );
}
export default AppointmentsList;
