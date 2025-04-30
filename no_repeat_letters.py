text = 'abcabcbb'

def checktext(text):   
    
    letters = list(text)
    newTextArray = []
    newText = ''
    
    for letter in letters:
        if letter not in newTextArray:
            newTextArray.append(letter)
            
    

checktext(text)