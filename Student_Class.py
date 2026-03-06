class Student:
    def __init__(self, name, num_scores):
        self.name = name
        self.test_scores = [0] * num_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        return self.test_scores[position]

    def setScore(self, position, value):
        self.test_scores[position] = value

    def getHighestScore(self):
        return max(self.test_scores)

    def getAverageScore(self):
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + str(self.test_scores)


# Example usage
s = Student("Alby", 3)

s.setScore(0, 85)
s.setScore(1, 90)
s.setScore(2, 78)

print("Student Name:", s.getName())
print("Score at position 1:", s.getScore(1))
print("Highest Score:", s.getHighestScore())
print("Average Score:", s.getAverageScore())
print(s)