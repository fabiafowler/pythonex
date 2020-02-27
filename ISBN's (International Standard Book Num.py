ISBN's (International Standard Book Numbers) are identifiers for books. 

The ISBN is a thirteen-digit code.

The last digit is a check number calculated as follows:
•	The first 12 digits are taken
•	Starting at index 1, if the index is odd - add it, and if the index is even – multiply the digit by three then add it.
•	From the sum find the remainder after dividing by 10.
•	10 minus the remainder give us the check digit
•	In other words the following algebra would give us the check digit:
( 10 – (( x1 + 3x2 + x3 + 3x4 + x5 + 3x6 + x7 + 3x8 + x9 + 3x10 + x11 + 3x12 ) % 10))

For ISBN: 978-0-306-40615-? The following check would happen:
•	9 +  3*7 +   8 +   3*0 +   3 +   3*0 +   6 +  3*4 +   0 +  3*6 + 1 +  3*5 = 93
•	93 / 10 =

a = input int("what is the 1st digit?)
b = input int("what is the 2nd digit?)
c = input int("what is the 3rd digit?)
d = input int("what is the 4th digit?)
e = input int("what is the 5th digit?)
f = input int("what is the 6th digit?)
g = input int("what is the 7th digit?)
h = input int("what is the 8th digit?)
i = input int("what is the 9th digit?)
j = input int("what is the 10th digit?)
k = input int("what is the 11th digit?)
l = input int("what is the 12th digit?)

result_1 = a + (3*b) + c +(3*d) + e + 3*f + g + 3*h + i + 3*j

ISBN= int(input("What is the ISBN number?"))
#even#
    for place in range(0,12,2):
    ISBN[place]
    sum1= int(ISBN[place])*3
    sum2= (ISBN[place]+) + sum1
    
    
#odd#
    for place in range(1,100,2):
    ISBN[place] 
    sum3= int(ISBN[place])
    sum4= SBN[place] + sum3

#equation#
    stage_1 = sum_2 + sum_4
    stage_2 = stage_2/10
    stage_3 = 10 - stage_2
    print("the answer is " stage_3)