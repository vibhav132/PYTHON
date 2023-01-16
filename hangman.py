import random
def hangman():
    x = ['mango','apple','strawberry','grape','pineapple']
    word = x[random.randint(0,4)]
    wrong_guesses = 0
    stages =  [ "" , "________ " , "|  | " , "| 0" , "| /|\ " , "| / \ " , "| " ]
    letters_left = list(word)
    score_board = ['_']*len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages)-1:
        print('\n')
        guess = input("Guess a Letter")
        if guess in letters_left:
            char_index = letters_left.index(guess)
            score_board[char_index] = guess
            letters_left[char_index] = '#'
        else:
            wrong_guesses += 1
        print(" ".join(score_board))
        print('\n'.join(stages[0:wrong_guesses+1]))
        if '_' not in score_board:
            print("YOU WIN!THE WORD WAS")
            print( word)
            win = True
            break
    if not win:
        print("YOU LOSE!!")
        print("The word is {}".format(word))


hangman()

