# The class of the car
class Car:

    # The __init__method
    def __init__(self, year, make, model, speed):
        self.__year = 2020
        self.__make = 'Tesla'
        self.__model = 'x'
        self.__speed = 0

    # set the method
    def setYear(self, __year):
        self.__year = __year

    #get the method
    def getYear(self):
        return self.__year

     # set the method
    def setMake(self, __make):
        self.__make = __make

    #get the method
    def getMake(self):
        return self.__make

     # set the method
    def setModel(self, __model):
        self.__model = __model

    #get the method    
    def getModel(self):
        return self.__model

     # set the method
    def setSpeed(self, __speed):
        self.__speed = __speed

    #get the method
    def getSpeed(self):
     return self.__speed
    
    def accelerate(self):
        if (self.__speed >= 120):
            print("warning: you cannot go faster than 120 MPH!!")
        else:
            self.__speed += 5

    def Break(self, __speed):
        if (self.__speed <= 0):

          print("Unable to brake, the vehicle is not moving!!")
    
        else:
            self.__speed-=5
        
#set the main function
def main():

   #Call the object  
   vehicle = Car(2020,'Tesla', 'x', 0)
   i=0

   # call while loop
   while i <=4:
        vehicle.accelerate()
    
        print(f"The speed of the car after acceleration number {i+1} is: ")

        print(vehicle.getSpeed())
        #stop the loop
        i=i+1

   print()

   j=0
   #call the while loop
   while j<=4:
        vehicle.Break(0)
     
        print(f"The speed of the car after brake number {j+1} is: ")
        print(vehicle.getSpeed())
        #stop the loop
        j=j+1

   
  
if __name__ == '__main__':
    main()


      
     
