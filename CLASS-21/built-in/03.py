from datetime import datetime, time, timezone, timedelta

print(datetime.now())

# After OOP understanding
# print(time(hour=22, minute=10))


# get UTC timezone specific datetime
# print(datetime.now(timezone.utc))

days_after_7 = datetime.now() + timedelta(days=7)
print(days_after_7)

# format = "%d - %m - %y %H:%M:%S %c"
format = "%A"
print(datetime.now().strftime(format))


print(days_after_7.strftime(format))


# Self Study
# Strptime