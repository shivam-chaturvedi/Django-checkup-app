import React from "react";
import './Notes.css';

function Notes(){
return(
    <div className="notes">
      <h4>Notes</h4>
      <textarea placeholder="Write notes..."></textarea>
      <button id="save">save note</button>
    </div>
);
}
export default Notes;