'''
    Author: : Đinh Thành Đức
    ID: 21110765
    Author: : Lê Quốc Thắng
    ID: 21110799
'''
from app.util import (
    LocalStore
)

class AuthHook:
    '''
        - set_authenticated(user): Marks the user as authenticated and sets user information.
        - check_authenticated(): Returns whether a user is authenticated.
        - get_user(): Retrieves user information either from the stored state or from the local store if not authenticated.
    '''
    state = {
        'is_authenticated': False,
        'user': None,
    }

    @staticmethod
    def set_authenticated(user):
        AuthHook.state['is_authenticated'] = True
        AuthHook.state['user'] = user

    @staticmethod
    def check_authenticated():
        return AuthHook.state['is_authenticated']
    
    @staticmethod
    def get_user():
        return AuthHook.state['user'] if AuthHook.state['user'] != None else LocalStore.get_data('data', 'profile')