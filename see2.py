word= "hello"
phrase = "hello hi hi hello"

def SEE1(word, phrase):
    
    word = word.lower()
    new_list = phrase.split()   
    number = len(new_list)

    count = 0
    for i in range(number):
        if word == new_list[i]:
            count+=1
    return count

print(SEE1(word, phrase))