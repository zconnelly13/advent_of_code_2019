import re


lower_bound = 245182
upper_bound = 790572


def check_adjacent(i):
    # Part I
    # return re.search(r'(\d)\1', str(i))

    # Part II
    return re.search(r'(?:^|(.)(?!\1))(\d)\2(?!\2)', str(i))


def check_non_decreasing(i):
    return list(str(i)) == sorted(str(i))


print(len([
    i for i in range(lower_bound, upper_bound + 1)
    if check_adjacent(i)
    and check_non_decreasing(i)
]))
