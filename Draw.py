class Draw:

    _table = None

    def __init__(self,robot):
        self._table = robot.get_table()
        self.draw_robot_table(robot.get_x(),robot.get_y(),robot.get_direction())


    @staticmethod
    def draw_robot(direction):
        if direction == 'NORTH':
            print('^'),
        elif direction == 'EAST':
            print('>'),
        elif direction == 'SOUTH':
            print('V'),
        elif direction == 'WEST':
            print('<'),



    def draw_robot_table(self, x,y,direction):
        table_height = self._table.get_height()
        table_width = self._table.get_width()

        for i in range( table_height - 1,-1,-1):
            for j in range(table_width):
                if i==y and j == x:
                    Draw.draw_robot(direction)
                else:
                    print('#'),

                if(j == table_width  - 1):
                        print('')

