from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///life_tracker.db')  # Renamed database
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
print("Creating database engine...")  # Add this line
engine = create_engine('sqlite:///life_tracker.db', echo=True)  # Add echo=True
print("Database module initialized")