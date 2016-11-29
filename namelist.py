def namelist(names):
    result = ""
    for i in range(len(names)):
        if i == len(names) - 2:
            join_string = " & "
        elif i == len(names) - 1:
            join_string = ""
        else:
            join_string = ", "

        result += names[i]['name'] + join_string

    return result

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
