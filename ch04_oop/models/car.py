from symtable import Class
import abc

class Car(abc.ABC):
    def __init__(self, model_name: str,engine_type: str,cylinders: int, base_price: float ):
        self.model_name: str = model_name
        self.engine_type: str = engine_type
        self.cylinders: int = cylinders
        self.base_price: float = base_price

    def drive(self):
        print(f"The {self.model_name} goes vroom!")

    @abc.abstractmethod
    def refuel(self):
        pass

    @property
    def is_electric(self):
        return self.engine_type == "electric"

    def __str__(self):
        return f"{type(self).__name__} Model: {self.model_name}, Price: ${self.base_price: ,.0f}"

    def __repr__(self):
        return self.__str__()

