from tkinter import *
import tkinter.filedialog

class App:
    def __init__(self, master): # The main window 'root' is actually the 'master'
        main_window = Frame(master) # Make a frame and put it into the main window--'root' or aka, 'master'
        main_window.pack() # Display that frame into the window.
        
        Label(main_window, text='Choose the fasta file you want to count... ').grid(row=0, column=0, sticky=E)
        button_browse = Button(main_window, text='Browse', fg='blue', command=self.fa_seq_count) # First you create a widget.
        button_browse.grid(row=0, column=1, sticky=W) # Then you display it.
        
        Label(main_window, text='The number of sequences in this fasta file is ').grid(row=1, column=0, sticky=E)
        self.result_var = IntVar()
        Label(main_window, text=self.result_var.get(), fg='blue').grid(row=1, column=1, sticky=W)
        
    def fa_seq_count (self):
        with open (tkinter.filedialog.askopenfilename(), 'r') as file: # When you use this line to open a file, you don't need to write file.close ()
            line = file.read().splitlines() 
            name_list = line[0::2] # The 1st name appears on the 0th line, then it appears on every 2nd line.
            seq_list = line[1::2] # The 1st seq appears on the 1st line, then it appears on every 2nd line.

        name_seq = dict(zip(name_list, seq_list))
        
        length = str (len (name_seq))
        self.result_var.set(length) # Main window doesn't display the number!
        
        print (length)

    
root = Tk() # Make a blank window.
root.wm_title('Fasta Sequence Counter')
app = App(root)

status = Label (root, text="I'm busy at processing!", bd=1, relief=SUNKEN, anchor=W) # A static status bar.
status.pack(side=BOTTOM, fill=X)

root.mainloop() # Your window will continuously display unless you close it. The close button will end this loop.
