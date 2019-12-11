import tkinter as tk
from tkinter import filedialog

APPNAME = "PyTextEditor"
AUTHOR = "Rully Ihza Mahendra"
APPVERSION = "1.0"


class PyTextEditor:

    def __init__(self, master):

        master.title("Untitled - " + APPNAME)
        master.geometry("1200x700")

        font_specs = ("Open Sans", 14)

        self.master = master
        self.filename = None
        self.file_extension = [
                    ("All Files", "*.*"),
                    ("Text Files", "*.txt"),
                    ("Python Scripts", "*.py"),
                    ("Javascript Files", "*.js"),
                    ("PHP Scripts", "*.php"),
                    ("HTML Files", "*.html"),
                    ("CSS Files", "*.css"),
                    ("C Files", "*.c"),
                    ("C++ Files", "*.cpp"),
                    ("C# Files", "*.cs"),
                    ("Java Files", "*.java"),
                    ("Markdown Documents", "*.md")
                ]

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)
        self.bind_shortcuts()


    # Commands for Menubar
    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - " + APPNAME)
        else:
            self.master.title("Untitled - " + APPNAME)
    

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()
    

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=self.file_extension
        )

        if self.filename:
            self.textarea.delete(1.0, tk.END)

            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read()) 

            self.set_window_title(self.filename)
    

    def save_file(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, 'w') as f:
                    f.write(textarea_content)
            
                self.statusbar.update_status(True)
            
            except Exception as e:
                print(e)
        else:
            self.save_as_file()


    def save_as_file(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=self.file_extension
            )

            textarea_content = self.textarea.get(1.0, tk.END)
            
            with open(new_file, 'w') as f:
                f.write(textarea_content)

            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)

        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind("<Control-n>", self.new_file)
        self.textarea.bind("<Control-o>", self.open_file)
        self.textarea.bind("<Control-s>", self.save_file)
        self.textarea.bind("<Control-S>", self.save_as_file)
        self.textarea.bind("<Key>", )


#####################################################################################
###################################### MENU BAR #####################################
#####################################################################################
class Menubar:

    def __init__(self, parent):
        font_specs = ("Open Sans", 10)
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File", command=parent.new_file, accelerator="Ctrl+N")
        file_dropdown.add_command(label="Open File", command=parent.open_file, accelerator="Ctrl+O")
        file_dropdown.add_command(label="Save", command=parent.save_file, accelerator="Ctrl+S")
        file_dropdown.add_command(label="Save As", command=parent.save_as_file, accelerator="Ctrl+Shift+S")
        file_dropdown.add_separator()
        file_dropdown.add_command(label='Exit', command=parent.master.destroy, accelerator="Alt+F4")

        menubar.add_cascade(label="File", menu=file_dropdown)



#####################################################################################
################################### Status Bar ######################################
#####################################################################################
class Statusbar:

    def __init__(self, parent):
        font_specs = ("Open Sans", 10)
        self.status = tk.StringVar()
        self.status.set(APPNAME + " " + APPVERSION + " | © " + AUTHOR + " - All Right Reserved.")

        label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                        bg="lightgrey", anchor="sw", font=font_specs
        )
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("File Has Been Saved! - " + APPVERSION + " " + AUTHOR)



if __name__ == "__main__":
    master = tk.Tk()
    pt = PyTextEditor(master)
    master.mainloop()