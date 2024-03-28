from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from base import SessionLocal
from base import Base
from doctors import Doctor
from fitness import FitnessExpert



Base = declarative_base()
#the code creates a database for patients with the class of Patient. The table details will be used to store and manage patient's data on heart risk failure. 
class Patient(Base):
    __tablename__ = 'patients'

    id = Column("id", Integer, primary_key=True)
    firstname = Column("Firstname",String)
    lastname = Column("Lastname",String)
    age = Column("Age", Integer)
    gender = Column("Gender",String)
    diabetes = Column("Diabetes Condition", Boolean)
    family_history = Column("Familyhistory", Boolean)
    obese = Column("Obese", Boolean)
    hypertension = Column("Hypertension",Boolean)
    heart_disease = Column("Heart Disease", Boolean)
    smoking=Column( "Smoker?", Boolean ) 
    address = Column("address",Integer)
    phone_number = Column("Phone Number",String)
    email = Column("email",String)
    other_illnesses = Column("Other Illnesses", String)
    doctor_id = Column("Doctorid", Integer, ForeignKey('doctors.id')) 
    doctor = relationship("Doctor", backref="patients")
    fitness_expert_id = Column("Fitness Expert". Integer, ForeignKey('fitness_experts.id'))
    fitness_expert = relationship("FitnessExpert", backref="patients") 
class Patient(Base):
  __tablename__ = 'patients'

  def __init__(self, firstname, lastname, age, gender, address="", phone_number="", email="",
                 diabetes=False, hypertension=False, smoking=False, weight=0.0, height=0.0,
                 family_history="", doctor=None, fitness=None, appointment_date=None):
   #the method enable object initialzation for the block
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

  def calculate_risk_score(self):
    risk_score = 0
    if self.age >= 65:
        risk_score += 1
    risk_score += int(self.diabetes)
    risk_score += int(self.hypertension)
    risk_score += int(self.smoking)
    #the code focuses on calculating Obesity based on WHO ((2023 reccomendation ))
    if self.weight and self.height:
        bmi = self.weight / (self.height / 100) ** 2
        if bmi < 18.5 or bmi >= 25:
            risk_score += 1
    risk_score += int(self.family_history)

    return risk_score

  def get_risk_category(self):
    if self.risk_score >= 4:
        return "You are at a HIGH RISK of heart failure. Please consult a doctor for further evaluation and management."
    elif self.risk_score >= 2:
        return "You are at a MODERATE RISK of heart failure. Consider lifestyle modifications and consult a doctor for personalized advice."
    else:
        return "You are at a LOW RISK of heart failure based on this assessment. However, it's important to maintain healthy habits and schedule regular checkups."

#testing
#patient1 = Patient("Markson", 80, "Male", diabetes=True, hypertension=True, smoking=True)
#print(f"Patient 1 Risk Score: {patient1.risk_score}")
#patient1 = Patient("JUSTUS MUTURI", 80, "FeMale", diabetes=false, hypertension=True, smoking=True)
#print(f"Patient 2 Risk category: {patient1.get_risk_category}")
      
   
 
