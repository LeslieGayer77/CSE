class Car(object):                                            # Type of object (Class)
    def __init__(self,  car_type, gas_left=50,):
        # These attributes that a phone has.
        # These should all be relevant to our program
        self.windows = True
        self.headlights = True
        self.gas_left = gas_left
        self.battery_left = True
        self.car_type = car_type
        self.battery_run_out_count = 0

    def gas(self, full):
            self.gas_left += full
            if self.gas_left > 100:
                self.gas_left = 100

    def drive(self, duration):
        if not self.headlights:
            print("Your car is totaled you cant drive")
            return
        gas_lost_per_minute = 1.5
        if self.gas_left <= 0:
            print("You have no more gas.")
            self.battery_run_out_count = self.battery_run_out_count + 1
            return
        if not self.windows:
            print("Your gonna get pulled over.")
            print("You shouldn't be driving")
        self.gas_left -= duration * gas_lost_per_minute
        if self.gas_left < 0:
            self.gas_left = 0
            print("your car ran out of gas!, better walk from here")
        elif self.gas_left == 0:
            print("You made it but now the cars out of gas. great")
        else:
            print("You made it.")
            print("Your car now has %s percent its gas" % self.gas_left)
        if self.battery_run_out_count == 3:
            self.battery_left = False
        if not self.battery_left:
            print("Your battery died. you cant drive anymore")
            return

    def crash_car(self):
            print("You crashed your car!")
            print("You cant drive this car anymore ")
            self.headlights = False

    def get_gas(self):
            print("You filled up your car")
            print("you now have 100 percent of your gas")
            self.gas_left = 100

    def smash_windows(self):
            print("You smashed your windows!")
            print("You cant drive this car anymore ")
            self.windows = False

    def fix_car(self):
            print("You fixed your car")
            print("You can now drive")
            self.windows = True
            self.headlights = True


my_car = Car("Mercedes", 100)
your_car = Car("Honda", 75)

my_car.drive(10)
my_car.crash_car()
my_car.drive(10)
my_car.fix_car()
my_car.drive(50)
my_car.get_gas()
my_car.drive(20)
print()
my_car.drive(10000)
my_car.get_gas()
my_car.drive(10000)
my_car.get_gas()
my_car.drive(10000)
my_car.get_gas()
my_car.drive(10000)