def vowel_or_consonant(character):
    ch = character.lower()
    for i in range(0,len(character)):
        if ch[i] == 'a' or ch[i] == 'e' or ch[i] == "i" or ch[i] == "o" or ch == "u":
            print(f"Character {character} is a vowel")
        
        else:
            print(f"Character {character} is a consonant")
    return None

if __name__ == "__main__":
    vowel_or_consonant("b")