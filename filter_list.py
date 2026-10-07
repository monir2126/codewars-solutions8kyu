def filter_list(my_list):
    result = []

    for item in my_list:
        if type(item) == int:
            result.append(item)

    return result
