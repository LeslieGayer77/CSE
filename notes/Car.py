class Car(object):                                            # Type of object (Class)
    def __init__(self, car_type ,gas_left=50,):
        # These attributes that a phone has.
        # These should all be relevant to our program
        self.windows = True
        self.headlights = True
        self.engine = True
        self.wheels = 4
        self.gas_left = gas_left
        self.battery_left = True
        self.car_type = car_type

    def gas(self, full):
            self.gas_left += full
            if self.gas_left > 100:
                self.gas_left = 100

    def drive(self, duration):
        if not self.windows:
            print("Your gonna get pulled over.")
            print("You shouldn't be driving")
            return
        if not self.headlights:
            print("Your gonna get pulled over.")
            print("You shouldn't be driving")
            return
        if not self.engine:
            print("You cant drive!")
            print("You have no engine!")
            return
        if not self.wheels == 4:
            print("You cant drive on just the wheels you have")
        gas_lost_per_minute = 1
        if self.gas_left <= 0:
            print("You have no more gas.")
            return
        self.gas_left -= duration * gas_lost_per_minute
        if self.gas_left < 0:
            self.gas_left = 0
            print("your car died, better walk from here")
        elif self.battery_left == 0:
            print("You made it but now the cars dead. great")
        else:
            print("You made it.")
            print("Your car now has %s percent its gas" % self.gas_left)

    def crash_car(self):
            print("You crashed")
            print("You cant drive this car anymore ")
            self.windows = False
            self.headlights = False


my_car = Car("Mercedes", 100)
your_car = Car("Honda", 75)

my_car.drive(10)
my_car.crash_car