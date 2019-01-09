showroom = set()

showroom.add("Honda Civic")
showroom.add("Austin 7")
showroom.add("Nissan Skyline")
showroom.add("Audi TT")

print("Number of cars in my showroom:", len(showroom))

showroom.add("Audi TT")
print("My Car Showroom:", showroom)

newCars = {"Honda Accord", "Nissan GT-R"}

showroom.update(newCars)
print("Bought some cars:", showroom)

showroom.discard("Honda Accord")
print("Sold a car:", showroom)

junkyard = {"Dodge Charger", "Audi TT", "Honda Civic", "Fiat 300", "Mini Cooper"}

duplicate_cars = showroom.intersection(junkyard)

showroom = showroom.union(junkyard)
print("Showroom after buying unique cars from junkyard:", showroom)

junkyard = duplicate_cars
print("unpurchased cars remaining junkyard:", junkyard)