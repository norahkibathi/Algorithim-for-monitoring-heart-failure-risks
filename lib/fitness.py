from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from lib.models import Patient
Base = declarative_base
engine = create_engine('sqlite:///fitness_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class FitnessExpert(Base):
  #database for fitness table in the database
  __tablename__ = 'fitness_experts'

  id = Column("id", Integer, primary_key=True)
  firstname = Column("Firstname", String)
  lastname = Column("Lastname", String)
  age = Column("Age", Integer)
  gender = Column("Gender", String)
  working_hours = Column("Working hours", Integer)  
  salary = Column("Salary", Float)  
  specialization = Column("specialization", String(50))
  # This is a one-to-many relationship where a single fitness expert can have many patients
  patients = relationship("Patient", backref="fitness_expert")  

  def __init__(self, firstname, lastname, age, gender, address="", email="", phone_number="", working_hours=0, salary=None):
        #attributes for the fitness class
     self.id = None  
     self.firstname = firstname 
     self.lastname = lastname
     self.age = age
     self.gender = gender
     self.address = address
     self.email = email
     self.phone_number = phone_number
     self.working_hours = working_hours
     self.salary = self.calculate_salary(working_hours) 

     def calculate_salary(self, working_hours):
        # the salary for the experts will be calculated using base salary and hourly rates
        # The base salary is set to $1000.0
        #the hourly rate is set at $50
        base_salary = 1000.00  
        hourly_rate = 50.00  
        total_salary = base_salary + (working_hours * hourly_rate)
        return total_salary

     def __str__(self):
   # Template for printing fitness expert details
       return f"Fitness Expert: ID: {self.id}, {self.firstname} {self.lastname} (ID: {self.id}) - Age: {self.age}, Gender: {self.gender}, Address:{self.address}, Email: {self.email} , Phone_number: {self.phone_number}, Working_Hours: {self.working_hours}, Salary: ${self.salary:.2f}"

