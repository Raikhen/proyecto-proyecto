def get_children(string):
    children = []
    initial_pos = string.find('(')
    final_pos = string.rfind(')')
    parentheses_count = 0

    if initial_pos > -1 and len(string) > initial_pos + 1:
        initial_pos += 1
        new_child = ''

        for i in range(initial_pos, final_pos):
            if string[i] == '(':
                parentheses_count += 1
            elif string[i] == ')':
                parentheses_count -= 1

            if string[i] == ',' and parentheses_count == 0:
                children.append(new_child.strip())
                new_child = ''
            else:
                new_child += string[i]

        children.append(new_child.strip())

        if parentheses_count == 0:
            return children

    return False
