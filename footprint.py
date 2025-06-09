# With this simple script you can calculate your footprint score based in some simple daily life criteria.

print ("Hello! Let's see what is your environemental footprint in our planet :)")
footprint = 0

has_pet = input("Do you have a pet (yes/no)? ")
pet_food = "yes"

if has_pet == "yes":
    # Pets consume resources like water, litter, and toys. 
    footprint = footprint + 5
    pet_food = input("Do your pet food contain meat? ")
    if pet_food == "yes":
        footprint = footprint + 10
if has_pet == "no":
    footprint
    

days = int(input("How many days a week do you commute to school or work? "))
if days != 0:
    transport = input("Do you commute by foot, bike, bus, train, or car? ")

    # Different methods of transportation have different environmental impacts.
    if transport == "car":
        footprint = footprint + (8 * days)
    elif transport == "bus" or transport == "train":
        footprint = footprint + (4 * days)
    elif transport == "bike" or transport == "foot":
        footprint = footprint + days
        
print("Your environmental footprint score is " + str(footprint) + ".")
