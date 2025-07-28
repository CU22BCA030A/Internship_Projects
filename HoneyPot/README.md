# 🛡️ Honeypot-as-a-Service (HaaS)

A **cloud-based honeypot project** designed to **trap and track intruders** via a fake admin login page. Unauthorized login attempts are logged with full metadata (IP, location, ISP, timestamp, etc.), and admins can view these logs in real-time.

---

##  Live Project

**Hosted on Netlify**  
 [https://dynamic-dodol-2919b3.netlify.app](https://dynamic-dodol-2919b3.netlify.app)

---

##  Authorized Credentials

Use the following to access the admin panel:
```
Username: admin  
Password: secure123
```

---

## 📁 Project Structure

```
honeypot
│
├── index.html            # Public login page
├── admin.html            # Admin panel with logs
├── fake-dashboard.html   # Message shown to intruders
│
├── index.js              # Firebase Function for IP geolocation
├── admin.js              # Form submission & logging logic
├── app.js                # Fetches & displays logs on admin.html
│
├── style.css             # Common CSS styles
└── README.md             # Project documentation
```

---

##  Technologies Used

| Feature        | Stack |
|----------------|-----------------------------|
| Frontend       | HTML, CSS, JavaScript       |
| Cloud Database | Firebase Firestore          |
| Hosting        | Netlify                     |
| IP Location    | ipapi.co / ip-api.com       |
| Backend Logic  | Firebase Cloud Functions    |

---

##  Key Features

-   Mimics a secure login interface.
-  Logs every unauthorized attempt in Firestore.
-  Captures IP, city, region, country, and ISP.
-  Timestamps every login attempt.
-  Admin dashboard displays logs in a clean UI.
-  Intruders see a fake dashboard, reinforcing illusion.

---

##  How It Works

1. **User lands on login page** → `index.html`.
2. **If correct credentials** → Redirected to `admin.html`.
3. **If incorrect credentials** → 
   - Details (username, password, IP, location, timestamp) logged to Firebase.
   - User redirected to `fake-dashboard.html`.

---

##  Deployment

This app is **fully deployed using Netlify**. Firebase is used as a backend service for:
- Real-time database (Firestore)
- Geo-lookup API
- Admin log monitoring

### Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Create a project
3. Enable Firestore
4. Add your config in `admin.js`:
```js
const firebaseConfig = {
  apiKey: "...",
  authDomain: "...",
  projectId: "...",
  ...
};
```
5. (Optional) Deploy `index.js` as a Firebase Cloud Function for server-side IP geolocation.

---

## Local Setup

```bash
git clone https://github.com/CU22BCA030A/Internship_Projects/new/main/HoneyPot)
```

Then either open `index.html` manually or use:

```bash
npm install -g live-server
live-server
```
