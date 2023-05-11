class DynamicTable:
    def __init__(self, capacity=1):
        self.table = [0] * capacity
        self.size = 0
        self.capacity = capacity
    def add(self, element):
        if self.size == self.capacity:
#Double the capacity of the table if it is full
            new_table = [0] * (self.capacity * 2)
            for i in range(self.size):
                new_table[i] = self.table[i]
            self.table = new_table
            self.capacity *= 2
        self.table[self.size] = element
        self.size += 1
       
    def size(self):
        return self.size
    def capacity(self):
        return self.capacity
def potential(table):
    return 2*table.size - table.capacity
def cost(table, operation):
#Calculate the amortized cost of the operation
    if operation == "add":
       
        if table.size == table.capacity:

#Double the table
            return potential(table) + 1
        else:
            return 1
    else:
        raise Exception("Invalid operation")
       
table = DynamicTable()
total_cost = 0
operation_cost = 1
operation_cos = 1
prev = 0
print("Item No.\tTable Size\tPotential\tOperation Cost\tTotal Cost\tAmortized Cost")
for i in range(1, 18):
    operation_cost = cost(table, "add")
    total_cost += operation_cost
    table.add(i)
#print("=" * 8)
    pot = potential(table)
    amortized_cost = operation_cost + (pot - prev)
    prev = pot
#print(amortized_cost)
    print(f"{i}\t\t {table.capacity}\t\t {potential(table)}\t\t{operation_cos}\t\t {operation_cost}\t\t {amortized_cost}")