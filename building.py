# File: building.py


class Building(object):
    def __init__(self, address):
        """
        This method initializes a new Building instance which has:
        address - (str) address of the building.
        """
        self.address = address


class House(Building):
    def __init__(self, address, flats, **kwargs):
        """
        This method initializes a new House instance which inherits from
        Building class and calls it's __init__ method
        and has additional params:
        flats - list[(str), (str), ...] - list of flats in the House.
        """
        Building.__init__(self, address)
        self.flats = flats
