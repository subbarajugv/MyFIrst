# I am happy
# two days to debug and write a neat code for averages
#it gives a prompt if string is entered and asks you to give a number
total = 0
count = 0
while True:
    numbers = input("Give a number (type done when you are done): ")
    if numbers == 'done':
        break
    try:
        value = float(numbers)
    except:
        print("Please give a number, not strings")
        numbers = input()
        value = float(numbers)
total = total + value
count += 1
average = total / count
print("average of the numbers you gave is " + str(average))
