word= "hello"
phrase = "hello hi hi hello"


def SEE1(word, phrase):
    
    word = word.lower()
    new_list = phrase.split()   
    number = len(new_list)
    print(number)
    
    for i in range(number+1):
        count=0
        if word in new_list():
            count+=1
        else:
            continue
    return count
