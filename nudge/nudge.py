#!/usr/bin/env python
from config import *
import httplib
import oauth.oauth as oauth

class Nudge( object ):
    def __init__( self ):
        self.consumer_key      = CONSUMER_KEY
        self.consumer_secret   = CONSUMER_SECRET
        self.httpport          = HTTPPORT
        self.base_url          = BASE_URL
        self.request_token_url = REQUEST_TOKEN_URL
        self.access_token_url  = ACCESS_TOKEN_URL
        self.oauth_url         = OAUTH_URL
        self.authorize_url     = AUTHORIZE_URL
        return None

    def is_auth( self ):
        try:
            return self.authorized
        except AttributeError:
            return 0

    def authorize( self ):
        if self.is_auth():
            return 1

        consumer = oauth.OAuthConsumer(
            self.consumer_key, self.consumer_secret
        )
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(
            consumer, http_url = self.request_token_url
        )
        oauth_request.sign_request(
            oauth.OAuthSignatureMethod_PLAINTEXT(), consumer, None
        )
        connection = httplib.HTTPConnection( 
            "%s:%d" % ( self.base_url, self.httpport )
        )
        connection.request(
            'POST',
            self.request_token_url, 
            headers = oauth_request.to_header()
        )

        response = connection.getresponse()
        token    = oauth.OAuthToken.from_string( response.read() )

        print """
            Because this is not a web-app, you will have to go to the following
            URL in a browser. Once there, you need to authorize this application
            on FitBit.com. You will then receive a token, or a string of
            non-sense characters. Import them below. Also, to prevent needed to
            do this again, update the config.py file.
            ----------
            Copy this into a browser: http://%s?oauth_token=%s
            """ % ( self.authorize_url, token.key )

        print "Please input the token you received from FitBit.com here."
        
        verifier = raw_input( '> ' )

        oauth_request = oauth.OAuthRequest.from_consumer_and_token(
            consumer, token = token, verifier = verifier,
            http_url = self.access_token_url
        )
        oauth_request.sign_request(
            oauth.OAuthSignatureMethod_PLAINTEXT(), consumer, token
        )
        connection.request(
            'POST',
            self.access_token_url,
            headers = oauth_request.to_header()
        )

        response = connection.getresponse()
        token    = oauth.OAuthToken.from_string( response.read() )

        print "token: %s" % token

        self.authorized = 1
        return 1
