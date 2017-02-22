# File: classroom.py


class Classroom(object):
    def __init__(self, number, capacity, equipment):
        """
        *** Called automaitcly when new instance of class is created.
        This method initializes a new Classroom instance which has:
        class_num param - (str) number of classroom
        capacity - (int) capacity of classroom
        equipment - (list(str, str, ..)) - list of equipment in the classroom

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom_2):
        """
        (None) -> (bool)
        This method returns (bool), which represents if the first classroom
        instance is larger then the second.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        return True if self.capacity > classroom_2.capacity else False

    def equipment_differences(self, room_2):
        """
        (object, object) -> list
        This method returns a list of unique equipment of first classroom
        which is not represented in classroom_2

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'mic', 'projector']
        """
        return sorted(list(set(self.equipment).difference(room_2.equipment)))

    def __str__(self):
        """
        This method returns an appropriate way of representing
        Classroom instance info.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        """
        return "Classroom {} has a capacity of {} persons and has the following equipment: {}.".format(
            self.number, self.capacity, ", ".join(self.equipment))

    def __repr__(self):
        """
        This method represents a Classroom instance in the following way:

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        """
        return "Classroom('{}', {}, ['{}'])".format(self.number, self.capacity,
                                                    "', '".join(
                                                        self.equipment))
