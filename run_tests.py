import unittest
'''
the file in /tests/homework/h_strings/tests_in_proc_out
has the test functions
'''
from tests.homework.b_in_proc_out import tests_in_proc_out
from tests.homework.h_strings import test_strings
suite = unittest.TestLoader().loadTestsFromModule(test_strings)

suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
unittest.TextTestRunner(verbosity=2).run(suite)

