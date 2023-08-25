import streamlit as st
import pandas as pd
import base64
import io

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Secondary Market For Life Insurance")

st.sidebar.image('favicon.png', use_column_width=True)
st.sidebar.subheader("Trading Life Insurance Contracts")

# Main Streamlit app code
def main(): 


    # Create a sidebar to switch between views
    view = st.sidebar.radio("Welcome, are you an investor or underwriter?", ["Investor", "Underwriter"])

    if view == "Investor":
        st.subheader("Buy Surrender from Secondary Market")

        st.write("Please provide the following information:")
        
        # Create form widgets to capture user inputs
        name = st.text_input("Name:")
        age = st.number_input("Age:")
        mode_of_payment = st.selectbox("Mode of Payment:", ["Monthly", "Quarterly", "Semi-Annually", "Annually", "Lumpsome"])
        term_of_settlement = st.selectbox("Desired Number Of Installments Payable (months):",["Below 36", "36 - 48 months", "48 - 60 months", "Over 60 months"])
        
        # Create a button to submit the form
        if st.button("Submit"):
            # Process and display user inputs
            st.write("Submitted Information:")
            st.write(f"Name: {name}")
            st.write(f"Age: {age}")
            st.write(f"Mode of Payment: {mode_of_payment}")
            st.write(f"Term of Settlement: {term_of_settlement} years")

    elif view == "Underwriter":
        # Add the dashboard elements here
        st.subheader("Sell Surrender To Secondary Market")

        st.write("Please provide the following information:")
        
        # Create form widgets to capture user inputs
        name = st.selectbox("Name Of Insurance Company:", ["ABSA Life", "APA Life", "Britam Life", "Corporate Insurance", "CIC Life", "GA Life", "Geminia Life", "ICEA Lion", "Jubilee Insurance", "Liberty Life", "Madison Insurance", "Old Mutual", "Prudential Life", "Sanalam Life"])
        policy = st.selectbox("Policy Type:", ["Investment Linked Policy", "Life Insurance Policy"])
        policy_term = st.number_input("Policy Term Of the Policy:")
        premium_term = st.number_input("Premium Term Of the Policy:")
        units_paid = st.text_input("Number of units paid:")
        units_outstanding = st.text_input("Number of units outstanding:")        
         
        
        # Create a button to submit the form
        if st.button("Submit"):
            # Process and display user inputs
            st.write("Submitted Information:")
            st.write(f"Name: {name}")
            st.write(f"Policy: {policy}")
            st.write(f"Policy: {policy_term}")
            st.write(f"Policy: {premium_term}")
            st.write(f"Total Units Paid: {units_paid}")
            st.write(f"Total Units Outstanding: {units_outstanding}")
           
    

       
if __name__ == "__main__":
    main()
