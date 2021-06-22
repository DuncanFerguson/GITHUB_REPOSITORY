# Student: Duncan Ferguson
# Student Id: 871641260
# Final Project
# Date 6/8/2021
# Teacher: dalton.crutchfield@du.edu

"""This file is to run the end GUI. It sets up a gui utilizine folders.
UNfortunatly there is only one folder at the moment. """

import tkinter as tk
from tkinter import ttk
import Create_DB

class GUI(object):
    """This class launches the main GUI. There are tabs that can be set up. But ran out of time to add more"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Search New Accounts Loaded")
        self.tabcontrol = ttk.Notebook(self.root)
        self.tabcontrol.pack(expand=True)
        # Setting up Initial Folders
        self.folder_1 = folder(self.tabcontrol,
                               "Search By New Account",
                               "Account_Name",
                               Create_DB.DOA().getnewaccounts(),
                               "STR", "NMA","Land_Description")

        self.root.mainloop()


class folder(object):
    def __init__(self, tab, title, combo1_name, combolist1, treecol1, treecol2, treecol3):
        """ This folder creates a new tab on the GUI. Combo1name is the name of the search
        the treecols are to fill out the tree columns"""
        self.tabcontrol = tab
        self.title = title
        self.combo1_name = combo1_name
        self.combolist1 = combolist1  # This is the original combobox list
        self.selIndex = []

        # Creating a frame to be operated by tab control
        self.frame = ttk.Frame(self.tabcontrol, width=400, height=280)
        self.frame.pack(fill='both', expand=True)
        self.tabcontrol.add(self.frame, text=self.title)

        # Creating First Combobox Label
        self.label = ttk.Label(self.frame, text=self.combo1_name, width=25)
        self.label.grid(column=0, row=1, pady=2, padx=2)

        # Creating First Combobox Dropdown
        self.combo1 = ttk.Combobox(self.frame, width=25)
        self.combo1.grid(column=1, row=1, pady=2, padx=2)
        self.combo1['values'] = combolist1  # Grabbing list to display in combobox1
        self.combo1_select = self.combo1.bind("<<ComboboxSelected>>", self.CallBack)  # Adding in action

        # Creating Tree Display
        self.tree1 = ttk.Treeview(self.frame, columns=(treecol1, treecol2, treecol3), show='headings')
        self.tree1.heading(treecol1, text=treecol1)
        self.tree1.heading(treecol2, text=treecol2)
        self.tree1.heading(treecol3, text=treecol3)
        self.tree1.grid(columns=3, rows=3, pady=5, padx=5)
        return

    def CallBack(self,event):
        """This is running of the First Search. Then Populating the Tree with the Results"""
        self.selIndex = self.combolist1[event.widget.current()]

        # Clearing out results
        for i in self.tree1.get_children():
            self.tree1.delete(i)

        # Looking through the query and placing in the values
        for row in Create_DB.DOA().getnewaccountstr(self.selIndex):
            self.tree1.insert("", "end", values=[row[0], row[1], row[2]])


if __name__ == '__main__':
    mainfolder = GUI()