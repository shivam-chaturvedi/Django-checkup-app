import React, { useRef, useState, useEffect } from "react";
import "./PatientDetail.css";
import History from "./History";
import Details from "./Details";
import Notes from "./Notes";
import AppointmentHistory from "./AppointmentHistory";
import TextEditor from "./main-pages/TextEditor";
import { convertTo24HourFormat } from "./AppointmentsList";
import { DOMAIN_NAME } from "./main-pages/config";

export default function PatientDetail(props) {
  const [isTextEditorVisible, setIsTextEditorVisible] = useState(false);
  const [patientDetails, setpatientDetails] = useState(props.patientDetails);
  const [appointment_history, setappointment_history] = useState(
    props.appointment_history
  );
  // eslint-disable-next-line
  const [isAppointmentsEmpty, setisAppointmentsEmpty] = useState(false);
  const textEditorRef = useRef(null);

  const handleSaveTextEditor = () => {
    setIsTextEditorVisible(false);
  };

  const handleClick = () => {
    setIsTextEditorVisible(true);
  };

  const fetchData = async (patient_id) => {
    let past = 0;
    let upcoming = 0;
    try {
      const response = await fetch(
        DOMAIN_NAME + "/api/patient/details?id=" + patient_id
      );
      const resData = await response.json();
      if (response.ok) {
        setpatientDetails(resData["success"]);
        let temp_list = resData["success"]["appointments"];
        for (let i = 0; i < temp_list.length; i++) {
          let appointment_date = new Date(
            temp_list[i].Date + " " + convertTo24HourFormat(temp_list[i].Time)
          );
          if (appointment_date.getTime() <= new Date().getTime()) {
            past++;
          } else {
            upcoming++;
          }
        }
        // console.log(past,upcoming);
        setappointment_history({
          upcomingAppointments: upcoming,
          pastAppointments: past,
        });
      } else {
        console.log(resData["error"]);
      }
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    if (!props.patient_id) {//props is null when we directly click on content button ain appointments list
      const patient_id = sessionStorage.getItem("defaultPatient");
      // console.log(patient_id);
      if (patient_id) {
        fetchData(patient_id);
      } else {
        setisAppointmentsEmpty(true);
      }
    }

    const handleUnload = () => {
      // console.log(props.setAppointmentPage);
      props.setAppointmentPage(false);
      
      sessionStorage.setItem('first_loaded',true);
      // sessionStorage.setItem('AppointmentPage',false);
    };
    document.addEventListener("mousedown", handleMouseDown);
    window.addEventListener("beforeunload", handleUnload);

    return () => {
      window.removeEventListener("beforeunload", handleUnload);
      document.removeEventListener("mousedown", handleMouseDown);
    };
  }, [props]);

  const handleMouseDown = (event) => {
    if (
      textEditorRef.current &&
      !textEditorRef.current.contains(event.target)
    ) {
      setIsTextEditorVisible(false);
    }
  };

  return (
    <>
      {isTextEditorVisible && (
        <div ref={textEditorRef}>
          <TextEditor onSave={handleSaveTextEditor} />
        </div>
      )}
      {isAppointmentsEmpty?<h1 id="no-appointments-msg">No Appointments!<br/>Patient Not Found</h1>:
        <div
          style={isTextEditorVisible ? { filter: "blur(5px)" } : null}
          className="parent"
        >
          <button onClick={handleClick}>Add Prescription</button>
          <div>
            <div className="two">
              <History
                name={String(patientDetails.First_name + patientDetails.Last_name)}
                unique_id={patientDetails.Unique_Id}
                upcoming={appointment_history.upcomingAppointments}
                past={appointment_history.pastAppointments}
              />
              <Details details={patientDetails} />
              <Notes />
            </div>
            <AppointmentHistory appointments={patientDetails.appointments} />
          </div>
        </div>
}
      
    </>
  );
}
