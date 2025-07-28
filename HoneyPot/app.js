// Fetch Logs and Populate Table
async function loadLogs() {
  const tableBody = document.querySelector("#logTable tbody");
  tableBody.innerHTML = ""; // Clear old rows

  try {
    const snapshot = await db.collection("honeypotLogs").orderBy("timestamp", "desc").get();
    snapshot.forEach(doc => {
      const data = doc.data();
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${data.username}</td>
        <td>${data.password}</td>
        <td>${data.ip}</td>
        <td>${data.location}</td>
        <td>${data.org}</td>
        <td>${new Date(data.timestamp).toLocaleString()}</td>
      `;
      tableBody.appendChild(row);
    });
  } catch (error) {
    console.error("Error fetching logs:", error);
    alert("Failed to load logs.");
  }
}

// Call the function on load
loadLogs();