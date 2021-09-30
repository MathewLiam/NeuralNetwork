from tkinter import Tk, Frame, Menu
from Modules.UI.Shared import MenuBar
from Modules.Network import Network

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

def main():
    """root = Tk()
    root.title("Neural Network")
    root.geometry("300x250")
    
    root.config(menu=MenuBar(root))

    myapp = App(root)
    myapp.mainloop()"""
    network = Network.Network(2, 10, 3, 1)
    while True:
        input1 = float(input("Val 1: "))
        input2 = float(input("Val 2: "))
        network.feed_forward([input1, input2])

if __name__ == "__main__":
    main()