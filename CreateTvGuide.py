import urllib
from HTMLParser import HTMLParser
from lxml import etree as et
import AltName

import sys        

def tempSiteData():
    global siteData
    site = urllib.urlopen('file://' + str(sys.argv[1]))
    return site.read()

def updateSiteData():
    global siteData
    site = urllib.urlopen('http://tvlistings.zap2it.com/tvlistings/ZCGrid.do?method=decideFwdForLineup&zipcode=21050&setMyPreference=false&lineupId=MD19432:X')
    return site.read()

root = et.Element("tv_guide")

class MyHTMLParser(HTMLParser):
    inName = False
    inNumber = False
    
    channel = None

    def handle_starttag(self, tag, attrs):
        if len(attrs) > 0 and tag == 'span' and attrs[0][1] == 'zc-st-n':
            self.inNumber = True
        if len(attrs) > 0 and tag == 'span' and attrs[0][1] == 'zc-st-c':
            self.inName = True

    def handle_endtag(self, tag):
        if tag == 'span':
            self.inNumber = False
            self.inName = False

    def handle_data(self, data):
        if self.inName:
            name = data.upper()
            et.SubElement(self.channel, "name").text = name
            for n in AltName.getAltNames(name):
                et.SubElement(self.channel, "name").text = n.upper()
        if self.inNumber:
            self.channel = et.SubElement(root, "channel")
            et.SubElement(self.channel, "number").text = data
        
def refreshGuide():
    parser = MyHTMLParser()
    
    #parser.feed(updateSiteData())
    parser.feed(tempSiteData())

    tree = et.ElementTree(root)
    tree.write("TvGuide.xml", pretty_print=True)

refreshGuide()
