from requests_oauthlib import OAuth2Session
from config import Config

def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Config.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(Config.CLIENT_ID, state=state, redirect_uri=Config.REDIRECT_URI)
    oauth = OAuth2Session(Config.CLIENT_ID, redirect_uri=Config.REDIRECT_URI,
                            scope=Config.SCOPE)
    return oauth
