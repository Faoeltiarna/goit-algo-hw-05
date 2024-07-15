import re


def generator_numbers(some_text: str):
    pattern = r"\d+\.\d+"
    matches = re.findall(pattern, some_text)
    for num in matches:
        yield float(num)


def sum_profit(text, generator_numbers, sum_income=0.0):
    num = generator_numbers(text)
    try:
        while num:
            sum_income += next(num)
    except StopIteration:
        pass
    return sum_income


text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями"
        " 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

