class Train:
    """ Train class that has  """
    
    def __init__ (self, totalSeats=480):
        self.totalSeats = totalSeats
        self._availableSeats =  totalSeats
    
    def __repr__ (self):
        return f'{self.__class__.__name__}: Total seats: {self.totalSeats!r}, Available seats: {self._availableSeats!r}'

    def __str__(self):
        return f'{self.__class__.__name__}: Total seats: {self.totalSeats}, Available seats: {self._availableSeats}'
        
    #Getter for availableSeats
    @property
    def availableSeats (self):
        return self._availableSeats
    #Setter to validate availableSeats
    @availableSeats.setter
    def availableSeats (self, seats):
        if seats < 0 or seats > self.totalSeats:
            raise ValueError (f'Available seats must be between 0 and {self.totalSeats}')
        else:
            self._availableSeats = seats
    
    #+= and -= operators overloading to facilitate seat bookings
    def __iadd__(self, other):
        if self._availableSeats + other > self.totalSeats or self._availableSeats + other < 0:
            raise ValueError (f'The result must be between 0 and {self.totalSeats}')
        else:
            self._availableSeats = self._availableSeats + other
            return self
            
    def __isub__(self, other):
        if self._availableSeats - other > self.totalSeats or self._availableSeats - other < 0:
            raise ValueError (f'The result must be between 0 and {self.totalSeats}')
        else:
            self._availableSeats = self._availableSeats - other
            return self
    

#Dictionary containing the trains going to the top
FoottoTopTrains = {}
#Dictionary containing the trains returning to the foot
ToptoFootTrains = {}

#Initialising trains going to the top
FoottoTopTrains.update({'9:00' : Train ()})
FoottoTopTrains.update({'11:00' : Train ()})
FoottoTopTrains.update({'13:00' : Train ()})
FoottoTopTrains.update({'15:00' : Train ()})

#Initialising trains returning to the foot
ToptoFootTrains.update({'10:00' : Train ()})
ToptoFootTrains.update({'12:00' : Train ()})
ToptoFootTrains.update({'14:00' : Train ()})
#Last train has 2 extra coaches (8*80 seats)
ToptoFootTrains.update({'16:00' : Train (640)})



testTrain = Train()
print (testTrain)
print()
testTrain.availableSeats = 20
print (testTrain)
print()
testTrain -= 20
print (testTrain)
print()

# print ('Trains going to the top')
# for time, train in FoottoTopTrains.items():
#    print ('Dep. time: ', time, 'Seats available: ', train.availableSeats)
# 
# print()
# print ('Trains returning to the foot')
# for time, train in ToptoFootTrains.items():
#    print ('Dep. time: ', time, 'Seats available: ', train.availableSeats)
# 
# 
# pause = input()
