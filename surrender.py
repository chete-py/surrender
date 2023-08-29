import streamlit as st
import pandas as pd
import base64
import calendar
import io

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Secondary Market For Life Insurance")

st.sidebar.image('favicon.png', use_column_width=True)
st.sidebar.subheader("Trading Life Insurance Contracts")

# Function to add a new entry to the CSV file
def add_entry_to_csv(data):
    # Load existing CSV data
    df = pd.read_csv("surrender.csv")

    # Append new data to the DataFrame
    new_entry = pd.DataFrame([data])
    newdf = pd.concat([df, new_entry], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    newdf.to_csv("surrender.csv", index=False)


    newdf = newdf.to_html(index=False)
    # Add inline CSS to change font size
    newdf = newdf.replace('<table', '<table style="font-size: 11px;"')       

    st.markdown(newdf, unsafe_allow_html=True)


# Main Streamlit app code
def main(): 


    # Create a sidebar to switch between views
    view = st.sidebar.radio("Welcome, are you an investor or underwriter?", ["Investor", "Underwriter", "View Records"])

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
                 df = pd.read_csv("surrender.csv")

        # Filter policies based on investor's inputs
        filtered_df = newdf[
            (newdf["Units Payable"] >= min_units_payable) & 
            (newdf["Units Payable"] <= max_units_payable) &
            (newdf["Term of Settlement"] == term_of_settlement)
        ]

        # Display the filtered policies
        if not filtered_df.empty:
            st.write("Available Policies:")
            st.dataframe(filtered_df)
        else:
            st.write("No policies found matching your criteria.")

    elif view == "Underwriter":
        # Add the dashboard elements here
        st.subheader("Sell Surrender To Secondary Market")

        st.write("Please provide the following information:")
        
        # Create form widgets to capture user inputs
        new_entry_data = {}
        new_entry_data ["Underwriter"] = st.selectbox("Name Of Insurance Company:", ["ABSA Life", "APA Life", "Britam Life", "Corporate Insurance", "CIC Life", "GA Life", "Geminia Life", "ICEA Lion", "Jubilee Insurance", "Liberty Life", "Madison Insurance", "Old Mutual", "Prudential Life", "Sanalam Life"])
        new_entry_data ["Policy Type"] = st.selectbox("Policy Type:", ["Investment Linked Policy", "Life Insurance Policy"])
        new_entry_data ["Start Date"] = st.date_input("Start Date")
        new_entry_data ["Maturity Date"] = st.date_input("Maturity Date")
        new_entry_data ["Surrender Date"] = st.date_input("Surrender Date")
        new_entry_data ["Units Paid"] = st.number_input("Number of units paid:")
        new_entry_data ["Units Payable"] = st.number_input("Number of units payable:") 
        new_entry_data ["Total Premium Received"] = st.number_input("Total Premium Received")
        new_entry_data ["Insurance Surrender Amount"] = st.number_input("Insurance Surrender Amount")
        new_entry_data ["Initial Lumpsome Amount"] = st.number_input("Investor Lumpsome Payment to Policy Holder")
        new_entry_data ["Total Investment Amount"] = st.number_input("Total Projected Investment Amount")
        new_entry_data ["Return On Investment"] = st.number_input("Return on Investment")
        
        
         
        
        # Create a button to submit the form
        if st.button("Submit"):
            # Process and display user inputs
            add_entry_to_csv(new_entry_data)
            st.success("New Policy added successfully!")

    elif view == "View Records":
        # Show the saved DataFrame here
        st.subheader("RECORDS") 
        lastdf = pd.read_csv("surrender.csv")

        lastdf = lastdf.to_html(index=False)
        last_df = lastdf.replace('<table', '<table style="font-size: 12px;"')

        # Convert the data frame to Markdown table format
        # markdown_table = lastdf.to_markdown(index=False)

        # Display the Markdown-formatted table using st.markdown()
        # st.markdown(markdown_table, unsafe_allow_html=True)
        #st.table(lastdf)

        st.markdown(last_df, unsafe_allow_html=True)
        
           
    

       
if __name__ == "__main__":
    main()
