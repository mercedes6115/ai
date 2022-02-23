def search4vowels(word:str) -> set:  
    vowels = set('aeiou')
    return vowels.intersection(set(word))

'''
annotation 주석과 같은 개념 
'''

def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))


print(search4letters('hitch-hiker','asdwqrsdwq'))