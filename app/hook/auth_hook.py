

from app.util import (
    LocalStore
)

class AuthHook:
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