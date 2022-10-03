# The puzzle is a secret word randomly chosen from a list.
    # The player guesses a letter in the puzzle.
    # If the guess is correct, the letter is revealed.
    # If the guess is incorrect, a line is cut on the player's parachute.
    # If the puzzle is solved the game is over.
    # If the player has no more parachute the game is over.

import random

class game:
    letters = []
    answers = []
    misses = 0

    def start(self):
        self.letters.clear()
        self.answers.clear()
        self.misses=0
        words = ['car', 'hat', 'ball', 'electronic', 'gaming']
        plc = random.randint(1,len(words))
        self.word = words[1-plc]        
        play = input('Welcome to jumper! Do you want to play? y/n ')
        if play == "n":
            print('Good bye.')
            return
        while True:
            letter = input('Please enter a letter. ')
            self.check_answer(letter) 
            if self.misses == 5:
                print('You died! ')    
                return                   

    def check_answer(self,letter):
        self.letters.append(letter)
        if letter in self.word:
            self.answers.append(letter)
        else:
            self.misses = self.misses + 1
        self.letters.sort()
        self.answers.sort()
        self.print_jumper() 
        self.eval()

    def eval(self):
        print('\n')
        word_guessed = ''
        for i in self.word:
            if i in self.answers:
                    word_guessed = word_guessed + i
            else: 
                    word_guessed = word_guessed + '_'
        print(word_guessed)
        if "_" not in word_guessed:
            print('You win! ')    
            return   

    def print_jumper(self):
        print('\n')
        if self.misses < 1:
            print(' ____ ')
        if self.misses < 2:
            print('/    \ ')
        if self.misses < 3:    
            print(' ____ ')
        if self.misses < 4:
            print('\    /')
        if self.misses < 5:
            print(' \  /')
        if self.misses == 5:
            print('   X   ')
        else:
            print('   O   ')    
        print(' / | \ ')
        print('  / \ ')
        print('\n')
        print(f'correct answers: {self.answers}')
        print(f'Total guesses {self.letters}')




    
#end game for win.
#Pint word in order.

g = game()
g.start()
