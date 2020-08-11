import urllib.request


def instructors(department):
    '''
    we need to convert a large text from website and mine useful information we want.
    this function is in order to create a list which contains all instructors' names in given department.
    :param department: the department which contains the instructors' names we are looking for
    :return: the instructors' name list
    '''
    text = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + department)
    instructors_list = []
    for line in text:
        decoded_line = line.decode('utf-8')
        cells = decoded_line.strip().split('|')
        if '+' in cells[4]:
            place = cells[4].find('+')
            instructor_name = cells[4][0:place]
        else:
            instructor_name = cells[4]
        if instructor_name not in instructors_list:
            instructors_list.append(instructor_name)
    instructors_list = sorted(instructors_list)
    return instructors_list


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    '''
    we need to convert a large text from website and mine useful information we want.
    this function is in order to create a list which meet with all requirements about such course we provided,
    include seats_available state, class level and class start time.
    :param dept_name: the department we are looking for
    :param has_seats_available: the state of available seats
    :param level: class level you want
    :param not_before: hope the start time not before
    :param not_after: hope the start time not after
    :return: the list of classes meet with all requirements
    '''
    text = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + dept_name)
    class_list = []
    for line in text:
        decoded_line = line.decode('utf-8')
        cells = decoded_line.strip().split('|')
        available_seats = int(cells[16]) - int(cells[15])
        if has_seats_available:
            if level is not None:
                level = (level // 1000) * 1000
                if int(level)+1000 > int(cells[1]) >= int(level):
                    if not_after is not None and not_before is not None:
                        if int(not_before) <= int(cells[12]) <= int(not_after):
                            if available_seats > 0:
                                class_list.append(cells)
                    elif not_before is None and not_after is not None:
                        if int(cells[12]) <= int(not_after):
                            if available_seats > 0:
                                class_list.append(cells)
                    elif not_before is not None and not_after is None:
                        if int(not_before) <= int(cells[12]):
                            if available_seats > 0:
                                class_list.append(cells)
                    elif not_after is None and not_before is None:
                        if available_seats > 0:
                            class_list.append(cells)
            else:
                if not_after is not None and not_before is not None:
                    if int(not_before) <= int(cells[12]) <= int(not_after):
                        if available_seats > 0:
                            class_list.append(cells)
                elif not_before is None and not_after is not None:
                    if int(cells[12]) <= int(not_after):
                        if available_seats > 0:
                            class_list.append(cells)
                elif not_before is not None and not_after is None:
                    if int(not_before) <= int(cells[12]):
                        if available_seats > 0:
                            class_list.append(cells)
                elif not_after is None and not_before is None:
                    if available_seats > 0:
                        class_list.append(cells)
        else:
            if level is not None:
                level = (level // 1000) * 1000
                if int(level)+1000 > int(cells[1]) >= int(level):
                    if not_after is not None and not_before is not None:
                        if int(not_before) <= int(cells[12]) <= int(not_after):
                                class_list.append(cells)
                    elif not_before is None and not_after is not None:
                        if int(cells[12]) <= int(not_after):
                                class_list.append(cells)
                    elif not_before is not None and not_after is None:
                        if int(not_before) <= int(cells[12]):
                                class_list.append(cells)
                    elif not_after is None and not_before is None:
                            class_list.append(cells)
            else:
                if not_after is not None and not_before is not None:
                    if int(not_before) <= int(cells[12]) <= int(not_after):
                        class_list.append(cells)
                elif not_before is None and not_after is not None:
                    if int(cells[12]) <= int(not_after):
                        class_list.append(cells)
                elif not_before is not None and not_after is None:
                    if int(not_before) <= int(cells[12]):
                        class_list.append(cells)
                elif not_after is None and not_before is None:
                    class_list.append(cells)
    return class_list




