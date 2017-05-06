import xml.etree.ElementTree as ET

enableHD = True

tree = ET.parse('TvGuide.xml')
root = tree.getroot()

def channelNumber(number):
    for channel in root:
        for r in channel:
            if r.tag == 'number' and r.text == number:
                print "Changing channel to", r.text

def channelName(name):
    name = name.upper()
    if name == 'ON':
        on()
    if enableHD:
        name = getHD(name)
    for channel in root:
        for r in channel:
            if r.tag == 'name' and r.text == name:
                print "Changing channel to", num
            if r.tag == 'number':
                num = r.text

def on():
    print "turning the tv on"

def off():
    print "turning the tv off"

def inc_volume():
    print "increasing the volume"

def dec_volume():
    print "decreasing the volume"
    
def volume():
    print "voluming"

def mute():
    print "muting the tv"

def getHD(name):
    for channel in root:
        for r in channel:
            if r.text == (name + "HD") or r.text == (name + " HD"):
                return prev.text
            prev = r
    return name
