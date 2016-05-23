import json, os

'''class Person'''
class Person():
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    
    '''initialization'''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        if (type(id) is not int) or (id<0):
            raise Exception("id is not an integer")
        self.__id=id

        if (type(first_name) is not str) or (first_name==""):
            raise Exception("first_name is not a string")
        self.__first_name=first_name

        if (all(isinstance(date_of_birth, int) for item in date_of_birth) or (len(date_of_birth)!=3)) or (date_of_birth[0]<1 or date_of_birth[0]>12) or (date_of_birth[1]<1 or date_of_birth[1]>31):
            raise Exception("date_of_birth is not a valid date")
        self.__date_of_birth=date_of_birth

        if (type(genre) is not str) or (genre not in Person.GENRES):
            raise Exception("genre is not valid")
        self.__genre=genre

        if (type(eyes_color) is not str) or (eyes_color not in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")
        self.__eyes_color=eyes_color
        
        self.last_name=""
        self.is_married_to=0
        self.children=[]
    '''end of initialization'''
    
    '''getters'''
    '''get id'''
    def get_id(self):
        return self.__id

    '''get genre'''
    def get_genre(self):
        return self.__genre

    '''get eyes color'''
    def get_eyes_color(self):
        return self.__eyes_color

    '''get date of birth'''
    def get_date_of_birth(self):
        return self.__date_of_birth

    '''get first name'''
    def get_first_name(self):
        return self.__first_name

    '''get eyes color'''
    def get_eyes_color(self):
        return self.__eyes_color
    '''end of getters'''

    '''Public methods'''
    '''str'''
    def __str__(self):
        return self.__first_name + " " + self.last_name

    '''is male'''
    def is_male(self):
        if self.__genre=="Male":
            return True
        return False

    '''age'''
    def age(self):
        '''today = datetime.date.today()'''
        today=[5, 20, 2016]
        return today[2]-self.__date_of_birth[2]

    '''overloading'''
    '''eq'''
    def __eq__(self, other):
        return self.age() == other.age()
    '''ne'''
    def __ne__(self, other):
        return self.age() != other.age()
    '''lt'''
    def __lt__(self, other):
        return self.age() < other.age()
    '''gt'''
    def __gt__(self, other):
        return self.age() > other.age()
    '''le'''
    def __le__(self, other):
        return self.age() <= other.age()
    '''ge'''
    def __ge__(self, other):
        return self.age() >= other.age()
    '''overloading end'''

    '''json definitions'''
    def json(self):
        json = {'id': self.__id,
            'eyes_color' : self.__eyes_color,
            'genre' : self.__genre,
            'date_of_birth': self.__date_of_birth,
            'first_name' : self.__first_name,
            'last_name' : self.last_name,
            'is_married_to' : self.is_married_to,
            'children' : self.children
        }
        return json

    '''load from json'''
    def load_from_json(self, json):
        if type(json) is not dict:
            raise Exception("json is not valid") 
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.last_name = json['last_name']
        self.is_married_to = json['is_married_to']
        self.children = json['children']

'''class baby'''
class Baby(Person):
    '''can run'''
    def can_run(self):
        return False

    '''need help'''
    def need_help(self):
        return True

    '''is young'''
    def is_young(self):
        return True
    
    '''can vote'''
    def can_vote(self):
        return False

    '''can be married'''
    def can_be_married(self):
        return False

    '''is married'''
    def is_married(self):
        if self.is_married_to != 0:
            return True
        return False

    '''divorce'''
    def divorce(self, p):
        self.is_married_to=0
        p.is_married_to=0

    '''just married with'''
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")

        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()

        if p.get_genre() == "Female" and self.get_genre() == "Male":
            p.last_name = self.last_name
        elif p.get_genre() == "Male" and self.get_genre() == "Female":
            self.last_name = p.last_name

    '''can have child'''
    def can_have_child(self):
        return False

    '''has child with'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color=''):
        if (p.__class__.__name__!='Adult' and p.__class__.__name__!='Senior') or (p is None):
            raise Exception("p is not an Adult of Senior")
        if (type(id) is not int) or (id<0):
            raise Exception("id is not an integer")
        if (type(first_name) is not str) or (first_name==""):
            raise Exception("first_name is not a string")
        if (all(isinstance(date_of_birth, int) for item in date_of_birth) or (len(date_of_birth)!=3)) or (date_of_birth[0]<1 or date_of_birth[0]>12) or (date_of_birth[1]<1 or date_of_birth[1]>31):
            raise Exception("date_of_birth is not a valid date")
        if (type(genre) is not str) or (genre not in Person.GENRES):
            raise Exception("genre is not valid")
        if (not self.can_have_child()) or (not p.can_have_child()):
            raise Exception("Can't have baby")

        if eyes_color=='':
            if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Green'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Brown'

        if (type(eyes_color) is not str) or (eyes_color not in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")

        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id) 

        return Baby(id,first_name,date_of_birth,genre,eyes_color)

    '''adopt child'''
    def adopt_child(self, c):
        if (not self.can_have_child()):
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

    '''who are my parents'''
    def who_are_my_parents(self, list_person):
        parents = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
            if self.get_id() in p.children:
                parents.append(p)
        return parents

    '''who are my grandparents'''
    def who_are_my_grand_parents(self, list_person):
        grandpar = []
        par = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
        par = self.who_are_my_parents(list_person)
        for item in par:
            for gp in item.who_are_my_parents(list_person):
                grandpar.append(gp)
        return grandpar

'''teenager'''
class Teenager(Person):
    '''can run'''
    def can_run(self):
        return True

    '''need help'''
    def need_help(self):
        return False

    '''is young'''
    def is_young(self):
        return True

    '''can vote'''
    def can_vote(self):
        return False

    '''can be married'''
    def can_be_married(self):
        return False

    '''is married'''
    def is_married(self):
        if self.is_married_to != 0:
            return True
        return False

    '''divorce'''
    def divorce(self, p):
        self.is_married_to=0
        p.is_married_to=0

    '''just married with'''
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")

        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()

        if p.get_genre() == "Female" and self.get_genre() == "Male":
            p.last_name = self.last_name
        elif p.get_genre() == "Male" and self.get_genre() == "Female":
            self.last_name = p.last_name

    '''can have child'''
    def can_have_child(self):
        return False

    '''has child with'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color=''):
        if (p.__class__.__name__!='Adult' and p.__class__.__name__!='Senior') or (p is None):
            raise Exception("p is not an Adult of Senior")
        if (type(id) is not int) or (id<0):
            raise Exception("id is not an integer")
        if (type(first_name) is not str) or (first_name==""):
            raise Exception("first_name is not a string")
        if (all(isinstance(date_of_birth, int) for item in date_of_birth) or (len(date_of_birth)!=3)) or (date_of_birth[0]<1 or date_of_birth[0]>12) or (date_of_birth[1]<1 or date_of_birth[1]>31):
            raise Exception("date_of_birth is not a valid date")
        if (type(genre) is not str) or (genre not in Person.GENRES):
            raise Exception("genre is not valid")

        if (not self.can_have_child()) or (not p.can_have_child()):
            raise Exception("Can't have baby")

        if eyes_color=='':
            if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Green'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Brown'

        if (type(eyes_color) is not str) or (eyes_color not in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")

        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)

        return Baby(id,first_name,date_of_birth,genre,eyes_color)

    '''adopt child'''
    def adopt_child(self, c):
        if (not self.can_have_child()):
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

    '''who are my parents'''
    def who_are_my_parents(self, list_person):
        parents = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
            if self.get_id() in p.children:
                parents.append(p)
        return parents

    '''who are my grandparents'''
    def who_are_my_grand_parents(self, list_person):
        grandpar = []
        par = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
        par = self.who_are_my_parents(list_person)
        for item in par:
            for gp in item.who_are_my_parents(list_person):
                grandpar.append(gp)
        return grandpar

'''Adult'''
class Adult(Person):
    '''can run'''
    def can_run(self):
        return True

    '''need help'''
    def need_help(self):
        return False

    '''is young'''
    def is_young(self):
        return False

    '''can vote'''
    def can_vote(self):
        return True

    '''can be married'''
    def can_be_married(self):
        return True

    '''is married'''
    def is_married(self):
        if self.is_married_to != 0:
            return True
        return False

    '''divorce'''
    def divorce(self, p):
        self.is_married_to=0
        p.is_married_to=0

    '''just married with'''
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")

        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()

        if p.get_genre() == "Female" and self.get_genre() == "Male":
            p.last_name = self.last_name
        elif p.get_genre() == "Male" and self.get_genre() == "Female":
            self.last_name = p.last_name

    '''can have child'''
    def can_have_child(self):
        return True

    '''has child with'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color=''):
        if (p.__class__.__name__!='Adult' and p.__class__.__name__!='Senior') or (p is None):
            raise Exception("p is not an Adult of Senior")
        if (type(id) is not int) or (id<0):
            raise Exception("id is not an integer")
        if (type(first_name) is not str) or (first_name==""):
            raise Exception("first_name is not a string")
        if (all(isinstance(date_of_birth, int) for item in date_of_birth) or (len(date_of_birth)!=3)) or (date_of_birth[0]<1 or date_of_birth[0]>12) or (date_of_birth[1]<1 or date_of_birth[1]>31):
            raise Exception("date_of_birth is not a valid date")
        if (type(genre) is not str) or (genre not in Person.GENRES):
            raise Exception("genre is not valid")

        if (not self.can_have_child()) or (not p.can_have_child()):
            raise Exception("Can't have baby")

        if eyes_color=='':
            if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Green'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Brown'

        if (type(eyes_color) is not str) or (eyes_color not in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")

        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)

        return Baby(id,first_name,date_of_birth,genre,eyes_color)

    '''adopt child'''
    def adopt_child(self, c):
        if (not self.can_have_child()):
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

    '''who are my parents'''
    def who_are_my_parents(self, list_person):
        parents = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
            if self.get_id() in p.children:
                parents.append(p)
        return parents

    '''who are my grandparents'''
    def who_are_my_grand_parents(self, list_person):
        grandpar = []
        par = []
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
        par = self.who_are_my_parents(list_person)
        for item in par:
            for gp in item.who_are_my_parents(list_person):
                grandpar.append(gp)
        return grandpar

'''Senior'''
class Senior(Person):
    '''can run'''
    def can_run(self):
        return False

    '''need help'''
    def need_help(self):
        return True

    '''is young'''
    def is_young(self):
        return False

    '''can vote'''
    def can_vote(self):
        return True

    '''can be married'''
    def can_be_married(self):
        return True

    '''is married'''
    def is_married(self):
        if self.is_married_to != 0:
            return True
        return False

    '''divorce'''
    def divorce(self, p):
        self.is_married_to=0
        p.is_married_to=0

    '''just married with'''
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if self.can_be_married() == False or p.can_be_married() == False:
            raise Exception("Can't be married")
        
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()

        if p.get_genre() == "Female" and self.get_genre() == "Male":
            p.last_name = self.last_name
        elif p.get_genre() == "Male" and self.get_genre() == "Female":
            self.last_name = p.last_name

    '''can have child'''
    def can_have_child(self):
        return False

    '''has child with'''
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color=''):
        if (p.__class__.__name__!='Adult' and p.__class__.__name__!='Senior') or (p is None):
            raise Exception("p is not an Adult of Senior")
        if (type(id) is not int) or (id<0):
            raise Exception("id is not an integer")
        if (type(first_name) is not str) or (first_name==""):
            raise Exception("first_name is not a string")
        if (all(isinstance(date_of_birth, int) for item in date_of_birth) or (len(date_of_birth)!=3)) or (date_of_birth[0]<1 or date_of_birth[0]>12) or (date_of_birth[1]<1 or date_of_birth[1]>31):
            raise Exception("date_of_birth is not a valid date")
        if (type(genre) is not str) or (genre not in Person.GENRES):
            raise Exception("genre is not valid")

        if (not self.can_have_child()) or (not p.can_have_child()):
            raise Exception("Can't have baby")

        if eyes_color=='':
            if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Green'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Blue'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Blue' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Brown' :
                eyes_color = 'Brown'
            elif self.get_eyes_color() == 'Brown' and p.get_eyes_color() == 'Green' :
                eyes_color = 'Brown'

        if (type(eyes_color) is not str) or (eyes_color not in Person.EYES_COLORS):
            raise Exception("eyes_color is not valid")

        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)

        return Baby(id,first_name,date_of_birth,genre,eyes_color)

    '''adopt child'''
    def adopt_child(self, c):
        if (not self.can_have_child()):
            raise Exception("Can't adopt child")
        self.children.append(c.get_id())

    '''who are my grandchildren'''
    def who_are_my_grandchildren(self, list_person):
        if not isinstance(list_person, list):
            raise Exception("list_person is not valid")
        for p in list_person:
            if p.__class__.__name__ == "Person":
                raise Exception("list_person is not valid")
        gchildren=[]
        for child in self.children:
            for gchild in child.children:
                gchildren.append(gchild)
        return gchildren
        

'''save JSON to file'''
def save_to_file(list, filename):
    for i in range(0, len(list)):
        name = list[i].__class__.__name__
        list[i] = list[i].json()
        list[i]['type'] = name
    with open(filename, 'w') as outfile:
        json.dump(list, outfile)
    outfile.close()

'''load JSON from file'''
def load_from_file(filename):
    if type(filename) != str or os.path.isfile(filename) != True:
        raise Exception("filename is not valid or doesn't exist")
    with open(filename) as jfile:
        data = json.load(jfile)
    jfile.close()
    list_of_obj = []
    a_dict = {"Senior": Senior, "Adult": Adult, "Teenager": Teenager, "Baby": Baby}
    for i in data:
        obj = a_dict[i['type']](1, "Julien", [12, 24, 1980], "Male", "Blue")
        obj.load_from_json(i)
        list_of_obj.append(obj)
    return list_of_obj
