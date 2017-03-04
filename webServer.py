#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET

tree = ET.parse('TvGuide.xml')
root = tree.getroot()

urls = (
    '/channel/number/(.*)', 'get_number',
    '/channel/name/(.*)', 'get_name'
)

app = web.application(urls, globals())

class get_number:
    def GET(self, number):
        for channel in root:
            for r in channel:
                if r.tag == 'number' and r.text == number:
                    print "Changing channel to", r.text

class get_name:
    def GET(self, name):
        for channel in root:
            for r in channel:
                if r.tag == 'name' and r.text == name:
                    print "here"
                    #if 'HD' not in r.text:
                    #    prev.text = getHD(name)
                    print "Changing channel to", num
                if r.tag == 'number':
                    num = r.text

def getHD(name):
    for channel in root:
        for r in channel:
            if r.text == (name + "HD") or r.text == (name + " HD"):
                return prev.text
            prev = r
    return name

if __name__ == "__main__":
    app.run()
