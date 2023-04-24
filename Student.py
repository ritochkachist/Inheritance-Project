from Person import Person

class Student(Person):
  def __init__(self, firstName, lastName, ssn, idNumber, major):
    super().__init__(firstName, lastName, ssn)
    self.idNumber = idNumber
    self.major = major

  def __repr__(self):
    return super().__repr__() + "\nID number: " + self.idNumber + "\nMajor: " + self.major 

  def getIdNumber(self):
    return self.idNumber

  def getMajor(self):
    return self.major

  def setIdNumber(self, newIdNumber):
    self.idNumber = newIdNumber

  def setMajor(self, newMajor):
    self.major = newMajor

  
    

