print("Welcome to Clinic Management System")
total_earnings = 0
patient_count = 0
while True:
    print("\n1. New Patient")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        print("Select Consultation Type")
        print("1. General Checkup (Rs.300)")
        print("2. Specialist Visit (Rs.600)")
        print("3. Emergency (Rs.1000)")
        consult = int(input("Enter option: "))
        if consult == 1:
            fee = 300
        elif consult == 2:
            fee = 600
        elif consult == 3:
            fee = 1000
        else:
            print("Invalid consultation type")
            continue
        lab_test = input("Need lab test? (yes/no): ")
        if lab_test.lower() == "yes":
            fee += 500
        print("\n--- Patient Bill ---")
        print("Name:", name)
        print("Age:", age)
        print("Total Fee: Rs.", fee)
        total_earnings += fee
        patient_count += 1
    elif choice == 2:
        print("\nTotal Patients Today:", patient_count)
        print("Total Earnings: Rs.", total_earnings)
        print("Clinic Closed.")
        break
    else:
        print("Invalid choice!")
