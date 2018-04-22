from GRam import GRam


gram = GRam(3, 1, 1)
gram.print_ram()
gram.insert("10", 1)
gram.insert("100", 1)
print("\n")
gram.print_ram()
gram.insert("111", 0)
print("\n")
gram.print_ram()

print("\n\n\n")

gram = GRam(5, 2, 0)
gram.insert("01000", 1)
gram.print_ram()
print("\n")
gram.insert("10101", 0)
gram.print_ram()
print("\n")
gram.spread()
gram.print_ram()
print("\n")

print(gram.retrieve("01000"))
print(gram.retrieve("00100"))
print(gram.retrieve("11101"))
