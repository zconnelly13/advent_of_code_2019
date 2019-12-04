from math import floor


with open('input.txt') as fp:
    modules = [int(line) for line in fp.readlines()]


def calculate_fuel(total, x):
    fuel = floor(x/3) - 2
    if fuel > 0:
        return calculate_fuel(total + fuel, fuel)
    else:
        return total


# Part I:
print(sum([floor(x/3) - 2 for x in modules]))

# Part II:
print(sum([calculate_fuel(0, x) for x in modules]))
