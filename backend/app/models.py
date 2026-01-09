from sqlalchemy import Column, Integer, String
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="junior_hr")  # junior_hr / senior_hr

from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, nullable=False)
    job_description = Column(String, nullable=False)
    expected_close_date = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)
    emp_id = Column(String, ForeignKey("employees.emp_id"))


