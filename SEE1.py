word= "hello"
phrase = "hello hi hi hello"

def SEE1(word, phrase):
    word = word.lower()  
    word_list = phrase.lower()
    word_list.split()
    for i in range (len(word_list)):
        count = 0
        if word in word_list:
            answer = count + answer
        break
    return answer