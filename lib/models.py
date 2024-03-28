from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
Base =declarative_base
def generate_uuid ():
    return str(uuid.uuid4()) 

class Patient(Base):
    # The table details will be used to store and manage patient's data 
# on heart risk failure. 
    __tablename__ = 'patients' 
    id = Column("PatientIDd", Integer, primary_key=True,default=uuid)
    firstname = Column("Firstname", String)
    lastname = Column("Lastname", String)
    age = Column("Age", Integer)
    gender = Column("Gender", String)
    diabetes = Column("Diabetes Condition", Boolean)
    family_history = Column("Familyhistory", Boolean)
    weight = Column("Weight", Float)  
    hypertension = Column("Hypertension", Boolean)
    heart_disease = Column("Heart Disease", Boolean)
    smoking = Column("Smoker?", Boolean)
    address = Column("address", String) 
    phone_number = Column("Phone Number", String)
    email = Column("email", String)
    doctor_id = Column("Doctor_id", Integer, ForeignKey('doctors.id'))
    doctor = relationship("Doctor", backref="patients")
    fitness_expert_id = Column("fitness_expert_id", Integer, ForeignKey('fitness_experts.id'))
    fitness_expert = relationship("FitnessExpert", backref="patients")

    def __init__(self, firstname, lastname, age, gender, address="", phone_number="", email="",
                 diabetes=False, hypertension=False, smoking=False, weight=0.0, height=0.0,
                 family_history="", doctor=None, fitness=None, appointment_date=None):
        # attributes for the patient class
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
        self.height = height
        self.family_history = family_history
        self.doctor = doctor
        self.fitness = fitness
        self.appointment_date = appointment_date
        self.risk_score = self.calculate_risk_score()
#enables achievemen of the code objective of monitoring the heart
    def calculate_risk_score(self):
        risk_score = 0
        if self.age >= 65:
            risk_score += 1
        risk_score += int(self.diabetes)
        risk_score += int(self.hypertension)
        risk_score += int(self.smoking)
        # the code focuses on calculating Obesity based on WHO ((2023 recommendation))
        if self.weight and self.height:
            bmi = self.weight / (self.height / 100) ** 2
            if bmi < 18.5 or bmi >= 25:
                risk_score += 1
        risk_score += int(self.family_history)

        return risk_score
#enables the pateint to know their next step after their heart has been monitired 
    def get_risk_category(self):
        if self.risk_score >= 4:
            return "You are at a HIGH RISK of heart failure. Please consult a doctor for further evaluation and management."
        elif self.risk_score >= 2:
            return "You are at a MODERATE RISK of heart failure. Consider lifestyle modifications and consult a doctor for personalized advice."
        else:
            return "You are at a LOW RISK of heart failure based on this assessment. However, it's important to maintain healthy habits and schedule regular checkups."

# testing
#patient1 = Patient("Markson","mutheu", 80, "Male", diabetes=True, hypertension=True, smoking=True)
#print(f"Patient 1 Risk Score: {patient1.risk_score}")
# patient2 = Patient("JUSTUS MUTURI", 80,
#                   gender="Female", age=70, weight=90, height=170)
# print(f"\n\n{patient1.get_label()} Risk Category: {patient1.get_risk_category()}\n")
        