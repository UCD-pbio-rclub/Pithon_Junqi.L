def play(): # My version. 
    import time 
    start_time = time.time ()
    
    import random
    words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
    global lives_remaining 
    lives_remaining = 14
    guessed_letters = ''
    correct_words = ''

    word = random.choice(words) # Python picks a word from the word list.
    while lives_remaining != 0:
        
        display_word = ''
        for letter in word:
            if guessed_letters.find(letter) > -1: # letter found
                display_word = display_word + letter
            else: # letter not found
                display_word = display_word + '-'
        print (display_word)
        
        print ('>>> Lives Remaining: ' + str(lives_remaining))
        guess = input('>>> Guess a letter or a whole word.')
        
        if len(guess) > 1: # Whole word guess 
            if guess == word: # Whole word guess is correct. 
                print('>>> You win! Well Done!')
                break 
            else: # Whole word guess is wrong.
                lives_remaining = lives_remaining - 1
                print ('>>> Your word is wrong!')
                 
        else: # Single letter guess
            guessed_letters = guessed_letters + guess
            if word.find (guess) == -1: # Single letter guess is wrong.
                lives_remaining = lives_remaining -1
                print ('>>> Your letter is wrong!')
                 
            else: # Single letter guess is correct.
                print ('>>> Your letter is correct!')
                correct_words = correct_words + guess 
                if correct_words == word: # All single letter guesses are correct.
                    print ('>>> You win! Well done!')
                    break 
                
    if lives_remaining == 0:
        print('>>> You are Hung!')
        print('>>> The word was: ' + word)

    print ('Your took', time.time () - start_time, 'seconds to guess the word.')
play ()
