import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import json_helper

"""
Migrated from PythonFundamentals.Exercises.Part8 
Use the below fileReader Test class to work develop framework for 
"""

class FileReaderTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_read_json(self, mock_stdout):
        test_cases = [
            (
                "my_awesome_file.txt",
                "IF YOU ARE SEEING THIS ON YOUR CONSOLE,\n"
                "THAT MEANS YOUR PROGRAM WORKED AS EXPECTED.\n"
                "WHY AM I YELLING???"
            )
        ]
        for file_path, expected in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.reckless_file_reader(file_path)
                actual = mock_stdout.getvalue()
                self.assertEqual(expected, actual)

    def test_read_all_json_files(self):
        test_cases = [
            ("locked_out_file.txt", PermissionError),
            ("file_that_does_not_exist.txt", FileNotFoundError)
        ]
        for file_path, expected in test_cases:
            with self.subTest(f"{file_path}"):
                with self.assertRaises(expected):
                    file_reader.reckless_file_reader(file_path)

    @unittest.skip("Useless test. This exists simply to trigger and demo the function under test.")
    def test_write_pickle(self):
        with self.assertRaises(PermissionError):
            file_reader.quick_way_to_get_fired("locked_out_file.txt")

    def test_is_dir(self):
        with self.assertLogs() as cm:
            file_reader.single_exception_handling_reader("file_that_does_not_exist.txt")
            self.assertIn("No such file or directory: 'file_that_does_not_exist.txt'", cm.output[0])

    def test_is_json(self):
        with self.assertRaises(PermissionError):
            file_reader.single_exception_handling_reader("locked_out_file.txt")

    def test_load_pickle(self):
        test_cases = [
            (
                "file_that_does_not_exist.txt",
                "No such file or directory: 'file_that_does_not_exist.txt'"
            ),
            (
                "locked_out_file.txt",
                "Permission denied: 'locked_out_file.txt'"
            )
        ]
        for file_path, message in test_cases:
            with self.subTest(f"{file_path} -> {message}"):
                with self.assertLogs() as cm:
                    file_reader.multiple_exception_handling_reader(file_path)
                    self.assertIn(message, cm.output[0])
