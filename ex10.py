# Level 2 Question 10

temperature = int(input("Enter the temperature in Celcius : "))

# Convert to fahrenheit

Fahrenheit = (temperature*9/5) + 32 

if(temperature<0 ):
    print("Very cold! Wear thick jacket")
elif(temperature >=0 and  temperature<=15 ):
    print("Cold . Wear Jacket")
elif( temperature>= 16 and temperature<= 25):
    print("Nice weather")
else :
    print("Hot ! Stay hydrated")

