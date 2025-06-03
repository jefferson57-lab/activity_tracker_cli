from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)

    activities = relationship('Activity', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"