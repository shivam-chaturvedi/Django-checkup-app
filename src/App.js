import React from 'react';
import { Routes,Route } from 'react-router-dom';
import Login from './components/Login';
import Error from './components/Error';
import FirstPage from './components/FirstPage';
function App() {
  
  return (
    <div>
      <Routes>
        <Route path='/' Component={FirstPage}/>
        <Route path='/login' Component={Login}/>
        <Route path='*' element={<Error/>}/>
      </Routes>
    </div>

  );
}

export default App;

