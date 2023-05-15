from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

# Establish the connection to the database
engine = create_engine('postgresql://username:password@localhost:5432/database_name')

Session = sessionmaker(bind=engine)
session = Session()

# Function to clean up user input and prevent SQL injection attacks
def clean_input(user_input):

  # Remove special characters and escape single quotes
    cleaned_input = re.sub('[^A-Za-z0-9]+', '', user_input)
    cleaned_input = cleaned_input.replace("'", "''")
    return cleaned_input

def execute_query(query):
user_input = 'user_value'
   try:
    cleaned_query = clean_input(query)
        results = session.execute(cleaned_query)
        session.commit()
        return results
    except:
session.rollback()
        return None
results = execute_query("SELECT * FROM users WHERE username = '{}'".format(user_input))

////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# version 2

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
