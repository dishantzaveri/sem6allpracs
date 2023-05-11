class AggregateStack:
    def __init__(self):
        self.stack=[]
        self.cost=0
    def push(self,item):
        self.stack.append(item)
        self.cost+=1
        self.printstack()
    def pop(self):
        self.stack.pop()
        self.cost+=1
        self.printstack()
    def multipop(self,k):
        for i in range(k):
            self.pop()
    def printstack(self):
        print(self.stack,"\n")
# s=AggregateStack()
# s.push(10)
# s.push(10)
# s.push(10)
# s.push(10)
# s.multipop(2)    

def aggregate_dynamic(n):
    size=1
    icost=0
    dcost=0
    totalcost=0
    total=0

    print("Element\tDoubling Cost\tInsertion cost\tTotal cost")
    for i in range(1,n+1):
        icost=1
        if i > size:
            size*=2
            dcost=i-1
        totalcost=dcost+icost
        total=total+totalcost
        print(i,"\t\t",dcost,"\t\t",icost,"\t\t",totalcost,"")
        icost=0
        dcost=0
    return total/n

n=int(input("Enter the number of elemnets: "))
print("Aggregate method")
a=aggregate_dynamic(n)
print("Amortized cost= ",a)

