

from math import * # this I added it later

print(1%6) #its a modulus operator and leaves the remainders

#power

print(pow(24,0.5))

# calculating roots

number_of_times = float(input("By how many times your wealth should be increased?  "))

number_of_days = int(input("and in how many days? "))

n_actual_root_calculate = float(1/number_of_days)

root_value = float(pow(number_of_times, n_actual_root_calculate))

daily_percent = (root_value - 1)*100

print("\nTo increase your wealth by " + str(number_of_times) + " times in " + str(number_of_days) + (" days")
      + "\nYou have to increase your wealth daily by " + str(daily_percent) + " percent" )
current_wealth=float(input("How much many do you have now? " ))
final_wealth=float(current_wealth*number_of_times)
print("that means your " + str(current_wealth) + " rupees will be " + str(final_wealth) + " rupees in "
      + str(number_of_days) + " days.")























