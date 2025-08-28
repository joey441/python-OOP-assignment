#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
class Smartphone:
    def __init__(self, model,color, brand):
        self.model=model
        self.color=color
        self.brand=brand
    #to make a call
    def calls(self, number):
        print(f'Calling {number} from contacts')
    #take photo
    def photos(self):
        print('Taking a photo')
    # Child class with polymorphism
class SmartphoneWith5G(Smartphone):
    def __init__(self, model, color, brand, supports_5g):
        super().__init__(model, color, brand)
        self.supports_5g = supports_5g

    # Override photos method
    def photos(self):
        print('Taking a high-resolution photo with AI enhancements')

    def check_5g(self):
        if self.supports_5g:
            print(f'{self.model} supports 5G!')
        else:
            print(f'{self.model} does not support 5G') 
#Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗,
#  while Plane.move() prints "Flying" ✈️).
class vehicle:
    def move(self):
        print('Starting the vehicle.')
# Plane class
class Plane:
    def move(self):
        print("Flying ")
# Boat class
class Boat:
    def move(self):
        print("Sailing")
# Function to demonstrate polymorphism
def make_it_move(vehicle):
    vehicle.move()  # Calls the correct move() based on the object type

# Create objects
my_car = vehicle()
my_plane = Plane()
my_boat = Boat()

# Call move() using polymorphism
make_it_move(my_car)    
make_it_move(my_plane)  
make_it_move(my_boat)   
