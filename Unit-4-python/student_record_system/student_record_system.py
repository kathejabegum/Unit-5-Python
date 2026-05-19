

students = []                      
subjects = ("Math", "Science")     
roll_set = set()                   

def average(m1, m2):               
    return (m1 + m2) / 2           


def count(n):                      
    if n == 0:
        return 0
    return 1 + count(n - 1)


while True:                        
    print("\n1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:                
        name = input("Enter name: ")     
        roll = int(input("Enter roll: "))

        if roll in roll_set:
            print("Roll already exists")
            continue

        roll_set.add(roll)

        m1 = int(input("Math marks: "))
        m2 = int(input("Science marks: "))

        avg = average(m1, m2)

        student = {                
            "Name": name,
            "Roll": roll,
            "Average": avg
        }

        students.append(student)

    elif choice == 2:
        for s in students:
            print(s)

        print("Total Students:", count(len(students)))

    elif choice == 3:
        break

    else:
        print("Invalid choice")