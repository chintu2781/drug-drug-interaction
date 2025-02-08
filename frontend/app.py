import streamlit as st

st.title("Drug-Drug Interaction Prediction")
drug1 = st.text_input("Enter Drug 1")
drug2 = st.text_input("Enter Drug 2")

if st.button("Predict"):
    # Call your model here
    prediction = "Interaction Detected"  # Replace with actual prediction
    st.write(f"Prediction: {prediction}")
