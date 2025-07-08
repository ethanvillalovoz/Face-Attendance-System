import React, { useState } from "react";

function ProcessBatch() {
  const [message, setMessage] = useState("");

  const handleProcess = async () => {
    const res = await fetch("http://127.0.0.1:8000/process/", {
      method: "POST",
    });
    const data = await res.json();
    setMessage(data.info || data.error);
  };

  return (
    <div>
      <h3>Process Batch</h3>
      <button onClick={handleProcess}>Run Batch Processing</button>
      <div>{message}</div>
    </div>
  );
}

export default ProcessBatch;