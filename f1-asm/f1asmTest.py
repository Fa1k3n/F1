import unittest

from f1asm import *

class TestF1Asm(unittest.TestCase):
    def testMvImm(self):
        asm = assembler()
        out = asm.decode_line("mv #2, r2")
        self.assertEqual(out, [2, 2, 2])
        out = asm.decode_line("mv r0, r1")
        self.assertEqual(out, [3, 0, 1])
        out = asm.decode_line("MV r0, R1")
        self.assertEqual(out, [3, 0, 1])

    def testComment(self):
        asm = assembler()
        out = asm.decode_line("; This is a comment and should be skipped")
        self.assertIsNone(out)
        out = asm.decode_line("      ; Leading whitespaces should be trimmed")
        self.assertIsNone(out)

    def testCompilerDirective(self):
        asm = assembler()
        out = asm.decode_line(".start $1a")
        self.assertIsNone(out)
        out = asm.decode_line("    .StaRt $1a")
        self.assertIsNone(out)

    def testUnknownMnemonicShouldThrowException(self):
        asm = assembler()
        with self.assertRaises(BadAsmException):
            out = asm.decode_line("out r0")

if __name__ == '__main__':
    unittest.main()
