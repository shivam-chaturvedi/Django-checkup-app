import React, { useState } from 'react';
import './Login.css';
import login_image from '../login_image.png';
import Home from './Home';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [ShowPassword,setShowPassword]=useState(false);
  const [HomePage,setHomePage]=useState(false);


  const handleSubmit = async (e) => {
    e.preventDefault();
    

    const data = {
      email: email,
      password: password
    };

    try {
      const response = await fetch('http://127.0.0.1:8000//api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      const responseData = await response.json();
      // console.log(responseData)
      
      // Handle the API response
      if (response.ok) {
        localStorage.setItem('access_token',responseData['access_token'])
        localStorage.setItem('refresh_token',responseData['refresh_token'])
        setMessage('Login successful');
        setHomePage(true);
        
      } else {
        setMessage(responseData['error']);
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    

    <div className="login">
      <img id="login-image" src={login_image} alt="login_image" />
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
      <div className="email-input">
        <input onChange={(e)=>setEmail(e.target.value)} type="email" placeholder="Email" required/>
      </div>
      <div className="pass-input">
        <input onChange={(e)=>setPassword(e.target.value)} type={ShowPassword ?"text" :"password"} placeholder="Password" required/>
        <span onClick={()=>setShowPassword(!ShowPassword)}>{ShowPassword?'Hide':'Show'}</span>
              
      </div>
      <span id="forgot">Forgot Password?</span>
      <button type='submit'>Log In</button>
      </form>
      <p style={{textAlign:'center',color:'red' ,fontSize:'20px'}}>{message}</p>
    </div>
   


  );
}

export default LoginForm;