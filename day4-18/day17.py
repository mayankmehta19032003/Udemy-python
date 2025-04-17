class Car:
    
    def __init__(self,wheels):
        self.number_of_wheels = wheels  
        
    def start(self):
        print("Car started....")


car1 = Car(8)
print(car1.number_of_wheels)
car1.start()