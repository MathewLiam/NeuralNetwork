from tkinter import Tk, Frame
from modules.network import Network
from modules.ui.shared import MenuBar

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

def main():
    root = Tk()
    root.title("Neural Network")
    root.geometry("300x250")
    
    root.config(menu=MenuBar.MenuBar(root))
    
    myapp = App(root)
    network = Network.Network(2, 10, 3, 1)
    myapp.mainloop()

if __name__ == "__main__":
    main()