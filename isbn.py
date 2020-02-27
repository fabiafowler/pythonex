ISBN= input("What is the ISBN number? ")
#even#
sum2 = 0
for place in range(1,12,2):
    even= ISBN[place]
    sum1= int(even)*3
    sum2= sum2 + sum1
    
    
#odd#
sum4 = 0
for place in range(0,12,2):
    odd= ISBN[place] 
    sum3= int(odd)
    sum4= sum4 + sum3

#equation#
print(sum4)
print(sum2)
stage_1 = sum2 + sum4
stage_2 = stage_1%10
stage_3 = 10 - stage_2
print("the answer is ", stage_3)