

class RobotPositionValidator:
    robot = None
    table = None

    def __init__(self,robot, table):
        self.robot = robot
        self.table = table

    def validate_position(self, x, y):

        table_width = self.table.get_width()
        table_height = self.table.get_height()

        if 0 <= x < table_width and 0 <= y < table_height :
            return True

        return False






