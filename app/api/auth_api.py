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
        response = post(f'{DOMAIN_API}/api/token/', json=payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'code': 'res_error'
            }
        
    @staticmethod
    def get_user_by_token(token: str):
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
        response = post(f'{DOMAIN_API}/api-view/sign-up/', json=payload)
        return response.json()
    
    @staticmethod
    def forgot_password(payload: dict):
        response = get(f'{DOMAIN_API}/api-view/common/forgot-password/', json=payload)
        return response.json()

    