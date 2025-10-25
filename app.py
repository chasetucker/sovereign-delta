import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sovereign Delta", layout="centered")
st.title("The Sovereign Delta: Cost of Inaction vs Reward of Alignment")

start = st.number_input("Starting Value", value=100.0, step=1.0)
default_rate = st.slider("Default Decline (per month)", -0.05, 0.00, -0.015, 0.001)
designed_rate = st.slider("Designed Growth (per month)", 0.00, 0.05, 0.02, 0.001)
curve_shape = st.slider("Curve Shape (smaller = more bend)", 0.20, 1.00, 0.35, 0.01)

months = np.linspace(0, 12, 97)
default_future = start + (default_rate * months * 12)
designed_future = start * (1 + designed_rate) ** (months ** curve_shape)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.fill_between(months, default_future, designed_future, color="#CBD5F0", alpha=0.6,
                label="The Sovereign Delta (Outcome Gap)")
ax.plot(months, default_future, "--", color="#F4B400", linewidth=2,
        label="Default Future (Projected Will)")
ax.plot(months, designed_future, color="#4A90E2", linewidth=3,
        label="Designed Future (Projected Could)")

ax.set_xlabel("Time (Months)", fontweight="bold")
ax.set_ylabel("Outcome Level (Health / Wealth / Energy / Harmony)", fontweight="bold")
ax.grid(alpha=0.2)
ax.legend()
st.pyplot(fig)
