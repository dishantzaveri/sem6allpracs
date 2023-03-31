import random
from tabulate import tabulate 
candidateList=['C1','C2','C3','C4','C5'] 
salary=25000
dict1={} 
dict1['C1']=55 
dict1['C2']=68 
dict1['C3']=90 
dict1['C4']=80 
dict1['C5']=50
skill_max=max(dict1['C1'],dict1['C2'],dict1['C3'],dict1['C4'],dict1['C5']) 
print(skill_max)
random.shuffle(candidateList)
print('Candidate interview Schedule:',candidateList)
print(tabulate({'Day':[1,2,3,4,5],'Candidate to be interviewed':candidateList},headers='keys',tablefmt='pretty'))
interview_cost=[] 
hiring_cost=[] 
interview=[] 
totalCost=0
prev_skill=dict1[candidateList[0]] # print(prev_skill) 
interview_cost.append(1) 
hiring_cost.append(0)
 

totalCost+=1 
interview.append(candidateList[0]) 
candidateList.pop(0)
# print(candidateList) 
count=0
if prev_skill!=skill_max:
   for i in candidateList:
# print(dict1[i])
    if dict1[i]>prev_skill:
        count+=1 
        interview_cost.append(1)
        hiring_cost.append((salary/30)*count) 
        totalCost+=(1+((salary/30)*count)) 
        interview.append(i) 
        prev_skill=dict1[i]
        if prev_skill==skill_max:
          break 
        count=0
    elif dict1[i]<prev_skill:
       count+=1 
    interview_cost.append(1) 
    hiring_cost.append('Not hired') 
    totalCost+=1 
    interview.append(i)
print(tabulate({'Interviewed Candidate':interview,'Interview Cost':interview_cost,'Hiring Cost':hiring_cost},headers='keys',tablefmt='pretty'))
 

print('Total Cost for this process:',totalCost)
