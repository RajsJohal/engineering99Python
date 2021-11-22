class Car:
    def __init__(self, top_speed, current_speed=0):
        self.currentSpeed = current_speed
        self.topSpeed = top_speed

    def get_speed(self):
        return self.currentSpeed

    def accelerate(self, extra_mph):
        if self.currentSpeed + extra_mph >= self.topSpeed:
            print("Cannot exceed Top Speed")
            self.currentSpeed = self.topSpeed
            return self.currentSpeed
        else:
            self.currentSpeed = self.currentSpeed + extra_mph
            return self.currentSpeed

    def brake(self, less_mph):
        if self.currentSpeed - less_mph <= 0:
            print("Your car has come to a stop")
        else:
            self.currentSpeed = max(self.currentSpeed - less_mph, 0)
            return self.currentSpeed

merc = Car(100, 50)

print(merc.accelerate(60))
print(merc.brake(100))

print(merc)