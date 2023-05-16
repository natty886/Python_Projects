# Class uses encapulation
# Protected variable
class Protect:
    def __init__(self):
    # Private variable
# NOTE: Python 3+ methods that start with double underscore causes name mangling
        self._self__secureVar = 144

    def getSecure(self):
       print(self._self__secureVar)

    def setSecure(self, secure):
       self._self__secureVar = secure

# Object gets data of private variable w/ new value.        
obj = Protect()
obj.getSecure()
obj.setSecure(51)
obj.getSecure()
