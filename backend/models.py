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
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    goal_steps = Column(Integer, nullable=False)

class stepsHistory(Base):
    __tablename__ = "stepsHistory"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)
    step_count_daily = Column(Integer, nullable=False, server_default=text('0'))
    goal_steps = Column(Integer, nullable=False, server_default=text('5000'))
    date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    goal_steps = Column(Integer, nullable=False)

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)
    email = Column(String)
    amount = Column(Integer)
    currency = Column(String)
    status = Column(String)
    user_id = Column(Integer)
    request_id = Column(String)