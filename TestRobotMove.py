import unittest
from Robot import Robot
from helper import excute_robot_command
from test_case_list import case_list

class TestRobotMove(unittest.TestCase):

    _robot = Robot(None,None)


    def test_place(self):
        excute_robot_command(self._robot,'PLACE 2,3,NORTH')
        self.assertEqual('2,3,NORTH', self._robot.report())


    def test_move_y(self):
        excute_robot_command(self._robot,'PLACE 2,3,NORTH')
        excute_robot_command(self._robot,'MOVE')
        self.assertEqual('2,4,NORTH', self._robot.report())

    def test_move_x(self):
            excute_robot_command(self._robot, 'PLACE 2,3,EAST')
            excute_robot_command(self._robot, 'MOVE')
            self.assertEqual('3,3,EAST', self._robot.report())


    def test_case_list(self):
        for case in case_list:
            for command in case.get('command_list'):
                 excute_robot_command(self._robot, command)
            self.assertEqual(case.get('output'), self._robot.report())

if __name__ == '__main__':
    unittest.main()