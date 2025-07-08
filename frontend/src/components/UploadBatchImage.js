import React, { useState } from "react";

function UploadBatchImage() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    setFile(selected);
    setPreview(selected ? URL.createObjectURL(selected) : null);
    setMessage("");
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file.");
      return;
    }
    setLoading(true);
    setMessage("");
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await fetch("http://127.0.0.1:8000/upload/batch/", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setMessage(data.info || data.error);
    } catch (err) {
      setMessage("Upload failed. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div style={{ marginBottom: "2rem" }}>
      <h3>Upload Batch Image</h3>
      <input type="file" onChange={handleFileChange} />
      {preview && (
        <div>
          <img src={preview} alt="preview" style={{ width: 100, margin: "1rem 0" }} />
        </div>
      )}
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>
      <div style={{ color: message.includes("failed") ? "red" : "green" }}>{message}</div>
    </div>
  );
}

export default UploadBatchImage;