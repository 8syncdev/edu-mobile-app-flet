'''
    Author: Nguyễn Phương Anh Tú
    
    
    
'''

# Importing necessary type hints from typing module
from typing import Optional, Literal, LiteralString

# Defining a class for user sign-in request
class UserSignInRequest(object):
    # Username and password fields with LiteralString type hint
    username: LiteralString
    password: LiteralString

# Defining a class for user sign-in response
class UserSignInResponse(object):
    # Token field with LiteralString type hint
    token: LiteralString

# Defining a class for user sign-up request
class UserSignUpRequest(object):
    # Username, password, email, and full name fields with LiteralString type hint
    username: LiteralString
    password: LiteralString
    email: LiteralString
    full_name: LiteralString

# Defining a class for user sign-up response
class UserSignUpResponse(object):
    # Token field with LiteralString type hint
    token: LiteralString

# Defining a class for user sign-out request
class UserSignOutRequest(object):
    # Token field with LiteralString type hint
    token: LiteralString

# Defining a class for user forgot password request
class UserForgotPasswordRequest(object):
    # Email field with LiteralString type hint
    email: LiteralString

# Defining a class for user forgot password response
class UserForgotPasswordResponse(object):
    # Message field with LiteralString type hint
    message: LiteralString
