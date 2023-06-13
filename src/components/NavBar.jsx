import React ,{ useState }from "react";
import './NavBar.css';
import checkup from '../checkup.png';
import up from '../up-arrow.png';
import down from '../down-arrow.png';
import profile from '../Profile-pic.png';

const NavBar = () => {


    const[state,setstate]=useState(false);
    const[image_url,setImage_url]=useState(up);
    const openmenu=()=>{
        if(state){
            setImage_url(up);
        }
        else{
            setImage_url(down);
        }
        setstate(!state);
    
    }

    return(
        <div>
    <div className="navbar">
    <img id="logo" src={checkup} alt="checkup" />
    <div className="child"> 
        <img id="profile-pic" src={profile} alt="profile-pic" />
        <p>Sanjeev Kumar</p>
        <img id ="menu-arrow" onClick={openmenu} src={image_url} alt="Menu"/>
         
    </div>
  </div>
  
  <div className="menu">
  {state && <ul>
      <li onClick={openmenu}>Sign Out</li><hr/>
      <li onClick={openmenu}>Edit Profile</li>
  </ul>}
  </div>
  </div>
 
    );
};

export default NavBar;
