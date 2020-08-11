credits = 0
points = 0
GPA = 0


def add_course(gpa, *args):
    global GPA
    global credits
    global points
    credits += 3
    points += + gpa * 3
    for i in args:
        credits = credits - 3 + i
        points = points - gpa * 3 + gpa * i


def gpa():
    GPA = points / credits
    return GPA


def credit_total():
    return credits


