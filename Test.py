import unittest
from Robot import Robot
from helper import excute_robot_command
from test_case_list import case_list

class Test(unittest.TestCase):




    def test_first_function(self):
        result = True
        self.assertEqual(True, result)



if __name__ == '__main__':
    unittest.main()