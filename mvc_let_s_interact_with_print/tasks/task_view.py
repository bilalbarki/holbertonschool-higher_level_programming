import Tkinter as tk

class TaskView(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        
        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")

        self.__title_var = []
        self.__entry_field = tk.Entry(self)
        self.__entry_field.grid(row=0, column=0)
        self.add_button = tk.Button(self, text="Add")
        self.add_button.grid(row=0, column=1)
        self.__row=1
        self.__title_label = []
        self.toggle_button = []
        self.del_button = []


    def update_title(self, title):
        if isinstance(title,str):
            self.__title_var.set(title)
        else:
            raise Exception("title is not a string")

    def get_entry(self):
        self.__title_var.insert(0,tk.StringVar())
        self.__title_var[0].set(self.__entry_field.get())

    def add_item(self):
        self.__new_button = tk.Button(self, text="Reverse")
        self.toggle_button.append(self.__new_button) 
        self.__new_button.grid(row=self.__row+1, column=0)

        self.__new_del_button = tk.Button(self, text="Delete")
        self.toggle_button.append(self.__new_del_button) 
        self.__new_del_button.grid(row=self.__row+1, column=1)
        self.get_entry()
        self.__new_label=tk.Label(self, textvariable=self.__title_var[0])
        self.__title_label.append(self.__new_label)
        self.__new_label.grid(row=self.__row+1, column=2)

        #self.__new_button.config(command=self.__toggle)

        self.__row=self.__row+1

        
