from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

activity_goals = Table(
    'activity_goals',
    Base.metadata,
    Column('activity_id', Integer, ForeignKey('activities.id')),
    Column('goal_id', Integer, ForeignKey('goals.id'))
)
