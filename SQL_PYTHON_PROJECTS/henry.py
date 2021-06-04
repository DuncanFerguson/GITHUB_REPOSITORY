# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3421; HW1 Henry
# Date: 4/28/2021
# Teacher: dalton.crutchfield@du.edu

"""This is the GUI for henrys book Store. The imports are all explained in the file they are getting imported from. But
essentially each one returns a list to be display in the various comboboxes.

The GUI object creates a frame and contains folders using the tkinter notebook.
You can add as many folders as you would liked but they must take a specific order of operations.
First, tabcontrol, then Tab str(name), str(comboboxname1), then combobox1 list query,
 followed by combobox2 query list lastly,
 is the tree value that currently displays branch name and on hand.
 That returns a third value for the price to be lazily displayed in lable4.

 The Folders lay out a creation that follows much of above but includes a baked in book title and tree headers
 This is because these dont change for the assignment, but could later be moved there are two call back functions
 that fire off when the comboboxs are selected. There is some duplication in clearing the boxes just to ensure
 users could not get wrong values."""

from henryDOA import Author
from henryDOA import Book_by_Author
from henryDOA import Publisher
from henryDOA import Book_by_Publisher
from henryDOA import Category
from henryDOA import Book_by_Category
from henryDOA import Books_Available


import tkinter as tk
from tkinter import ttk


class GUI(object):
    """This class launches the main GUI. There are three folders/tabs. Those point to the different
    searches. In those folders, HenrySBA, HenrySBP, and HenrySBC there are two combo boxes. Then a tree with
    information on where the book is available."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Henry's Bookstore")
        self.tabcontrol = ttk.Notebook(self.root)
        self.tabcontrol.pack(expand=True)

        # Setting up Initial Folders
        self.folder_1 = folder(self.tabcontrol,
                               "Search By Author",
                               "Author Name: ",
                               Author(),
                               Book_by_Author(),
                               Books_Available())

        self.folder_2 = folder(self.tabcontrol,
                               "Search By Publisher",
                               "Publisher: ",
                               Publisher(),
                               Book_by_Publisher(),
                               Books_Available())

        self.folder_3 = folder(self.tabcontrol,
                               "Search By Category",
                               "Category: ",
                               Category(),
                               Book_by_Category(),
                               Books_Available())


        self.root.mainloop()


class folder(object):
    def __init__(self, tab, title, combo1_name, combolist1, combolist2, combotree):
        """ This folder creates a new tab on the GUI. Values that are taken in
        are a tab for control, the title of the tab, QUERRY list return 1, QUERRY list return 2,
        QUERRY list return 3"""
        self.tabcontrol = tab
        self.title = title
        self.combo1_name = combo1_name
        self.combolist1 = combolist1  # This is the original combobox list
        self.combolist2 = combolist2  # This takes in query looking book titles
        self.combotree = combotree  # This is a query looking for a list of a list with tree info
        self.selIndex = []

        # Creating a frame to be operated by tab control
        self.frame = ttk.Frame(self.tabcontrol, width=400, height=280)
        self.frame.pack(fill='both', expand=True)
        self.tabcontrol.add(self.frame, text=self.title)

        # Creating First Combobox Label
        self.label = ttk.Label(self.frame, text=self.combo1_name, width=25)
        self.label.grid(column=0, row=1, pady=2, padx=2)

        # Creating Second Combobox Label
        self.combo2_name = "Book Title: "
        self.label2 = ttk.Label(self.frame, text=self.combo2_name, width=25)
        self.label2.grid(column=0, row=2, pady=2, padx=2)

        # Creating Book Price Label & Price Display
        self.label3 = ttk.Label(self.frame, text="Book Price:", width=25)
        self.label3.grid(column=0, row=3, pady=2, padx=2)

        # Creating First Combobox Dropdown
        self.combo1 = ttk.Combobox(self.frame, width=25)
        self.combo1.grid(column=1, row=1, pady=2, padx=2)
        self.combo1['values'] = combolist1.getlist()  # Grabbing list to display in combobox1
        self.author_select = self.combo1.bind("<<ComboboxSelected>>", self.CallBack)  # Adding in action

        # Creating Second Combobox Dropdown
        self.combo2 = ttk.Combobox(self.frame, width=25, state='readonly')
        self.combo2.grid(column=1, row=2, pady=2, padx=2)

        # Creating Blank Price
        self.label4 = ttk.Label(self.frame, text='$')
        self.label4.grid(column=1, row=3, pady=2, padx=0)

        # Creating Tree Display
        self.tree1 = ttk.Treeview(self.frame, columns=('BRANCH_NAME', 'BOOKS_ON_HAND'), show='headings')
        self.tree1.heading('BRANCH_NAME', text='Branch Name')
        self.tree1.heading('BOOKS_ON_HAND', text='Book on Hand')
        self.tree1.grid(columns=2, rows=3, pady=5, padx=5)
        return


    def CallBack(self,event):
        """This is running of the First Search. Then Sending off the search to a second query
        to then populate the second combo list. This Combobox clears all other labels and trees"""
        self.label4['text'] = '$'
        self.selIndex = self.combolist1.getlist()[int(event.widget.current())]
        self.booklist = self.combolist2.getlist(self.selIndex)
        self.combo2['values'] = self.booklist  # setting combobox2 values to populate
        self.book_select = self.combo2.bind("<<ComboboxSelected>>", self.CallBack2)
        self.author_select = self.combolist1.getlist()[int(event.widget.current())]

        # Resetting Combobox 1
        self.combo2.set("")

        # Deleting Tree Entries
        for i in self.tree1.get_children():
            self.tree1.delete(i)


    def CallBack2(self, event):
        """Calling Back The Second Combowindow select. Sending the selection of
        to Get the books Available By Title then displaying the returned list into
        combotree"""
        # Resetting the tree in case they choose to look a second Combobox2 Value
        for i in self.tree1.get_children():
            self.tree1.delete(i)

        # Grabbing Combobox2 entry
        self.selIndex2 = event.widget.current()

        # Grabbing book selected
        self.book_select = self.booklist[self.selIndex2]

        # Looking through the query for books Available for placing in Combotree
        for row in self.combotree.getlist(self.book_select):
            self.tree1.insert("", "end", values=[row[0], row[1]])
            self.bookprice = row[2]

        # Setting Price Label
        self.label4['text'] = "$" + str(self.bookprice)


if __name__ == '__main__':
    mainfolder = GUI()