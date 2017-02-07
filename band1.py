class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
    
    def solo(self, length = 2):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end =" ")
        #print()
        return 
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
nigel = Guitarist()
nigel.solo(6)
print(nigel.sounds)


"""
Extend the example code to add a Drummer class. Drummers should be able to solo, 
count to four, and spontaneously combust. 
Then add a Band class. 
Bands should be able to hire and fire musicians, 
and have the musicians play their solos after 
the drummer has counted time.
"""
class Drummer(Musician):
    def __init__ (self):
        super().__init__(["Tap", "Thud", "Ding"])
        
    def  count_to (self,number): 
	    for number in range (0, number): 
	        print (number)
    def spontaneously_combust(self):
        print ("Poof")

bob = Drummer()
bob.solo()

bob.count_to(4)
bob.spontaneously_combust()
print (bob.sounds)


class  Band(object):
    def hire(self,person):
        our_band = []
        our_band = our_band.append(person)
        
    def fire(self,person,band=None):
        if len(our_band == 0):
            our_band = []
        else:
            our_band = band.remove(person) 
            
            
    #band is a musician or band has a musician. "if it is a" then needs to inherit from.  
    
    
    
    
    





