# Program to calculate daily wealth to multiply your wealth  in a given number of days
# yeah I know...I am greedy. But have fun
name = input("Hey! first what is your name? ")
wealth_multiplier = float(input(name + "! How many times your wealth should be improved? "))
days = int(input("Okay! In how many days? "))
# Actual calculations start here
daily_percent = (float(wealth_multiplier**(1/days)) - 1)*100
print("Hey " + name + "! So if you daily increase your wealth approximately by " + str(round(daily_percent)) +
      "% you will multiply your wealth by " + str(wealth_multiplier) + " times in " + str(days) + " days")
current_wealth = int(input("Give me your current wealth rounded of rupees: "))
print(" If you daily increase it by " + str(round(daily_percent)) +
      "% then it will be " + str(wealth_multiplier*current_wealth) + " in just " + str(days) + " days. Ciao!")
