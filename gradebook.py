grade_book = {}
weight_book = {}


def assignment(kind, grade, weight=1):
    '''
    this function is in order to create two dictionaries which contain each assignment's total grade and each
    assignment's total weight.
    :param kind: the title of the assignment
    :param grade: the grade you get in such assignment
    :param weight: the weight each assignment has
    :return: two dictionary grade_book and weight_book
    '''
    global grade_book
    global weight_book
    total_points = grade * weight
    if kind not in grade_book:
        grade_book[kind] = total_points
    else:
        grade_book[kind] += total_points
    if kind not in weight_book:
        weight_book[kind] = weight
    else:
        weight_book[kind] += weight
    return grade_book and weight_book


def total(syllabus):
    '''
    this function is in order to calculate the grade you get by using the ration multiple the total_grade and divided by
    total weight. add each part of the grade you will get the total grade until now.
    :param syllabus: the ratio which is provided by the syllabus
    :return: the total grade you get until now
    '''
    global grade_book
    global weight_book
    result = 0
    for kind in syllabus:
        if kind in grade_book:
            if weight_book[kind] == 0:
                result += 0
            else:
                result += syllabus[kind] * grade_book[kind] / weight_book[kind]
    return result
