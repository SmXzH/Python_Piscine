def parsing_input(height: list[int | float], weight: list[int | float]):
    """
    Parse input for BMI calculation

    Args:
        height: list of int or float
        weight: list of int or float
    """
    if not all(isinstance(h, (int, float)) for h in height) or \
       not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError('List should be int or float')
    if not all(h > 0 for h in height) or not all(w > 0 for w in weight):
        raise ValueError('Height and weight should be positive')


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI from height and weight

    Args:
        height: list of int or float
        weight: list of int or float
    """
    bmi_list = []

    for h, w in zip(height, weight):
        if h < 0 or w < 0:
            raise ValueError('Height and weight should be positive')
        bmi = w / (h ** 2)
        bmi_list.append(bmi)

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply limit to BMI

    Args:
        bmi: list of int or float
        limit: int
    """
    if not isinstance(limit, int):
        raise TypeError('Limit should be int')
    if limit < 0:
        raise ValueError('Limit should be positive')
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError('BMI should be int or float')

    return [b > limit for b in bmi]
