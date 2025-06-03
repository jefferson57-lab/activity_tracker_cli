def seed_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Sample users
    users = [
        User(username="creative_jane", email="jane@example.com"),
        User(username="studious_bob", email="bob@example.com")
    ]

    # Sample activities
    activities = [
        Activity(name="Spanish lesson", duration=30, category="Learning", date="2023-10-01", user=users[0]),
        Activity(name="Morning jog", duration=45, category="Physical", date="2023-10-01", user=users[0]),
        Activity(name="Watercolor painting", duration=60, category="Creative", date="2023-10-02", user=users[0]),
        Activity(name="Team meeting", duration=90, category="Professional", date="2023-10-02", user=users[1]),
        Activity(name="Meditation", duration=20, category="Mindfulness", date="2023-10-03", user=users[1])
    ]

    session.add_all(users + activities)
    session.commit()