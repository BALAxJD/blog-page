import React, { useState, useEffect } from "react";
import { getPosts, updatePost, updatePostasync } from "../api";
import { useParams, useNavigate } from "react-router-dom";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";

function EditPost() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [status, setStatus] = useState("draft");
  const [preview, setPreview] = useState(false);

  useEffect(() => {
    getPosts().then((response) => {
      const post = response.data.find((p) => p.id === parseInt(id));
      if (post) {
        setTitle(post.title);
        setContent(post.content);
        setStatus(post.status);
      }
    });
  }, [id]);

  const handleUpdate = async () => {
    const postData = { title, content, status };
    await updatePost(id, postData);
    navigate("/");
  };

  return (
    <div>
      <h>Edit Post</h>
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
        <button onClick={handleUpdate}>Update</button>
      )}
    </div>
  );
}
export default EditPost;
