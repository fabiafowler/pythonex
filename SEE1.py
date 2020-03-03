word= "hello"
phrase = "hello hi hi hello"

def SEE1(word, phrase):
    word = word.lower()  
    word_list = phrase.split(" ")
    number_of_words = len(word_list)
    print(word_list)

    
    for i in range (number_of_words):
        count = 0
        if word in word_list:
            answer = count + answer
        break
    return answer