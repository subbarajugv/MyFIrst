# Program to calculate daily wealth to multiply your wealth  in a given number of days
# yeah I know...I am greedy. But have fun
wealth_multiplier = float(input(" How many times your wealth should be improved? "))
days = int(input(" You want your wealth to be multiplied by " + str(wealth_multiplier) +
                 " times and in how many days? "))
name = input(" Oh by the way what is your name? ")
# Actual calculations start here
daily_percent = (float(wealth_multiplier**(1/days)) - 1)*100
print("Subbaraju! you daily need to increase your wealth by " + str(daily_percent) +
       "% inorder to multiply your wealth by " + str(wealth_multiplier) + " times in " + str(days) + " days")