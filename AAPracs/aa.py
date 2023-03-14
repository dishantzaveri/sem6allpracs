import math
class BinaryCounter:
    def _init_(self, n):
        self.bits = [0] * n
        self.potential = 0

    def increment(self):
        i = 0
        while i < len(self.bits) and self.bits[i] == 1:
            self.bits[i] = 0
            i += 1
        if i < len(self.bits):
            self.bits[i] = 1
        self.potential = sum(self.bits)
        self.display_table()

    def get_value(self):
        reverse_binary = ''.join(str(bit) for bit in self.bits)
        binary = ''.join(reversed(reverse_binary))
        return int(binary, 2)

    def display_table(self):
        value = self.get_value()
        reverse_binary = ''.join(str(bit) for bit in self.bits)
        binary = ''.join(reversed(reverse_binary))
        potential = self.potential
        print("Decimal\tBinary\tPotential")
        print(f"{value}\t{binary}\t {potential}\n")

n = int(input("Enter the increments: "))
counter = BinaryCounter(int(math.log(n,2))+1)
for i in range(n):
    counter.increment()