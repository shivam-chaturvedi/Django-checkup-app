import React from "react";
import './Content.css';

function Content(props) {
  return (
    <div className="content">
      <span id="time">{props['time']}</span>
      <span id="date">{props['date']}</span>
      <span id="name">{props['name']}</span>
      <span id="id">{props['id']}</span>
      <span id="condition">{props['condition']}</span>
      <img
        src="https://media.istockphoto.com/id/928418914/vector/trash-can-garbage-can-rubbish-bin-icon.jpg?s=612x612&w=0&k=20&c=3ryjRO7fxFtK05q5NSR_4xrcVOOYMtmS2fzsmwsRchc="
        alt="delete"
      />
    </div>
  );
}
export default Content;
