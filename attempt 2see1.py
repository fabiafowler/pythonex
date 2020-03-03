phrase = "hello hi hi hello"
word = "hello"

def see1(word, phrase):
    count = 0
    word = word.strip()
    list = phrase.split()
    
    for i in range(len(list)):
        if word == i:
            count+=1
            continue
        else:
            continue
        return count
