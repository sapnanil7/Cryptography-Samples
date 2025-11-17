hourly_rate = 15.50
hours_worked = 45
if hours_worked >= 40:
    bonus = 50
else:
    bonus = 0

base_pay = hourly_rate * hours_worked
total_pay = base_pay + bonus

print ("The Total pay of the employee is: {}".format(total_pay))