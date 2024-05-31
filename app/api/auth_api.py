'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
    Author: : Đinh Thành Đức
    ID: 21110765
    Main Purpose:
    => Implementing the AuthAPI class to handle user authentication API requests.
'''
from typing import (
    Optional,
    Literal
)

from requests import (
    get,
    post,
)

from app.schema import (
    UserSignInRequest
)

from app import (
    DOMAIN_API
)

from app.util import (
    LocalStore
)


from app.hook import (
    AuthHook
)

class AuthAPI:   
    @staticmethod 
    def get_token(payload: UserSignInRequest):
        '''
        Author: Nguyễn Phương Anh Tú
        ID: 21110105
        Sends a POST request to retrieve a token based on the provided user sign-in payload. Returns the token if successful, otherwise returns an error code.
        '''
        response = post(f'{DOMAIN_API}/api/token/', json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'code': 'res_error'
            }
        
    @staticmethod
    def get_user_by_token(token: str):
        '''
        Author: Nguyễn Phương Anh Tú
        ID: 21110105
        Sends a GET request to fetch user information using the provided token. Returns user data if successful, otherwise returns an error code.
        '''
        response = get(f'{DOMAIN_API}/users/get-user-by-token', headers={
            'Authorization': f'TokenByAnhTuDev {token}'
        })
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'code': 'res_error'
            }
            

    @staticmethod
    def check_auth():
        '''
        Author: Nguyễn Phương Anh Tú
        ID: 21110105
        Checks if the user is authenticated by attempting to retrieve the token from local storage and verifying it with the server. Returns True if authenticated, otherwise False.
        '''
        token = LocalStore.get_data('access', 'token')
        if token:
            user = AuthAPI.get_user_by_token(token)
            if user.get('code') == 'res_error':
                return False
            else:
                AuthHook.set_authenticated(user.get('data'))
                return True
        else:
            return False
        
    @staticmethod
    def sign_up(payload: dict):
        '''
        Author: : Đinh Thành Đức
        ID: 21110765
        Sends a POST request to sign up a new user with the provided payload. Returns the server response.
        '''
        response = post(f'{DOMAIN_API}/api-view/sign-up/', json=payload)
        return response.json()
    
    @staticmethod
    def forgot_password(payload: dict):
        '''
        Author: : Đinh Thành Đức
        ID: 21110765
        Sends a GET request to initiate the forgot password process with the provided payload. Returns the server response.
        '''
        response = get(f'{DOMAIN_API}/api-view/common/forgot-password/', json=payload)
        return response.json()

    