class Transport:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Transport):
    def move(self):
        print("Driving 🚗")

class Plane(Transport):
    def move(self):
        print("Flying ✈️")

class Boat(Transport):
    def move(self):
        print("Sailing 🚤")

class Animal(Transport):
    def move(self):
        print("Walking 🐾")

# Create a list of transports and animals
transports = [Car(), Plane(), Boat(), Animal()]

# Loop through each object and call the move() method
for transport in transports:
    transport.move()
