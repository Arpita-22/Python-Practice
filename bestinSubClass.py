class Pet(object):
    """
    Multiline comment!  
    """
    #class attribute
    num_pets = 0
    

    def __init__(self, name):
        self.name = name
        # self.num_pets += 1
        Pet.num_pets += 1

    def speak(self):
        # x = self.num_pets
        # self.num_pets += 1
        print("my name is %s and the number of pets is %d" %(self.name, self.num_pets))


rover = Pet("rover")
spot = Pet("spot")
smile = Pet("smile")

rover.speak()
spot.speak()
smile.speak()


