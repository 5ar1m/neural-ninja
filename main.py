import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

# 2. Title
st.markdown("<h1 style='text-align: center;'>Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.write("---")

# 3. Row 1: Age and Gender
col1, col2 = st.columns(2)

with col1:
    # Constraint: Age between 18 and 70
    age = st.number_input("Age:", min_value=18, max_value=70, step=1)

with col2:
    # Constraint: Male and Female options
    gender = st.selectbox("Gender:", ["Male", "Female"])

# 4. Row 2: Monthly Usage
# Constraint: Between 5 and 200
usage = st.number_input("Monthly Usage (in hours):", min_value=5, max_value=200, step=1)

# 5. Row 3: Number of Transactions
# Constraint: Between 1 and 50
transactions = st.number_input("Number of Transactions:", min_value=1, max_value=50, step=1)

# 6. Row 4: Subscription Type and Complaints
col3, col4 = st.columns(2)

with col3:
    # Constraint: Basic/Premium/Gold
    subscription = st.selectbox("Subscription Type:", ["Basic", "Premium", "Gold"])

with col4:
    # Constraint: Between 0 and 10
    complaints = st.number_input("Complaints:", min_value=0, max_value=10, step=1)

# Spacing
st.write("")
st.write("")

# 7. Button (Centered)
# We use columns to center the button visually
_, col_btn, _ = st.columns([0.35, 0.3, 0.35])

with col_btn:
    predict_btn = st.button("Predict Churn", use_container_width=True)

# 8. Mock Prediction Logic
if predict_btn:
    with st.spinner("Analyzing customer data..."):
        time.sleep(1) # Simulating processing time
        
        # Since we don't have a real model, we'll just print the inputs for now
        st.success("Prediction Complete!")
        
        # Display what was captured (For debugging/verification)
        st.json({
            "Age": age,
            "Gender": gender,
            "Monthly Usage": usage,
            "Transactions": transactions,
            "Subscription": subscription,
            "Complaints": complaints
        })