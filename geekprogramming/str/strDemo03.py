word=input('plz input a word:')
if word[len(word)-3:len(word)]!='ing':
    word=word+'ing'
    print(word)
elif word[len(word)-3:len(word)]=='ing':
    word=word+'ly'
    print(word)
