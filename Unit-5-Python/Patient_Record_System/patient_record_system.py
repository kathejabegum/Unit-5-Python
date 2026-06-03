import csv

file_name = "patients.csv"

# -------- CREATE FILE WITH HEADER --------
def create_file():
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Disease"])
    print("File created successfully!\n")


# -------- ADD PATIENT --------
def add_patient():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    
    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, age, disease])
    
    print("Patient added!\n")


# -------- VIEW PATIENTS --------
def view_patients():
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            
            print("\n--- Patient Records ---")
            for row in reader:
                print(row)
                
    except FileNotFoundError:
        print("File not found. Create file first.\n")


# -------- MENU --------
while True:
    print("\n1. Create File")
    print("2. Add Patient")
    print("3. View Patients")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        create_file()
    elif choice == "2":
        add_patient()
    elif choice == "3":
        view_patients()
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Invalid choice")