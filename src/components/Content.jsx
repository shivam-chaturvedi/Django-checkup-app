import React from "react";
import './Content.css';
import delete_button from '../delete.png'



function Content(props) {
  return (
    <div className="content">
      <span id="time">{props['time']}</span>
      <span id="date">{props['date']}</span>
      <span id="name">{props['name']}</span>
      <span id="id">{props['id']}</span>
      <span id="condition">{props['condition']}</span>
      <img
        src={delete_button}
        alt="delete"
      />
    </div>
  );
}
export default Content;
