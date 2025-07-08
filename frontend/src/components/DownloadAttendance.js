import React from "react";

function DownloadAttendance() {
  const handleDownload = () => {
    window.open("http://127.0.0.1:8000/attendance/", "_blank");
  };

  return (
    <div>
      <h3>Download Attendance</h3>
      <button onClick={handleDownload}>Download Attendance CSV</button>
    </div>
  );
}

export default DownloadAttendance;