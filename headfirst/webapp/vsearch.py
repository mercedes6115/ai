def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))
