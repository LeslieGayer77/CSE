class Phone(object):                                            # Type of object (Class)
   def  __init__(self, carrier, charge_left):
       # These attributes that a phone has.
       #These should all be relevant to our program
       self.screen = True
       self.camera = 2
       self.microphone = True
       self.carrier = carrier
       self.batter_left = charge_left

    def charge(self, time):
        self.batter_left += time
        if self.batter_left > 100:
            self.batter_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You cant make a phone call.")
            print("Your screen is broken")
            return

        battery_loss_per_minute = 5
        if self.batter_left <= 0:
            print("The phone is dead.")
            return
        self.batter_left -= duration * battery_loss_per_minute
        if self.batter_left <0:
            self.batter_left = 0
            print("Yur phone dies during the conversation")
        elif self.batter_left == 0:
            print("Your phone dies at the end of the conversation.")
        else
            print("You successfully make the phone call.")
            print("Your phone is now at %s" % self.battery_left)

my_phone = Phone("ATT", 100)
your_phone = Phone("Bell", 0)



