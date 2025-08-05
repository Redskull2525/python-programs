# Class to represent each student in the mess
class Student:
    def __init__(self, name, roll_no):
        self.name = name                # Student's name
        self.roll_no = roll_no          # Unique roll number
        self.meals = 0                  # Initial meal count is 0

    # Add meals for a student
    def add_meal(self, count=1):
        self.meals += count             # Increase meal count

    # Update meals directly (overwrite)
    def update_meals(self, new_count):
        self.meals = new_count          # Set meal count to new value

    # Calculate total bill based on meal rate
    def calculate_bill(self, rate_per_meal):
        return self.meals * rate_per_meal

    # Display full record for a student
    def display_record(self, rate_per_meal):
        print(f"Name     : {self.name}")
        print(f"Roll No. : {self.roll_no}")
        print(f"Meals    : {self.meals}")
        print(f"Bill     : ₹{self.calculate_bill(rate_per_meal)}")
        print("-" * 30)


# Class to manage all student records in the mess
class MessRecord:
    def __init__(self):
        self.students = {}              # Dictionary to store student records by roll_no
        self.rate_per_meal = 50         # Default meal rate is ₹50

    # Change the rate per meal
    def set_meal_rate(self, new_rate):
        self.rate_per_meal = new_rate
        print(f"✅ Meal rate updated to ₹{self.rate_per_meal} per meal.")

    # Add a new student to the mess
    def add_student(self, name, roll_no):
        if roll_no in self.students:
            print("❌ Student already exists!")  # Prevent duplicate roll numbers
        else:
            self.students[roll_no] = Student(name, roll_no)
            print(f"✅ Student {name} added.")

    # Remove a student by roll number
    def remove_student(self, roll_no):
        if roll_no in self.students:
            removed = self.students.pop(roll_no)  # Remove and return the student
            print(f"✅ Student {removed.name} removed.")
        else:
            print("❌ Student not found.")

    # Record meals for a student
    def record_meal(self, roll_no, count=1):
        if roll_no in self.students:
            self.students[roll_no].add_meal(count)
            print(f"✅ {count} meal(s) recorded for {self.students[roll_no].name}.")
        else:
            print("❌ Student not found.")

    # Manually update meal count for a student
    def update_meal_count(self, roll_no, new_count):
        if roll_no in self.students:
            self.students[roll_no].update_meals(new_count)
            print(f"✅ Meal count updated to {new_count} for {self.students[roll_no].name}.")
        else:
            print("❌ Student not found.")

    # Reset all meal records to 0 (e.g. at month-end)
    def reset_all_meals(self):
        for student in self.students.values():
            student.meals = 0
        print("✅ All meal records reset to 0.")

    # Display all student records in the mess
    def show_all_records(self):
        if not self.students:
            print("⚠️ No student records found.")
        else:
            print("\n=== Mess Records ===")
            for student in self.students.values():
                student.display_record(self.rate_per_meal)

    # Search and display record for a specific student
    def search_student(self, roll_no):
        if roll_no in self.students:
            print("🔍 Student found:")
            self.students[roll_no].display_record(self.rate_per_meal)
        else:
            print("❌ Student not found.")


# 🧑‍🍳 Menu-driven program to interact with the user
def mess_menu():
    mess = MessRecord()  # Create an empty mess record

    while True:
        # Display menu options
        print("\n====== Mess Record Menu ======")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Record Meal")
        print("4. Update Meal Count")
        print("5. Set/Change Meal Rate")
        print("6. Search Student")
        print("7. Show All Records")
        print("8. Reset All Meal Records")
        print("9. Exit")
        print("==============================")

        # Get user choice
        choice = input("Enter your choice (1-9): ")

        # Option 1: Add a new student
        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            mess.add_student(name, roll)

        # Option 2: Remove a student
        elif choice == "2":
            roll = input("Enter roll number to remove: ")
            mess.remove_student(roll)

        # Option 3: Record meals for a student
        elif choice == "3":
            roll = input("Enter roll number: ")
            count = int(input("Enter number of meals to add: "))
            mess.record_meal(roll, count)

        # Option 4: Update meal count manually
        elif choice == "4":
            roll = input("Enter roll number: ")
            new_count = int(input("Enter new meal count: "))
            mess.update_meal_count(roll, new_count)

        # Option 5: Change meal rate
        elif choice == "5":
            new_rate = int(input("Enter new meal rate (₹): "))
            mess.set_meal_rate(new_rate)

        # Option 6: Search for a student
        elif choice == "6":
            roll = input("Enter roll number to search: ")
            mess.search_student(roll)

        # Option 7: Show all student records
        elif choice == "7":
            mess.show_all_records()

        # Option 8: Reset all meal records
        elif choice == "8":
            confirm = input("Are you sure you want to reset all meal records? (yes/no): ")
            if confirm.lower() == "yes":
                mess.reset_all_meals()

        # Option 9: Exit the program
        elif choice == "9":
            print("👋 Exiting... Have a good day!")
            break

        # Handle invalid input
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 9.")


# Run the menu-driven application
# mess_menu()
