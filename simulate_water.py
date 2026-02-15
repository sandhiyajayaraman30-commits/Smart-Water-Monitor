import random, time, json, os

def generate_data():
    return {
        "deviceId": "sim-water-meter",
        "flowRate": round(random.uniform(0.1, 2.0), 2),
        "totalUsage": random.randint(30, 350),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def save_data(data):
    filename = 'water_data.json'
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)

    with open(filename, 'r+') as f:
        records = json.load(f)
        records.append(data)
        f.seek(0)
        json.dump(records, f, indent=4)

if __name__ == "__main__":
    print("🚀 Simulation started (Ctrl+C to stop)")
    while True:
        data = generate_data()
        save_data(data)
        print(f"📥 Saved: {data}")
        time.sleep(5)
