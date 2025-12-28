# Level 1 question 2
# Ask the user for their birth year (as string), convert it to integer, calculate their age in 2025 and print:

birth = str(input("What is your birth year ?"))
year = int(birth)
age = 2025 - year
print("You will be " + str(age) + " years old in 2025")