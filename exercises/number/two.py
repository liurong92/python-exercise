'''
Building on the previous example, let's also assume that you have saved $918 to fund your new
adventure. You wonder how many days you can keep one server running before your money
runs out. Of course, you hope your social network becomes popular and requires 20 servers to
keep up with the demand. How much will it cost to operate at that point?
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
How much does it cost to operate twenty servers per day?
How much does it cost to operate twenty servers per month?
How many days can I operate one server with $918?
'''

total = 918
cost_per_hour = 0.51
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
one_server_for_days = total / cost_per_day

print('1: {:.2f}'.format(cost_per_day))
print('2: {:.2f}'.format(cost_per_month))
print('3: {:.2f}'.format(cost_per_day * 20))
print('4: {:.2f}'.format(cost_per_month * 20))
print('5: {:.2f}'.format(one_server_for_days))