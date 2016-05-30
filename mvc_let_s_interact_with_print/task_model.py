class TaskModel():
    '''initializaton'''
    def __init__(self, title):
        if isinstance(title,str) and title!="":
            self.__title=title
            self.__callback_title = None
        else:
            raise Exception("title is not a string")

    '''getter for title'''
    def get_title(self):
        return self.__title

    '''setter for callback_title'''
    def set_callback_title(self, value):
        self.__callback_title = value

    '''reverses title and if callback_title is set, calls it with titl as argument'''
    def toggle(self):
        self.__title = self.__title[::-1]
        if self.__callback_title:
            self.__callback_title(self.__title)

    '''returns str for print'''
    def __str__(self):
        return self.__title
