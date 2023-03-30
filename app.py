import streamlit as st
import pandas as pd
import requests
from datetime import datetime

#function to get the data from the url every Sunday
def get_data():
    # Send a request to the website
    url = 'https://freakqency.pythonanywhere.com'
    response = requests.get(url)

    responses = response.content.decode('utf-8')

    # Split the string into rows and columns
    rows = responses.split('\n')
    cols = rows[0].split(':')
    data = [r.split(':') for r in rows if r]

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=["Assigned to","Task"])
    df.to_csv('tasks.csv', index=False)

if datetime.today().weekday() == 0:
    get_data()

# Read the data from the CSV file
df = pd.read_csv('tasks.csv')

# Show the updated DataFrame after the user checks the checkboxes
st.write("Here's the updated task list:")
st.write(df)
