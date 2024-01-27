import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def generate_date_range(start_date, end_date):
    date_range = []
    current_date = start_date
    while current_date <= end_date:
        date_range.append(current_date.strftime("%d-%m-%Y"))
        current_date += timedelta(days=1)
    return date_range

def generate_flight_pattern(flight_number, start_date, end_date):
    date_range = generate_date_range(start_date, end_date)
    pattern = f"{flight_number} | {' | '.join(date_range)}"
    return pattern

data = {
    'Flight Number': ['ABC123', 'XYZ456', '123XYZ'],
    'Start Date': ['12-01-2024', '15-01-2024', '10-01-2024'],
    'End Date': ['25-01-2024', '20-01-2024', '18-01-2024'],
    'Additional Info': ['Info1', 'Info2', 'Info3'],
}

df = pd.DataFrame(data)

st.title("Flight Pattern Generator")

start_date = st.date_input("Select Start Date:")
end_date = st.date_input("Select End Date:")

selected_flight_numbers = st.multiselect("Select Flight Numbers:", df['Flight Number'].tolist(), default=df['Flight Number'].tolist())

if st.button("Generate Pattern"):
    if selected_flight_numbers and start_date and end_date:
        flight_patterns = []
        for flight_number in selected_flight_numbers:
            pattern = generate_flight_pattern(flight_number, start_date, end_date)
            flight_patterns.append(pattern)
            st.success(f"Flight Pattern for {flight_number}: {pattern}")
    else:
        st.warning("Please fill in all the required fields.")

st.write("All Available Flight Information:")
df_display = pd.DataFrame({
    'Checkbox': (st.checkbox("", value=(flight_number in selected_flight_numbers), key=f"checkbox_{i}") for i, flight_number in enumerate(df['Flight Number'])),
    'Flight Number': df['Flight Number'],
    'Start Date': df['Start Date'],
    'End Date': df['End Date'],
    'Additional Info': df['Additional Info']
})

st.dataframe(df_display[['Checkbox', 'Flight Number', 'Start Date', 'End Date', 'Additional Info']])
