import React from "react";
import './Details.css';

function Details(){
    return(
        <div className="details">
        <div className="upper">
            <div className="left">
            <span className="titles-color">Age</span><br/>
            <p className="detail-content" >54 years</p>
            </div>
            <div className="middle">
                <span className="titles-color">Gender</span><br/>
                <p id="gender" className="detail-content">Male</p>
            </div>
            <div className="right">
                <span className="titles-color">D.O.B</span><br/>
                <p className="detail-content">05-11-1978</p>
            </div>
        </div>
        <div className="lower">
            <div className="left">
                <span  className="titles-color" >Ph. Number</span><br/>
                <p  className="detail-content">+91 2323445434</p>
            </div>
            <div className="middle">
                <span className="titles-color">Address</span><br/>
                <p className="detail-content">
                  Lorem ipsum dolor sit amet, consectetur adipisicing elit. Esse, provident?
                </p>
            </div>
            <div className="right">
                <span className="titles-color">Email</span><br/>
                <p className="detail-content">chaturvedishivam5876.gmail.com</p>
            </div>
        </div>
    </div>
    
    );

}
export default Details;