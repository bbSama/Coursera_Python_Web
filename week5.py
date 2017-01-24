import xml.etree.ElementTree as ET
import urllib

url = raw_input("Enter location: ")
data = urllib.urlopen(url).read()

print 'Retrieving',url
print 'Retrieved %d characters'%(len(data))

tree = ET.fromstring(data)
counts = tree.findall('.//count')
Sum = sum([int(x.text) for x in counts])
print 'Count:',len(counts)
print 'Sum:',Sum
