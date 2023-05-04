from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

# Establish the connection to the database
engine = create_engine('postgresql://username:password@localhost:5432/database_name')
