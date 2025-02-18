# Function with return
def get_percentage(amount, percentage):
    result = (amount * percentage) / 100

    return result


percentage_amount = get_percentage(amount=50000, percentage=50)
percentage_amount = get_percentage(amount=50000, percentage=25.5)

print(percentage_amount)
