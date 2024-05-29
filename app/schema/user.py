
from typing import (
    Optional,
    Literal,
    LiteralString
)

class UserSignInRequest(object):
    username: LiteralString
    password: LiteralString