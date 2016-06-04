# -*- coding: utf-8
from xml.dom.minidom import Document
import json
from car import Car

filename = "7-main.json"
file_obj = open(filename)
cars_json = json.load(file_obj)
file_obj.close()
cars=[]
doc = Document()
cars_element = doc.createElement('cars')
doc.appendChild(cars_element)

for car in cars_json:
    c = Car(car)
    cars.append(c)
    c_xml = c.to_xml_node(doc)
    
    '''create new xml element year and add text 2015 in it'''
    year_element = doc.createElement('year')
    year_element.appendChild(doc.createTextNode("2015"))
    c_xml.appendChild(year_element)

    '''create new xml element weight and add text 1000 in it'''
    weight_element = doc.createElement('weight')
    weight_element.appendChild(doc.createTextNode("1000"))
    c_xml.appendChild(weight_element)

    '''find the tag brand, replace its value by a new value and convert to CDATASection'''
    node = c_xml.getElementsByTagName('brand')[0]
    replace_by = u'©' + node.firstChild.nodeValue
    node.removeChild(node.firstChild)
    cdata_brand_element = doc.createCDATASection(replace_by)
    node.appendChild(cdata_brand_element)
    cars_element.appendChild(c_xml)

print doc.toxml(encoding='utf-8')
