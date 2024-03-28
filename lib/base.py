#the project preffered a centralised database management system to clean codes and effienciency
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///algorithim_for_monitoring_heart failure.db"  
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
Base = declarative_base()
Base.metadata.create_all(engine)
# the code is for creating data base sessions 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
