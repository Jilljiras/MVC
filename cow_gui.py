import tkinter as tk
from controller.cow_controller import CowController

class CowGUI:
    def __init__(self, master, controller: CowController):
        self.master = master
        self.controller = controller
        self.master.title("Cow Management")

        self.cow_id_label = tk.Label(master, text="Cow ID:")
        self.cow_id_label.pack()
        self.cow_id_entry = tk.Entry(master)
        self.cow_id_entry.pack()

        self.milk_button = tk.Button(master, text="Milk Cow", command=self.milk_cow)
        self.milk_button.pack()

        self.reset_button = tk.Button(master, text="Reset Cow", command=self.reset_cow)
        self.reset_button.pack()

        self.report_button = tk.Button(master, text="Show Report", command=self.show_report)
        self.report_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.milk_lemon_button = tk.Button(master, text="Add Lemon (for white cows)", command=self.add_lemon, state=tk.DISABLED)
        self.milk_lemon_button.pack()

    def milk_cow(self):
        cow_id = self.cow_id_entry.get()
        if not cow_id.isdigit() or len(cow_id) != 8 or cow_id.startswith('0'):
            self.result_label.config(text="Invalid cow ID")
            return

        result = self.controller.milk_cow(int(cow_id))
        if "BSOD" in result:
            self.milk_lemon_button.config(state=tk.DISABLED)
        else:
            self.milk_lemon_button.config(state=tk.NORMAL)

        self.result_label.config(text=result)

    def reset_cow(self):
        cow_id = self.cow_id_entry.get()
        if not cow_id.isdigit() or len(cow_id) != 8 or cow_id.startswith('0'):
            self.result_label.config(text="Invalid cow ID")
            return

        result = self.controller.reset_cow(int(cow_id))
        self.result_label.config(text=result)

    def add_lemon(self):
        cow_id = self.cow_id_entry.get()
        cow = self.controller.db.get_cow(int(cow_id))
        if cow and cow.breed == "white":
            cow.is_bsod = False  # Reset BSOD status
            self.controller.db.add_cow(cow)
            self.result_label.config(text="Lemon added. Milk will be sour.")
        else:
            self.result_label.config(text="Lemon can only be added to white cows.")

    def show_report(self):
        report = self.controller.report()
        milk_counts = report["milk_counts"]
        total_milk = report["total_milk"]
        report_text = (f"Plain milk: {milk_counts['Plain milk']} bottles\n"
                       f"Chocolate milk: {milk_counts['Chocolate milk']} bottles\n"
                       f"Sour milk: {milk_counts['Soy milk']} bottles\n"
                       f"Total milk: {total_milk} bottles")
        self.result_label.config(text=report_text)
