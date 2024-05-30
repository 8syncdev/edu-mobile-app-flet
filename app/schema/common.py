
from typing import (
    Optional,
    Literal,
    Dict,
    List
)

class CommentResponse(object):
    id: int
    content: str
    sentiment: str
    created_at: str
    updated_at: str
    user: int # primary key of user
    course: int # primary key of course



class GetAllCommentResponse(object):
    detail: Literal['comments']
    data: Dict[
        Literal['next', 'previous'],
        Optional[str]
    ]
    count: int
    results: List[CommentResponse]