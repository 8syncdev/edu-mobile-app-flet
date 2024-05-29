

from typing import (
    Optional,
    Literal,
    Dict,
    List
)


class CourseResponse(object):
    id: Optional[int]
    title: str 
    description: str
    price: float
    instructor_name: str
    extent_name: str
    created_at: str
    updated_at: str
    slug: str


class CoursePaginationResponse(object):
    links: Optional[Dict[
        Literal['next', 'previous'],
        Optional[str]
    ]]
    count: int
    results: List[CourseResponse]