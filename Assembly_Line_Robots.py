'''
Create an assembly line class for different types robots (6) with different set of configuration settings (7) each
'''

import unittest
from enum import Enum
import random

class RobotTypes(Enum):
    ROBOT_A = "Robot A"
    ROBOT_B = "Robot B"
    ROBOT_C = "Robot C"
    ROBOT_D = "Robot D"
    ROBOT_E = "Robot E"
    ROBOT_F = "Robot F"

ALL_ROBOTS = list(RobotTypes)

class RobotSettings(Enum):
    ROBOT_SETTING_1 = "Setting1"
    ROBOT_SETTING_2 = "Setting2"
    ROBOT_SETTING_3 = "Setting3"
    ROBOT_SETTING_4 = "Setting4"
    ROBOT_SETTING_5 = "Setting5"
    ROBOT_SETTING_6 = "Setting6"
    ROBOT_SETTING_7 = "Setting7"

# Define each robot's configuration
# Each element in an array represent one setting/character that is present (1) or not (0)
ROBOT_A = [1, 0, 1, 0, 1, 0, 1]
ROBOT_B = [0, 0, 1, 0, 1, 0, 1]
ROBOT_C = [1, 0, 1, 1, 1, 0, 1]
ROBOT_D = [1, 0, 1, 0, 1, 0, 1]
ROBOT_E = [1, 0, 1, 0, 1, 1, 1]
ROBOT_F = [0, 0, 1, 1, 1, 1, 1]

class Robot:
    def __init__(self, robot_type):
        if robot_type == "":
            self.robot_type = random.choice(ALL_ROBOTS).name
        elif robot_type  not in RobotTypes:
            raise ValueError(f"Robot type '{robot_type}' is not a valid robot type")
        else:
            self.robot_type = robot_type

    def identify_robot_type(self, settings):
        if len(settings) != len(RobotSettings):
            print("Wrong number of settings")
        else:
            if settings == ROBOT_A:
                self.robot_type = RobotTypes.ROBOT_A
            if settings == ROBOT_B:
                self.robot_type = RobotTypes.ROBOT_B
            if settings == ROBOT_C:
                self.robot_type = RobotTypes.ROBOT_C
            if settings == ROBOT_D:
                self.robot_type = RobotTypes.ROBOT_D
            if settings == ROBOT_E:
                self.robot_type = RobotTypes.ROBOT_E
            if settings == ROBOT_F:
                self.robot_type = RobotTypes.ROBOT_F
        return self.robot_type

    def __str__(self):
        return f"Nice robot of {self.robot_type.value}"

class AssemblyLineRobots:
    def __init__(self, robot_type):
        self.robot = Robot(robot_type)


class TestAssemblyLineRobots(unittest.TestCase):
    def test_create_print_robot_name(self):
        print("Create a robot and print its name")
        assembly_line = AssemblyLineRobots(RobotTypes.ROBOT_A)
        actual = assembly_line.robot.__str__()
        expected = "Nice robot of Robot A"
        self.assertEqual(actual, expected)

    def test_identify_robot(self):
        print("Indentify a robot by its settings")
        settings = [0, 0, 1, 1, 1, 1, 1]
        assembly_line = AssemblyLineRobots("")
        actual = Robot(assembly_line.robot.identify_robot_type(settings)).__str__()
        expected = "Nice robot of Robot F"
        self.assertEqual(actual, expected)

