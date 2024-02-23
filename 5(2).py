import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\s+\d+\.\d+\s+'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total_sum = sum(numbers_generator)
    return total_sum

text = " 20.12 or 12.28, and 333.1 or 1.1 "
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
