import Tkinter

def unableErr():
    root = Tkinter.Tk()
    frame = Tkinter.Frame(root)
    errorMsg = Tkinter.Label(root, text="Error: You can't do that!")
    errorMsg.pack()
    quitButton = Tkinter.Button(frame, text="OK", command=quit)
    quitButton.pack()
    frame.pack()
    root.title("Error")
    root.mainloop()
def clearEntry(userInput):
    userinput.Entry.Delete(0, 'end')


#unableErr()
