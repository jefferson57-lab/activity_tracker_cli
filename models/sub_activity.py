from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class SubActivity(Base):
    __tablename__ = 'sub_activities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)  # Generic quantity field (could be reps, minutes, etc.)
    sets = Column(Integer)

    activity_id = Column(Integer, ForeignKey('activities.id'))

    # Relationship
    activity = relationship('Activity', back_populates='sub_activities')

    def __repr__(self):
        return f"<SubActivity(id={self.id}, name='{self.name}', quantity={self.quantity}, sets={self.sets})>"