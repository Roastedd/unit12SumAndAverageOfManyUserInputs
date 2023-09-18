# Find the sum and average of any given amount of numbers 
sum = 0
totalnumbers = 0
print("I will find the sum and average of any given numbers.")
while True:
  usernum = float(input("Enter a number: "))
  sum += usernum
  totalnumbers += 1

  choice = input("Add another number? Type (y/n): ")
  if choice.casefold() == "n":
    break

average = sum/totalnumbers

print("Sum: {}" .format(sum))
print("Average: {}" .format(average))