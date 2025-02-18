def get_percentage(amount, percentage):
    if not isinstance(amount, int):
        if not isinstance(amount, float):
            return

    if not isinstance(percentage, int):
        if not isinstance(percentage, float):
            return

    result = (amount * percentage) / 100

    return result


percentage_amount = get_percentage(amount=50000, percentage=25.5)
print(percentage_amount)

percentage_amount = get_percentage(amount=5000, percentage="J")
print(percentage_amount)
