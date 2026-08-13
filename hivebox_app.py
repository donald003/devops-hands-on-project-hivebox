"""HiveBox API pulling data from OpenSenseMap"""
from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify
import requests

app = Flask(__name__)
VERSION = "0.0.1"

SENSEBOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c"
]

@app.route("/version")
def version():
    """Return the current app version"""
    return jsonify({"version": VERSION})

@app.route("/temperature")
def temperature():
    """Return the average temperature of given SenseBoxes"""
    temps = []
    one_hour_ago = datetime.now(timezone.utc) - timedelta(hours=1)

    for box_id in SENSEBOX_IDS:
        url = f"https://api.opensensemap.org/boxes/{box_id}"
        try:
            response = requests.get(url, timeout=3)
            data = response.json()

            for sensor in data["sensors"]:
                if sensor["title"] == "Temperatur":
                    measurement = sensor["lastMeasurement"]
                    timestamp = datetime.fromisoformat(
                        measurement["createdAt"].replace("Z", "+00:00"))

                    if timestamp > one_hour_ago:
                        temps.append(float(measurement["value"]))

        except requests.exceptions.RequestException:
            continue

    if not temps:
        return jsonify({"error": "No temperature data"}), 404

    avg_temp = sum(temps) / len(temps)
    return jsonify({"average_temperature": round(avg_temp, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
