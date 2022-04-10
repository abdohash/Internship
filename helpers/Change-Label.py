import os
import xml.etree.ElementTree as ET

files = os.listdir('/Annotations') # path to xml Annotations files

for file in files:
    tree = ET.parse(file)
    temp = tree.find('object')
    temp[0].text = 'non-standard' # standard or non-standard depending on the dataset
    tree.write(file)
