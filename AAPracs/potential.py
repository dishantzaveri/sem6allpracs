class Potential:
    def __init__(self) -> None:
        self.stack=[]
        self.size = 0
    def push(self,item):
        Amortized_cost=0
        self.stack.append(item)
        Amortized_cost+=1+len(self.stack)-self.size
        self.size+=1
        return f"Amortized cost of insertion: {Amortized_cost}"
    def pop(self):
        Amortized_cost = 0
        self.stack.pop()
        Amortized_cost+= 1+len(self.stack)-self.size 
        self.size-=1
        return f"Amortized cost for deletion: {Amortized_cost}"
    def multipop(self,k):
        Amortized_cost = 0
        for i in range(k):
            self.pop()
        Amortized_cost+=k+len(self.stack)-self.size
        self.size-=k
        return f"Amortized cost for multipop: {Amortized_cost}"
# s=Potential()
# print(s.push(20))
# print(s.push(30))
# print(s.pop())
# s.push(40)
# s.push(39)
# print(s.multipop(2))

def potential(n):
    size=1
    icost=0
    dcost=0
    totalcost=0
    total=0

    print("Elements\tDoubling cost\tInsertion cost\tTotal cost")
    for i in range(1,n+1):
        icost=1
        if i>size:
            size*=2
            dcost=i-1
        totalcost=icost+dcost
        total+=totalcost
        print(i,"\t\t",dcost,"\t\t",icost,"\t\t",totalcost)
        dcost=0
        icost=0
        am=total/n
    return am

n=int(input("enter the number of elements"))
sc=potential(n)
