import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import "./TextEditor.css";

const TextEditor = ({ onSave }) => {
  const [content, setContent] = useState("");
  const [dragging, setdragging] = useState(false);
  const [position, setPosition] = useState({ x: 200, y: 200 });
  const [startPosition, setStartPosition] = useState({ x: 0, y: 0});

  const handleMouseMove = (e) => {
    if (!dragging) return;
    const deltaX = e.clientX - startPosition.x;
    const deltaY = e.clientY - startPosition.y;
    setPosition((prevPosition) => ({
      x: prevPosition.x + deltaX,
      y: prevPosition.y + deltaY,
    }));
    setStartPosition({ x: e.clientX, y: e.clientY });
  };

  const handleChange = (value) => {
    setContent(value);
  };

  const handleSave = (e) => {
    onSave();
  };

  const modules = {
    toolbar: {
      container: [
        // [{'customButton':{ style: { backgroundColor: '#e6e6e6', color: '#333333' } }}],
        [{ header: [1, 2, 3, 4, 5, 6, false] }],
        ["bold", "italic", "underline", "strike"],
        [{ list: "ordered" }, { list: "bullet" }],
        [{ indent: "-1" }, { indent: "+1" }],
        ["link", "image"],
        ["clean"],
      ],
      // handlers: {
      //   customButton: () => {
      //     console.log('Custom button clicked');
      //   }
      // }
    },
  };

  return (
    <div
      style={{ top: position.y, left: position.x }}
      onMouseDown={(e) => {
        setdragging(true);
        setStartPosition({ x: e.clientX, y: e.clientY });
      }}
      onMouseUp={() => setdragging(false)}
      onMouseMove={handleMouseMove}
      className="text-editor-container"
    >
      <ReactQuill
        value={content}
        onChange={handleChange}
        modules={modules}
        className="text-editor"
      />
      <button onClick={handleSave} className="save-button">
        Save
      </button>
    </div>
  );
};

export default TextEditor;
