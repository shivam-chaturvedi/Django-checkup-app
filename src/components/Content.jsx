import React from "react";
import './Content.css';
import delete_button from '../components/images/delete.png';

function Content(props) {

  function onContentClick(){
    props.onContentClick(props['id'],props.patient_id);
    // console.log(props.patient_id);
  }

  const cancelAppointment= async(id)=>{
    
    try{
    const response=await fetch('http://localhost:8000/api/appointment/cancel?id='+id,{method:'DELETE'});
    const res=await response.json();
    if(response.ok){
      console.log(res["success"]);
      // window.location.reload();
      window.location.replace("/");
    }
    else{
      console.log(res["error"]);
    }
    }catch(error){
      console.log(error);
    }
  }

  return (
    <div className="content" onClick={onContentClick}>
      <span id="time">{props['time']}</span>
      <span id="date">{props['date']}</span>
      <span id="name">{props['name']}</span>
      <span id="id">{props['Unique_Id']}</span>
      <span id="condition">{props['condition']}</span>
      <img
        src={delete_button}
        alt="delete"
        onClick={(e)=>{
          e.stopPropagation();
          cancelAppointment(props.id)
        }}
      />
    </div>
  );
}
export default Content;
