class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self._model = model  # Protected attribute
        self.__engine_status = "off"  # Private attribute
    
    def start_engine(self):
        self.__engine_status = "on"
        print("Engine started!")
    
    def stop_engine(self):
        self.__engine_status = "off"
        print("Engine stopped!")
    
    def get_engine_status(self):
        return self.__engine_status

my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output: Toyota
print(my_car._model)  # Output: Corolla (Protected attribute accessed, though not recommended)
print(my_car.__engine_status)  # Error: AttributeError
print(my_car.get_engine_status())  # Output: off

