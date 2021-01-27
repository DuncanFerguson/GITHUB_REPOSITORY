from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tax Roll Scrubber")
        # master.window(root, width=300, height=400)

        self.label = Label(master, text="Welcome to the Taxroll Scrubber\n"
                           "Would you like to proceed? \n")
        self.label.pack()

        self.greet_button = Button(master, text="Yes", command=self.greet)
        self.greet_button.pack()

        self.import_button = Button(master, text="Import File", command=self.importFile)
        self.import_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def importFile(self):
        print("Importing")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()