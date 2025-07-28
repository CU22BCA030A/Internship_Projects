// ✅ Initialize Firebase (using compat)
const firebaseConfig = {
  apiKey: "AIzaSyDU7qyZSR31CZ4viLaJ6E8VQabJO2vP-co",
  authDomain: "honeypot-a5856.firebaseapp.com",
  projectId: "honeypot-a5856",
  storageBucket: "honeypot-a5856.appspot.com",
  messagingSenderId: "556877726399",
  appId: "1:556877726399:web:fd1577c6c7838001cb7c0a",
  measurementId: "G-CWTQ1ETYLL"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// Geo information
async function getGeoInfo() {
  try {
    const res = await fetch("https://ipapi.co/json/"); // Ensure correct URL and API
    const data = await res.json();
    return {
      ip: data.ip,
      location: `${data.city}, ${data.region}, ${data.country_name}`,
      org: data.org,
      region: data.region,
    };
  } catch (err) {
    console.error("Geo fetch error:", err);
    return {
      ip: "Unknown",
      location: "Unknown",
      org: "Unknown",
      region: "Unknown"
    };
  }
}

// Handle Form Submission
document.getElementById("honeypotForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const timestamp = new Date().toISOString();  // Corrected timestamp assignment

  const geo = await getGeoInfo();

  if (username === adminUsername && password === adminPassword) {
    alert("✅ Welcome, Admin!");
    window.location.href = "admin.html";  // Ensure proper redirect
  } else {
    try {
      await db.collection("honeypotLogs").add({
        username,
        password,
        ip: geo.ip,
        location: geo.location,
        org: geo.org,
        region: geo.region,
        timestamp: timestamp  // Corrected timestamp assignment
      });
      alert("🚨 Unauthorized access detected. Intrusion logged.");
      window.location.href = "fake-dashboard.html";
    } catch (error) {
      console.error("❌ Firestore write error:", error);
      alert("Something went wrong while logging the intrusion.");
    }
  }

  document.getElementById("honeypotForm").reset();
});