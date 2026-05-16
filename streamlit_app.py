import streamlit as st
import pandas as pd
import joblib
from optbinning import OptimalBinning # for binning total_il_high_credit_limit
import re # for email validation
import shap
from function import predict_new_loan, denied, model
# App Title

st.title("Credit Risk Loan Prediction App")
st.write("This app predicts the probability of loan default based on user inputs.")
st.write("Please fill in the following details to get Probability of Default, Estimated Loss and Recommendation:" )

# User Inputs Field
# Customer information
customer_name = st.text_input("Customer Name", placeholder="John Doe", max_chars= 50)
customer_id = st.text_input("Customer ID", placeholder="123456", max_chars=50)
customer_phone = st.text_input("Customer Phone Number", placeholder="(123) 456-7890", max_chars=15)
customer_email = st.text_input("Customer Email", placeholder="xxx@xxx.xxx", max_chars=50)

# numeric inputs
loan_amnt = st.number_input("Loan Amount", min_value=500, max_value=50000, placeholder=10000, step=500)
monthly_debt = st.number_input("Monthly Debt", min_value=0, max_value=20000, placeholder=500, step=500,)
fico_range_low = st.number_input("FICO Score", min_value=300, max_value=850, placeholder=680, step=1)
annual_inc = st.number_input("Annual Income", min_value=1000, max_value=1000000, placeholder=60000, step=1000)
dti = monthly_debt / (annual_inc / 12) * 100 if annual_inc > 0 else 0
revol_util = st.number_input("Revolving Line Utilization Rate (%)", min_value=0.0, max_value=200.0, placeholder=30.0, step=0.1)
pub_rec_bankruptcies = st.number_input("Number of Public Record Bankruptcies", min_value=0, max_value=10, placeholder=0, step=1)
tax_liens = st.number_input("Number of Tax Liens", min_value=0, max_value=10, placeholder=0, step=1)
total_il_high_credit_limit = st.number_input("Total Installment Credit Limit", min_value=0, max_value=1000000, placeholder=20000, step=1000)

# drop downs for categorical inputs
term = st.selectbox("Loan Term", options=["36 months", "60 months"])
emp_length = st.selectbox("Employment Length", options=["< 1 year", "1 year", "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years","nan"])
home_ownership = st.selectbox("Home Ownership", options=["RENT", "OWN", "MORTGAGE", "OTHER"])
purpose = st.selectbox("Purpose of Loan", options=["debt_consolidation", "credit_card", "home_improvement", "major_purchase", "small_business", "car", "wedding", "medical", "moving", "vacation", "house", "educational", "renewable_energy", "other"])
verification_status = st.selectbox("Verification Status", options=["Verified", "Source Verified", "Not Verified"])

# button for prediction

if st.button("Predict"):
    
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, customer_email):
        st.error("Invalid email format. Please enter a valid email address.")
    elif len(customer_name) < 2:
        st.error("Enter valid customer name.")
    elif len(customer_id) < 2:
        st.error("Enter valid customer ID.")
    elif len(customer_phone) < 10:
        st.error("Enter valid customer phone number.")
    else:
        prob_default, expected_loss, recommendation, input_df = predict_new_loan(
            loan_amnt, dti, fico_range_low, annual_inc, revol_util,
            pub_rec_bankruptcies, tax_liens, total_il_high_credit_limit,
            term, emp_length, home_ownership, purpose, verification_status
        )
        
        st.subheader("Prediction Results:")
        st.write(f"Probability of Default: {prob_default:.2%}")
        st.write(f"Estimated Loss: ${expected_loss:.2f}")
        st.write(f"Recommendation: {recommendation}")
        if recommendation == 'High Risk Customer, Recommend Decline':
            reasoning = denied(model, input_df)
            st.write(reasoning)


