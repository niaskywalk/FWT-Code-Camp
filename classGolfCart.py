class Vehicle:
    def __init__ (self, make, model, color, weight, numDoors, topSpeed, currentSpeed):
        self.make = make
        self.model = model
        self.color = color
        self.weight = weight
        self.numDoors = numDoors
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
    def accelerate(self):
        if self.currentSpeed < self.topSpeed:
            self.currentSpeed = self.currentSpeed + 5
            print("Vroooom! "+ self.make + " " + self.model + " traveling at " + str(self.currentSpeed) + " MPH")
        else:
            print("Can't go faster. Top Speed reached!")
        return self.currentSpeed
    
    def brake(self):
        if self.currentSpeed > 0:
            self.currentSpeed = self.currentSpeed - 5
        if self.currentSpeed < 5:
            self.currentSpeed = 0
        return self.currentSpeed

markCar = Vehicle("Nissan", "Rogue", "Silver", 4200, 5, 110, 0)

markCar.accelerate()
print("The " + markCar.make + " " + markCar.model + " is now moving at " + str(markCar.currentSpeed) + "MPH.") 

golfCart = Vehicle("Melex", "EC21", "white", 800, 0, 25, 0)

golfCart.accelerate()
golfCart.accelerate()
golfCart.accelerate()
golfCart.accelerate()
golfCart.accelerate()
golfCart.accelerate()
golfCart.accelerate()

