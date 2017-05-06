#!/usr/bin/env python
import web
from web.wsgiserver import CherryPyWSGIServer as Cherry
import commands as tv

Cherry.ssl_certificate = "domain.crt"
Cherry.ssl_private_key ="domain.key"



urls = (
    '/channel/number/(.*)', 'number',
    '/channel/name/(.*)', 'name',
    '/tv/on', 'on',
    '/tv/off', 'off',
    '/volume/increase', 'inc_volume',
    '/volume/decrease', 'dec_volume',
    '/volume/value/(.*)', 'volume',
    '/volume/mute', 'mute'
)

app = web.application(urls, globals())

class number:
    def GET(self, n):
        tv.channelNumber(n)

class name:
    def GET(self, n):
        tv.channelName(n)

class on:
    def GET(self):
        tv.on()

class off:
    def GET(self):
        tv.off()

class inc_volume:
    def GET(self):
        tv.inc_volume()

class dec_volume:
    def GET(self):
        tv.dec_volume()

class volume:
    def GET(self, vol):
        tv.volume()

class mute:
    def GET(self):
        tv.mute()

if __name__ == "__main__":
    app.run()
    print "here"
