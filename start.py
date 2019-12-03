from Robot import Robot
from helper import excute_robot_command

robot = Robot(None, None)



while True:
    command_text = raw_input()

    if command_text == 'exit':
        break
    else:
        excute_robot_command(robot, command_text)





    # robot.place(0,0,'NORTH')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())
    #
    #
    #
    # robot.place(0,0,'NORTH')
    # robot.rotate('LEFT')
    # print(robot.get_x(),robot.get_y(),robot.get_direction())
    #
    #
    # robot.place(1,2,'EAST')
    # robot.move()
    # robot.move()
    # robot.rotate('LEFT')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())
    #
    #
    # robot.place(4,2,'EAST')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())
    #
    #
    # robot.place(4,2,'NORTH')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())
    #
    #
    # robot.place(4,4,'NORTH')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())



    # robot.place(4,4,'WEST')
    # robot.rotate('LIFT')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())



    # robot.place(0,0,'WEST')
    # robot.rotate('LIFT')
    # robot.move()
    # print(robot.get_x(),robot.get_y(),robot.get_direction())


    # robot.place(0,4,'NORTH')
    # robot.move()
    # robot.rotate('LIFT')
    # robot.move()

    # robot.place(4, 0, 'EAST')
    # robot.move()
    # robot.right()
    # robot.move()



