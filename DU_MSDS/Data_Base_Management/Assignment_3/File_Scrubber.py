from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import tkinter as tk
import pandas as pd

# Student: Duncan Ferguson
# Student Id: 871641260
# Final Project
# Date 6/8/2021

'''The Gaper Taxroll Scrubber is a program that helps someone scrub a taxroll. 
This Program lets a user take a raw file. Select a column that contains unorganized names. These names
are then reorganized into the proper form.'''


class GUI(object):
    """This GUI takes commands in the following order [Boolean, Text]. The first bit of Boolean turns on different
    buttons or displays to appear. There is option for a second button. There is also an upload file functionality
    that asks the user to select the file path and create a dataframe for a file they would like to upload."""

    def __init__(self, print_text, button_1, button_2):
        self.button_1_pushed = False
        self.button_2_pushed = False
        self.rawfilepanda = pd.DataFrame()

        # Standard Box Design
        self.master = Tk()
        # self.master.iconbitmap(default="Images/Gaper_Taxroll.ico")  # This is the icon for display. Click off for submit
        self.GUITitle = self.master.title("Gaper Taxroll - Looping GUI")
        self.boxsize = self.master.geometry("400x400")  # Size of the Box

        # Displaying print text
        if print_text[0]:
            self.Topline = Label(self.master, text=print_text[1], pady=40).pack(pady=10)  # Entry Text
        # Looking to see if a first button should be created
        if button_1[0]:
            self.myButton_1 = Button(self.master, text=button_1[1], padx=50, pady=10,
                                     command=self.button_1_trigger).pack()
        # Looking to see if a second button should be created
        if button_2[0]:
            self.myButton_2 = Button(self.master, text=button_2[1], padx=50, pady=10,
                                     command=self.button_2_trigger).pack(pady=10)
        self.master.mainloop()  # Looping Master to run tkinter

    def button_1_trigger(self):
        """Return a true value for button_1_pushed"""
        self.button_1_pushed = True
        self.button_2_pushed = False
        self.master.quit()

    def button_2_trigger(self):
        """Return a true value for button_2_pushed"""
        self.button_2_pushed = True
        self.button_1_pushed = False
        self.master.quit()

    def uploadfile(self):
        """This asks the user to open a file"""
        self.rawfilepanda = pd.read_csv(askopenfilename(title="Select a File"), header=0, index_col=False)
        self.master.destroy()
        return self.rawfilepanda


class HeaderGui:
    """The Headers GUI loops through a list of headers and displays them as push buttons. The class takes a prompt text
    and then the buttons. It returns a string of column header that is selected."""

    def __init__(self, text, header_list):
        self.root = tk.Tk()
        self.v = tk.IntVar()
        self.v.set(-1)
        self.root.title("Select A Column Header")
        self.Topline = Label(self.root, text=text, pady=10).pack(pady=10, padx=5)  # Entry Text
        self.choice = ""
        self.header_list = header_list
        self.create_header_choice()
        self.root.mainloop()

    def create_header_choice(self):
        """Looping through the header list to create buttons"""
        for name in range(len(self.header_list)):
            Radiobutton(self.root,
                        text=self.header_list[name],
                        indicatoron=0,
                        width=20,
                        variable=self.v,
                        command=self.selectchoice,
                        value=str(name)).pack()

    def selectchoice(self):
        """Returning the choice of button. As the value of the list"""
        self.choice = self.header_list[self.v.get()]
        self.root.destroy()
        return


def startoption(start_text):
    """This function prompts a welcome screen. Asks the users if they would like to start the program. If they
    choose to start. A open file finder will be prompted. The file select will then be turned into a panda."""
    start_screen = GUI([True, start_text],
                       [True, "Click To start"],
                       [True, "Exit"])
    if start_screen.button_1_pushed:
        start_screen.uploadfile()
        return start_screen.rawfilepanda
    else: exit()


def fixnames(rawlist, nameindex):
    """This function takes in a panda, and the column that contains the names. It then goes through the column
    and reorders the names. If the name is a company account that is marked in a new column. The raw list is then
    returned with two new name columns: Company_Account, SF_Account_Names"""

    # These are the delimiters for suffix's
    suffixtypes = ["JR", "II", "III", "IV", "V", "ESTATE", "TR", "TRUSTEE", "HEIRS", "EST"]

    # List of company endings to skip on
    companynames = ["LLC", "COMPANY", "ESTATE", "INC", "FDN", "FOUNDATION", "EXPLORATION", "ROYALTIES", "CORP",
                    "PARTNERSHIP", "INC", "CO", "OKLAHOMA", "TEXAS", "LTD", "PARTNERS", "FDN", "LP", "MINERALS",
                    "PROPERTIES", "TRUST", "CORPORATION", "OIL"]

    # Blank lists to append new data to
    sf_account_names = []
    company_account = []

    # Looping through the names in the rawlist[nameindex] and replacing name order
    for raw_name in rawlist[nameindex]:
        namesplit = raw_name.split(" ")  # This takes the name, splits it into a list of names
        if len(namesplit) == 1:
            company_account.append("No")
            sf_account_names.append(raw_name)
        elif namesplit[-1] in companynames:
            company_account.append("Yes")
            sf_account_names.append(raw_name)
        elif namesplit[-1] in suffixtypes:
            company_account.append("No")
            sf_account_names.append(lastnamesuffixswap(namesplit))
        else:
            company_account.append("No")
            sf_account_names.append(lastnameswap(namesplit))

    # Adding new columns to data frame
    # rawlist["Company_Account"] = company_account
    rawlist["Account_Names"] = sf_account_names

    return rawlist


