from Robot import Robot
from helper import excute_robot_command

robot = Robot(None, None)



while True:
    command_text = raw_input()

    if command_text == 'exit':
        break
    else:
        excute_robot_command(robot, command_text)

