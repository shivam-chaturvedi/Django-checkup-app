import React, { useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import "./TextEditor.css";

const TextEditor = ({ onSave }) => {
  const [content, setContent] = useState("");


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
    <div className="text-editor-container">
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
