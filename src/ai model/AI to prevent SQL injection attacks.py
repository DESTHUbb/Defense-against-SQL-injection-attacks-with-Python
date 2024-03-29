from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

engine = create_engine('postgresql://username:password@localhost:5432/database_name')

Session = sessionmaker(bind=engine)
session = Session()

def clean_input(user_input):


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

engine = create_engine('postgresql://username:password@localhost:5432/database_name')

Session = sessionmaker(bind=engine)
session = Session()

def clean_input(user_input):
    cleaned_input = text(user_input).bindparams()
    return cleaned_input

def execute_query(query, user_input):
    try:
        
cleaned_query = clean_input(query)
        results = session.execute(cleaned_query, {"user_input": user_input})
    
     session.commit()
        return results
    except Exception as e:
        session.rollback()
        print(f"Error executing query: {e}")
        return None
        
user_input = 'user_value'
query = "SELECT * FROM users WHERE username = :user_input"
results = execute_query(query, user_input)
