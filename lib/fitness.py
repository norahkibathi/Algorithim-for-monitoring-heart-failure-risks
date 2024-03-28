from sqlalchemy import Column, Integer, String,Float, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class FitnessExpert(Base):
  __tablename__ = 'fitness_experts'

  id = Column("id",Integer, primary_key=True)
  firstname = Column("Firstname",String)
  lastname = Column("Lastname",String)
  age = Column("Age", Integer)
  gender = Column("Gender",String)
  working_hours = Column("Working hours",Integer)
  salary = Column("Salary", Float, nullable=False)
  specialization = Column("specialization", String(50))  
  working_hours = Column("working_hours", Integer)
  #this is a one to many relationship where a single fitness expert can have many patients
  patients = relationship("Patient", backref="fitness_expert")  

  def __init__(self, name, working_hours=0, salary=0.0):
    self.name = name
    self.working_hours = working_hours
    self.salary = salary
