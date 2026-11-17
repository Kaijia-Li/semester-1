# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

        # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        if type(name) != str:
            raise TypeError
        if name == "":
            raise ValueError
        if type(birth) != date:
            raise TypeError
        
        self.name = name
        self.birth = birth

          # Implement methods initials() and is_birthday() here
            # (see README.md for further details)

    def initials(self):
        """
        use split() to separate name
        """
        res = ""
        for each in self.name.split():
            res += each[0].upper()
        return res

    def is_birthday(self):
        today = date.today()
        return self.birth.month == today.month and self.birth.day == today.day
        