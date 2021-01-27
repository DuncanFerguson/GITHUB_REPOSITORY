import tkinter as tk
from tkinter import filedialog
import pandas as pd


def importcsv():
    root = tk.Tk()
    root.title("Tax Roll")

    canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
    canvas1.pack()
    def getCSV():

        global df

        import_file_path = filedialog.askopenfilename()
        df = pd.read_csv(import_file_path)
        print(df)

    browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='blue', fg='white',
                             font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browseButton_CSV)

    root.mainloop()

importcsv()
