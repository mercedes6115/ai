def search4vowels(word:str) -> set:  
    vowels = set('aeiou')
    return vowels.intersection(set(word))

'''
annotation 주석과 같은 개념 
'''
print(search4vowels('hitch-hiker'))