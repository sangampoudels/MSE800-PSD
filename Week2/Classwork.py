class StudentManager:
    def __init__(self):
        self.students = []

    def collect_student_data(self, count):
        """Collects name, age, and ID for a specified number of students."""
        for i in range(count):
            print(f"\n--- Enter details for student {i + 1} ---")
            name = input("Name: ")
            age = int(input("Age: "))
            student_id = input("Student ID: ")
            self.students.append({"name": name, "age": age, "id": student_id})

    def display_sorted_students(self):
        """Sorts students by name and prints their name and age."""
        # Sort by name (alphabetical)
        sorted_list = sorted(self.students, key=lambda x: x['name'])
        
        print("\n--- Student List (Sorted by Name) ---")
        for student in sorted_list:
            print(f"Name: {student['name']}, Age: {student['age']}")

if __name__ == "__main__":
    manager = StudentManager()
    
    # Collect data for 3 students
    manager.collect_student_data(3)
    
    # Print the list in order
    manager.display_sorted_students()