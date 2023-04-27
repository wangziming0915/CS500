class Veihicles:
    def __init__(self, id: int, avaliable: bool, model: str, color: str, model_year: int, enhanced_safety_features: bool, security: bool, entertainment: bool, sunroofs: bool) -> None:
        self._id = id
        self._avaliable = avaliable
        self._model = model
        self._color = color
        self._model_year = model_year
        self._enhanced_safety_features = enhanced_safety_features
        self._security = security
        self._entertainment = entertainment
        self._sunroofs = sunroofs

    def display(self):
        print(f"The id is {self._id}. The avaliable is {self._avaliable}. The model is {self._model}, the base_price is {self._base_price}, the color is {self._color}, the model_year is {self._model_year}.")
    

class Trucks(Veihicles):
    def __init__(self, id: int, avaliable: bool, model: str, color: str, model_year: int, cargo_bed_size: str, engine_power: int, enhanced_safety_features: bool, security: bool, entertainment: bool, sunroofs: bool) -> None:
        super().__init__(id, avaliable, model, color, model_year, enhanced_safety_features, security, entertainment, sunroofs)
        self.__cargo_bed_size = cargo_bed_size
        self.__engine_power = engine_power
        self._base_price = 35000
        self.__total_price = 35000
        if enhanced_safety_features:
            self.__total_price += 3000
        if security:
            self.__total_price += 1000
        if entertainment:
            self.__total_price += 2000
        if sunroofs:
            self.__total_price += 2500

    @property
    def total_price(self) -> int:
        return self.__total_price

    @property
    def cargo_bed_size(self) -> str:
        return self.__cargo_bed_size
    
    @property
    def engine_power(self) -> int:
        return self.__engine_power
    
    def display(self) -> None:
        super().display()
        print(f"This is a truck. The cargo_bed_size is {self.cargo_bed_size}, the engine_power is {self.__engine_power}.")

    
class SUVs(Veihicles):
    def __init__(self, id: int, avaliable: bool, model: str, color: str, model_year: int, drive_pad: str, root_rack_type: str, enhanced_safety_features: bool, security: bool, entertainment: bool, sunroofs: bool) -> None:
        super().__init__(id, avaliable, model, color, model_year, enhanced_safety_features, security, entertainment, sunroofs)
        self.__driver_pad = drive_pad
        self.__root_rack_type = root_rack_type
        self._base_price = 40000
        self.__total_price = 40000
        if enhanced_safety_features:
            self.__total_price += 3000
        if security:
            self.__total_price += 1000
        if entertainment:
            self.__total_price += 2000
        if sunroofs:
            self.__total_price += 2500

    @property
    def total_price(self) -> int:
        return self.__total_price

    @property
    def drive_pad(self) -> str:
        return self.__driver_pad
    
    @property
    def root_rack_type(self) -> str:
        return self.__root_rack_type
    
    def display(self) -> None:
        super().display()
        print(f"This is a SUV. The driver_pad is {self.drive_pad}, the root_rack_type is {self.root_rack_type}.")

class Minivans(Veihicles):
    def __init__(self, id: int, avaliable: bool, model: str, color: str, model_year: int, sliding_doors: bool, hinged_rear_doors: bool, enhanced_safety_features: bool, security: bool, entertainment: bool, sunroofs: bool) -> None:
        super().__init__(id, avaliable, model, color, model_year, enhanced_safety_features, security, entertainment, sunroofs)
        self.__sliding_doors = sliding_doors
        self.__hinged_rear_doors = hinged_rear_doors
        self._base_price = 45000
        self.__total_price = 45000
        if enhanced_safety_features:
            self.__total_price += 3000
        if security:
            self.__total_price += 1000
        if entertainment:
            self.__total_price += 2000
        if sunroofs:
            self.__total_price += 2500

    @property
    def total_price(self) -> int:
        return self.__total_price

    @property
    def sliding_doors(self) -> bool:
        return self.__sliding_doors
    
    @property
    def hinged_rear_doors(self) -> bool:
        return self.__hinged_rear_doors
    
    def display(self):
        super().display()
        print(f"This is a Minivan. The sliding_doors is {self.sliding_doors}, the hinged_rear_doors is {self.hinged_rear_doors}.")


