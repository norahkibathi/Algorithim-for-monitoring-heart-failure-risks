from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Doctor(Base):
  __tablename__ = 'doctors'

  ssn = Column("SSN",Integer, primary_key=True)
  firstname = Column("Firstname",String)
  lastname = Column("Lastname",String)
  age = Column("Age", Integer)
  gender = Column("Gender",String)
  working_hours = Column("Working hours",Integer)
  salary = Column("Salary", Float, nullable=False)
  patients = relationship("Patient", backref="doctor")

  def __init__(self,id,firstname, lastname, gender,age,salary,working_hours=0):
    self.id = None  
    self.firstname = firstname 
    self.lastname = lastname
    self.age = age
    self.gender = gender
    self.working_hours = working_hours
    self.salary = salary 
    self.calculate_salary()

  def calculate_salary(self,working_hours)gi
   salary = working_hours * 2000

