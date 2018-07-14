def convert_fq_to_fa ():
    import tkinter.filedialog # Open a file in a dialogue. This is easier than writing down the whole directory.
    import os 

    with open (tkinter.filedialog.askopenfilename(initialdir='C:/Users/louie/Desktop'), 'r') as file: # You can change the default initial directory.
        file_name = str(str(file.name).split('/')[-1]).split('.')[0] # This line works with askopenfilename () to get the file's name without extension name to be used as the new converted file'name--this keeps the converted file's name as the same as the original one's.

        line = file.read().splitlines() 
        name_list = line[0::4] # The 1st name appears on the 0th line, then it appears on every 4th line.
        seq_list = line[1::4] # The 1st seq appears on the 1st line, then it appears on every 4th line.

    if len (name_list) != len (seq_list):
        print (">>> The length of the name list and the sequence list don't match!")
    else: 
        fa_file = open('C:/Users/louie/Desktop/'+ file_name + '.fa', 'w')
        for i in range (int (len (name_list))): 
            fa_file.write(name_list [i].replace('@', '>') + '\n' + seq_list [i]+ '\n')
        fa_file.close ()
        print ('>>> Work is done!')
