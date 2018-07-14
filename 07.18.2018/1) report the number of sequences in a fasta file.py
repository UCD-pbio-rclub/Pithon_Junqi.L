def fa_seq_count ():
    import tkinter.filedialog # Open a file in a dialogue. This is easier than writing down the whole directory.
    
    with open (tkinter.filedialog.askopenfilename(), 'r') as file: 
        line = file.read().splitlines() 
        name_list = line[0::2] # The 1st name appears on the 0th line, then it appears on every 2nd line.
        seq_list = line[1::2] # The 1st seq appears on the 1st line, then it appears on every 2nd line.

    name_seq = dict(zip(name_list, seq_list)) # I chose to make a dict for the ease of question 4
    # Actually question 4 asks to convert a fastq to fasta, so you don't have to make this dict.

    print ('>>> Your name-seq dictionary looks like: ')
    print (name_seq)
    print ('>>> The number of sequences in this fasta file is ' + str (len (name_seq)))
