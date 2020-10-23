from urllib.parse import urlencode

from social_core.backends.oauth import BaseOAuth2


class AkunOAuth2(BaseOAuth2):
    """Akun OAuth2 authentication backend"""
    name = 'akun'
    AUTHORIZATION_URL = 'https://akun-kp.cs.ui.ac.id/cas/oauth2.0/authorize'
    ACCESS_TOKEN_URL = 'https://akun-kp.cs.ui.ac.id/cas/oauth2.0/token'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('attributes', 'attributes'),
        ('expires_in', 'expires')
    ]

    def get_user_details(self, response):
        """Return user details from Akun profile"""
        print('backends.py:18', response)
        return {
            'username': response.get('id'),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://akun-kp.cs.ui.ac.id/cas/oauth2.0/profile?' + urlencode({
            'access_token': access_token
        })
        return self.get_json(url)
