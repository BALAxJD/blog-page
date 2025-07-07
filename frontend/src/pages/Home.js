import { Link } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { getPosts } from "../api";

function Home() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    getPosts().then((response) => {
      setPosts(response.data);
    });
  }, []);

  return (
    <div>
      <h1>Blog Post</h1>
      <link to="/create">Create New Posts</link>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            <Link to={`/edit/${posts.id}`}>{posts.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
export default Home;
