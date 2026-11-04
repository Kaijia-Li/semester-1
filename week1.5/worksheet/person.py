# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        if type(name) != str:
            raise TypeError
        if name == "":
            raise ValueError
        if type(birth) != date:
            raise TypeError
        
        self.name = name
        self.birth = birth

    def initials(self):
        res = ""
        for each in self.name.split():
            res += each[0].upper()
        return res

    def is_birthday(self):
        return date.today() == self.birth
        
        
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)


p = Person("simon",date.today())
print(p.name)