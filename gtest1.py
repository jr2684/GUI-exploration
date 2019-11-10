# this code is purely to figure out how the hell TKinter works/ works with user input.
# Mainly going to focus on how to turn button presses in GUI into on/off loop control
# Also going to try and figure out how to read numeric values from GUI

#following code sets up window geometry

from tkinter import*   #imports all tkinter commands into script. Bulky, but doing it for readibility  

class App:      #creates a new class 

    def __init__(self,master):  #defines a function with variables self and master
        self.start = IntVar()
        self.start = 0
        
        bigwin = Frame(master)
        bigwin.pack()

        self.button = Button(bigwin, text="QUIT", fg='red', command=bigwin.quit)
        self.button.pack(side=LEFT)
        
        self.hi_there = Button(bigwin, text="Hello", fg='green', command=self.say_hi)
        self.hi_there.pack(side=LEFT)
        
        self.num = Button(bigwin, text="press this to make start increase by 1", fg='green', command=self.number1)
        self.num.pack(side=RIGHT)
        
        self.num2 = Button(bigwin, text="press this to make start increase by 2", fg='green', command=self.number2)
        self.num2.pack(side=RIGHT)

        self.num5 = Button(bigwin, text="write the value of number to file", fg='blue', command=self.write_variable)
        self.num5.pack(side=RIGHT)
        
        self.snum = Button(bigwin, text="press this to see what number start is", fg='blue', command=self.snumber)
        self.snum.pack(side=RIGHT)
        
        
    
    def say_hi(self):
        print( "hi there everyone!")
        
    def number1(self):
        print( "1")
        self.start = self.start + 1 

    def number2(self):
        print( "2")
        self.start = self.start + 2

    def snumber(self):
        print( "start is equal to the value:",self.start)
        
    def write_variable(self):
        file = open('text.txt','w')
        file.write(str(self.start))
        file.close()
        
       
gui_test = Tk()   #creates GUI window enviroment

app = App(gui_test)

#while app.start == 0:
#    print("GOOP")

gui_test.mainloop()   #makes window run indefinitely
gui_test.destroy()   #closes window once quit is pressed
