import itertools
import random

# This implementation uses a "matrix", instead of map (like python's dictionary), because the 
# default G-RAM implementation considers the use of a fixed, pre-allocated "memory".

class GRam:

    def __init__(self, address_width, spreading_distance, spreading_mode):
        self.address_width = address_width
        self.spreading_distance = spreading_distance 
        self.ram = [] 
        self.altered_addresses = []   # ...

        # 0: called by the user / 1: called after a pattern incertion
        self.spreading_mode = spreading_mode if spreading_mode in (0, 1) else 0 

        self.initialize_memory()

    def initialize_memory(self):
        for binary_set in itertools.product(["0", "1"], repeat = self.address_width):
            self.ram.append(["".join(binary_set), "n"])

    def insert(self, address, value):
        if len(address) != self.address_width or value not in (0, 1):
            print("Address or value invalid.")
            return 

        for i in range(len(self.ram)):
            if self.ram[i][0] == address:
                self.ram[i][1] = value

                if address not in self.altered_addresses:
                    self.altered_addresses.append(address)
                
                if self.spreading_mode == 1:
                    self.spread(address)

                break

    def retrieve(self, address):
        if len(address) != self.address_width:
            print("Address invalid.")
            return 

        for i in range(len(self.ram)):
            if self.ram[i][0] == address:
                if self.ram[i][1] == "n":
                    return random.getrandbits(1)
                else:
                    return self.ram[i][1]

    def spread(self, address = ""):
        if address != "" and len(address) != self.address_width:
            print("Address invalid.")
            return 

        # spreading phase
        if len(address) == self.address_width:
            # spread only a single address
            self.spread_value([address])
        else:
            # spread all non "u" addresses
            self.spread_value(self.altered_addresses)

    def spread_value(self, root_addresses = []):

        for line in self.ram:
            if line[0] in root_addresses:
                for candidate_to_change in self.ram:
                    if candidate_to_change[0] not in self.altered_addresses and self.hamming_distance(candidate_to_change[0], line[0]) <= self.spreading_distance:
                        if candidate_to_change[1] == "n":
                            candidate_to_change[1] = line[1]
                        elif candidate_to_change[1] != "n" and candidate_to_change[1] != line[1]:
                            candidate_to_change[1] = "n"


    # based on wikipedia's example, available at 
    # https://pt.wikipedia.org/wiki/Dist%C3%A2ncia_de_Hamming
    def hamming_distance(self, s1, s2):
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    def print_ram(self):
        for line in self.ram:
            print(line)

