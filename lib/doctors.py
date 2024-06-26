from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from lib.models import Patient
Base = declarative_base
class Doctor(Base):
  __tablename__ = 'doctors'
#database for doctors  table in the database
  id = Column("id",Integer, primary_key=True)
  firstname = Column("Firstname",String)
  lastname = Column("Lastname",String)
  age = Column("Age", Integer)
  gender = Column("Gender",String)
  email = Column("Email", String) 
  address = Column("Address", String)  
  phone_number = Column("Phone Number", String)  
  working_hours = Column("Working hours",Integer)
  salary = Column("Salary", Float, nullable=False)
  #this is a one to many relationship where a single doctors expert can have many patients
  patients = relationship("Patient", backref="doctor")

  def __init__(self,id,firstname, lastname, gender,age,address,email, phone_number,salary,working_hours=0):
   #attributes for the doctors class
    self.id = None  
    self.firstname = firstname 
    self.lastname = lastname
    self.age = age
    self.gender = gender
    self.address =address
    self.email= email
    self.phone_number = phone_number
    self.working_hours = working_hours
    self.salary = salary 
    self.calculate_salary()

  def calculate_salary(self,working_hours,salary):
        #Calculating doctor's salary based on his/her working hours since cardiologists will be working on consulatation basis 
    salary = (2000 * working_hours)

  def __str__(self):
   #template for printing doctors details 
       return f"fitness Expert:ID: {self.id}, {self.first_name} {self.last_name} Age: {self.age}, Gender: {self.gender},Address:{self.address}, Email: {self.email} , Phone_number: {self.phone_number}, Working Hours: {self.working_hours}, Salary: ${self.salary:.2f}"

#example
  #doctor1 = Doctor("Douglous", "Wambai", 39, "Male", "gathage", "dagy@gmail", 07224455, 90000, 90)