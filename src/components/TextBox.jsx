import React, { useState, useRef } from 'react';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import undoImage from '../person.png';
import redoImage from '../calendar.png';

const TextEditor = () => {
  const [content, setContent] = useState('');

  const handleChange = (value) => {
    setContent(value);
  };

  const handleUndo = () => {
    if (editorRef.current) {
      editorRef.current.editor.history.undo();
    }
  };

  const handleRedo = () => {
    if (editorRef.current) {
      editorRef.current.editor.history.redo();
    }
  };

  const modules = {
    toolbar: [
      [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
      ['bold', 'italic', 'underline', 'strike'],
      [{'list': 'ordered'}, {'list': 'bullet'}],
      [{'indent': '-1'}, {'indent': '+1'}],
      ['link', 'image'],
      ['clean']
    ],
  };
  
  // const formats = [
  //   'header',
  //   'bold', 'italic', 'underline', 'strike',
  //   'list', 'bullet',
  //   'indent',
  //   'link', 'image'
  // ];

  // const modules = {
  //   toolbar: [
  //     [{ 'undo': { handler: handleUndo, icon: `<img src=${undoImage} alt="Undo" />` } }],
  //     [{ 'redo': { handler: handleRedo, icon: `<img src=${redoImage} alt="Redo" />` } }],
  //     [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
  //     ['bold', 'italic', 'underline', 'strike'],
  //     [{'list': 'ordered'}, {'list': 'bullet'}],
  //     [{'indent': '-1'}, {'indent': '+1'}],
  //     ['link', 'image'],
  //     ['clean']
  //   ]
  // };

  const editorRef = useRef();

  return (
    <div>
      <ReactQuill
        value={content}
        onChange={handleChange}
        modules={modules}
        ref={editorRef}
      />
    </div>
  );
};

export default TextEditor;