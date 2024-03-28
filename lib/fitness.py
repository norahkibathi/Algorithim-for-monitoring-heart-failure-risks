from requests import session
from sqlalchemy import Column, Integer, String,Float, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from base import SessionLocal

class FitnessExpert(Base):
  __tablename__ = 'fitness_experts'

  
  id = Column(Integer, primary_key=True)
  firstname = Column("Firstname", String)
  lastname = Column("Lastname", String)
  age = Column("Age", Integer)
  gender = Column("Gender", String)
  working_hours = Column("Working hours", Integer)  
  salary = Column("Salary", Float)  
  specialization = Column("specialization", String(50))
  #this is a one to many relationship where a single fitness expert can have many patients
  patients = relationship("Patient", backref="fitness_expert")  

  def __init__(self,id,firstname, lastname, gender,age,address,email, phone_number, working_hours=0,salary=None):
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
        #Calculating fitness_expert's salary based on his/her working hours since fitness experts will be working on consulatation basis 
    salary = (500 * working_hours)

  def __str__(self):
   #template for printing doctors details 
       return f"fitness Expert:ID: {self.id}, {self.first_name} {self.last_name} (ID: {self.id}) - Age: {self.age}, Gender: {self.gender},Address:{self.address}, Email: {self.email} , Phone_number: {self.phone_number}, Working Hours: {self.working_hours}, Salary: ${self.salary:.2f}"
#examples
fitness_expert1 = FitnessExpert("Kennedy", "Mbungua", 35, "Male", 40, 0.0, "Cardio", "mbugs@email.com", 2000)  


print(fitness_expert1.__str__())


session.add (fitness_expert1 )
session.commit(fitness_expert1)