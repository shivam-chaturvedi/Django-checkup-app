import React from "react";
import './AppointmentContent.css';
import paper from '../components/images/paper.png';
import print from '../components/images/print.png';

export default function AppointmentContent(){
return(
<div className="appointment-content">
      <div className="datetime">
        <span id="appointment-date">26 Nov'19</span>
        <span id="appointment-time">09.00 -10.00</span>
      </div>
      <div className="treatment">
        <span id="treat">Treatment</span>
        <span id="open">Open Access</span>
      </div>
      <div className="note-print">
        <img id="paper" src={paper} alt="paper" />
        <span id="note">Note</span>
        <img id="print" src={print} alt="print" />
      </div>
    </div>

);
}