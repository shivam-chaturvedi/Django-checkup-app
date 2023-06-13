import React ,{useState} from "react";
import './AppointmentContentX.css';
import AppointmentContent from "./AppointmentContent";
import ellipse from '../Ellipse 7.png';
import line from '../Line 4.png';
import ellipse2 from '../Ellipse 8.png';


export default function AppointmentContentX(){
    const [ellipse_image,setImage]=useState(ellipse);
    return (
        <div onMouseOver={()=>setImage(ellipse2)} onMouseOut={()=>setImage(ellipse)} className="appoinment-content-x">
            <div className="effect-img">
            <img id="line" src={line} alt="line"/>
            <img id="ellipse" src={ellipse_image} alt="elippse"/>
            <img id="line" src={line} alt="line"/>
            </div> 
            <AppointmentContent/>
        </div>
    );
}