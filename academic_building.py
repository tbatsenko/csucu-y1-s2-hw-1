# File: academic_building.py
from classroom import Classroom
from building import Building


class AcademicBuilding(Building):
    def __init__(self, address, classrooms, **kwargs):
        """
        *** Called automaitcly when new instance of class is created.
        This method initializes a new AcademicBuilding instance
        which inherits from Building class and calls it's __init__ method
        and has additional params:
        classrooms - (list(Classroom, Classroom, ...)) - list of classrooms
        in the building.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        >>> for room in building.classrooms:
        ...  print(room)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        Building.__init__(self, address)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        (AcademicBuilding) -> list((tuple), (tuple), ...)
        This method returns a list of equipment in the AcademicBuilding.
        Each equipment is represented by tuple:
        ((str) - name of equipment, (int) - amount of such an equipment in the
        building.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
        """
        lst_of_equipment = [item for room in self.classrooms
                            for item in room.equipment]
        lst_of_equipment = [(item, lst_of_equipment.count(item))
                            for item in lst_of_equipment]
        return sorted(set(lst_of_equipment))

    def __str__(self):
        """
        This method returns an appropriate way of representing
        AcademicBuilding instance info when called 'print'.
        повертати рядок для представлення навчального корпусу:

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        return self.address + '\n' + '\n'.join(['%s']*len(
            self.classrooms)) % tuple(self.classrooms)
import doctest
doctest.testmod()
