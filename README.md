# 🛰️ ISS Live Mission Control Tracker

A beginner-friendly Python application that tracks the **International Space Station (ISS)** in real-time. The script fetches the live orbital coordinates of the station and the current list of astronauts on board using public APIs, while cleanly displaying core life-support hardware baselines directly in your terminal.

---

## ✨ Features

* **Real-Time Tracking:** Pulls live latitude and longitude coordinates directly from the space station.
* **Live Crew Counter:** Displays the exact number and full names of the astronauts currently living inside the ISS.
* **Hardware & ECLSS Telemetry:** Displays realistic simulations of the Environmental Control and Life Support System (O2 levels and cabin pressure) alongside hardcoded electrical grid specifications.
* **Auto-Refresh Engine:** Runs continuously inside a clean 10-second loop until manually stopped.
* **Beginner-Friendly Architecture:** Written using clear, linear logic without advanced object-oriented programming (no complex classes or `self` keywords).

---

## 📊 Dashboard Preview

When you execute the script, it prints a clean dashboard layout inside your terminal:

```text
==================================================
🛰️  ISS LIVE MISSION CONTROL DASHBOARD
⏰ Sync Time: 2026-10-15 23:31:00
==================================================
📍 ORBITAL POSITION:
   • Latitude:  51.4872
   • Longitude: -0.1245

💨 LIFE SUPPORT & ENVIRONMENTAL SYSTEM:
   • Cabin Oxygen Level: 21.04%  (Target: 21%)
   • Cabin Pressure:     14.78 PSI (Target: 14.7 PSI)

🔋 HARDWARE & POWER:
   • Battery Bank Charge: 96.4%
   • Power System Grid:   124V DC (Operational)
   • Orbital Speed:       ~28,000 km/h

👨‍🚀 ACTIVE CREW ON BOARD (7):
   - Astronaut Name 1
   - Astronaut Name 2
   - Astronaut Name 3
==================================================
⚡ Refreshing telemetry data in 10 seconds... (Ctrl+C to quit)
```

---

## 🚀 Getting Started

### 📋 Prerequisites
You only need to install the **`requests`** library to allow Python to communicate with the web endpoints.

```bash
pip install requests
```

### 💻 Running the Script
1. Clone or download this repository to your local computer.
2. Open your terminal or command prompt in the project folder.
3. Run the tracking application using:

```bash
python iss_tracker.py
```

---

## 🛠️ How It Works (Under the Hood)

This program gathers data by talking to public JSON application programming interfaces (APIs) provided by **Open Notify**:

1. **`http://open-notify.org`** - Used to fetch live latitude, longitude, and timestamps.
2. **`http://open-notify.org`** - Used to get the total number of humans in space. The program then loops through this list and filters out anyone whose active craft matches `"ISS"`.
3. **Telemetry Emulation:** Because live life-support metrics are heavily protected by NASA for safety reasons, this script generates realistic orbital fluctuations around standard engineering specifications (**21% Oxygen** and **14.7 PSI Cabin Pressure**) using Python's built-in `random` module.

---

## 🛑 Stopping the Program
To safely shutdown the telemetry connection stream, simply press **`Ctrl + C`** inside your running terminal window. 
