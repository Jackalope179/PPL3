import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        input = """

        Class Program{
            Hello(){
                Return;
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,1))
