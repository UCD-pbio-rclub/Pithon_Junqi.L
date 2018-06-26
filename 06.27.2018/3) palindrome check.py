def palindrome_check ():
    import time 
    start_time = time.time ()
    
    string = input ('Please input your string here: ') # input () always gives string
    # Palindrome doesn't distinguish between letters and numbers.
    
    if len (string) <= 1:
        print ('Your string need to be longer than 2 letters for the check.')
    else: 
        string = string.lower () # Palindrome shouldn't be case-sensitive, while Python is case-sensitive when comparing items in a list.
        import re # Remove punctuations.
        string_no_punctuation = re.sub(r'[^\w\s]','',string)
        character_list = list ((string_no_punctuation).replace (' ', '')) # Remove spaces.
        
        def palindrome_judging (check_list): # You can also use character_list == character_list.reverse () to judge.
            palindrome_judge = True
            if len (check_list) % 2 == 0: # The number of characters is even.
                for x in range (0, int (len (check_list)/2)):
                    if check_list [x] != check_list [len (check_list) - 1 - x]:
                        palindrome_judge = False
            else: # The number of characters is odd.
                for x in range (0, int ((len (check_list) - 1) / 2)):
                    if check_list [x] != check_list [len (check_list) - 1 - x]:
                        palindrome_judge = False
            return palindrome_judge

        if string.find (' ') < 0: # string.find (' ') is -1 if there's no space at all
            print ('Your string is a word.') 
        else: # The string has space int it.
            print ('Your string is a sentence.')
        result = palindrome_judging (character_list)
    
        if result == True:
            print ('Your string is a palindrome.')
        else: 
            print ('Your string is NOT a palindrome.')
        
    print ('Your program took', time.time () - start_time, 'seconds to run')
