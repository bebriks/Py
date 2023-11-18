class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        '''
           Представление всей информации для вывода в методе print()
        '''
        return (f"Transport(coordinates={self.coordinates}, speed={self.speed}, brand={self.brand}, year={self.year}, "
                f"number={self.number})")

    @property
    def coordinates(self):
        return self.coordinates

    @coordinates.setter
    def coordinates(self, val):
        if isinstance(val, int or float):
            self.coordinates = val

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, val):
        if isinstance(val, int or float):
            self.speed = val

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, val):
        if isinstance(val, str):
            self.brand = val

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, val):
        if isinstance(val, int):
            self.year = val

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, val):
        if isinstance(val, int):
            self.number = val

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width


class Passenger():

    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, val):
        if isinstance(val, int):
            self._passengers_capacity = val

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, val):
        if isinstance(val, int):
            self._number_of_passengers = val


class Cargo():
    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, val):
        self.__carrying = val


class Plane(Transport):
    def __init__(self, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = height

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, val):
        if isinstance(val, int or float):
            self.height = val


class Auto(Transport):
    def __init__(self, way, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.way = way

    @property
    def way(self):
        return self.way

    @way.setter
    def way(self, val):
        if isinstance(val, int or float):
            self.way = val


class Ship(Transport):
    def __init__(self, port, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)
        self.port = port

    @property
    def port(self):
        return self.port

    @port.setter
    def port(self, val):
        if isinstance(val, str):
            self.port = val


class Car(Auto):
    def __init__(self, *args, **kwargs):
        super(Car, self).__init__(*args, **kwargs)


class Bus(Auto, Passenger):
    def __init__(self, *args, **kwargs):
        super(Bus, self).__init__(*args, **kwargs)


class CargoAuto(Auto, Cargo):
    def __init__(self, *args, **kwargs):
        super(CargoAuto, self).__init__(*args, **kwargs)


class Boat(Ship):
    def __init__(self, *args, **kwargs):
        super(Boat, self).__init__(*args, **kwargs)


class PassengerShip(Ship, Passenger):
    def __init__(self, *args, **kwargs):
        super(PassengerShip, self).__init__(*args, **kwargs)


class CargoShip(Ship, Cargo):
    def __init__(self, *args, **kwargs):
        super(CargoShip, self).__init__(*args, **kwargs)


class Seaplane(Plane, Ship):
    def __init__(self, *args, **kwargs):
        super(Seaplane, self).__init__(*args, **kwargs)

# аналогично создать классы для самолета и класс Seaplane(Plane, Ship).
