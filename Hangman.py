import random
import pycountry

def getCountries():
    # Special characters present - whitespace, comma, apostrophe, fullstop
    countries = [c.name for c in pycountry.countries if " " not in c.name]
    return countries

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def replaceCorrectLetters(s, ch, pos):
    for i in range(len(pos)):
        s[pos[i]] = ch + ' '

def display(selectedCountry):
    length = len(selectedCountry)
    hangman = ['_ '] * length

    print('------------------------------------------------')
    print('----------------  HANGMAN GAME  ----------------')
    print('------------------------------------------------\n')

    print(''.join(hangman), end = '\n\n')

    numberOfTries = 5

    while "_ " in hangman:
        if numberOfTries == 0:
            break

        letter = (input('Guess a letter : ')).upper()

        pos = findOccurrences(selectedCountry, letter)

        # print(letter, pos)

        if len(pos) != 0:
            replaceCorrectLetters(hangman, letter, pos)
        else:
            numberOfTries -= 1
            print(numberOfTries)

        print()
        print(''.join(hangman), end = '\n\n')
    
    print('YOU WON !!!' if numberOfTries > 0 else 'GAME OVER !!! \n\nTHE CORRECT ANSWER IS {}.\n'.format(selectedCountry))

if __name__ == "__main__":
    countryList = getCountries()
    selectedCountry = (random.choice(countryList)).upper().replace('-','')
    display(selectedCountry)