class Student(object):
    def __init__(ssss, name, score):
        ssss.name = name
        ssss.score = score

    def get_grade(ssss):
        if ssss.score >= 90:
            return 'A'
        elif ssss.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())