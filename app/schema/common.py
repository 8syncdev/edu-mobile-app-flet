'''
Author: : Đinh Thành Đức
ID: 21110765
'''
from typing import Optional, Literal, Dict, List

# Define the structure of a single comment response
class CommentResponse:
    id: int  # Unique identifier for the comment
    content: str  # Content of the comment
    sentiment: str  # Sentiment of the comment
    created_at: str  # Timestamp indicating when the comment was created
    updated_at: str  # Timestamp indicating when the comment was last updated
    user: int  # Primary key of the user who made the comment
    course: int  # Primary key of the course associated with the comment

# Define the structure of the response containing multiple comments
class GetAllCommentResponse:
    detail: Literal['comments']  # Literal indicating the response detail type
    data: Dict[Literal['next', 'previous'], Optional[str]]  # Dictionary containing links to next and previous pages
    count: int  # Total count of comments
    results: List[CommentResponse]  # List of CommentResponse objects representing individual comments
