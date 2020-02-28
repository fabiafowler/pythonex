def Find_your_grade():
        
    homework= int(input("what was your homework score /25? "))
    assessment = int(input("what was your assessment score /50? "))
    final_exam =int(input("what was your final exam score /100? "))

    if homework <= 10: 
        print("you failed")
        average_score = int(homework*3 + assessment*4 + final_exam) /3

        return "Unfortunately, you needed to pass all modules to get a grade"
            
    elif assessment <= 25: 
        print("you failed")
        average_score = int(homework*3 + assessment*4 + final_exam) /3
        return "Unfortunately, you needed to pass all modules to get a grade"

    elif final_exam <= 50: 
        print("you failed")
        average_score = int(homework*3 + assessment*4 + final_exam) /3
        return "Unfortunately, you needed to pass all modules to get a grade"

    else:
        average_score = int(homework*3 + assessment*4 + final_exam) /3
    
    return average_score
    
name= input("what is your full name? ")  

print("hello ", name, "your average is ", Find_your_grade(), "%")    
    