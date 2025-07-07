import React, { useState } from "react";
import { createPost } from "../api";
import { useNavigate } from "react-router-dom";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";

function CreatePost() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [status, setStatus] = useState("draft");
  const [preview, setPreview] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async () => {
    const postData = { title, content, status };
    await createPost(postData);
    navigate("/");
  };

  return (
    <div>
      <h1>Create New Post</h1>
      <input
        type="text"
        placeholder="Enter title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <ReactQuill value={content} onChange={setContent} />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        <option value="draft">Draft</option>
        <option value="published">Published</option>
      </select>

      <button onClick={() => setPreview(!preview)}>
        {preview ? "Edit mode" : "preview"}
      </button>
      {preview ? (
        <div>
          <h2>Preview</h2>
          <h3>{title}</h3>
          <div dangerouslySetInnerHTML={{ __html: content }} />
        </div>
      ) : (
        <button onClick={handleSubmit}>Post</button>
      )}
    </div>
  );
}
export default CreatePost;
