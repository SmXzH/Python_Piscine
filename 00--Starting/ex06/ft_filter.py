def ft_filter(my_func, iter):
    """
    Equivalent to filter(function, iterable)
    Construct an iterator from those elements of iterable
                for which function returns true.
    """
    return [item for item in iter if my_func(item)]
