#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
import re
# In data stage,
#     - Create a script in ruby or python to parse the included steam.xml and gog.xml, print out
#     timestamp, filesize, hash for both bg3.exe and bg3.exe. Call this script in the data stage
#     of the job.
#     - Remember version (4.1.1….)

file = ET.parse(sys.argv[1]).getroot()
build_manifest = file.get('build')
print('Parsing file', sys.argv[1])
for child in file.findall('files/File'):
    if child.text.find('bg3.exe') != -1:
        print("hash:", child.attrib.get('hash'), "size:", child.attrib.get('size'))
print("Version:", re.search(r'Version:(([^\s]+))', build_manifest).groups()[0])
print("timestamp:", re.search(r'on (([^\s]+))', build_manifest).groups()[0], re.search(r'at (([^\s]+))', build_manifest).groups()[0])
