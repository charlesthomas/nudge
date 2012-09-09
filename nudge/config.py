"""
These values should be set by the user implementing this module.
"""
CONSUMER_KEY='8fbf14c614594d24b8e10fd8a7e68e20'
CONSUMER_SECRET='a5c2c97752814291bfbfcbb5c0f08433'

"""
These values will probably remain relatively constant, and won't need to be
touched by users implementing this module. However, they are included in order
to abstract the configurable values, in case FitBit changes functionality in
their API.
"""

BASE_URL          = 'api.fitbit.com'
HTTPPORT          = 80
REQUEST_TOKEN_URL = '/oauth/request_token'
ACCESS_TOKEN_URL  = '/oauth/access_token'

OAUTH_URL         = 'www.fitbit.com'
AUTHORIZE_URL     = OAUTH_URL + '/oauth/authenticate'
