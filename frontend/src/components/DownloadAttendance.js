import React, { useState } from "react";

function DownloadAttendance() {
  const [attendance, setAttendance] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchAttendance = async () => {
    setLoading(true);
    const res = await fetch("http://127.0.0.1:8000/attendance/");
    const data = await res.json();
    setAttendance(data.attendance || []);
    setLoading(false);
  };

  return (
    <div>
      <h3>Attendance Records</h3>
      <button onClick={fetchAttendance}>View Attendance</button>
      {loading && <div>Loading...</div>}
      <ul>
        {attendance.map((record, idx) => (
          <li key={idx}>
            {record.name} - {record.timestamp}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DownloadAttendance;