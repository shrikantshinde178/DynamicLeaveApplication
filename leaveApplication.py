import calendar
from datetime import datetime, timedelta

def generate_leave_application():
    try:
        year = 2022  # You can update this dynamically if needed
        student_name = input("\nEnter your name: ")
        teacher_name = input("\nEnter your teacher name: ")
        month = int(input("\nEnter the Month (1-12): "))
        print("\n", calendar.month(year, month))
        
        date_input = input("\nSelect the date (DD): ")
        date_of_application = datetime.today()
        leave_tenure = int(input("\nLeave tenure (in days only): "))
        class_name = input("\nEnter the class: ")
        department = input("\nDepartment Name: ")
        subject_line = input("\nEnter the subject Line: ")
        reason = input("\nReason of Leave: ")

        # leave end date by adding leave tenure to the application date
        leave_end_date = date_of_application + timedelta(days=leave_tenure)

        # Creating the leave application
        leave_application = f"""
        Leave Application:

        Applicant Name: {student_name}
        Authorised Teacher: {teacher_name}
        Date of Application: {date_of_application.strftime("%Y-%m-%d %H:%M:%S")}
        Application submission time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        Requested Tenure Leave: {leave_tenure} days
        Class of the applicant: {class_name}
        Department of the Candidate: {department}
        Subject Line: {subject_line}
        Reason of Leave: {reason}

        Leave Start Date: {date_input} {calendar.month_name[month]}, {year}
        Leave End Date: {leave_end_date.strftime("%Y-%m-%d")}
        """

        print("\nApplication submitted successfully.")
        print("\nDetails as per application -")
        print(leave_application)
        
    except Exception as e:
        print(f"Error occurred: {e}")

# function to generate leave application
generate_leave_application()
