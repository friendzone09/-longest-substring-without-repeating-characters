text = input('Introduce un texto: ')

def checktext(text):   
    
    letters = list(text)
    newTextArray = []
    newText = ''
    
    for letter in letters:
        if letter not in newTextArray:
            newTextArray.append(letter)
    
    for letter in newTextArray:
        newText += letter
        
    print(len(newTextArray))
    
    print(f'The answer is "{newText}" with the length of {len(newTextArray)}')
    
checktext(text)