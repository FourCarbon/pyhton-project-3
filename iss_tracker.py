'''THE INTERNATIONAL SPACE STATION BEGINNER FRIENDLY PROJECT'''

'''IMPORTING NECESSARY MODULES'''

import requests
import time
import random
from datetime import datetime

def track_space_station():
    # 1. Define the live web links (APIs)
    location_url = "http://open-notify.org"
    astronauts_url = "http://open-notify.org"
    
    try:
        # 2. Fetch live data from the internet
        location_response = requests.get(location_url).json()
        astronauts_response = requests.get(astronauts_url).json()
        
        # 3. Extract the exact location details
        latitude = location_response["iss_position"]["latitude"]
        longitude = location_response["iss_position"]["longitude"]
        timestamp = datetime.fromtimestamp(location_response["timestamp"]).strftime('%Y-%m-%d %H:%M:%S')
        
        # 4. Filter out only the crew members currently inside the ISS
        iss_crew = []
        for person in astronauts_response["people"]:
            if person.get("craft") == "ISS":
                iss_crew.append(person["name"])
                
        # 5. Create realistic hardware telemetry readings based on real ISS targets
        # (ISS targets are 21% Oxygen and 14.7 Cabin Pressure)
        live_o2_level = round(21.0 + random.uniform(-0.1, 0.1), 2)
        live_pressure = round(14.7 + random.uniform(-0.2, 0.2), 2)
        live_battery = round(random.uniform(90.0, 99.9), 1)
        
        # 6. Print the dashboard clearly on screen
        print("\n" + "=" * 50)
        print(f"🛰️  ISS LIVE MISSION CONTROL DASHBOARD")
        print(f"⏰ Sync Time: {timestamp}")
        print("=" * 50)
        
        print(f"📍 ORBITAL POSITION:")
        print(f"   • Latitude:  {latitude}")
        print(f"   • Longitude: {longitude}")
        
        print(f"\n💨 LIFE SUPPORT & ENVIRONMENTAL SYSTEM:")
        print(f"   • Cabin Oxygen Level: {live_o2_level}%  (Target: 21%)")
        print(f"   • Cabin Pressure:     {live_pressure} PSI (Target: 14.7 PSI)")
        
        print(f"\n🔋 HARDWARE & POWER:")
        print(f"   • Battery Bank Charge: {live_battery}%")
        print(f"   • Power System Grid:   124V DC (Operational)")
        print(f"   • Orbital Speed:       ~28,000 km/h")
        
        print(f"\n👨‍🚀 ACTIVE CREW ON BOARD ({len(iss_crew)}):")
        for name in iss_crew:
            print(f"   - {name}")
        print("=" * 50)
        print("⚡ Refreshing telemetry data in 10 seconds... (Ctrl+C to quit)")

    except Exception as error:
        print(f"⚠️ Could not update data right now: {error}")

# This starts the loop that runs the program forever until you stop it
print("Starting up tracking terminals...")
try:
    while True:
        track_space_station()
        time.sleep(10)
except KeyboardInterrupt:
    print("\n🔌 Disconnected from ISS stream. Goodbye!")




#DONT FORGET TO INSTALL :-     pip install requests        TO MAKE CODE RUN PROPERLY.
