# Accounting method
# Dynamic Tables
def accounting(n):
    size=1
    total=0
    dcost=0
    icost=0
    bank=0
    print("Elements\tDoubling Copying Cost\tInsertion Cost\tTotal Cost\t\tBank") 
    for i in range(1,n+1):
        icost=1 
        if i>size:
            size*=2
            dcost=i-1
        total=icost+dcost
        bank+=(3-total) 
        print(i,"\t\t\t\t",dcost,"\t\t",icost,"\t",total,"\t\t\t",bank) 
        icost=0
        dcost=0
# n=int(input("Enter number of elements:")) 
# print("Accounting method") 
# accounting(n) 

class AccountingStack:
    def __init__(self):
        self.stack=[]
        self.cost=0
        self.balance=0
    def push(self,item):
        self.stack.append(item)
        self.cost+=1
        self.balance+=1
        self.printstack()

    def pop(self):
        self.stack.pop()
        self.cost+=1
        self.balance-=1
        self.printstack()

    def multipop(self,k):
        for i in range(k):
            self.pop()

    def printstack(self):
        print(self.stack,"\nBalance",self.balance,"\n")

s=AccountingStack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.printstack()
s.multipop(2)

print("Amortized cost= ",s.cost/6)
