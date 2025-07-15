'''
Given a file where expressions are separated by :
Read a file line by line and report the statistics of expressions that appear more than once
'''
import unittest


class ReadFile:
    def __init__(self, file):
        self.file = file

    def read_file_generate_statistics(self):
        print("\nReading a file")
        stat = {}
        try:
            file = open(self.file, "r")
            while True:
                current = file.readline()
                if not current:
                    file.close()
                    break
                current_array = current.split(":")
                print(current_array)
                for expression in current_array:
                    if expression.strip() in stat:
                        stat[expression.strip()] += 1
                    else:
                     stat[expression.strip()] = 1

        except FileNotFoundError:
            print("File not found")
            return {}

        repeated_expressions = {}
        for k, v in stat.items():
            if v != 1:
                repeated_expressions.update({k: v})
        return repeated_expressions


class TestReadFile(unittest.TestCase):
    def test_read_file_generate_statistics(self):
        print("\n*** TC: Reading a file with many repeated expressions")
        file1 = ReadFile("Work_with_files_1.txt")
        result = file1.read_file_generate_statistics()
        expected = {'Hello World': 3, 'Hello from JavaScript': 2, 'Hello from python': 2}
        self.assertEqual(expected, result)

    def test_read_file_no_duplicates(self):
        print("\n*** TC: Reading a file with no repeated expressions")
        file1 = ReadFile("Work_with_files_2.txt")
        result = file1.read_file_generate_statistics()
        expected = {}
        self.assertEqual(expected, result)

    def test_read_file_no_file(self):
        print("\n*** TC: Reading a file with no repeated expressions")
        file1 = ReadFile("Work_with_files_3.txt")
        result = file1.read_file_generate_statistics()
        expected = {}
        self.assertEqual(expected, result)