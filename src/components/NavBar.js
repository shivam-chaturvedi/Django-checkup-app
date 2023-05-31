import React ,{ useState }from "react";
import './NavBar.css';
import checkup from '../checkup.png';

const NavBar = () => {

    let up='https://cdn-icons-png.flaticon.com/512/271/271239.png';

    let down='https://cdn-icons-png.flaticon.com/128/32/32195.png';
    const[state,setstate]=useState(false);
    const[image_url,seturl]=useState(up);
    const openmenu=()=>{
        if(state){
            seturl(up);
        }
        else{
            seturl(down);
        }
        setstate(!state);
    
    }

    return(
        <div>
    <div className="navbar">
    <img id="logo" src={checkup} alt="checkup" />
    <div className="child"> 
        <img id="profile-pic" src="https://www.shutterstock.com/image-vector/laptop-blank-screen-silver-color-260nw-1382811212.jpg" alt="profile-pic" />
        <p>Sanjeev Kumar</p>
        <img id ="menu-arrow" onClick={openmenu} src={image_url} alt="Menu"/>
         
    </div>
  </div>
  
  <div className="menu">
  {state && <ul>
      <li><button onClick={openmenu}>Sign Out</button></li><hr/>
      <li><button onClick={openmenu}>Edit Profile</button></li>
  </ul>}
  </div>
  </div>
 
    );
};

export default NavBar;
