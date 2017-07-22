
import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('xx.xml')
root = tree.getroot()
for el in root.findall('country'):
    #el = root.find('country')
    xmlstr = minidom.parseString(ET.tostring(el)).toprettyxml(indent="   ")
    print xmlstr
    print('------------')
    break

