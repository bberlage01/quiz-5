#Problem 1
def tire_pressure(pressure):
    if pressure<28:
        print("Tire pressure is low")
    else:
        return None
tire_pressure(21)
tire_pressure(45)

#Problem 2
def thermostat(temp):
    if temp<52:
        print("The heater is on")
    elif temp==52:
        print("The heater is on")
    elif 52<temp<71:
        print("Heater and AC are off")
    elif temp==71:
        print("AC is on")
    elif temp>71:
        print("AC is on")

thermostat(50)
thermostat(55)
thermostat(75)

#Problem 3
def food(fruit):
    if fruit=="banana":
        print("Banana it is!")
    elif fruit=="cherry":
        print("I cherish you!")
    elif fruit=="apple":
        print("I applesolutely like you!")
    elif fruit=="orange":
        print("Orange you glad to see me?")
    elif fruit=="melon":
        print("You are one in a melon")

food("banana")
food("cherry")
food("apple")
food("orange")
food("melon")
