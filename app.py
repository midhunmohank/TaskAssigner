import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import json
import sqlite3

# # Create a connection to the database
conn = sqlite3.connect('tasks.db')


#function to get the data from the url every Sunday
def get_data():
    # Send a request to the website
    url = 'https://freakqency.pythonanywhere.com'
    response = requests.get(url)



    # Convert json to dictionary
    data = json.loads(response.text)

        # Convert the dictionary to a list of tuples
    data_list = [(name, task) for name, task in data.items()]

    # Create a DataFrame from the list
    df = pd.DataFrame(data_list, columns=['Names', 'Task'])

    # Write the DataFrame to a sqlite database

    df.to_sql('tasks', conn, if_exists='replace', index=False)

# get_data()
# # Get the data every Sunday
if datetime.today().weekday() == 0:
    get_data()


# # Show the updated DataFrame after the user checks the checkboxes
st.write("Here's the updated task list:")

#Fetch the data from the database
df = pd.read_sql('SELECT * FROM tasks', conn)

# Show the DataFrame
st.dataframe(df)

