def myfind(string, char):
    '''
    the purpose of this function is to find the place of index which firstly appear in the string.
    :param string: the strings we input
    :param char: the index we need to find
    :return: the place of index firstly appear
    '''
    place = -1
    new_string = string
    length_char = len(char)
    length_string = len(string)
    times = length_string - length_char + 1
    for i in range(times):
        if char == new_string[0:length_char]:
            place += 1
            break
        else:
            new_string = new_string[1:]
            place += 1
    if char == new_string[0:length_char]:
        place = place
    else:
        place = -1
    return place


def mysplit(strings):
    '''
    the purpose of this function is to find the splitting list of original strings.
    :param strings: we strings we need to split
    :return: the new list of the splitting strings
    '''
    words = []
    word = ''
    for char in strings:
        if char == ' ':
            words.append(word)
            word = ''
        else:
            word += char
    words.append(word)
    return words
