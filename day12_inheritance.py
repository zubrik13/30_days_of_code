class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def average(self):
        avg = sum(self.scores) / len(self.scores)
        return avg

    def calculate(self):
        a = self.average()
        if 90 <= a <= 100:
            return "O"
        elif 80 <= a <= 90:
            return "E"
        elif 70 <= a <= 80:
            return "A"
        elif 55 <= a <= 70:
            return "P"
        elif 40 <= a <= 55:
            return "D"
        else:
            return "T"


# line = input().split()
# numScores = int(input()) # not needed for Python
# scores = list(map(int, input().split()))

inp = "Heraldo Memelli 8135627"
numScores = 2
sc = "100 80"
line = inp.split()

firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, sc.split()))
s = Student(firstName, lastName, idNum, scores)

s.printPerson()
print("Grade:", s.calculate())
