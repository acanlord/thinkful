class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")


class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boom", "Crash", "Bang"])

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

    def count(self):
        for i in range(1, 5):
            print (i)


    def combust(self):
        print("Poof im on fire!")


class Band(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boom", "Crash", "Bang"])

    def hire(self):
        print("Your hired")


    def fire(self):
        print("Your Fired")
