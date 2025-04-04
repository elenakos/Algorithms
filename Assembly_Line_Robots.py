'''
Create an assembly line class for different types robots (6) with different set of configuration settings (7) each
'''

import unittest
from enum import Enum
import random
from unittest import case


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

ALL_SETTINGS = list(RobotSettings)

# Define each robot's configuration
# Each element in an array represent one setting/character that is present (1) or not (0)
ROBOT_A_SET = [1, 0, 1, 0, 1, 0, 1]
ROBOT_B_SET = [0, 0, 1, 0, 1, 0, 1]
ROBOT_C_SET = [1, 0, 1, 1, 1, 0, 1]
ROBOT_D_SET = [1, 0, 1, 0, 1, 0, 1]
ROBOT_E_SET = [1, 0, 1, 0, 1, 1, 1]
ROBOT_F_SET = [0, 0, 1, 1, 1, 1, 1]

class Robot:
    def __init__(self, robot_type=None, settings=None):
        if robot_type == "" or robot_type is None:
            self.robot_type = random.choice(ALL_ROBOTS).name
        elif robot_type  not in RobotTypes:
            raise ValueError(f"Robot type '{robot_type}' is not a valid robot type")
        else:
            self.robot_type = robot_type
        self.robot_settings = []
        match self.robot_type:
            case RobotTypes.ROBOT_A:
                self.robot_settings = ROBOT_A_SET
            case RobotTypes.ROBOT_B:
                self.robot_settings = ROBOT_B_SET
            case RobotTypes.ROBOT_C:
                self.robot_settings = ROBOT_C_SET
            case RobotTypes.ROBOT_D:
                self.robot_settings = ROBOT_D_SET
            case RobotTypes.ROBOT_E:
                self.robot_settings = ROBOT_E_SET
            case RobotTypes.ROBOT_F:
                self.robot_settings = ROBOT_F_SET

    def identify_robot_type(self, settings):
        if len(settings) != len(RobotSettings):
            print("Wrong number of settings")
        else:
            if settings == ROBOT_A_SET:
                self.robot_type = RobotTypes.ROBOT_A
            if settings == ROBOT_B_SET:
                self.robot_type = RobotTypes.ROBOT_B
            if settings == ROBOT_C_SET:
                self.robot_type = RobotTypes.ROBOT_C
            if settings == ROBOT_D_SET:
                self.robot_type = RobotTypes.ROBOT_D
            if settings == ROBOT_E_SET:
                self.robot_type = RobotTypes.ROBOT_E
            if settings == ROBOT_F_SET:
                self.robot_type = RobotTypes.ROBOT_F
        return self.robot_type

    def return_setting_value_for_a_robot(self, setting):
        print("Setting value for robot [" + self.robot_type.__str__() + "]")
        value = None
        match setting:
            case RobotSettings.ROBOT_SETTING_1:
                value = self.robot_settings[0]
            case RobotSettings.ROBOT_SETTING_2:
                value = self.robot_settings[1]
            case RobotSettings.ROBOT_SETTING_3:
                value = self.robot_settings[2]
            case RobotSettings.ROBOT_SETTING_4:
                value = self.robot_settings[3]
            case RobotSettings.ROBOT_SETTING_5:
                value = self.robot_settings[4]
            case RobotSettings.ROBOT_SETTING_6:
                value = self.robot_settings[5]
            case RobotSettings.ROBOT_SETTING_7:
                value = self.robot_settings[6]

        return value


    def __str__(self):
        return f"This robot is of [{self.robot_type.value}] type"

class AssemblyLineRobots:
    def __init__(self, robot_type=None):
        self.robot = Robot(robot_type)


class TestAssemblyLineRobots(unittest.TestCase):
    def test_create_and_print_robot_name(self):
        print("\nTC: Create a robot and print its name")
        assembly_line = AssemblyLineRobots(RobotTypes.ROBOT_A)
        actual = assembly_line.robot.__str__()
        expected = "This robot is of [Robot A] type"
        self.assertEqual(actual, expected)

    def test_identify_a_robot_by_settings(self):
        print("\nTC: Indentify a robot by its settings")
        settings = [0, 0, 1, 1, 1, 1, 1]
        assembly_line = AssemblyLineRobots()
        actual = Robot(assembly_line.robot.identify_robot_type(settings)).__str__()
        expected = "This robot is of [Robot F] type"
        self.assertEqual(actual, expected)

    def test_get_specific_setting_value_for_robot(self):
        print("\nTC: Print a specific setting value for a specific robot type")
        robot = Robot(RobotTypes.ROBOT_E)
        actual_setting_value = robot.return_setting_value_for_a_robot(RobotSettings.ROBOT_SETTING_1)
        expected_setting_value = 1
        self.assertEqual(expected_setting_value, actual_setting_value)
