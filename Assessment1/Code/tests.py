def four(arg1):

    list1 = arg1.split()
    num1 = list1[0]
    num2 = list1[1]
    num3 = list1[2]

    sum1 = 0
    sum2 = 0
    sum3 = 0

#to get 1st number
    for i in range(len(num1)):
        sum1 = sum1 + int(num1[i])

    for i in range(len(num2)):
        sum2 = sum2 + int(num2[i])

    for i in range(len(num3)):
        sum3 = sum3 + int(num3[i])



if (answer1 > answer2) and (answer1 > answer3):
    return answer1
elif (answer2 > answer3) and (answer2 > answer1):
    return answer2
elif (answer3 > answer2) and (answer3 > answer1):
    return ""

four("15 72 80 164") == 11

