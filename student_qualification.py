# Name: Firisiya Chiomadzi
# File Name: student_qualification.py
# Description: This Python app accepts student names and GPAs and determines if they qualify for the Dean's List or Honor Roll.

# Function to determine student qualification
def student_qualification():
    
    """
    This function prompts the user to input student information and determines if they qualify for the Dean's List or Honor Roll.
    
    Inputs:
    - Last name (string)
    - First name (string)
    - GPA (float)
    
    Outputs:
    - Qualification status (string)
    """

    print("Welcome to the Student Qualification App!")
    print("Enter 'ZZZ' as the last name to quit processing records.\n")

    while True:
        last_name = input("Enter the student's last name: ")
        if last_name == 'ZZZ':
            print("Exiting the program...")
            break

        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"Sorry, {first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

# Main execution
if __name__ == "__main__":
    student_qualification()