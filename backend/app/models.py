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


from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))  # Link to job
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    resume = Column(String)  # store file path or URL
    experience = Column(Float)  # in years
    ctc = Column(Float)  # current salary
    expected_ctc = Column(Float)  # expected salary

    job = relationship("Job", backref="applications")  # optional ORM relationship


from sqlalchemy import Column, Integer, DateTime, JSON
from app.database import Base
from datetime import datetime


class EmployeeManagement(Base):
    __tablename__ = "employee_management"

    id = Column(Integer, primary_key=True, index=True)

    # -------- Personal --------
    personal = Column(
        JSON,
        default=lambda: {
            "employee_code": "",
            "name": {"first_name": "", "last_name": ""},
            "contact": {"email": "", "phone": ""},
            "dob": "",
            "gender": "",
            "blood_group": "",
            "marital_status": "",
            "address": {
                "house": "",
                "street": "",
                "city": "",
                "state": "",
                "pincode": ""
            },
            "emergency_contact": {
                "name": "",
                "relation": "",
                "phone": ""
            }
        }
    )

    # -------- Employment --------
    employment = Column(
        JSON,
        default=lambda: {
            "role": "",
            "designation": "",
            "department": "",
            "employment_type": "",
            "date_of_joining": "",
            "work_location": "",
            "manager_id": "",
            "manager_name": "",
            "status": "Active"
        }
    )

    # ✅ -------- Compensation (LIST) --------
    compensation = Column(
        JSON,
        default=lambda: []   # IMPORTANT: list
    )

    # -------- Attendance --------
    attendance = Column(
        JSON,
        default=lambda: {
            "summary": {
                "total_working_days": 0,
                "present_days": 0,
                "absent_days": 0,
                "leave_days": 0
            },
            "monthly": {}
        }
    )

    # -------- Assets --------
    assets = Column(
        JSON,
        default=lambda: {
            "laptop": {
                "brand": "",
                "model": "",
                "serial_number": "",
                "assigned_date": ""
            },
            "id_card": {
                "card_number": "",
                "issued_date": ""
            },
            "other_assets": []
        }
    )

    # -------- Documents --------
    documents = Column(
        JSON,
        default=lambda: {
            "aadhar": "",
            "pan": "",
            "passport": "",
            "resume": "",
            "offer_letter": "",
            "appointment_letter": "",
            "experience_letter": "",
            "previous_job_relieving_letter": ""
        }
    )

    # -------- Exit Details --------
    exit_details = Column(
        JSON,
        default=lambda: {
            "resignation_date": "",
            "last_working_day": "",
            "reason": "",
            "exit_status": "",
            "hr_remarks": ""
        }
    )

    created_at = Column(DateTime, default=datetime.utcnow)
