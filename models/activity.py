# models/activity.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from db import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    duration = Column(Float)  # in minutes
    category = Column(String)  # e.g., learning, creative, physical, social
    notes = Column(String)    # optional notes

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='activities')

    def __repr__(self):
        return f"<Activity(id={self.id}, name='{self.name}', category='{self.category}')>"