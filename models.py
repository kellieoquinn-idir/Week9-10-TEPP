##This file handles all the models in our database. Helps establishes schema and internal relationships
from sqlalchemy import Column, Numeric, ForeignKey, Integer, String, Boolean, DateTime, Text, Numeric
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

DBModelBase = declarative_base()

class Customer(DBModelBase):
     __tablename__ = "Customers"
     id = Column(Text, primary_key=True, index=True)                              # UUID
     name = Column(String(150), nullable=False)
     timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)        # exact time of call
     day_of_call = Column(String(10), nullable=False)                             # e.g. "Monday"
     hour_of_day = Column(Integer, nullable=False)                                # 0–23
     wait_time = Column(Integer, nullable=False)                                  # minutes
     issue_category = Column(Text, nullable=False)                              # Billing, Technical, Service, Account
     resolution_status = Column(Boolean, nullable=False)                          #True if resolved, False if not                     


