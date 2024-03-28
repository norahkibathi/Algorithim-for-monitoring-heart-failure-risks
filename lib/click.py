

# the import allows the cli application within the system
app = typer.Typer()
users = []

# code for getting a database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Function to get a currently logged-in user (placeholder)

def get_current_user(session):
   #represents the exising data base for users 
   #the users  are being searched by their id, or user names
    user_id = session.get('user_id') 
    if user_id:
        for user in users:
            if user["username"] == session.get('username'): 
                return user
            
        else:
            print("User ID found in session but user not found in user list")
            return None 
   # in case there is no user 
    return None
def register(username, password, user_type):
    #the code allows new users to register
    if any(user["username"] == username for user in users):
        print("Username already exists")
    else:
        users.append({"username": username, "password": bcrypt.hash(password), "user_type": user_type})
        print("Registration successful")
def login(username, password):
    #the function checks whether the entered credentials are correct for the existing user
     for user in users:
        if user["username"] == username and bcrypt.verify(password, user["password"]):
            return user
     return None
# Login Menu
@app.command()
def login_menu():
    print("Login")
    username = input("Username: ")
    password = getpass("Password: ")

    with get_session() as session:
       #ensures that the log in users have used the correct creditials
        user = session.query(Patient).filter_by(username=username).first()  
        if user and bcrypt.verify(password, user.password_hash):
            return user
        else:
            print("Invalid username or password.")
            return None
    user = get_logged_in_user()  # Retrieve user object (assuming login has already happened)





# Registration Function
def register_user(session, user_type):
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    password_hash = bcrypt.hash(password)  # Hash password

    # Create a new user object based on user type
    if user_type == "patient":
        new_user = Patient(username=username, password_hash=password_hash)
    elif user_type == "doctor":
        new_user = Doctor(username=username, password_hash=password_hash)
    elif user_type == "fitness_expert":
        new_user = FitnessExpert(username=username, password_hash=password_hash)
    else:
        print("Invalid user type.")
        return
    session.add(new_user)
    session.commit()
    print(f"User {username} registered successfully!")
#allows the user
# Main Menu
@app.command()
def main_menu():
    user = login_menu()  # Attempt login before entering main menu
    if user:
        if isinstance(user, Patient):
            patient_menu(user)
        elif isinstance(user, Doctor):
            doctor_menu(user)
        elif isinstance(user, FitnessExpert):
            fitness_expert_menu(user)
    else:
        print("Login failed. Please try again or register as a new user.")

# Registration Menu (Optional)
@app.command()
def registration_menu():
    print("Register")
    print("1. Register as Patient")
    print("2. Register as Doctor (For authorized personnel only)") 
    print("3. Register as Fitness Expert (For authorized personnel only)") 
    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3"]:
        user_type = "patient" if choice == "1" else ("doctor" if choice == "2" else "fitness_expert")
        with get_session() as session:
            register_user(session, user_type)
    else:
        print("Invalid choice.")

# Patient Menu
def patient_menu(user):
    while True:
        print("\nPatient Management")
        print("1. Update Personal Information")
        print("2. View Personal Information")
        print("3. Find Doctor")
        print("4. Find Fitness Expert")
        print("5. Calculate Risk Score")  # Placeholder (logic assumed elsewhere)
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Example update patient information functionality (replace with your logic)
            print("Update Personal Information (placeholder)")
        elif choice == "2":
            # Example view patient information functionality (replace with your logic)
            print("View Personal Information (placeholder)")
        elif choice == "3":
            # Example find doctor functionality (replace with your logic)
            print("Find Doctor (placeholder)")
        elif choice == "4":
            # Example find
