test1 = int(input("What was your first test score?"))
test2 = int(input("What was your second test score?"))
test3 = int(input("What was your third test score?"))
averageresult = (test1+test2+test3)/3

class students:
    class_ = "student"
    average = averageresult

    def __init__(self, name, age):
        self.name= name
        self.age= age


John = students("John", "24")

print(getattr(John, "average"))



