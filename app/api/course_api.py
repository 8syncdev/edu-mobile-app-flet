'''
    Author: Nguyễn Phương Anh Tú
    
    
    
'''
from typing import (
    Optional,
    Literal,
    List,
    Dict,
    Any
)

from requests import (
    get,
    post,
)

from app.schema import *

from app import (
    DOMAIN_API
)
LessonResponse=Dict[str, Any]

class CourseAPI:
    @staticmethod
    def get_all_courses(page: Optional[int] = 1) -> CoursePaginationResponse:
        '''
            Author: Nguyễn Phương Anh Tú
            
            Sends a GET request to retrieve all courses, with optional pagination. Returns the server response as a CoursePaginationResponse
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/courses/{page_query}')

        return response.json()
    
    @staticmethod
    def get_all_lessons_of_course(course_id: int, page: Optional[int] = 1) -> List[LessonResponse]:
        '''
            Author: Nguyễn Phương Anh Tú
            
            Sends a GET request to retrieve all lessons of a specific course, with optional pagination. Returns the server response as a list of LessonResponse objects
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/lessons/{course_id}/list-lesson-of-course/{page_query}')
        return response.json()
    
    @staticmethod
    def get_all_detail_lesson(lesson_id: int, page: Optional[int] = 1) -> LessonResponse:
        '''
            
            
            Sends a GET request to retrieve all detail lessons of a specific lesson, with optional pagination. Returns the server response as a LessonResponse
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/detail-lessons/{lesson_id}/list-detaillesson-of-lesson/{page_query}')
        return response.json()
    
    @staticmethod
    def get_detail_one_lesson(lesson_id: int) -> LessonResponse:
        '''
            
            
            Sends a GET request to retrieve the details of a specific lesson. Returns the server response as a LessonResponse object
        '''
        response = get(f'{DOMAIN_API}/detail-lessons/{lesson_id}/')
        return response.json()
    
    @staticmethod
    def get_all_exercise_by_slug(slug: str) -> Any:
        '''
            Author: Nguyễn Phương Anh Tú
            
            Sends a GET request to retrieve all exercises of a specific lesson. Returns the server response as a list of ExerciseResponse objects
        '''
        response = get(f'{DOMAIN_API}/exercises/get-all-exercise-by-name?slugTagName={slug}')
        return response.json()
    
    @staticmethod
    def get_one_detail_exercise(exercise_id: int) -> Any:
        '''
            Author: Nguyễn Phương Anh Tú
            
            Sends a GET request to retrieve the details of a specific exercise. Returns the server response as a ExerciseResponse object
        '''
        response = get(f'{DOMAIN_API}/exercises/{exercise_id}/')
        return response.json()



