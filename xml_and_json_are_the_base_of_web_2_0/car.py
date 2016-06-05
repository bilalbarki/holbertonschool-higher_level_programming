import json

class Car():
    '''initialization'''
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            if isinstance(args[0], dict):
                name = args[0].get('name')
                brand = args[0].get('brand')
                nb_doors = args[0].get('nb_doors')
            elif isinstance(args[0],basestring):
                splitted = args[0].split(",")
                name = splitted[0]
                brand = splitted[1]
                nb_doors = int(splitted[2])
            else:
                name = None
                brand = None
                nb_doors = None
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not isinstance(name,basestring) or name == "":
            raise Exception("name is not a string")
        if brand == None or not isinstance(brand,basestring) or brand == "":
            raise Exception("brand is not a string")
        if nb_doors == None or not isinstance(nb_doors, int) or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    '''getter for name'''
    def get_name(self):
        return self.__name

    '''getter for brand'''
    def get_brand(self):
        return self.__brand

    '''getter for nb_doors'''
    def get_nb_doors(self):
        return self.__nb_doors

    '''returns a dictionary'''
    def to_hash(self):
        return {'name': self.__name,
                'brand': self.__brand,
                'nb_doors': self.__nb_doors}

    '''returns a string for printing this class'''
    def __str__(self):
        return "%s %s (%d)" % (self.__name, self.__brand, self.__nb_doors)

    '''setter for nb_doors'''
    def set_nb_doors(self, number):
        self.__nb_doors = number

    '''converts to json string'''
    def to_json_string(self):
        return json.dumps(self.to_hash())

    '''returns an xml node'''
    def to_xml_node(self, doc):
        car = doc.createElement("car")
        
        car.setAttribute("nb_doors", str(self.__nb_doors))
        name = doc.createElement("name")
        name.appendChild(doc.createCDATASection(self.__name))
        car.appendChild(name)

        brand = doc.createElement('brand')
        brand.appendChild(doc.createTextNode(self.__brand))
        car.appendChild(brand)

        return car

    '''returns a comma separated string containing the variables'''
    def to_comma(self):
        return "%s,%s,%d\n" % (self.__name, self.__brand, self.__nb_doors)
