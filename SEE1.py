word= "hello"
phrase = "hello hi hi hello"

def SEE1(word, phrase):
    word = word.lower()  
    word_list=[]
    sepwords = phrase.split(" ")
    word_list =[(sepwords)] 
    number_of_words = int(len(word_list))
    print(word_list)

    
    for i in range (number_of_words+1):
        count = 0
        if word in word_list:
            answer = count + answer
        break
    return answer

OR
word= "hello"
phrase = "hello hi hi hello"

def SEE1(word, phrase):
    
    word = word.lower()
    new_list = phrase.split()   
    number = len(new_list)

    
    for i in range(number+1):
        count=0
        if word in new_list():
            count+=1
        else:
            contine
    return count

    print(count)
