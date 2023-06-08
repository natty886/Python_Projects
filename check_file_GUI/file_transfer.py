import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
from os import path
import shutil
import datetime
from datetime import date, time, timedelta



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Title of GUI window
        self.master.title("File Transfer")
        #Button - source select
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Position - source select button
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Entry - source select
        self.source_dir = Entry(width=75)
        #Position - source select entry
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))

        #Button - destination select
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Position - destination select button
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Entry - destination select
        self.destination_dir = Entry(width=75)
        #Position - destination select entry
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Button - transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Position - transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Button - exit
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Position - exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    

    #Function - select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #Clears content in Entry widget | allows proper path insert
        self.source_dir.delete(0, END)
        #Method to insert user selection to source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #Function - select destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #Clears content in Entry widget | allows proper path insert
        self.destination_dir.delete(0, END)
        #Method to insert user selection to destination_dir Entry
        self.destination_dir.insert(0, selectDestDir)

    #Function - transfer files from one directory to another
    def transferFiles(self):
        #Source Directory
        source = self.source_dir.get()
        #Destination Directory
        destination = self.destination_dir.get()
        #File list in Source Directory
        source_files = os.listdir(source)
        #time_format = time.gmtime(os.path.getmtime(source_files))
        #Runs each file in Source Directory
        for i in source_files:
            #File path for specific file
            filePath = os.path.join(source, i)
            #Modification time of file
            modTime = os.path.getmtime(filePath)
            #Variable - 24 hours deducted from current date 
            time24Hours = datetime.datetime.now() - timedelta(hours = 24)
            #Variable - modification timestamp of file
            datetime_of_file = datetime.datetime.fromtimestamp(modTime)
            if time24Hours < datetime_of_file:
                
                #moves each file from source to destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    #Function - Exits program
    def exit_program(self):
        #Root = main GUI window | Terminates main loop and all widgets inside
        root.destroy()
 


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

