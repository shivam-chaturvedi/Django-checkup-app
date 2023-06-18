import React, { useEffect, useState } from "react";
import Content from "./Content";
import "./AppointmentsList.css";
import search_image from "../components/images/search_image.png";

function AppointmentsList() {
  const [list, setlist] = useState([]);
  const [filteredlist, setfilteredlist] = useState(list);

  const handleSearch = (e) => {
    let query = e.target.value;
    // console.log(query);
    let name = "";
    let temp = list.filter((item) => {
      if (item.Patient.Middle_name === "") {
        name = item.Patient.First_name + " " + item.Patient.Last_name;
      } else {
        name =
          item.Patient.First_name +
          " " +
          item.Patient.Middle_name +
          " " +
          item.Patient.Last_name;
      }
      if (name.toLowerCase().startsWith(query.toLowerCase())) {
        return item;
      }
      return null;
    });
    setfilteredlist(temp);
  };

  const fetchData = async () => {
    try {
      const currentdate = new Date();
      const date =
        currentdate.getFullYear().toString() +
        "-" +
        (currentdate.getMonth() + 1).toString().padStart(2, "0") +
        "-" +
        currentdate.getDate().toString().padStart(2, "0");

      const response = await fetch(
        "http://127.0.0.1:8000/api/appointments?date=" + date
      );
      const resData = await response.json();
      if (response.ok) {
        let temp = resData["success"];
        const sortedAppointments = temp.sort((a, b) => {
          const timeA = convertTo24HourFormat(a.Time);
          const timeB = convertTo24HourFormat(b.Time);
          return (
            new Date("1970/01/01 " + timeA) - new Date("1970/01/01 " + timeB)
          );
        });

        function convertTo24HourFormat(time) {
          const [hour, minute] = String(time).slice(0, -2).split(":");
          const period = String(time).slice(-2);
          let hourIn24Format = parseInt(hour);

          if (period.toLowerCase() === "pm" && hourIn24Format !== 12) {
            hourIn24Format += 12;
          }

          return hourIn24Format.toString().padStart(2, "0") + ":" + minute;
        }
        setlist(sortedAppointments);
        setfilteredlist(sortedAppointments);
      } else {
        console.log(resData["error"]);
      }
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <div className="search-bar">
        <img src={search_image} alt="search" />
        <input
          spellCheck="false"
          type="search"
          placeholder="Search by Patient's name..."
          onChange={handleSearch}
        />
      </div>
      <div className="titles">
        <span>Time</span>
        <span>Date</span>
        <span>Patient Name</span>
        <span>ID</span>
        <span>Condition</span>
      </div>
      {filteredlist.length === 0 ? (
        <h1 id="empty-array-msg">No Appointments!</h1>
      ) : (
        <div className="container">
          {filteredlist.map((item, index) => (
            <Content
              key={index}
              name={
                item.Patient.First_name +
                " " +
                item.Patient.Middle_name +
                " " +
                item.Patient.Last_name
              }
              time={item.Time}
              date={item.Date}
              id={item.Patient.Unique_Id}
              condition={item.Condition}
            />
          ))}
        </div>
      )}
    </div>
  );
}
export default AppointmentsList;
