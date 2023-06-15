import React, { useRef, useState, useEffect } from "react";
import "./PatientDetail.css";
import History from "./History";
import Details from "./Details";
import Notes from "./Notes";
import AppointmentHistory from "./AppointmentHistory";
import TextEditor from "./main-pages/TextEditor";

export default function PatientDetail() {
  const [isTextEditorVisible, setIsTextEditorVisible] = useState(false);
  const textEditorRef = useRef(null);

  const handleSaveTextEditor = () => {
    setIsTextEditorVisible(false);
  };

  const handleClick = () => {
    setIsTextEditorVisible(true);
  };

  useEffect(() => {
    document.addEventListener("mousedown", handleMouseDown);
    return () => {
      document.removeEventListener("mousedown", handleMouseDown);
    };
  }, []);

  const handleMouseDown = (event) => {
    if (
      textEditorRef.current &&
      !textEditorRef.current.contains(event.target)
    ) {
      setIsTextEditorVisible(false);
    }
  };

  return (
    <>
      {isTextEditorVisible && (
        <div ref={textEditorRef}>
          <TextEditor onSave={handleSaveTextEditor} />
        </div>
      )}
      <div style={isTextEditorVisible?{filter:"blur(5px)"}:null} className="parent">
        <button onClick={handleClick}>Add Prescription</button>
        <div className="two">
          <History />
          <Details />
          <Notes />
        </div>
        <AppointmentHistory />
      </div>
    </>
  );
}
