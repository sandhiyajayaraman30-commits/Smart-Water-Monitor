import streamlit as st
import pandas as pd
import json
import time
import os
import matplotlib.pyplot as plt

# --- 🎨 PAGE CONFIG ---
st.set_page_config(
    page_title="Smart Water Monitor",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 📂 LOAD DATA ---
def load_water_data():
    if not os.path.exists('water_data.json'):
        return pd.DataFrame(columns=['deviceId', 'flowRate', 'totalUsage', 'timestamp'])
    
    with open('water_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def load_prediction():
    if not os.path.exists('prediction.json'):
        return {"predictedUsage": 0, "isAnomaly": False, "lastUpdated": ""}
    
    with open('prediction.json', 'r') as f:
        return json.load(f)

# Load data
df = load_water_data()
pred = load_prediction()

# --- 📊 MAIN DASHBOARD ---
st.title("💧 Smart Water Usage Monitor — AI Powered (Local Edition)")
st.markdown("                                                                   

                           
st.markdown(                                                                                            , unsafe_allow_html=True)

st.markdown('<p class="### Simulated IoT + ML Insights — All Running on Your Laptop!")

# --- 🔄 AUTO REFRESH ---
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Dashboard auto-refreshes every 5 seconds 🌞</p>', unsafe_allow_html=True)

                            
st.header("# --- 📈 CHART SECTION ---
st.header("📈 Water Usage Trends")

            
st.line_chart(df.set_index('timestamp')['totalUsage'])

                                         
if len(df) >= 24:
    last_24 = df.tail(24)
    fig, ax = plt.subplots()
    ax.bar(last_24['timestamp'], last_24['totalUsage'], color='skyblue')
    ax.set_title("# Line chart
st.line_chart(df.set_index('timestamp')['totalUsage'])

# Bar chart for last 24 hours (simulated)
if len(df) >= 24:
    last_24 = df.tail(24)
    fig, ax = plt.subplots()
    ax.bar(last_24['timestamp'], last_24['totalUsage'], color='skyblue')
    ax.set_title("Last 24 Hours Usage")
    ax.set_xlabel("Time")
    ax.set_ylabel("Liters")
    plt.xticks(rotation=45)
    st.pyplot(fig)

                                    
st.header("# --- 🤖 AI PREDICTION SECTION ---
st.header("🔮 AI Predictions")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Predicted Usage Tomorrow",
        value=f"{pred['predictedUsage']:.1f} L",
        delta=f"{pred['predictedUsage'] - df['totalUsage'].mean():.1f} L vs Avg"
    )

with col2:
    st.metric(
        label="Last Updated",
        value=pred['lastUpdated']
    )

                            
st.header("# --- 🚨 ALERT SECTION ---
st.header("🚨 Alerts & Insights")

if pred['isAnomaly']:
    st.error("⚠️ POSSIBLE LEAK DETECTED!")
    st.write("Usage is significantly higher than average.")
else:
    st.success("✅ System Normal — No Anomalies Detected")

                                 
st.header("# --- 💡 SMART TIPS SECTION ---
st.header("💡 Water Saving Tips")

usage_today = df['totalUsage'].iloc[-1] if len(df) > 0 else 0
avg_usage = df['totalUsage'].mean() if len(df) > 0 else 100

if usage_today > avg_usage * 1.2:
    st.markdown(                                                                                                                                                                                                                                           , unsafe_allow_html=True)

elif usage_today < avg_usage * 0.8:
    st.markdown(                                                                                                                                                                                                             , unsafe_allow_html=True)

else:
    st.write(""""
    <div style="background-color:#FFF3CD; padding:10px; border-radius:5px;">
        <strong>Tip:</strong> You're using 20% more water than average today.<br>
        Check for leaking faucets or running toilets!
    </div>
    """, unsafe_allow_html=True)

elif usage_today < avg_usage * 0.8:
    st.markdown("""
    <div style="background-color:#D4EDDA; padding:10px; border-radius:5px;">
        <strong>Great Job!</strong> You're saving water efficiently.<br>
        Keep up the good habits!
    </div>
    """, unsafe_allow_html=True)

else:
    st.write("You're using average amount of water today.")

                              
st.header("# --- 📋 RECENT READINGS ---
st.header("📋 Recent Readings")
st.table(df.tail(10))

                               
if st.button("# --- 🎯 EXPO MODE BUTTON ---
if st.button("📸 Expo Mode: Freeze Screen"):
    st.success("✅ Dashboard frozen for expo presentation!")
    st.stop()

# --- 🔄 REFRESH EVERY 5 SECONDS ---
time.sleep(5)
st.experimental_rerun()