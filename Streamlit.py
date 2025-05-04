import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# --- Section: Hello and Input ---
st.title("Streamlit App Demo")

# Simple greeting
st.write('## Hello World')

# Text input
movie = st.text_input('Favorite Movie?')
if movie:
    st.write(f"Your favorite movie is: {movie}")

# Button interaction
if st.button("Click Me"):
    st.success("Button was clicked!")

# --- Section: Markdown and Formatting ---
st.markdown("## Markdown Demo")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
''')
st.markdown("Here's a bouquet — :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# --- Section: Load and Display CSV ---
st.markdown("## Movies Data")
try:
    data = pd.read_csv("movies.csv")
    st.write(data)
except FileNotFoundError:
    st.warning("The file 'movies.csv' was not found.")

# --- Section: Chart with Random Data ---
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.markdown("## Random Charts")
st.bar_chart(chart_data)
st.line_chart(chart_data)

# --- Section: Mortgage Calculator ---
st.title("Mortgage Repayments Calculator")
st.write("### Input Data")
col1, col2 = st.columns(2)

home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

# Mortgage Calculations
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)
col1.metric("Monthly Repayments", f"${monthly_payment:,.2f}")
col2.metric("Total Repayments", f"${total_payments:,.0f}")
col3.metric("Total Interest", f"${total_interest:,.0f}")

# --- Section: Payment Schedule Chart ---
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    schedule.append([i, monthly_payment, principal_payment, interest_payment, remaining_balance, year])

df = pd.DataFrame(schedule, columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"])

st.write("### Payment Schedule")
payments_df = df.groupby("Year")["Remaining Balance"].min()
st.line_chart(payments_df)
