# Write a program to read xml file.
# Read parent tag and child tag inside that parent tag.
# Read the attribute of that child tag and print the value of that attribute.
# Use xml.dom.minidom library
# Example - from xml.dom.minidom import parse
# Copy the below xml text and save it as .xml file
# Use parse(path of xml file) to read xml file from path

import xml
from xml.dom.minidom import parse

# store the xml file data in document variable
document = xml.dom.minidom.parse("myfile.xml")
# get all template tags
templates = document.getElementsByTagName("template")
# print no. of found template
print("%d templates found." % templates.length)

for template in templates:
    print("------------------------------")
    print(template.tagName, end=":")    # to print currnt template tag name
    print(" id =", template.getAttribute("id"))     # to get the attribute from a tag
    xpaths = template.getElementsByTagName("xpath")
    for xpath in xpaths:
        print(xpath.tagName, end=":")
        print(" position =", xpath.getAttribute("position"))
    links = template.getElementsByTagName("link")
    for link in links:
        print(link.tagName, end=":")
        print(" rel =", link.getAttribute("rel"), ",")
        print("      href =", link.getAttribute("href").split('/')[-1])     # string after last slash
    scripts = template.getElementsByTagName("script")
    for script in scripts:
        print(script.tagName, end=":")
        print(" src =", script.getAttribute("src").split('/')[-1])
