import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser

url = 'http://docs.python.org/'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #Button - default html page
        self.btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        #Position - default html page button
        self.btn.grid(row=2, column=1, padx=(0,0), pady=(0,15))

        #Label - custom text entry
        label = Label(text="Enter custom text or click the Default HTML page button")
        label.grid(row=0, column=0, padx=(20,0), pady=(20,10))
        
        #Entry - custom text
        self.custom_entry = Entry(width=85)
        #Position - custom text entry
        self.custom_entry.grid(row=1, column=0, columnspan=3, padx=(0,0), pady=(0,20))

        #Button - submit custom text
        self.submitText_btn = Button(text="Submit Custom Text", width=20, height=2, command=self.customEntry)
        #Position - submit custom text button
        self.submitText_btn.grid(row=2, column=2, padx=(0,20), pady=(0,15))


    #Function -
    def customEntry(self):
        with open("index.html", "w") as f:
            f.write(self.custom_entry.get())
            f.close()
            webbrowser.get(chrome_path).open("index.html", new=1, autoraise=True)

    #Function - creates and writes in HTML file
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.get(chrome_path).open("index.html", new=1, autoraise=True)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
