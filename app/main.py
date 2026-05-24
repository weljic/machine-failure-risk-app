import streamlit as st
from app.model import predict_failure_probability, classify_failure

st.set_page_config(page_title="Machine Failure Risk Estimator")

st.title("Machine Failure Risk Estimator")
st.write(
    "Enter machine sensor readings to estimate the probability of failure. "
    "This is a simplified demo model for the assessment."
)

# Input fields
temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=300.0, value=80.0)
vibration = st.number_input("Vibration Level", min_value=0.0, max_value=100.0, value=20.0)
pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=500.0, value=100.0)

if st.button("Assess Failure Risk"):
    prob = predict_failure_probability(temperature, vibration, pressure)
    label = classify_failure(prob)

    st.subheader("Result")
    st.metric("Failure Probability", f"{prob:.1%}")
    st.write(f"**Risk Classification:** {label}")

    st.caption("Note: This is a simplified model for demonstration purposes.")