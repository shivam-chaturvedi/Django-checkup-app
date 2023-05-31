import React from "react";
import './Details.css';

function Details(){
    return(
        <div className="details">
        <div className="upper">
            <div className="left">
            <span id="titles-color">Age</span><br/>
            <p id="content" >54 years</p>
            </div>
            <div className="middle">
                <span id="titles-color">Gender</span><br/>
                <p id="content">Male</p>
            </div>
            <div className="right">
                <span id="titles-color">D.O.B</span><br/>
                <p id="content">05-11-1978</p>
            </div>
        </div>
        <div className="lower">
            <div className="left">
                <span id="titles-color">Ph. Number</span><br/>
                <p id="content">+91 2323445434</p>
            </div>
            <div className="middle">
                <span id="titles-color">Address</span><br/>
                <p id="content">
                    B-402,new panchwati colony,ghaziabad,uttar pradesh
                </p>
            </div>
            <div className="right">
                <span id="titles-color">Email</span><br/>
                <p id="content">chaturvedishivam5876.gmail.com</p>
            </div>
        </div>
    </div>
    
    );

}
export default Details;