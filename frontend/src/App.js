import React from "react";
import "./App.css";
import UploadKnownFace from "./components/UploadKnownFace";
import UploadBatchImage from "./components/UploadBatchImage";
import ProcessBatch from "./components/ProcessBatch";
import DownloadAttendance from "./components/DownloadAttendance";

function App() {
  return (
    <div className="App">
      <h1>Face Attendance System</h1>
      <UploadKnownFace />
      <UploadBatchImage />
      <ProcessBatch />
      <DownloadAttendance />
    </div>
  );
}

export default App;
