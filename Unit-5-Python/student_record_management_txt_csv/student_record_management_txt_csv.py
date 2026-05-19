import csv
txt_data = []
csv_data = []
def add_txt():
 sid = input("Enter ID: ")
 name = input("Enter Name: ")
 marks = input("Enter Marks: ")
 txt_data.append(f"{sid} {name} {marks}")
 print("Record added (TXT)!")
def add_csv():
 sid = input("Enter ID: ")
 name = input("Enter Name: ")
 marks = input("Enter Marks: ")
 csv_data.append([sid, name, marks])
 print("Record added (CSV)!")
def view_txt():
 print("\n--- TXT Records ---")
 for record in txt_data:
 print(record)
def view_csv():
 print("\n--- CSV Records ---")
 for row in csv_data:
 print("ID:", row[0], "Name:", row[1], "Marks:", row[2])
def search_csv():
 sid = input("Enter ID to search: ")
 found = False
 for row in csv_data:
 if row[0] == sid:
 print("Record Found:", row)
 found = True
 break
 if not found:
 print("Record not found!")
while True:
 print("\n--- Student Record System ---")
 print("1. Add Student (TXT)")
 print("2. Add Student (CSV)")
 print("3. View TXT")
 print("4. View CSV")
 print("5. Search CSV")
 print("6. Exit")
 choice = input("Enter choice: ")
 if choice == "1":
 add_txt()
 elif choice == "2":
 add_csv()
 elif choice == "3":
 view_txt()
 elif choice == "4":
 view_csv()
 elif choice == "5":
 search_csv()
 elif choice == "6":
 print("Program Exited.")
 break
 else:
 print("Invalid choice!")
