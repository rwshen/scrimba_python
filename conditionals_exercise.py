def num_days(month):
    days = 31
    if month in ['apr', 'jun', 'sep','nov']:
        days = 30
    elif month == 'feb':
        days = 28
    return f"number of days in {month.title()} is {days}."

print(num_days('oct'))
print(num_days('feb'))
print(num_days('june'))
print(num_days('april'))