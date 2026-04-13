import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="EMI Predictor", layout="wide")

# 🔁 Sidebar Navigation
page = st.sidebar.selectbox(
    "📌 Select Page",
    ["EMI Eligibility Check", "Maximum EMI Prediction"]
)

# ==============================
# 🟢 PAGE 1: EMI ELIGIBILITY
# ==============================
if page == "EMI Eligibility Check":

    st.markdown("<h1 style='text-align:center;'>💳 EMI Eligibility Predictor</h1>", unsafe_allow_html=True)

    clf_model = pickle.load(open(r"D:\Emi Predict\Models-1\clas_xgb.pkl", "rb"))

    left_col, right_col = st.columns([1, 2])

    with left_col:
        st.info("👉 Enter your financial details and check eligibility.")

    with right_col:
        st.subheader("📋 Enter Your Monthly Details")

        monthly_salary = st.number_input("Monthly Salary", min_value=0)
        school_fees = st.number_input("School Fees", min_value=0)
        college_fees = st.number_input("College Fees", min_value=0)
        travel_expenses = st.number_input("Travel Expenses", min_value=0)
        groceries_utilities = st.number_input("Groceries & Utilities", min_value=0)
        other_monthly_expenses = st.number_input("Other Monthly Expenses", min_value=0)
        current_emi_amount = st.number_input("Current EMI Amount", min_value=0)
        credit_score = st.number_input("Credit Score", min_value=0)
        requested_amount = st.number_input("Requested Amount", min_value=0)
        bank_balance = st.number_input("Bank Balance", min_value=0)
        emergency_fund = st.number_input("Emergency Fund", min_value=0)

        if st.button("🔍 Check Eligibility"):
            try:
                features = np.array([[monthly_salary, school_fees, college_fees,
                                      travel_expenses, groceries_utilities,
                                      other_monthly_expenses, current_emi_amount,
                                      credit_score, requested_amount,
                                      bank_balance, emergency_fund]])

                eligibility = clf_model.predict(features)[0]

                st.subheader(f"📊 Result : {eligibility}")

                if eligibility == 1:
                    st.success("✅ Eligible for EMI")
                elif eligibility == 2:
                    st.success("❌ EMI is at high risk")
                else:
                    st.error("❌ Not Eligible")

            except Exception as e:
                st.error(f"Error: {e}")


# ==============================
# 🔵 PAGE 2: MAX EMI PREDICTION
# ==============================
elif page == "Maximum EMI Prediction":

    st.markdown("<h1 style='text-align:center;'>💰 Maximum EMI Predictor</h1>", unsafe_allow_html=True)
   
    reg_model = pickle.load(open(r"D:\Emi Predict\Data Cleaning 1\reg_linear1.pkl", "rb"))

    st.subheader("📋 Enter Details")
    # DROPDOWNSsssss
    
    emi_eligibility = st.selectbox("EMI Eligibility", ["Eligible", "Not Eligible"])
    existing_loans = st.selectbox("Existing Loans", ["Yes", "No"])

    # NUMERIC INPUTS
    monthly_salary = st.number_input("Monthly Salary", min_value=0)
    travel_expenses = st.number_input("Travel Expenses", min_value=0)
    groceries_utilities = st.number_input("Groceries & Utilities", min_value=0)
    college_fees = st.number_input("college fees", min_value=0)
    current_emi_amount = st.number_input("Current EMI Amount", min_value=0)
    bank_balance = st.number_input("Bank Balance", min_value=0)
    school_fees = st.number_input("School fees", min_value=0)
    monthly_rent = st.number_input("Monthly rent", min_value=0)

    # CONVERSIONS
    emi_map = {"Eligible": 1, "Not Eligible": 0}
    loan_map = {"Yes": 1, "No": 0}

    if st.button("💰 Predict Max EMI"):
        try:
            features = np.array([[
                emi_map[emi_eligibility],monthly_salary, college_fees, travel_expenses, groceries_utilities,
                                      school_fees, current_emi_amount,
                                      bank_balance, monthly_rent,loan_map[existing_loans],
            ]], dtype=float)

            prediction = reg_model.predict(features)[0]
            prediction = max(0, prediction)

            st.subheader("📊 Result")
            st.success(f"💰 Maximum EMI You Can Afford: ₹ {round(prediction,2)}")

        except Exception as e:
            st.error(f"Error: {e}")