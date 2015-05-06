
class BadAsmException(Exception):
    pass

class Expression:
    def __init__(self):
        self.toks = []

    def consume(self, op):
        self.toks.append(op)

    def encode(self):
        ret_val = []
        for tok in self.toks:
            ret_val.append(tok.encode())
        return ret_val

class Mnemonic:
    op_codes = {
        "ld": 0,
        "st": 1,
        "mv_imm": 2,
        "mv_reg": 3,
        "br": 4
    }
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic

    def encode(self):
        op_code = None
        try:
            op_code = Mnemonic.op_codes[self.mnemonic]
        except KeyError:
            raise BadAsmException("Unknown mnemonic: ", self.mnemonic)
        return op_code

    def __str__(self):
        return self.mnemonic

class Operand:
    def encode(self):
        return None

    def __str__(self):
        return ""

class Register(Operand):
    def __init__(self, reg_name):
        if reg_name[0].lower() != 'r':
            raise BadAsmException("Bad formatted register name", reg_name)
        self.reg_name = reg_name[1:]

    def encode(self):
        return int(self.reg_name)

    def __str__(self):
        return "r" + self.reg_name

class Immediate(Operand):
    def __init__(self, imm_name):
        if imm_name[0] != "#":
            raise BadAsmException("Bad formatted immediate", imm_name)
        self.imm_val = int(imm_name[1:])

    def encode(self):
        return self.imm_val

    def __str__(self):
        return "#" + str(self.imm_val)

class assembler:
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
        return Mnemonic(mnemonic).encode()

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

        expr = Expression()

        for tok in toks:
            op = None
            try:
                op = Mnemonic(tok)
            except BadAsmException:
                pass
            else:
                expr.consume(op)
                continue

            try:
                op = Register(tok)
            except BadAsmException:
                pass
            else:
                # Handle it as a register
                expr.consume(op)
                continue

            try:
                op = Immediate(tok)
            except BadAsmException:
                pass
            else:
                # Handle it as an immediate
                continue

            raise BadAsmException("Unknown token", tok)

        return expr.encode()

