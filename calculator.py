def function(*args):
    dict = {}
    lst = []
    largest_number = 0
    for i in args:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in args:
        if dict[i] > largest_number:
            largest_number = dict[i]
    for i in dict:
        if dict[i] == largest_number:
            lst.append(i)
    return lst


print(function('salad', 'pizza', 'salad', 'salad', 'pizza', 'pizza','pizza','salad','pizza'))
