def longest(s1, s2):
    result = ""

    for letter in s1:
        if letter not in result:
            result = result + letter

    for letter in s2:
        if letter not in result:
            result = result + letter

    result = sorted(result)

    return "".join(result)
