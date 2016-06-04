from xml.dom.minidom import Document
import json
from car import Car

'''initializations'''
filename = "5-main.json"
file_obj = open(filename)
cars_json = json.load(file_obj)
file_obj.close()
cars=[]
brands=[]
doors=0
doc = Document()
element_cars = doc.createElement('cars')

doc.appendChild(element_cars)

for car in cars_json:
    c=Car(car)
    cars.append(c)
    if not c.get_brand() in brands:
        brands.append(c.get_brand())
    doors+=c.get_nb_doors()
    c_xml = c.to_xml_node(doc)
    element_cars.appendChild(c_xml)

print len(brands)
print doors
print cars[3]
print doc.toxml(encoding='utf-8')
