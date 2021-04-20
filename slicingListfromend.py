dailyList = [107.92, 108.67, 109.86, 110.15]

# def showBalance(dailyList):
#     for i in range(1, 3):
#         balance_slice = dailyList[i:i+2]
#         print("slice starting %d days ago: %s" % (len(dailyList) - i, balance_slice))     

# showBalance(dailyList)

#   def show_balances(daily_balances):

#     # do not include -1 because that slice will only have 1 balance, yesterday
#     for day in range(-3, -1):
#         balance_slice = daily_balances[day : day + 2]

#         # use positive number for printing
#         print("slice starting %d days ago: %s" % (abs(day), balance_slice))


def show_balances(daily_balances):
    numBalance = len(daily_balances)
    for day in range(numBalance -3, numBalance -1):
        balance_slice = daily_balances[day : day + 2]
        days_ago = numBalance - day
        print("slice starting %d days ago: %s" % (abs(days_ago), balance_slice))


show_balances(dailyList)