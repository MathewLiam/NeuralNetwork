"""Entry point for the neural network application"""

from tkinter import Tk, Frame
from modules.network.network import network
from modules.ui.shared.menu_bar import menu_bar

class App(Frame):
    """Extension of the tkinter frame class

    Args:
        Frame ([tKinter.Frame]): Application frame
    """
    def __init__(self, master):
        super().__init__(master)
        self.pack()

def main():
    """runs the neural network application"""
    root = Tk()
    root.title("Neural Network")
    root.geometry("300x250")

    root.config(menu=menu_bar(root))

    myapp = App(root)
    _network = network(2, 10, 3, 1)
    myapp.mainloop()

if __name__ == "__main__":
    main()
