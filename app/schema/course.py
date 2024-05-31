'''
Author: Nguyễn Phương Anh Tú
ID: 21110105
'''
from typing import Optional, Literal, Dict, List

# Define the structure of a single course response
class CourseResponse:
    id: Optional[int]  # Unique identifier for the course
    title: str  # Title of the course
    description: str  # Description of the course
    price: float  # Price of the course
    instructor_name: str  # Name of the instructor of the course
    extent_name: str  # Name of the extent of the course
    created_at: str  # Timestamp indicating when the course was created
    updated_at: str  # Timestamp indicating when the course was last updated
    slug: str  # Slug of the course

# Define the structure of the response containing multiple courses
class CoursePaginationResponse:
    links: Optional[Dict[Literal['next', 'previous'], Optional[str]]]  # Dictionary containing links to next and previous pages
    count: int  # Total count of courses
    results: List[CourseResponse]  # List of CourseResponse objects representing individual courses
