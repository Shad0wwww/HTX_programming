import random;

word_list = ["python", "java"]

class Hangman:
    guess = 10
    correctWord = random.choice(word_list)
    disguisedWord = len(correctWord) * "_"
    
    def addLetterToDisguisedWord(index: int, guessedLetter: str) -> str:
    
        for i in range(len(Hangman.correctWord)):
            if i == index:
                Hangman.disguisedWord = Hangman.disguisedWord[:i] + guessedLetter + Hangman.disguisedWord[i+1:]
        Hangman.checkIfWordIsGuessed()
        return Hangman.disguisedWord
    
    def resetGame() -> None:
        Hangman.guess = 10
        Hangman.correctWord = random.choice(word_list)
        hangman(True)

    def checkIfWordIsGuessed() -> None:
        if Hangman.disguisedWord == Hangman.correctWord:
            print("______________________________")
            print("")
            print("Congratulations! You guessed the word", Hangman.correctWord)
            print("Do you want to play again? (yes/no)")
            print("______________________________")
            answer = input()
            if answer == "yes":
                Hangman.resetGame()
                return
            else:
                exit(0)

    def guessLetter(guessedLetter: str) -> None:
        
        if Hangman.guess <= 0:
            print("You have no more guesses left. The word was", Hangman.correctWord)
            return

        for i in range(len(Hangman.correctWord)):

            if Hangman.correctWord[i] == guessedLetter:
                print(Hangman.addLetterToDisguisedWord(i, guessedLetter))
                hangman(False)
                return
               
        Hangman.guess -= 1
        print("You have", Hangman.guess, "guesses left.")
        hangman(False)
        return
            
def startGameDetails() -> None: 
    print("Try to guess this word:")
    print(Hangman.disguisedWord)
    print("You have", Hangman.guess, "guesses left.")
    
def hangman(firstTime: bool) -> None:
    if firstTime:
        startGameDetails()
    letter = input("Enter a letter: ")

    if len(letter) > 1:
        print("Please enter only one letter.")
        hangman(False)

    if letter not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a letter.")
        hangman(False)

    Hangman.guessLetter(letter)
    
if __name__ == "__main__":
    print("Welcome to Hangman!")
    hangman(True)