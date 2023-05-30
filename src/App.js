import React from 'react';
import NavBar from './components/NavBar';
import { Routes,Route } from 'react-router-dom';
import Home from './components/Home';
import Error from './components/Error';
// import SideBar from './components/SideBar';
// import ScrollBar from './components/ScrollBar'
// import Download from './components/Download'
// import './components/ScrollBar.css';
function App() {
  // let list=[];
  // for(let i=0;i<90;i++){
  //   list[i]={
  //     name:'Name'+String(i)
  //   }
  // }
  return (
    <div>
      <Routes>
        <Route path='/' Component={Home}/>
        <Route path='/home' Component={NavBar}/>
        <Route path='*' element={<Error/>}/>
      </Routes>
    </div>

  //   <div className='parent'>
  //     <h2>Names</h2><hr/>
  //   <div>
  //     {list.map((x)=><ScrollBar name={x.name}/>)}
  //   </div>
  //   </div>

  );
}

export default App;

