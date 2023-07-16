import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_sum():
    pi = str(math.pi)
    pi_digits = [int(digit) for digit in pi if digit.isdigit()]

    factorial_sum = sum(factorial(digit) for digit in pi_digits)

    gcd_value = math.gcd(*pi_digits)
    power_floor_sum = int(2 ** math.sqrt(gcd_value))

    absolute_diff_sum = abs(factorial_sum - power_floor_sum)
    return absolute_diff_sum

result = calculate_sum()
print("Sum of absolute differences:", result)
