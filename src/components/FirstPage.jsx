import React from "react";
import "./FirstPage.css";
import checkup_logo from '../checkup_logo.png'
import {useNavigate} from "react-router-dom";

export default function FirstPage() {
    const navigate=useNavigate();
    const moveToLoginPage=()=>{
        navigate('/login');
    }

  return (
    <>
      <div className="starting-page">
        <h1>Let's get started!</h1>
        <div className="rectangle">
          <img src={checkup_logo} alt="checkup" />
        </div>
        <h2>Checkup</h2>
        <button onClick={moveToLoginPage} >Log In</button>
      </div>
    </>
  );
}
