import tkinter as tk
class Passwordchecker(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

   def initialize_user_interface(self):
       self.parent.geometry("200x200")
       self.parent.title("Password checker")
       self.entry=tk.Entry(self.parent)
       self.entry.pack()
       self.button=tk.Button(self.parent,text="Enter", command=self.PassCheck)
       self.button.pack()
       self.label=tk.Label(self.parent,text="Please a password")
       self.label.pack()

   def PassCheck(self):
       password = self.entry.get()
       if len(password)>=9 and len(password)<=12:
          self.label.config(text="Password is correct")
       else:
          self.label.config(text="Password is incorrect")

if __name__ == '__main__':

   root = tk.Tk()
   run = Passwordchecker(root)
   root.mainloop()