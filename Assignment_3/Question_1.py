# Car Class
class Car:
    def __init__(self, year_model, make):
        # declaring car variables
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # accelerate function adds 5 to the speed
    def accelerate(self):
        self.__speed += 5

    # brake function lowers the speed by 5
    def brake(self):
        self.__speed -= 5

    # shows the current speed of the car
    def get_speed(self):
        return self.__speed


# main
if __name__ == '__main__':
    my_car = Car(2011, "Cadillac")

    # range to accelerate 5 times
    for temp in range(0, 5):
        my_car.accelerate()
        # shows current speed
        print("Current speed: ", my_car.get_speed())
    # range to brake 5 times
    for temp in range(0, 5):
        my_car.brake()
        #shows current speed
        print("Current speed: ", my_car.get_speed())
