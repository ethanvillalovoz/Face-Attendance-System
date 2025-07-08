import React, { useState } from "react";

function UploadKnownFace() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("http://127.0.0.1:8000/upload/known/", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setMessage(data.info || data.error);
  };

  return (
    <div>
      <h3>Upload Known Face</h3>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <div>{message}</div>
    </div>
  );
}

export default UploadKnownFace;