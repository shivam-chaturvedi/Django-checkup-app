import React from "react";
import "./History.css";

function History() {
  return (
    <div className="history">
      <p id="his-name">Sanjeev Kumar</p>
      <br />

      <p id="his-id">SP006</p>
      <br />
      <span id="his-appointments">Appointments</span>
      <br />
      <div className="inner-history">
        <div className="past">
          <span id="his-num">5</span>
          <br />
          <span id="his">Past</span>
        </div>
        <div className="vertical"></div>
        <div className="upcoming">
          <span id="his-num">2</span>
          <br />
          <span id="his">Upcoming</span>
        </div>
      </div>
    </div>
  );
}
export default History;
