from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import uuid
import math

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class Patient(Base):
    __tablename__ = 'patients'
    id = Column("PatientID", Integer, primary_key=True, default=generate_uuid)
    firstname = Column("Firstname", String)
    lastname = Column("Lastname", String)
    age = Column("Age", Integer)
    gender = Column("Gender", String)
    address = Column("address", String)
    phone_number = Column("Phone Number", String)
    email = Column("email", String)
    diabetes = Column("Diabetes Condition", Boolean)
    family_history = Column("Familyhistory", Boolean)
    weight = Column("Weight", Float)
    hypertension = Column("Hypertension", Boolean)
    smoking = Column("Smoker?", Boolean)
    risk_score = Column("risk_score", Integer, default=0) 
    risk_category = Column("risk_category", String, default='')  

    def __init__(self, firstname, lastname, age, gender, address="", phone_number="", email="",
                 diabetes=False, hypertension=False, smoking=False, weight=0.0, height=0.0,
                 family_history=""):
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.diabetes = diabetes
        self.hypertension = hypertension
        self.smoking = smoking
        self.weight = weight
        self.family_history = family_history
        self.calculate_risk_score()
        self.get_risk_category()

    def calculate_risk_score(self):
        self.risk_score = 0
        if self.age >= 65:
            self.risk_score += 1
        self.risk_score += int(self.diabetes)
        self.risk_score += int(self.hypertension)
        self.risk_score += int(self.smoking)
        if self.weight:
            bmi = self.weight / ((self.height / 100) ** 2)
            if bmi < 18.5 or bmi >= 25:
                self.risk_score += 1
        self.risk_score += int(self.family_history)

    def get_risk_category(self):
        if self.risk_score >= 4:
            self.risk_category = "You are at a HIGH RISK of heart failure. Please consult a doctor for further evaluation and management."
        elif self.risk_score >= 2:
            self.risk_category = "You are at a MODERATE RISK of heart failure. Consider lifestyle modifications and consult a doctor for personalized advice."
        else:
            self.risk_category = "You are at a LOW RISK of heart failure based on this assessment. However, it's important to maintain healthy habits and schedule regular checkups."

# Create engine and session
db = "sqlite:///heart_monitor.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Query patients
patients = session.query(Patient).all()

# Creating data for the database
patient1 = Patient("Markson", "mutheu", 80, "Male", diabetes=True, hypertension=True, smoking=True, family_history=False)
print(f"Patient 1 Risk Score: {patient1.risk_score}")
print(f"Patient 1 Risk Category: {patient1.risk_category}")

# Close the session
session.close()
