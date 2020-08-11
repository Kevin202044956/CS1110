def myreduce(func, lst):
    """
    the purpose of this function is to create a dictionary and invoke the first and second elements from the dictionary,
    plug in the result of the function into the dictionary until get the final answer.
    :param func: the function wiggle or waggle which we need to use
    :param lst:the origin list which is provided by the system
    :return:the final result of the function
    """
    new_list = []
    for element in lst:  # because the list is mutable, we need to create a new list here!
        new_list.append(element)
    times = len(new_list) - 1
    for i in range(times):
        the_dict = {'a': new_list[0], 'b': new_list[1]}
        a = the_dict['a']
        b = the_dict['b']
        result = func(a, b)
        new_list.pop(0)
        new_list.pop(0)
        new_list.insert(0, result)
    return new_list[0]


def mymap(func, lst):
    """
    the purpose of this function is to create a dictionary and invoke each element from the list,
    changed by the function and put the result back to the list with the same position.
    :param func: the function wiggle or waggle which we need to use
    :param lst: the origin list which is provided by the system
    :return: the final list which is changed by the function
    """
    times = len(lst)
    new_list = []
    for i in range(times):
        the_dict = {'a': lst[i]}
        a = the_dict['a']
        result = func(a)
        new_list.append(result)
    return new_list
