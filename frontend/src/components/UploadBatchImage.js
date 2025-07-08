import React, { useState } from "react";

function UploadBatchImage() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("http://127.0.0.1:8000/upload/batch/", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setMessage(data.info || data.error);
  };

  return (
    <div>
      <h3>Upload Batch Image</h3>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <div>{message}</div>
    </div>
  );
}

export default UploadBatchImage;