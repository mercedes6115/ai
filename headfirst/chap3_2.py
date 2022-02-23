vowels = ['a','e','i','o','u']
word = input('Provide a word to search for vowels: ')
found = {} # 딕셔너리 키 값은 반드시 초기화 시켜줘야한다 
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0) # 딕셔너리 초기화함수
        found[letter] +=1
for k,v in sorted (found.items()):
        print(k, 'was found',v,'time(s)')