import json, pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import time

# Load data
with open('water_data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['day'] = df['timestamp'].dt.dayofyear
df['hour'] = df['timestamp'].dt.hour

# Train simple model (if enough data)
if len(df) > 5:
    X = df[['day', 'hour']]
    y = df['totalUsage']
    model = LinearRegression()
    model.fit(X, y)

    # Predict next hour (fake future point)
    next_point = [[df['day'].iloc[-1] + 1, 8]]  # Tomorrow 8 AM
    predicted = model.predict(next_point)[0]

    # Anomaly check
    mean = df['totalUsage'].mean()
    std = df['totalUsage'].std()
    latest = df['totalUsage'].iloc[-1]
    is_anomaly = latest > mean + 2 * std

    # Save prediction
    pred_data = {
        "predictedUsage": round(predicted, 1),
        "isAnomaly": bool(is_anomaly),
        "lastUpdated": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open('prediction.json', 'w') as f:
        json.dump(pred_data, f, indent=4)

    print(f"🔮 Predicted: {predicted:.1f} L | Anomaly: {is_anomaly}")
else:
    print("⚠️ Not enough data yet. Need >5 rows.")