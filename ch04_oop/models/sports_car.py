from models.car import Car


class SportsCar(Car):

    def drive(self):
        print(f"SportsCar: the {self.model_name} tears alog the highway!")

    def refuel(self):
        print(f"SportsCar: the {self.model_name} only wants the best gas.")