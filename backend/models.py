from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class Users(Base):
    __tablename__ = "Users"
    """
       this is one of the tables which will store the data for the users.
       Each row shows the data of which the column will store
    """
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=True, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class stepsHistory(Base):
    __tablename__ = "stepsHistory"

    id = Column(String, primary_key=True, nullable=False)
    user_id = Column(String, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)
    step_count_daily = Column(Integer, nullable=False, server_default=0)
    goal_steps = Column(Integer, nullable=False, server_default=5000)
    date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
