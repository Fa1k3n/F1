import unittest

from f1asm import *

class TestF1AsmC(unittest.TestCase):
    def testMvImm(self):
        asm = assembler()
        asm.decode_line("mv #2, r2")


if __name__ == '__main__':
    unittest.main()
