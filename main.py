import tkinter as tk
from model.database import Database
from controller.cow_controller import CowController
from view.cow_gui import CowGUI

def main():
    root = tk.Tk()
    db = Database('data.json')  # Adjust the path to your data file
    controller = CowController(db)
    gui = CowGUI(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
