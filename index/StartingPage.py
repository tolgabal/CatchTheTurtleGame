import tkinter
from MainGame import MainGame

"""if __name__ == "__main__":
    MainGame(10)"""
    
class StartingPage:
    
    def __init__(self):
        self.startingScreen = tkinter.Tk()
        self.startingScreen.title("Catch The Turtle")
        self.startingScreen.minsize(250,150)
        self.TryLabel = tkinter.Label(text="Please enter the game counter value:")
        self.TryLabel.pack()
        self.timeEntry = tkinter.Entry(self.startingScreen)
        self.timeEntry.pack()
        self.startButton = tkinter.Button(text="Start" , command=self.startGame)
        self.startButton.pack()
        
        self.startingScreen.mainloop()
    
    
    def startGame(self):
        entryVal = self.timeEntry.get()
        self.startingScreen.destroy()
        MainGame(int(entryVal))

    
if __name__ == "__main__":
    StartingPage()
    