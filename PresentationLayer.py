import tkinter as tk
from tkinter import ttk
import PreferencesIO


class PreferencesFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")

        self.parent = parent

        self.preferences = PreferencesIO.readFromFile()

        self.name = tk.StringVar(value=self.preferences.get("name", ""))
        self.language = tk.StringVar(value=self.preferences.get("language", "English"))
        self.autosave = tk.IntVar(value=self.preferences.get("autosave", 5))  

        self.initComponents()

    def initComponents(self):
        self.pack()

        
        ttk.Label(self, text="Name:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.name).grid(column=1, row=0)

      
        ttk.Label(self, text="Language:").grid(column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.language).grid(column=1, row=1)

 
        ttk.Label(self, text="Autosave every X minutes:").grid(column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.autosave).grid(column=1, row=2)

       
        self.makeButtons()

    def makeButtons(self):
        buttonFrame = ttk.Frame(self)
        buttonFrame.grid(column=0, row=3, columnspan=2, sticky=tk.E, pady=10)

       
        ttk.Button(buttonFrame, text="Save", command=self.savePreferences).grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Cancel", command=self.parent.destroy).grid(column=1, row=0, padx=5)

    def savePreferences(self):

         autosave_value = self.autosave.get()
         if autosave_value <= 0:
             raise ValueError("Autosave must be greater than 0.")

         
         preferences_dictionary = {
             "name": self.name.get(),
             "language": self.language.get(),
             "autosave": autosave_value
         }

         
         PreferencesIO.saveToFile(preferences_dictionary)
         self.parent.destroy()



def main():
    root = tk.Tk()
    root.title("Preferences")
    app = PreferencesFrame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
