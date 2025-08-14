import unittest
from functions.get_files_info import *


class TestGetFilesFunction(unittest.TestCase):
    def test_in_local_directory(self):
        tst = get_files_info("calculator", ".")
        result = """Result for current directory:
 - main.py: file_size=576 bytes, is_dir=False
 - tests.py: file_size=1343 bytes, is_dir=False
 - pkg: file_size=92 bytes, is_dir=True
 """
        self.assertEqual(tst, result)

#     def test_in_pkg(self):
#         tst = get_files_info("calculator", "pkg")
#         result = """Result for 'pkg' directory:
#  - calculator.py: file_size=1739 bytes, is_dir=False
#  - render.py: file_size=768 bytes, is_dir=False
# """
#         self.assertEqual(tst, result)
#
#     def test_in_root_bin(self):
#         tst = get_files_info("calculator", "/bin")
#         result = """Result for '/bin' directory:
#     Error: Cannot list "/bin" as it is outside the permitted working directory
# """
#         self.assertEqual(tst, result)
#
#     def test_in_relative_path(self):
#         tst = get_files_info("calculator", "../")
#         result = """Result for '../' directory:
#     Error: Cannot list "../" as it is outside the permitted working directory
#     """
#         self.assertEqual(tst, result)


if __name__ == "__main__":
    unittest.main()
