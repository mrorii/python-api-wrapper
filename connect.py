from requests_oauthlib import OAuth1Session
import webbrowser


request_token_url = 'http://api.musescore.com/oauth/request_token'
base_authorization_url = 'http://musescore.com/oauth/authorize'
access_token_url = 'http://api.musescore.com/oauth/access_token'
client_key = 'musichackday'
client_secret='musichackday2013'
resource_owner_key=''
resource_owner_secret=''


#obtain a request token
oauth = OAuth1Session(client_key, client_secret=client_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
print fetch_response

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')


# Obtain authorization
authorization_url = oauth.authorization_url(base_authorization_url)
print 'Please go here and authorize,', authorization_url
webbrowser.open(authorization_url)
redirect_response = raw_input('Press any key when authorized')


# Obtain access token
oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)
oauth_tokens = oauth.fetch_access_token(access_token_url)
print oauth_tokens

resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')

cred = {"client_key": client_key, "client_secret": client_secret, 
        "resource_owner_key": resource_owner_key, 
        "resource_owner_secret": resource_owner_secret}

import json
with open('credentials.json', 'w') as outfile:
  json.dump(cred, outfile)
