from RobotPositionValidator import RobotPositionValidator
from RobotTable import  RobotTable
from config import DIRECTION_RELATED_COORDINATION,DIRECTION_LIST
from Draw import Draw

class Robot:

    _x = 0
    _y = 0
    _direction = 'NORTH'
    _validator = None
    _table= None

    def __init__(self, table, validator):

        self._table = table if table else RobotTable()
        self._validator = validator if validator else RobotPositionValidator(self, self._table )


    def set_x(self, new_x):
        self._x = new_x

    def get_x(self):

        return self._x

    def set_y(self, new_y):
        self._y = new_y

    def get_y(self):
        return self._y

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def get_table(self):
        return self._table

    def set_location(self, new_x, new_y):

        if not self._validator.validate_position(new_x, new_y):
            return False

        self.set_x(new_x)
        self.set_y(new_y)

    def place(self,new_x,new_y, face):
        self.set_location(new_x,new_y)
        self.set_direction(face)
        self.report()

    def _rotate(self,clockwise = 1):

        current_direction_index = DIRECTION_LIST.index(self.get_direction())
        new_direction_index = (current_direction_index + clockwise) % 4

        self.set_direction(DIRECTION_LIST[new_direction_index])


    def right(self):

        self._rotate(clockwise= 1)
        self.report()

    def left(self):
        self._rotate(clockwise= -1)
        self.report()


    def move(self):

        new_x = self.get_x()
        new_y = self.get_y()

        type_of_move, move_value = DIRECTION_RELATED_COORDINATION.get(self.get_direction())

        new_x = new_x + move_value if type_of_move == 'X' else new_x
        new_y = new_y + move_value if type_of_move == 'Y' else new_y

        self.set_location(new_x, new_y )
        self.report()


    def report(self):
        Draw(self)
        output= str(self.get_x()) +',' +str(self.get_y())+','+ self.get_direction()
        print(output)
        return output













