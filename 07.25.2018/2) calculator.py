from tkinter import *

expression = "" # Globally declare the expression variable
 
def press(num): # Function to update expression in the text entry box
    global expression # Point out the global expression variable
   
    expression = expression + str(num) # Concatenation of string. This gives '98' when '9' and '8' are pressed orderly.
    equation.set(expression) # Update the expression by using set method.

def equalpress(): # Function to evaluate the final expression
    # Put that code inside the try block which may generate the error
    try: # Try and except statement is used for handling the errors like zero division error etc.
        global expression
        total = str(eval(expression)) # eval function evaluate the expression and str function convert the result into string
        equation.set(total)
        expression = ""
    except: # If error is generate then handle by the except block
        equation.set(" error ")
        expression = ""

def clear(): # Function to clear the contents of text entry box
    global expression
    expression = ""
    equation.set("")
    
if __name__ == "__main__":
    
    gui = Tk() # Create a GUI window
    gui.configure(background="white") # Set the background colour of GUI window.
    gui.title("Junqi's Calculator") # Set the title of GUI window.
    # gui.geometry("265x125") # Set the configuration of GUI window.
    
    equation = StringVar() # StringVar() is the variable class we create an instance of this class.
    expression_field = Entry(gui, textvariable=equation) # Create the text entry box for showing the expression.
 
    expression_field.grid(columnspan=4, ipadx=1)
 
    equation.set("Let's calculate!")
 

    button1 = Button(gui, text='1', fg='blue', bg='white',command=lambda: press(1), height=1, width=1)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='2', fg='blue', bg='white',command=lambda: press(2), height=1, width=1)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='3', fg='blue', bg='white',command=lambda: press(3), height=1, width=1)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text='4', fg='blue', bg='white',command=lambda: press(4), height=1, width=1)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='5', fg='blue', bg='white',command=lambda: press(5), height=1, width=1)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='6', fg='blue', bg='white',command=lambda: press(6), height=1, width=1)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text='7', fg='blue', bg='white',command=lambda: press(7), height=1, width=1)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='8', fg='blue', bg='white',command=lambda: press(8), height=1, width=1)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='9', fg='blue', bg='white',command=lambda: press(9), height=1, width=1)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text='0', fg='blue', bg='white',command=lambda: press(0), height=1, width=1)
    button0.grid(row=5, column=0)

    plus = Button(gui, text='+', fg='blue', bg='white',command=lambda: press("+"), height=1, width=1)
    plus.grid(row=2, column=3)

    minus = Button(gui, text='-', fg='blue', bg='white',command=lambda: press("-"), height=1, width=1)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text='×', fg='blue', bg='white',command=lambda: press("*"), height=1, width=1)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text='÷', fg='blue', bg='white',command=lambda: press("/"), height=1, width=1)
    divide.grid(row=5, column=3)

    equal = Button(gui, text='=', fg='blue', bg='white',command=equalpress, height=1, width=1)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='C', fg='blue', bg='white',command=clear, height=1, width=1)
    clear.grid(row=5, column='1')

    gui.mainloop()
