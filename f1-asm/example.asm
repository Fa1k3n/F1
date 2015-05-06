; Comment starts with semicolon

; A compiler directive starts with a .
.alias OUTPUT R0
.start 0x10

; A label has text followed by colon
; labels can contain all alpha chars, big and small
a_label:

; An assembler directive is of the type, [label:] mnemonic op1|label|alias [, <op2>]
mv R0, R1

; Immediate numbers starts with hash # followed by a four bit
; number in hexadecimal (0-F)
mv #8, R1

; Addresses starts with $ followed by two four bit hexadecimal
; numbers
ld $2a, R1

; For branching and jumps it is possible to use both labels and
; direct addresses, i.e. both these statements are valid
jmp a_label
jmp $2a

; A block is a segment of code that can be relocated in memory
; but not split
.block NAME

; Each program must have a MAIN/main block, this will be
; located at address 0 after linking
.block main

