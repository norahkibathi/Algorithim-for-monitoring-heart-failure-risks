import typer
from sqlalchemy.orm import Session  
from lib import Patient, Doctor, FitnessExpert, SessionLocal
def get_user_details(user_type):
    session = SessionLocal() 
    details = {}
    if user_type == "patient":
        details["firstname"] = input("Enter your first name: ")
        details["lastname"] = input("Enter your last name: ")
        details["age"] = int(input("Enter your age: "))
        details["gender"] = input("Enter your gender (M/F): ")
        details["address"] = input("Enter your address: ")
        details["email"] = input("Enter your email: ")
        details["phonenumber"] = input("Enter your phonenumber: ")
        details["diabetes"] = bool(input("Do you have diabetes? (y/n): ").lower() == "y")
        details["hypertension"] = bool(input("Do you have hypertension? (y/n): ").lower() == "y")
        details["smoking"] = bool(input("Do you smoke? (y/n): ").lower() == "y")
        details["weight"] = float(input("Enter your weight (kg): "))
        details["height"] = float(input("Enter your height (m): "))
        details["family_history"] = input("Enter your family history (optional): ")
    elif user_type == "fitness_expert":
        details["firstname"] = input("Enter your first name: ")
        details["lastname"] = input("Enter your last name: ")
        details["age"] = int(input("Enter your age: "))
        details["gender"] = input("Enter your gender (M/F): ")
        details["address"] = input("Enter your address: ")
        details["email"] = input("Enter your email: ")
        details["phonenumber"] = input("Enter your phonenumber: ")
        details["specialization"] = input("Enter your area of specialization (optional): ")
        details["working_hours"] = int(input("Enter fitness expert's working hours: "))
        details["salary"] = details["working_hours"] * 50 # the calculation is based on the assumption of $50 per hour
    elif user_type == "doctor":
        details["firstname"] = input("Enter your first name: ")
        details["lastname"] = input("Enter your last name: ")
        details["age"] = int(input("Enter your age: "))
        details["gender"] = input("Enter your gender (M/F): ")
        details["address"] = input("Enter your address: ")
        details["email"] = input("Enter your email: ")
        details["phonenumber"] = input("Enter your phonenumber: ")
        details["specialization"] = input("Enter your area of specialization (optional): ")
        details["working_hours"] = float(input("Enter fitness expert's working hours: "))
        details["salary"] = details["working_hours"] * 2000 # payment is done on hourly basisis
    return details
app = typer.Typer()
import typer
from sqlalchemy.orm import Session
from lib import Patient, Doctor, FitnessExpert, SessionLocal

app = typer.Typer()

@app.command()
#creates a new user
def create_user(user_type: str):
    details = get_user_details(user_type)

    session = SessionLocal()

    new_user = None
    #retrives  the class based on the type of user and creates an instance of it with the received data
    
    if user_type == "patient":
        new_user = Patient(**details)
    elif user_type == "fitness_expert":
        new_user = FitnessExpert(**details)
    elif user_type == "doctor":
        new_user = Doctor(**details)

    session.add(new_user)
    session.commit()

    print(f"{user_type.capitalize()} created successfully!")

    session.close()


if __name__ == "__main__":
    app()

