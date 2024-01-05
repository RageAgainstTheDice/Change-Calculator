change_cents = int(input('Enter change here: '))

if change_cents == 0:
    print('No change')
else:
    print('Your change:')

num_dollars = change_cents // 100
if num_dollars > 1:
    print(num_dollars, 'Dollars')
elif num_dollars == 1:
    print(num_dollars, 'Dollar')
change_cents_new = change_cents % 100

num_of_quarters = change_cents_new // 25
# print('number of quarters:', num_of_quarters)
if num_of_quarters > 1:
    print(num_of_quarters, 'Quarters')
elif num_of_quarters == 1:
    print(num_of_quarters, 'Quarter')
change_cents_new = change_cents_new % 25
# print ('change updated = ', change_cents)

num_of_dimes = change_cents_new // 10
# print('number of dimes:', num_of_dimes)
if num_of_dimes > 1:
    print(num_of_dimes, 'Dimes')
elif num_of_dimes == 1:
    print(num_of_dimes, 'Dime')
change_cents_new = change_cents_new % 10
# print('change updated = ', change_cents)

num_of_nickels = change_cents_new // 5
# print('number of nickels:', num_of_nickels)
if num_of_nickels > 1:
    print(num_of_nickels, 'Nickels')
elif num_of_nickels == 1:
    print(num_of_nickels, 'Nickel')
change_cents_new = change_cents_new % 5
# print('change updated = ', change_cents)

num_of_pennies = change_cents_new // 1
# print('number of pennies:', num_of_pennies)
if num_of_pennies > 1:
    print(num_of_pennies, 'Pennies')
elif num_of_pennies == 1:
    print(num_of_pennies, 'Penny')
change_cents_new = change_cents_new % 1
# print('change updated =', change_cents)
