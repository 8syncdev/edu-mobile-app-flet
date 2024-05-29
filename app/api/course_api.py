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
            #* Đây chỉ page 1, từ kỉ thuật phân trang từ bên Backend dev
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/courses/{page_query}')

        return response.json()
    
    @staticmethod
    def get_all_lessons_of_course(course_id: int, page: Optional[int] = 1) -> List[LessonResponse]:
        '''
            #* Đây chỉ page 1, từ kỉ thuật phân trang từ bên Backend dev
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/lessons/{course_id}/list-lesson-of-course/{page_query}')
        return response.json()
    
    @staticmethod
    def get_all_detail_lesson(lesson_id: int, page: Optional[int] = 1) -> LessonResponse:
        '''
            #* Đây chỉ page 1, từ kỉ thuật phân trang từ bên Backend dev
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/detail-lessons/{lesson_id}/list-detaillesson-of-lesson/{page_query}')
        return response.json()
    
    @staticmethod
    def get_detail_one_lesson(lesson_id: int) -> LessonResponse:
        '''
            #* Lấy chi tiết 1 bài học
        '''
        response = get(f'{DOMAIN_API}/detail-lessons/{lesson_id}/')
        return response.json()

