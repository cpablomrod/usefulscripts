#Lets calculate the weight of an object in different planets!
#The user must tells us the planet he wants:
planet = input("Choose your planet: Mars, Mercury, Venus or Jupiter ")

#We setup the gravity to 0
gravity = 0.0

if planet == "Mars" or planet == "Mercury": 
    gravity = 3.7

elif planet == "Venus":
    gravity = 8.9

elif planet == "Jupiter":
    gravity = 23.1

else:
    print("Unrecognized planet")

#If gravity has another value different from O it should do the calculation
if gravity:
    earth_weight =  float(input("What is the weight on earth(kg): "))

    #The formula for the objects weight is mass * gravity
    earth_gravity = 9.81
    mass = earth_weight / earth_gravity
    new_weight = round(mass * gravity,1) 

    print("The weight would be " + str(new_weight) + " kg on " + planet + " .”)
