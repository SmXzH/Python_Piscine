import sys


def check_odd_or_even(num):
    assert isinstance(num, int), "AssertionError: argument is not an integer"
    assert len(sys.argv) == 2, \
        "AssertionError: more than one argument is provided"

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
        check_odd_or_even(num)
    except ValueError:
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: no argument provided")
