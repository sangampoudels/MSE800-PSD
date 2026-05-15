#calling function from the users.
from users import (
    student_login,
    submit_assignment,
    view_grades
)

# Main function controls program execution
def main():
    # Calls login function
    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")


if __name__ == "__main__":
    main()
