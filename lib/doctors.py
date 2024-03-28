from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from lib.base import Base
from base import SessionLocal

class Doctor(Base):
  __tablename__ = 'doctors'
#database for doctors  table in the database
  id = Column("id",Integer, primary_key=True)
  firstname = Column("Firstname",String)
  lastname = Column("Lastname",String)
  age = Column("Age", Integer)
  gender = Column("Gender",String)
  working_hours = Column("Working hours",Integer)
  salary = Column("Salary", Float, nullable=False)
  #this is a one to many relationship where a single doctors expert can have many patients
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

  def calculate_salary(self,working_hours,salary):
        #Calculating doctor's salary based on his/her working hours since cardiologists will be working on consulatation basis 
    salary = (2000 * working_hours)

  def __str__(self):
   #template for printing doctors details 
       return f"Doctor:ID: {self.id}, {self.first_name} {self.last_name} (ID: {self.id}) - Age: {self.age}, Gender: {self.gender}, Working Hours: {self.working_hours}, Salary: ${self.salary:.2f}"

#example
  #doctor1 = Doctor("Douglous", "Wambai", 39, "Male", 90000, 90)