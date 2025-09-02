# to run this give this command in command prompt 'streamlit run loan_app.py'
# loan_app.py
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Bank Loan Data Preprocessing", layout="wide")

st.title("📊 Bank Loan Application Data Preprocessing & Outlier Detection")
st.markdown("Upload your CSV file and preprocess the data step by step.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # --- Show Raw Data ---
    st.subheader("🔍 Raw Data (Full Details)")
    st.dataframe(df)   # Full dataset (scrollable)

    # Ensure numeric conversions
    for col in ["Income", "CreditScore", "LoanAmount"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # --- Missing Values ---
    st.subheader("🛠 Handle Missing Values")
    st.write("Missing values (count per column):")
    st.write(df.isnull().sum())

    st.write("🔎 Rows with Missing Values:")
    missing_rows = df[df.isnull().any(axis=1)]
    if missing_rows.empty:
        st.write("✅ No rows with missing values.")
    else:
        st.dataframe(missing_rows)

    # Fill missing values
    if "Income" in df.columns:
        df["Income"].fillna(df["Income"].median(), inplace=True)
    if "CreditScore" in df.columns:
        df["CreditScore"].fillna(round(df["CreditScore"].mean()), inplace=True)
    if "LoanAmount" in df.columns:
        df = df.dropna(subset=["LoanAmount"])

    # --- Remove Duplicates ---
    if "ApplicationID" in df.columns:
        before = df.shape[0]
        df = df.drop_duplicates(subset=["ApplicationID"], keep="first")
        after = df.shape[0]
        st.write(f"✅ Removed {before - after} duplicate rows based on `ApplicationID`.")

    # --- Standardize LoanStatus ---
    if "LoanStatus" in df.columns:
        df["LoanStatus"] = df["LoanStatus"].astype(str).str.strip().str.lower().map(
            lambda x: "Approved" if str(x).startswith("app") else "Rejected"
        )

    # --- Outlier Detection ---
    st.subheader("🚨 Outlier Detection (IQR method)")

    def detect_outliers(series):
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return lower, upper

    for col in ["Income", "LoanAmount"]:
        if col in df.columns:
            lower, upper = detect_outliers(df[col])
            df[col + "_is_outlier"] = (df[col] < lower) | (df[col] > upper)

            # Show count
            st.write(f"Outliers in **{col}**: {df[col + '_is_outlier'].sum()}")

            # Highlight outliers directly in a small table
            def highlight_outliers(val):
                if val < lower or val > upper:
                    return "background-color: red; color: white;"
                return ""
            
            styled = df[[col]].style.applymap(highlight_outliers)
            st.write(f"🔎 Highlighted Outliers in **{col}** (outside {lower:.2f} - {upper:.2f}):")
            st.dataframe(styled)

    # Mark if review needed
    df["NeedsReview"] = df[[c for c in df.columns if c.endswith("_is_outlier")]].any(axis=1)

    # --- High Risk Loans ---
    if {"Income", "LoanAmount"}.issubset(df.columns):
        high_risk = df[df["LoanAmount"] > 2 * df["Income"]]
        st.subheader("⚠️ High-Risk Loans (LoanAmount > 2 × Income)")
        if high_risk.empty:
            st.write("No high-risk loans detected.")
        else:
            st.dataframe(high_risk)

    # --- Group & Aggregate ---
    if {"EmploymentStatus", "LoanAmount"}.issubset(df.columns):
        group_avg = df.groupby("EmploymentStatus")["LoanAmount"].mean().reset_index()
        st.subheader("📌 Average LoanAmount by Employment Status")
        st.dataframe(group_avg)

    # --- Download cleaned dataset ---
    st.subheader("💾 Download Cleaned Data")
    cleaned_csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download cleaned CSV",
        data=cleaned_csv,
        file_name="cleaned_loan_data.csv",
        mime="text/csv",
    )

    st.success("✅ Preprocessing completed!")
else:
    st.info("Please upload a CSV file to begin.")
