class TaskModel():
    '''initializaton'''
    def __init__(self):
            self.__title=[]
            self.__callback_title = None

    '''getter for title'''
    def get_title(self):
        return self.__title

    def set_title(self,title):
        self.__title.append(title)

    '''setter for callback_title'''
    def set_callback_title(self, value):
        self.__callback_title = value

    '''reverses title and if callback_title is set, calls it with titl as argument'''
    def toggle(self,  index):
        self.__title[index] = self.__title[index][::-1]
        if self.__callback_title:
            self.__callback_title(self.__title)

    '''returns str for print'''
    def __str__(self):
        return self.__title
