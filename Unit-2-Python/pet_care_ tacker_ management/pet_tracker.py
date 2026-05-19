import os

class PetCareTracker:
    def __init__(self):
        # Save file in Documents folder
        self.file_path = os.path.join(os.path.expanduser("~"), "Documents", "pet_log.txt")

    def add_entry(self):
        pet_name = input("Enter pet name: ")
        pet_type = input("Enter pet type (Dog/Cat/etc.): ")
        date = input("Enter date (YYYY-MM-DD): ")
        activity = input("Enter activity (Fed, Walked, Groomed, etc.): ")
        notes = input("Any notes: ")

        # Ensure the folder exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        with open(self.file_path, "a") as file:
            file.write(f"{pet_name} | {pet_type} | {date} | {activity} | {notes}\n")
        print("Pet activity added successfully!")

    def view_entries(self):
        try:
            with open(self.file_path, "r") as file:
                data = file.readlines()
                if not data:
                    print("No pet activity found.")
                else:
                    print("\n--- All Pet Activities ---")
                    for line in data:
                        pet_name, pet_type, date, activity, notes = line.strip().split(" | ")
                        print(f"Pet: {pet_name} | Type: {pet_type} | Date: {date} | Activity: {activity} | Notes: {notes}")
        except FileNotFoundError:
            print("No pet log found. Add an entry first!")

    def search_entries(self):
        keyword = input("Enter pet name or date to search: ").lower()
        try:
            with open(self.file_path, "r") as file:
                found = False
                for line in file:
                    if keyword in line.lower():
                        pet_name, pet_type, date, activity, notes = line.strip().split(" | ")
                        print(f"Found -> Pet: {pet_name} | Type: {pet_type} | Date: {date} | Activity: {activity} | Notes: {notes}")
                        found = True
                if not found:
                    print("No matching pet activity found.")
        except FileNotFoundError:
            print("No pet log found. Add an entry first!")

    def menu(self):
        while True:
            print("\n--- Pet Care Tracker ---")
            print("1. Add Pet Activity")
            print("2. View All Activities")
            print("3. Search Activity")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entries()
            elif choice == "3":
                self.search_entries()
            elif choice == "4":
                print("Exiting Pet Care Tracker...")
                break
            else:
                print("Invalid choice! Try again.")


# Run the Pet Care Tracker
if __name__ == "__main__":
    app = PetCareTracker()
    app.menu()