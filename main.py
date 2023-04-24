# Margarita Chistiakova
# 3/1/2023
# Person Class + Student Class

from Student import Student
from Person import Person

#firstStudent = Student("Margarita", "Chistiakova", "444-444-4444", "3290791", "Computer Science")
student = None
studentList = []

print("Welcome to my program! Here I do silly things with code.")

choice = 0
while choice != 7:
  print("""
  1. Create a new person
  2. Change person's last name
  3. Change person's ID
  4. Change person'd major
  5. See details about a person
  6. Make your student go to a university
  7. Quit the program\n""")
  
  print("Please enter a number from the menu above:")
  
  choice = int(input())
  if choice == 1:
    print("Please enter person's first name: ")
    firstName = input()
    print("Please enter person's last name: ")
    lastName = input()
    print("Please enter person's Social Security Number: ")
    ssn = input()
    print("Is this person a student? Enter 1 for 'Yes' and 2 for 'No'")
    choice2 = int(input())
    if choice2 == 1:
      print("Please enter student's ID:")
      idNumber = input()
      print("Please enter student's major: ")
      major = input()
      print("\n")
      
      student = Student(firstName, lastName, ssn, idNumber, major)
      studentList.append(student)
    else:
      student = Person(firstName, lastName, ssn)
      studentList.append(student)
      
  elif choice == 2:
    if len(studentList) == 1:
      print(f"The current last name of this person is\n{student.getlastName()}")
      #print(student.getlastName())
      print("Please enter a new last name of the person: ")
      newLname = input()
      print(student.setlastName(newLname))
    elif len(studentList) != 1:
      print(f"There are currently {len(studentList)} people in the list.")
      print("Please choose one: ")
      choice = int(input())
      print(student.getlastName())
      print("Please enter a new last name of the person: ")
      newLname = input()
      print(studentList[choice - 1].setlastName(newLname))

  elif choice == 3:
      if len(studentList) == 1:
        print("The current ID number of this students is: ")
        print(student.getIdNumber())
        print("Please enter a new ID of the student: ")
        newId = int(input())
        print(student.setIdNumber(newId))
      elif len(studentList) != 1:
        print(f"There are currently {len(studentList)} students in the list.")
        print("Please choose one: ")
        choice = int(input())
        print(student.getIdNumber())
        print("Please enter a new ID of the person: ")
        newId = int(input())
        print(studentList[choice - 1].setIdNumber(newId))

  elif choice == 4:
      if len(studentList) == 1:
        print("The current major of this student is: ")
        print(student.getMajor())
        print("Please enter a new major of the student: ")
        newMajor = input()
        print(student.setMajor(newMajor))
      elif len(studentList) != 1:
        print(f"There are currently {len(studentList)} students in the list.")
        print("Please choose one: ")
        choice = int(input())
        print(student.getMajor())
        print("Please enter a new major of the student: ")
        newMajor = input()
        print(studentList[choice - 1].setMajor(newMajor))

  elif choice == 5:
      if len(studentList) == 1:
        print(student.__repr__())
      elif len(studentList) != 1:
        print(f"There are currently {len(studentList)} students in the list.")
        print("Please choose one: ")
        choice = int(input())
        print(studentList[choice - 1].__repr__())

  elif choice == 6:
      if len(studentList) == 1:
        print(student.goToUniversity())
      elif len(studentList) > 1:
        print(f"There are currently {len(studentList)} students in the list.")
        print("Please choose one: ")
        choice = int(input())
        print(studentList[choice - 1].goToUniversity())
      elif len(studentList) == 0:
        print("No students were created yet.")

  elif choice == 7:
      print("Thank you for taking part in my silliness! Have a good day :3")

  else:
    print("There is no such option. Please choose something else.")