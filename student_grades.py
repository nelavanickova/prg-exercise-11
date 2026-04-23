class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, find):
        misto = []
        for index, cislo in enumerate(self.scores):
            if cislo == find:
                misto.append(index)
        return misto

    def get_sorted(self):
        noovy = self.scores.copy()
        delka = len(noovy)

        zmena = True
        while zmena:
            zmena = False
            for i in range(len(noovy) - 1):
                if noovy[i] > noovy[i + 1]:
                    noovy[i], noovy[i + 1] = noovy[i + 1], noovy[i]
                    zmena = True
        return noovy


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(3))
    print(results.find(100))
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]