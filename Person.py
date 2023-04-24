
class Person():
  def __init__(self,firstName, lastName, ssn):
    self.firstName = firstName
    self.lastName = lastName
    self.ssn = ssn

  def __repr__(self):
    return "The details of the person are: \nFirst name: " + self.firstName + "\nLast name: " + self.lastName + "\nSSN: " + self.ssn

  def getfirstName(self):
    return self.firstName

  def getlastName(self):
    return self.lastName

  def getSSn(self):
    return self.ssn

  def setfirstName(self, newFirstName):
    self.firstName = newFirstName

  def setlastName(self, newLastName):
    self.lastName = newLastName

  def setSSN(self, newSSN):
    self.ssn = newSSN

  def goToUniversity(self):
    return self.firstName + " " + self.lastName + " now goes to university!"