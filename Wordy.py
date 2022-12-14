from random_word import RandomWords

def generateWord():
    # Return a single random word
    word = RandomWords().get_random_word().upper()
    print(word)
    return word
    # return RandomWords().get_random_word().upper()

def checkLetter(selectedWord, letter):
    pos = selectedWord.find(letter)
    if pos == -1:
        return

def helper():
    letterStatus = ['\u2705', '\u274C', '\u2795']
    print(letterStatus)

def display(selectedWord):
    length = len(selectedWord)
    wordy = ['_ '] * length
    numberOfTries = 5

    print('------------------------------------------------')
    print('----------------   WORDY GAME   ----------------')
    print('------------------------------------------------\n')

    print(''.join(wordy), end = '\n\n')

    helper()

    while numberOfTries > 0:
        guess = (input('Guess the word : ')).upper()

        if guess == selectedWord:
            print('***')
            break

        print()
        print(''.join(wordy), end = '\n\n')
    
    print('YOU WON !!!' if numberOfTries > 0 else 'GAME OVER !!! \n\nTHE CORRECT ANSWER IS {}.\n'.format(selectedWord))


if __name__ == '__main__':
    selectedWord = generateWord()
    display(selectedWord)

    word = "mississippi"
    print(word.find("i"))
    print(word.find("a"))