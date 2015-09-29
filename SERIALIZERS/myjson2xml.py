__author__ = 'niko'
from json2xml.json2xml import Json2xml
data = Json2xml.fromurl('https://coderwall.com/vinitcool76.json').data

print ("THE JSON IS ==========================================")
print data

print ("THE XML IS ==========================================")
data_object = Json2xml(data)
print data_object.json2xml()


