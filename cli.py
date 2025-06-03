from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# Database setup
engine = create_engine('sqlite:///activity_tracker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    duration = Column(Float)
    category = Column(String)
    notes = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

# Create tables
Base.metadata.create_all(engine)

# Activity categories
ACTIVITY_CATEGORIES = [
    "📚 Learning",
    "🎨 Creative",
    "🏃 Physical",
    "🧘 Mindfulness",
    "👥 Social",
    "🏠 Domestic",
    "💼 Professional"
]

def log_activity(user):
    print("\n📝 Log a New Activity")
    name = input("Activity name: ")
    date = input("Date (YYYY-MM-DD): ")
    duration = float(input("Duration (minutes): "))
    
    print("\nSelect a category:")
    for i, category in enumerate(ACTIVITY_CATEGORIES, 1):
        print(f"{i}. {category}")
    category_choice = int(input("Enter category number: "))
    
    notes = input("Optional notes: ")
    
    activity = Activity(
        name=name,
        date=date,
        duration=duration,
        category=ACTIVITY_CATEGORIES[category_choice-1][2:],  # Remove emoji
        notes=notes,
        user_id=user.id
    )
    
    session.add(activity)
    session.commit()
    print(f"✅ '{name}' activity logged successfully!")

def main():
    # Create a demo user
    demo_user = User(username="demo", email="demo@example.com")
    session.add(demo_user)
    session.commit()
    
    print("Activity Tracker CLI")
    log_activity(demo_user)

if __name__ == "__main__":
    main()