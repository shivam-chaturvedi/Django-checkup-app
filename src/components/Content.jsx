import React from "react";
import "./Content.css";
import delete_button from "../components/images/delete.png";
import { DOMAIN_NAME } from "./main-pages/config";

function Content(props) {
  function onContentClick() {
    props.onContentClick(props["id"], props.patient_id);
    // console.log(props.patient_id);
  }

  const cancelAppointment = async (id) => {
    if (props.appointments_list.length === 1) {
      sessionStorage.setItem("first_loaded", false);
      sessionStorage.removeItem("defaultPatient"); //this is done so last patient id is remved so patientdetails page dont use deleted patient id
    } else {
      sessionStorage.setItem("first_loaded", true);
    }
    try {
      const response = await fetch(
        DOMAIN_NAME + "/api/appointment/cancel?id=" + id,
        { method: "DELETE" }
      );
      const res = await response.json();
      if (response.ok) {
        // console.log(res["success"]);
        // window.location.reload();
        props.fetchAppointments();
        // window.location.replace("/");
      } else {
        console.log(res["error"]);
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="content" onClick={onContentClick}>
      <span id="time">{props["time"]}</span>
      <span id="date">{props["date"]}</span>
      <span id="name">{props["name"]}</span>
      <span id="id">{props["Unique_Id"]}</span>
      <span id="condition">{props["condition"]}</span>
      <img
        src={delete_button}
        alt="delete"
        onClick={(e) => {
          e.stopPropagation();
          cancelAppointment(props.id);
        }}
      />
    </div>
  );
}
export default Content;
