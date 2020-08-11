def check(card_number):
    """
    the check function is based on such algorithm: get sum1 of every other digit, including the right-most digit.
    let each digital of remaining list multiple by 2 and add each position of the new list, get the sum2,
    adding the two sums you get, if the result is a multiple of 10 then it was a valid number.
    :param card_number: the credit card number provided
    :return: weather the card number is valid or not
    """
    number_length = len(str(card_number))
    tolist = list(str(card_number))
    temp_strings = ''
    rev_list = []
    list_1 = []
    list_2 = []
    temp_list = []
    sum_1 = 0
    sum_2 = 0
    for i in range(number_length):
        index = tolist.pop(-1)
        rev_list.append(index)
    for number in rev_list[::2]:
        list_1.append(number)
    for number in rev_list[1::2]:
        temp_list.append(number)
    for number in list_1:
        sum_1 += int(number)
    for number in temp_list:
        number = int(number)*2
        list_2.append(number)
    for number in list_2:
        temp_strings += str(number)
    list_2 = list(temp_strings)
    for number in list_2:
        sum_2 += int(number)
    if (sum_1 + sum_2) % 10 == 0:
        return True
    else:
        return False
