import calendar
from datetime import datetime

try:
    year = 2022
    StudentName = input("\nEnter your name : ")
    TeachersName = input("\nEnter your teacher name : ")
    gettingMonth=int(input("\nEnter the Month : "))    
    print("\n", calendar.month(year,gettingMonth))
    Date=input("\n Select the date : ")
    DateOfApplication= datetime.today()
    LeaveTenture = int(input("\nleave tenure (in days only) : "))
    ClassName = input("\nEnter the class : ")
    Department =  input("\nDepartment Name : ")
    SubjectLine = input("\nEnter the subject Line : ")
    Reason =str(input("\nReason of Leave : "))
    print("\nApplication submitted successfully.")
   
    print("\n\ndetails is as per application - ")
    print("\n\tApplicant Name = ",StudentName)
    print("\tAuthorised Teacher = ",TeachersName)
    print("\tDate of Application = ",DateOfApplication)
    print("\tApplication submission time = ",datetime.now())
    print("\tRequested Tenture Leave = ",LeaveTenture)
    print("\tClass of the applicant = ",ClassName)
    print("\tDepartment of the Candidate = ",Department)
    
except:  
    print("Unknown Error Occures")