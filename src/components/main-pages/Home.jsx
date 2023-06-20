import React, { useState} from "react";
import NavBar from "../NavBar";
import SideBar from "../SideBar";
import "./Home.css";
import AppointmentsList from "../AppointmentsList";
import PatientDetails from "../PatientDetail";
import { convertTo24HourFormat } from "../AppointmentsList";

const Home = () => {
  const [AppointmentPage, setAppointmentPage] = useState(true);
  const [ContentData, setContentData] = useState({});
  const [patientData, setpatientData] = useState(null);
  const [pastAppointments, setpastAppointments] = useState(null);
  const [upcomingAppointments, setupcomingAppointments] = useState(null);
  let DetailButtonState=null;

  const fetchData = async (patient_id) => {
    try {
      const response = await fetch(
        "http://localhost:8000/api/patient/details?id=" + patient_id
      );
      const resData = await response.json();
      if (response.ok) {
        // console.log(resData);
        let temp_list = resData["success"]["appointments"];
        for (let i = 0; i < temp_list.length; i++) {
          let appointment_date = new Date(
            temp_list.Date + " " + convertTo24HourFormat(temp_list.Time)
          );
          if (appointment_date.getTime() < new Date().getTime()) {
            setpastAppointments(pastAppointments + 1);
          } else {
            setupcomingAppointments(upcomingAppointments + 1);
          }
        }
      } else {
        console.log(resData["error"]);

      }
      setpatientData(resData["success"]);
    } catch (error) {
      console.log(error);
    }
  };


  const onContentClick = (appointment_id, patient_id) => {
    // console.log(appointment_id,patient_id);
    setContentData({appointment_id:appointment_id,patient_id:patient_id});
    fetchData(patient_id);
    handleDetailsButton();
  };

  const setDetailButtonState= (changeState) => {
    DetailButtonState=changeState;
    
  };

  const handleAppointmentButton = () => {
    setAppointmentPage(true);
  };

  const handleDetailsButton = () => {
    setAppointmentPage(false);
    // console.log(DetailButtonRef.current);
    DetailButtonState(false);//false here means to set the appointment button active to false and setting details button active
  };

  return (
    <>
      <NavBar />
      <div className="PATIENT-DETAILS">
        <SideBar
          setDetailButtonState={setDetailButtonState}
          onAppointmentButton={handleAppointmentButton}
          onDetailsButton={handleDetailsButton}
        />
        {AppointmentPage ? (
          <AppointmentsList onContentClick={onContentClick} />
        ) : (
          <PatientDetails
            appointment_id={ContentData.appointment_id}
            patient_id={ContentData.patient_id}
            patientDetails={patientData}
            appointment_history={{upcomingAppointments:upcomingAppointments,pastAppointments:pastAppointments}}
          />
        )}
      </div>
    </>
  );
};
export default Home;
