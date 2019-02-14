import Special_Random


class Phone(object):                                            # Type of object (Class)
    def __init__(self, carrier, charge_left=50):
        # These attributes that a phone has.
        # These should all be relevant to our program
        self.screen = True
        self.camera = 2
        self.microphone = True
        self.carrier = carrier
        self.battery_left = charge_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You cant make a phone call.")
            print("Your screen is broken")
            return
        battery_loss_per_minute = 5
        if self.battery_left <= 0:
            print("The phone is dead.")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone dies during the conversation")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation.")
        else:
            print("You successfully made the phone call.")
            print("Your phone is now at %s" % self.battery_left)

    def smash_phone(self):
        print("SMASHHHHHH!!!!!!")
        print("It broke")
        self.screen = False


my_phone = Phone("ATT", 100)
your_phone = Phone("Bell", 0)
default_phone = Phone("Verizon")

my_phone.make_call(10)
my_phone.make_call(10)
my_phone.make_call(100)

print(Special_Random.RandomWiebe.my_random())
