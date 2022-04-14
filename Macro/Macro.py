import keyboard
import tkinter as tk
import threading
import time

InputedKey = "space"
WaitTime = 0.05
Active = False

def CheckforActivation():
    global Active     
    
    while True:
        keyboard.wait('f5')
        Active = not Active
        
        if Active == True and InputedKey != "":
            T1 = threading.Thread(target=Run)
            T1.daemon = True
            T1.start()

def Run():
    while Active == True:
        keyboard.press_and_release(InputedKey)
        time.sleep(WaitTime)

class MyTkApp():
    def __init__(self):

        def SetKey(event):
            global InputedKey
            InputedKey = KeyInput.get()

        def SetWait(event):
            global WaitTime            
            WaitTime = int(WaitInput.get())
            
        self.root = tk.Tk()
        self.root.title('Macro')
        self.root.geometry("600x150")

        Label = tk.Label(self.root, text="Wanted Key Name: ", font=('Helvatical bold',18))
        Label.place(x = 5, y = 10,)

        WaitLabel = tk.Label(self.root, text="Delay between each press (s): ", font=('Helvatical bold',18))
        WaitLabel.place(x = 5, y = 55,)

        InstructLabel = tk.Label(self.root, text="Key to activate/deactivate: F5", font=('Helvatical bold',18))
        InstructLabel.place(x = 5, y = 100,)

        KeyInput = tk.Entry(self.root, font=('Helvatical bold',14))
        KeyInput.grid(row=0, column=1)
        KeyInput.bind('<Return>', SetKey)
        KeyInput.insert(0, "space")
        
        WaitInput = tk.Entry(self.root, font=('Helvatical bold',14))
        WaitInput.grid(row=0, column=1)
        WaitInput.bind('<Return>', SetWait)
        WaitInput.insert(0, 0.05)
        
        KeyInput.place(x = 225,
                y = 14,
                width=200,
                height=25)
        
        WaitInput.place(x = 340,
                y = 60,
                width=200,
                height=25)
        
        self.root.mainloop()


T2 = threading.Thread(target=CheckforActivation)
T2.daemon = True
T2.start()

app = MyTkApp()
