
class BadAsmException(Exception):
    pass

class assembler:
    op_codes = {
        "ld": 0,
        "st": 1,
        "mv_imm": 2,
        "mv_reg": 3,
        "br": 4
        ""
    }

    def tokenize(self, line):
        line = line.replace(",", "")
        return line.split()

    def decode_imm(self, imm_str):
        if imm_str[0] != "#":
            raise Exception

        return int(imm_str[1:])

    def decode_reg(self, reg_str):
        return int(reg_str[1:])

    def decode_mnemonic(self, mnemonic):
        op_code = None
        try:
            op_code = assembler.op_codes[mnemonic]
        except KeyError:
            raise BadAsmException("Unknown mnemonic", mnemonic)
        return op_code

    def is_comment(self, line):
        return line[0] == ";"

    def is_compiler_directive(self, line):
        return line[0] == "."

    def prepare_line(self, line):
        line = line.lower()
        return line.lstrip()

    def decode_line(self, line):
        line = self.prepare_line(line)
        if self.is_comment(line):
            return None
        if self.is_compiler_directive(line):
            return None
        toks = self.tokenize(line)
        if len(toks) > 2:
            (mnemonic, arg1, arg2) = toks
        else:
            (mnemonic, arg1) = toks
            arg2 = ""
        if mnemonic == "mv":
            try:
                arg1 = self.decode_imm(arg1)
                mnemonic += "_imm"
            except Exception:
                arg1 = self.decode_reg(arg1)
                mnemonic += "_reg"
            arg2 = self.decode_reg(arg2)
        op_code = self.decode_mnemonic(mnemonic)

        return [op_code, arg1, arg2]

