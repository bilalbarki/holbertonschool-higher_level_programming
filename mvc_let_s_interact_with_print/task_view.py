import Tkinter as tk
'''View class'''
class TaskView(tk.Toplevel):
    '''initialization'''
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        
        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(self, textvariable=self.__title_var)
        self.__title_label.pack(side="right")
        self.toggle_button = tk.Button(self, text="Reverse")
        self.toggle_button.pack(side="left")

    '''update title'''
    def update_title(self, title):
        if isinstance(title,str):
            self.__title_var.set(title)
        else:
            raise Exception("title is not a string")
