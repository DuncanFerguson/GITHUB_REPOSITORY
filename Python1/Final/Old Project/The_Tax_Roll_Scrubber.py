import tkinter as tk
from tkinter import filedialog
import pandas as pd
import csv

#Student: Duncan Ferguson
#Student Id: 871641260
#Class: 3005-2
#Assignment: Final

'''This Program takes a list of Mineral Owner and NRA values then creates a NRA dictionary with reorganized
 reorganizes names. There is the option to use the list that is in the file, or rewrite the file path. There is also
 the option just to print the list, or save it as a csv file'''



# List of Suffix Types that should remain at the end of a name swap
suffixtypes = ["JR", "II", "III", "IV", "V", "ESTATE", "TR", "TRUSTEE"]

# List of company endings to skip on
companynames = ["LLC", "COMPANY", "ESTATE", "INC", "FDN", "FOUNDATION", "EXPLORATION", "ROYALTIES", "CORP",
                "PARTNERSHIP", "INC", "CO", "LTD", "PARTNERS", "FDN", "LP", "MINERALS", "PROPERTIES", "TRUST"]

class Table:

    def __init__(self,root):

        for i in range(total_rows):
            for j in range(totalcolumns):
                self.e = Entry(root, width=20, fg='blue',
                                font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


def importcsv():
    """This function opens the file that is listed in taxrollfilelocation, and places the values into a list"""
    root = tk.Tk()
    root.title("Tax Role Import")

    canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
    canvas1.pack()


    def getCSV():
        """This is the actual GUI asking for the import file. Then making that file a global taxrollfilelocation"""
        import_file_path = filedialog.askopenfilename()

        global taxrollfilelocation

        taxrollfilelocation = pd.read_csv(import_file_path)  # File name

    browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='blue', fg='white',
                                 font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_CSV)
    root.mainloop()


def selectfields():
    """This Function lets the user choose which headers they would like to include: """
    taxrollfile = pd.DataFrame(taxrollfilelocation, columns=['Owner', 'NRA'])  # Grabbing Headers
    # taxrollfile = pd.DataFrame(taxrollfilelocation)  # Grabbing Headers
    listfromfile = taxrollfile.values.tolist()  # Placing file columns into a list
    total_rows = len(listfromfile)
    total_columns = len(listfromfile)
    print(listfromfile[0])

    listfromfile = [['Ferguson Duncan Jr', 640]]

    return listfromfile


def totalnra(list2nradict):
    """This Function takes in a list of [names, NRA]. It then makes and returns a dictionary with the NRA sums"""
    list2nrasumdict = {}  # Blank Dictionary
    for (name, NRA_Amount) in list2nradict:
        if name in list2nrasumdict:
            list2nrasumdict[name] += NRA_Amount  # If Name exists, add NRA Amount
        else:
            list2nrasumdict[name] = NRA_Amount  # If Name doesn't exist, make dictionary entry
    return list2nrasumdict


def fixnames(fixdict):
    """This function returns the NRA Dictionary with the proper names"""
    newnrasum = {}
    nrasumlist = []
    for i in fixdict:
        nrasumlist += [[i, fixdict[i]]]  # Casting nrsSum dictionary into a list with the rawnames
    for i in nrasumlist:
        names = [i[0]]  # This is really a string that I am representing as a list so that I can split it later
        newname = determineswap(names, suffixtypes,
                                companynames)  # running through the name swapper and returning a name in list value
        newnrasum[newname[0]] = [i[1]]  # Adding NRA to the new Dictionary with the newname
        newnrasum[newname[0]].append(i[0])  # Adding the Raw name to the dictionary for safe keeping
    return newnrasum


def determineswap(names, suffixtypes, companynames):
    """This funcation looks at the name and determines which other function to run the name through
    this way we can send the name to the right area"""
    for i in range(len(names)):  # This loops through the list
        namesplit = names[i].split(" ")  # This takes the name, splits the different types of names into a list
        if len(namesplit) == 1 or namesplit[-1] in companynames:  # If one word or  a company name, just keep as is
            names[i] = names[i]
        elif namesplit[-1] in suffixtypes:  # This looks to see if there is a suffix type at the end
            names[i] = lastnamesuffixswap(namesplit)
        else:  # This assumes if there is no suffix or company name, run normal name swap
            names[i] = lastnameswap(namesplit)
    return names  # Returning the properly modified name


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


def endoption(newnrasum):
    """This function lets you choose whether to save the dictionary or
    print it newnrasum dictionary or saves it to a CSV File"""
    print("\nThe Raw List has been scrubbed\n")
    ending = input("Press 'P' or 'p' to print NRA Sum Dictionary\n"
                   "Press 'S' or 's' to save CSV File\n"
                   "Press 'Any other Key to Exit\n")
    if ending == 's' or ending == 'S':
        return
    elif ending == 'p' or ending == 'P':  # Simple Printing of dictionary
        print("Key = New Owner Name : Value = [NRA, Raw Name]")
        print(newnrasum)
        exit()
    else:
        exit()


def dicttolist(newnrasum):
    """This Function takes in a dictionary and writes it to a csv file"""
    rows = []
    for i in newnrasum:  # Casting newNRA Sum dictionary back into a list
        name = i
        nra = newnrasum[i][0]
        rawname = newnrasum[i][1]
        rows.append([name, nra, rawname])
    return rows


def exportfile(savelist):
    """This Function enables the user to select from a GUI where they want to export their file too"""
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
    canvas1.pack()

    def exportCSV(savelist):
        """This Function opens the GUI Asking to save the file"""
        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        fields = ['Name', 'NRA', 'Raw Name']
        with open(export_file_path, 'w', newline='') as csvfile:  # writing my csv file
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(savelist)

    saveAsButton_CSV =tk.Button(text='Export CSV', command=exportCSV, bg='blue', fg='white',
                                font=('helvetica', 12, 'bold'))
    canvas1.create_window(150,150,window=saveAsButton_CSV)
    exportCSV(savelist)


importcsv()  # Importing the CSV File with a GUI
rawlist = selectfields() #Selecting the fields from that file with a GUI

nrasum = totalnra(rawlist)  # Place raw list into a dictionary
modifiednradict = fixnames(nrasum)  # This is returning back the new name values in a NRA Dictionary
endoption(modifiednradict)  # This is giving you an option for how to end

exportList = dicttolist(modifiednradict)
exportfile(exportList)

