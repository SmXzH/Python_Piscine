def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array

    Args:
        family: list of list of float
        start: int
        end: int

    """
    if not isinstance(family, list):
        raise ValueError("family must be a list")
    family_lengths = [len(sublist) for sublist in family]
    if len(set(family_lengths)) != 1:
        raise ValueError("All sublists in family must have the same length")
    if start < 0 or end > len(family[0]):
        raise ValueError("start must be greater than or equal to 0")

    print("My shape is:", (len(family), len(family[0])))

    res = family[start:end]

    print("My new shape is:", (len(res), len(res[0])))

    return res
