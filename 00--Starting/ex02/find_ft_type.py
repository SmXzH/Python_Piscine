def all_thing_is_obj(object: any) -> int:
    objtype = type(object)
    if objtype == list:
        print(f'List : {objtype}')
    elif objtype == tuple:
        print(f'Tuple : {objtype}')
    elif objtype == set:
        print(f'Set : {objtype}')
    elif objtype == dict:
        print(f'Dict : {objtype}')
    elif objtype == str:
        print(f'{object} is in the kitchen : {objtype}')
    else:
        print('Type not found')
    return 42
