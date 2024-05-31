def NULL_not_found(object: any) -> int:
    objtype = type(object)
    if object is None:
        print(f'Nothing: {object} {objtype}')
        return 0
    elif objtype is float:
        print(f'Cheese: {object} {objtype}')
        return 0
    elif objtype == int and object == 0:
        print(f'Zero: {object} {objtype}')
        return 0
    elif objtype is str and object == '':
        print(f'Empty: {objtype}')
        return 0
    elif objtype is bool and object is False:
        print(f'Fake: {object} {objtype}')
        return 0
    else:
        print('Type not found')
        return 1
    return 1
