# -*- coding: utf-8 -*-

import sys, gzip, base64
if sys.version_info[0] >= 3:
    import urllib.request, urllib.error, urllib.parse 
    from io import StringIO
else:
    import urllib2
    from StringIO import StringIO

API = sys.modules[ "__main__" ].API
URL = 'http://api.wunderground.com/api/%s/%s/%s/q/%s.%s'

def wundergroundapi(features, settings, query, fmt):
    url = URL % (API, features, settings, query, fmt)
    try:
        if sys.version_info[0] >= 3:
            req = urllib.request.Request(url)
            req.add_header('Accept-encoding', 'gzip')
            response = urllib.request.urlopen(req)
        else:
            req = urllib2.Request(url)
            req.add_header('Accept-encoding', 'gzip')
            response = urllib2.urlopen(req)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            compr = gzip.GzipFile(fileobj=buf)
            data = compr.read()
        else:
            data = response.read()
        response.close()
    except:
        data = ''
    return data
