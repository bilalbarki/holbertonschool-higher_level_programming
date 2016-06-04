from xml.dom.minidom import Document
import json
from car import Car

filename = "6-main.json"
file_obj = open(filename)
cars_json = json.load(file_obj)
file_obj.close()
cars=[]
my_list = []

for car in cars_json:
    c = Car(car)
    cars.append(c)
    '''append to_comma() string to my_list variable'''
    my_list.append(c.to_comma())

print "".join(my_list)
