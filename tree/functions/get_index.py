def get_index(string):
    index_as_string = ''
    pos = 2

    while pos < len(string) and string[pos].isdigit():
        index_as_string += string[pos]
        pos += 1

    if index_as_string == '':
        return -1

    return int(index_as_string)
