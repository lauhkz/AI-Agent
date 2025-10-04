import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


# class TestGetFilesInfoFunction(unittest.TestCase):
#      def test_in_local_directory(self):
#          tst = get_files_info("calculator", ".")
#          result = """Result for current directory:
# - pkg: file_size=4096 bytes, is_dir=True
# - tests.py: file_size=1343 bytes, is_dir=False
# - main.py: file_size=576 bytes, is_dir=False
# Error: """
#          self.assertEqual(tst, result)
#
#      def test_in_pkg(self):
#          tst = get_files_info("calculator", "pkg")
#          result = """Result for 'pkg' directory:
# - render.py: file_size=767 bytes, is_dir=False
# - calculator.py: file_size=1738 bytes, is_dir=False
# Error: """
#          self.assertEqual(tst, result)
#
#      def test_in_root_bin(self):
#          with self.assertRaises(Exception) as context:
#              get_files_info("calculator", "/bin")
#          self.assertEqual(str(context.exception), 'Error: Cannot list "/bin" as it is outside the permitted working directory')
#
#      def test_in_relative_path(self):
#          with self.assertRaises(Exception) as context:
#              get_files_info("calculator", "../")
#          self.assertEqual(str(context.exception), 'Error: Cannot list "../" as it is outside the permitted working directory')
#

class TestGetFileContentFunction(unittest.TestCase):
    # def test_function(self):
    #     result = get_file_content("calculator", "lorem.txt")
    #     print(result)
    # def test_function(self):
    #     tst1 = get_file_content("calculator", "main.py")
    #     print(tst1)
    #     tst2 = get_file_content("calculator", "pkg/calculator.py")
    #     print(tst2)
    #     tst3 = get_file_content("calculator", "/bin/cat")
    #     print(tst3)
    #     tst4 = get_file_content("calculator", "pkg/does_not_exist.py")
    #     print(tst4)
    # def test_write_function(self):
    #     tst1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #     print(tst1)
    #     tst2 = write_file("calculator","pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #     print(tst2)
    #     tst3 = write_file("calculator","/tmp/temp.txt", "this should not be allowed")
    #     print(tst3)
    def test_run_py(self):
        tst1 = run_python_file("calculator", "main.py")
        print(tst1)
        tst2 = run_python_file("calculator", "main.py", ["3 + 5"])
        print(tst2)
        tst3 = run_python_file("calculator", "tests.py")
        print(tst3)
        tst4 = run_python_file("calculator", "../main.py")
        print(tst4)
        tst5 = run_python_file("calculator", "nonexistent.py")
        print(tst5)


if __name__ == "__main__":
    unittest.main()
