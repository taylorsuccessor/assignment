class Draw:

    def __init__(self,x,y,direction):
        Draw.draw_robot_table(x,y,direction)

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


    @staticmethod
    def draw_robot_table(x,y,direction):

        for i in range(4,-1,-1):
            for j in range(5):
                if i==y and j == x:
                    Draw.draw_robot(direction)
                else:
                    print('#'),

                if(j == 4):
                        print('')