class Sedans(Veihicles):
    def __init__(self, id: int, avaliable: bool, model: str, color: str, model_year: int, space: str, seat: str, enhanced_safety_features: bool, security: bool, entertainment: bool, sunroofs: bool) -> None:
        super().__init__(id, avaliable, model, color, model_year, enhanced_safety_features, security, entertainment, sunroofs)
        self.__space = space
        self.__seat = seat
        self._base_price = 30000
        self.__total_price = 30000
        if enhanced_safety_features:
            self.__total_price += 3000
        if security:
            self.__total_price += 1000
        if entertainment:
            self.__total_price += 2000
        if sunroofs:
            self.__total_price += 2500

    @property
    def total_price(self) -> int:
        return self.__total_price


    @property
    def total_price(self) -> int:
        return self.__total_price

    @property
    def space(self) -> str:
        return self.__space
    
    @property
    def seat(self) -> str:
        return self.__seat
    
    def display(self):
        super().display()
        print(f"This is a Sedan. The space is {self.seat}, the seat is {self.seat}.")

class Stock():
    def __init__(self) -> None:
        self.__list_of_vehicles = []

    @property
    def list_of_vehicles(self) -> list[Veihicles]:
        return self.__list_of_vehicles
    
    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        if self.index <= len(self.list_of_vehicles):
            cur_index = self.index
            self.index += 1
            return self.list_of_vehicles[cur_index]
        else:
            raise StopIteration

    def add_vehicle(self, vehicle: Veihicles):
        self.list_of_vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Veihicles):
        for cur_vehicle in self.list_of_vehicles:
            if cur_vehicle._id == vehicle._id:
                self.list_of_vehicles.remove(cur_vehicle)
                print(f"Vehicle removed.")
                return
        print(f"Target vehicle does not exist.")
        return
    
    def search_vehicle(self, vehicle_id: int):
        for cur_vehicle in self.list_of_vehicles:
            if cur_vehicle._id == vehicle_id:
                cur_vehicle.display()
                return
        print(f"Target vehicle does not exist.")
        return
    
    def print_avaliable_vehicle(self):
        for cur_vehicle in self.list_of_vehicles:
            if cur_vehicle._avaliable:
                cur_vehicle.display()
    
    def find_most_expensive(self) -> Veihicles:
        most_expensive = self.list_of_vehicles[0]
        for cur_vehicle in self.list_of_vehicles:
            if cur_vehicle.total_price > most_expensive.total_price:
                most_expensive = cur_vehicle
        
        return most_expensive
    
    def find_least_expensive(self) -> Veihicles:
        least_expensive = self.list_of_vehicles[0]
        for cur_vehicle in self.list_of_vehicles:
            if cur_vehicle.total_price < least_expensive.total_price:
                least_expensive = cur_vehicle
        
        return least_expensive

    def create_new_vehicle(self):
        total_price = 0
        print(f"What kind of vehicle do you want to create?")
        print(f"1. Sedans\n2. Trucks\n3. SUVs\n4. Minivans\n")
        car_type = int(input("Enter number for the type of your vehicle: "))
        if car_type == 1:
            total_price += 30000
        elif car_type == 2:
            total_price += 35000
        elif car_type == 3:
            total_price += 40000
        elif car_type == 4:
            total_price += 45000
        safety_features = int(input(f"Do you want enhanced safety features?\n1. Yes\n2. No"))
        security = int(input(f"Do you want security?\n1. Yes\n2. No\n"))
        print()
        entertainment = int(input(f"Do you want entertainment?\n1. Yes\n2. No\n"))
        print()
        sunroofs = int(input(f"Do you want sunroofs?\n1. Yes\n2. No\n"))
        print()
        if safety_features == 1:
            total_price += 3000
        if security == 1:
            total_price += 1000
        if entertainment == 1:
            total_price += 2000
        if sunroofs == 1:
            total_price += 2500

        print(f"The total price of the created vehicle is {total_price}.")

def main():
    truck1 = Trucks(1111, True, 1, "Red", 1, "small", 500, True, True, False, False)
    minivan1 = Minivans(1112, True, 2, "Black", 2, True, False, False, False, True, True)
    sedan1 = Sedans(1113, True, "3", "White", 5, "Large", "Soft", False, False, True, False)
    stock1 = Stock()
    stock1.add_vehicle(truck1)
    stock1.add_vehicle(minivan1)
    stock1.add_vehicle(sedan1)
    stock1.print_avaliable_vehicle()
    print()
    stock1.search_vehicle(1111)
    print()
    stock1.find_least_expensive().display()
    stock1.find_most_expensive().display()
    #stock1.create_new_vehicle()



if __name__ == "__main__":
    main()

