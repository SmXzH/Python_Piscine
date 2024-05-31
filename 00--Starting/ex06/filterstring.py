import sys


def filter_string(S, N):
    """
    Filter words in a string based on their length.

    Args:
        S (str): The input string containing words separated by spaces.
        N (int): The minimum length threshold for words to \
            be included in the filtered list.

    Returns:
        list: A list containing words from the input string `S` \
            with lengths greater than `N`.

    """
    assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
    assert isinstance(S, str) and isinstance(N, int), \
        "AssertionError: the arguments are bad"

    return [word for word in S.split() if len(word) > N]


if __name__ == "__main__":
    try:
        S, N = sys.argv[1], int(sys.argv[2])
        print(filter_string(S, N))
    except (IndexError, ValueError):
        print("AssertionError: the arguments are bad")