def lastnameswap(namesplit):
    """This changes the order of the names. Example: Last, First, Middle
    Ending Example: First, Middle, Last. The returned value is in string form"""
    newname = ""  # Creating a new blank string
    z = 1
    while z < len(namesplit):
        newname += " " + namesplit[z]  # adding a space then the name starting from the second position
        z += 1
    newname += " " + namesplit[0]
    newname = newname.lstrip()  # Stripping out the leading space
    return newname


def lastnamesuffixswap(namesplit):
    """This changes the order of the names if it sees a suffix for a swap. Example: Last, First, Middle, Suffix
    Ending Example: First, Middle, Last, Suffix. The returned value is in string form"""
    newname = ""
    z = 1
    while z < len(namesplit) - 1:
        newname += " " + namesplit[z]
        z += 1
    newname += " " + namesplit[0] + " " + namesplit[-1]  # Moves the lastname right before the suffix
    newname = newname.lstrip()
    return newname


def lookup_ids(raw_file, accounts):
    """This function is taking in two dataframes. And two indexs. Then returning the values from the second dataframe to
    the new column in the first data frame"""

    leftjoin = pd.merge(raw_file, accounts,
                        how='left',
                        left_on='Account_Names',
                        right_on='Account_Names',
                        )
    return leftjoin


def create_new_accounts(raw_file):
    """This function takes the accounts. Filters out the companies and account with ID and makes a new contact file"""
    print("Arrived_At_Address_Scrubber")

    # Delimiters too look for a Street Address
    street_delimiters = ["RD", "LN", "AVE", "BLVD", "CREEK", "CT", "DR", "CIR", "PL", "ST",
                         "WAY", "TRL", "HWY", "RDG"]

    # Filtering through the look up accounts, getting rid of company accounts. And Accounts that already exist.
    new_accounts = raw_file[raw_file['Account_ID'].isnull()]  # Filtering out accounts with id
    # new_accounts = new_accounts[new_accounts['Company_Account'].isin(['No'])]  # Filtering out company accounts
    headers = list(new_accounts.columns.values)  # snagging headers
    # new_accounts.sort_values('Account_Names')  # Sorting by Names
    address_header = HeaderGui("Select the Column with the ADDRESS that need scrubbing\n", headers)

    # Copying over just the names and addresses
    simple_accounts = new_accounts[['Account_Names', address_header.choice]].copy()
    simple_accounts.sort_values('Account_Names', inplace=True)
    simple_accounts.drop_duplicates(subset='Account_Names', keep=False, inplace=True)  # Deduping based on names

    # Setting up blank columns to add
    zip_codes = []
    states = []
    street_address = []
    city = []

    # Parsing through the address and separating them out.
    # TODO this city split is quite correct, but leaving due to time
    # TODO Spend a whole lot of time here
    for row in simple_accounts[address_header.choice]:
        address_split = row.split(', ')  # Splitting address on ', '
        state_zip = address_split[1].split(' ')  # Splitting on ' '
        zip_codes.append(state_zip[1])  # Grabbing Zip Code
        states.append(state_zip[0])  # Grabbing state
        street_address.append(address_split[0].rsplit(' ',1)[0])
        city.append(address_split[0].split()[-1])

    # Adding new columns to data frame
    simple_accounts['Address'] = street_address
    simple_accounts['City'] = city
    simple_accounts['State'] = states
    simple_accounts['Zip_Codes'] = zip_codes
    return simple_accounts


def endoption(panda_file):
    """This option asks the user if they would like to save their new accounts that have been created. It takes in a
    dataframe and converts it into a csv through the GUI Class to be saved."""
    decide = GUI([True, "Where Would you Like to save the new Accounts?\n"
                        "Note, you will have to check the cities before uploading to salesforce"], [True, "Save File"],
                 [True, "Exit"])  # Save option through looping gui class
    if decide.button_1_pushed:
        filepath = asksaveasfile(defaultextension=".csv")
        filepath.write(panda_file.to_csv(header=True, index=False, line_terminator='\n'))
        exit()
    else:
        exit()


def main():
    """Main Function for running the code. Most of the sure prompts are located here."""

    # Asks User which file they would like to use for the Raw Tax Roll File
    rawlist = startoption("Welcome to the Gaper Taxroll.\nTo start we will have to import a CSV File.\n "
                          "This file is located in\n\n"
                          "**Folder Name: RAW_Taxroll_Files**\n\n"
                          "**File Name: Sample_File_2_Scrubb**\n\n"
                          "Click the start button to proceed.")

    # Asking User to select the column where the accounts that need to be scrubbed are located
    rawlist_account_col = HeaderGui("Click the button that contains the \nACCOUNTS/NAME/OWNER/MINERAL_OWNER",
                                    list(rawlist.columns.values))

    # Scrubbing names to be in proper form
    names_scrubbed_list = fixnames(rawlist, rawlist_account_col.choice)
    # print("Scrubbed Names",names_scrubbed_list)


    # Asking User to located Salesforce Accounts
    # print("This is where the Old Code gets edited")
    sf_accounts = startoption("We now have to select an update the salesforce accounts file.")

    # Asking user for column of name to be scrubbed and return Id column
    sf_account_col = HeaderGui("Click the button that contains the \nNAMES for comparing accounts",
                               list(sf_accounts.columns.values))
    sf_ids = HeaderGui("Click the button with the IDs to be returned", list(sf_accounts.columns.values))

    # Looking up the ids on from the selections
    raw_file_w_id = lookup_ids(names_scrubbed_list, sf_ids.choice, sf_accounts, sf_account_col.choice)

    # Creating new accounts sheet
    new_contacts = create_new_accounts(raw_file_w_id)

    # Prompting user to save new accounts sheet
    endoption(new_contacts)


if __name__ == "__main__":
    main()
