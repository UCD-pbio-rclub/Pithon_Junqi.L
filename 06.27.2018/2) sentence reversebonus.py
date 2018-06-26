def sentence_reverse_2 (sentence):
    import time 
    start_time = time.time ()
    
    if not isinstance (sentence, str):
        raise TypeError ('Please input STRING only :(')
    
    final_punctuation = sentence [-1] # Obtain the punctuation.
    new_sentence = sentence [: -1] # Remove the punctuation.
    word_list = new_sentence.split (' ') # Used list here since order matters for lists.
    word_list.reverse ()
    
    x = 0
    new_sentence = ''
    while x < len (word_list):
        new_sentence = new_sentence + str (word_list [x]) + ' '
        x = x + 1
    new_sentence = (new_sentence [: -1] + final_punctuation).capitalize () #Remove the last space, add the punctuation, and capitalize the first letter.
    
    print ('Your program took', time.time () - start_time, 'seconds to run')
    return new_sentence
