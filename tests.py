import unittest
from functions.get_files_info import *


class TestGetFilesFunction(unittest.TestCase):
     def test_in_local_directory(self):
         tst = get_files_info("calculator", ".")
         result = """Result for current directory:
- pkg: file_size=4096 bytes, is_dir=True
- tests.py: file_size=1343 bytes, is_dir=False
- main.py: file_size=576 bytes, is_dir=False
Error: """
         self.assertEqual(tst, result)

     def test_in_pkg(self):
         tst = get_files_info("calculator", "pkg")
         result = """Result for 'pkg' directory:
- render.py: file_size=767 bytes, is_dir=False
- calculator.py: file_size=1738 bytes, is_dir=False
Error: """
         self.assertEqual(tst, result)

     def test_in_root_bin(self):
         with self.assertRaises(Exception) as context:
             get_files_info("calculator", "/bin")
         self.assertEqual(str(context.exception), 'Error: Cannot list "/bin" as it is outside the permitted working directory')

     def test_in_relative_path(self):
         with self.assertRaises(Exception) as context:
             get_files_info("calculator", "../")
         self.assertEqual(str(context.exception), 'Error: Cannot list "../" as it is outside the permitted working directory')


if __name__ == "__main__":
    unittest.main()
