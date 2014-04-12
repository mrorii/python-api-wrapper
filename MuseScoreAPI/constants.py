"""
    Constants For All MuseScore Endpoints
    -----------------------------------
    
    Version 1.0,EST API.
    
    URLs for each endpoint are composed of the following pieces:
        PROTOCOL://{subdomain}.DOMAIN/VERSION/{resource}?{parameters}
"""

__author__ = "Nicolas Froment"
__date__ = "April 12, 2014"
__license__ = "MIT"


PROTOCOL = 'http'

DOMAIN = 'musescore.com'

VERSION = 'services/rest'

USER_AGENT = 'python-MuseScoreAPI'

STREAMING_SOCKET_TIMEOUT = 90  # 90 seconds per Twitter's recommendation


REST_SUBDOMAIN = 'api'

REST_SOCKET_TIMEOUT = 5

REST_ENDPOINTS = {
        # resource:              ( method )
        'me':                    ('GET',),  
        'user/:PARAM':           ('GET',),              # ID 
        'user/:PARAM/score':     ('GET',),              # ID 

        'score':                 ('GET', 'POST'),  
        'score/:PARAM':          ('GET', 'DELETE'),     # ID  
        'score/:PARAM/time':     ('GET'),               # ID 
        'score/:PARAM/space':    ('GET',),              # ID 

        'resolve':               ('GET',)  
}