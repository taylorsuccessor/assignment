def excute_robot_command(robot,command_text):


    if command_text.startswith('PLACE'):
        try:
            command, params_text = command_text.split(' ')

            x,y,direction = params_text.split(',')

            robot.place(int(x),int(y),direction)
        except:
            print('please, follow  PLACE command format (PLACE X,Y,FACE) ')

    elif command_text.startswith('MOVE'):
        robot.move()

    elif command_text.startswith('LEFT'):
        robot.left()

    elif command_text.startswith('RIGHT'):
        robot.right()

    elif command_text.startswith('REPORT'):
            robot.report()


    else:
        print('please select one of commands(PLACE, MOVE,LEFT,RIGHT,REPORT)')
