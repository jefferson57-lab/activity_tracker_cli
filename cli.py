from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Database setup
engine = create_engine('sqlite:///activity_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Models
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
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

    # Select category first
    print("Select a category:")
    for i, category in enumerate(ACTIVITY_CATEGORIES, 1):
        print(f"{i}. {category}")
    
    try:
        category_choice = int(input("Enter category number: ").strip())
        if not 1 <= category_choice <= len(ACTIVITY_CATEGORIES):
            raise ValueError
    except ValueError:
        print("❌ Invalid category selection.")
        return

    selected_category = ACTIVITY_CATEGORIES[category_choice - 1][2:]  # Remove emoji

    # Proceed with the rest of the details
    name = input("Activity name: ").strip()
    if not name:
        print("❌ Activity name cannot be empty.")
        return

    date = input("Date (YYYY-MM-DD): ").strip()
    duration_input = input("Duration (minutes): ").strip()
    try:
        duration = float(duration_input)
    except ValueError:
        print("❌ Invalid duration. Please enter a number.")
        return

    notes = input("Optional notes: ").strip()

    activity = Activity(
        name=name,
        date=date,
        duration=duration,
        category=selected_category,
        notes=notes,
        user_id=user.id
    )

    session.add(activity)
    session.commit()
    print(f"✅ '{name}' activity logged successfully under '{selected_category}' category!")


def create_or_login_user():
    print("\n👤 Welcome to Activity Tracker")
    username = input("Enter your username: ").strip()

    user = session.query(User).filter_by(username=username).first()
    if user:
        print(f"👋 Welcome back, {username}!")
    else:
        email = input("Enter your email to create a new account: ").strip()
        if not email:
            print("❌ Email cannot be empty.")
            return None
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        print(f"✅ User '{username}' created successfully!")

    return user

def view_activities(user):
    print(f"\n📋 Activities for {user.username}:")
    activities = session.query(Activity).filter_by(user_id=user.id).all()
    if not activities:
        print("No activities found.")
    for activity in activities:
        print(f"- {activity.date} | {activity.name} ({activity.duration} min) [{activity.category}] - {activity.notes}")

def delete_user(user):
    confirmation = input(f"\n⚠️ Are you sure you want to delete user '{user.username}' and all associated activities? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        session.query(Activity).filter_by(user_id=user.id).delete()
        session.delete(user)
        session.commit()
        print("🗑️ User and their activities deleted successfully.")
        return True
    else:
        print("❎ Deletion canceled.")
        return False

def main():
    user = create_or_login_user()
    if not user:
        return

    while True:
        print("\n📌 Menu:")
        print("1. Log a new activity")
        print("2. View your activities")
        print("3. Delete your account")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()
        if choice == '1':
            log_activity(user)
        elif choice == '2':
            view_activities(user)
        elif choice == '3':
            if delete_user(user):
                break
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
