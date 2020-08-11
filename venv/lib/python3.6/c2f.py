x = input("What is the temperature in Celsius? ")
x = float(x)
def temperature(x):
    x = 1.8*x+32
    return x
a = temperature(x)
a = round(temperature(x), 2)
print('It is', a, 'degrees Fahrenheit')