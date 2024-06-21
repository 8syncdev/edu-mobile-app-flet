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
    DOMAIN_API,
    SENTIMENT_API_DOMAIN
)

from app.util import (
    LocalStore
)

class CommonAPI:
    @staticmethod
    def send_contact(data: Dict[str, Any]) -> Dict[str, Any]:
        '''
        Sends a POST request to submit contact information to the server. Returns the server response.
        '''
        response = post(f'{DOMAIN_API}/api-view/common/contact/', json=data)
        return response.json()
    
    @staticmethod
    def comment_course(data: Dict[str, Any]) -> CommentResponse:
        '''
        Sends a POST request to submit a comment for a course to the server. Returns the server response as a CommentResponse.
        '''
        token = LocalStore.get_data('access', 'token')
        response = post(f'{DOMAIN_API}/api-view/common/comment-course/', json=data, headers={
            'Authorization': f'TokenByAnhTuDev {token}'
        })
        return response.json()

    @staticmethod
    def get_all_comments(page: Optional[int] = 1) -> GetAllCommentResponse:
        '''
        Sends a GET request to retrieve all comments, with optional pagination. Returns the server response as a GetAllCommentResponse.
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/api-view/common/get-all-comment/{page_query}')
        return response.json()
    
    @staticmethod
    def get_analysis_sentiment() -> Dict[str, Any]:
        '''
        Sends a GET request to retrieve sentiment analysis data from the server. Returns the server response.
        '''
        response = get(f'{DOMAIN_API}/api-view/common/get-data-analysis/')
        return response.json()
    
    @staticmethod
    def check_admin_role() -> bool:
        '''
        Checks if the current user has admin role privileges by sending a GET request to the server. Returns True if the user has admin privileges, otherwise False.
        '''
        try:
            token = LocalStore.get_data('access', 'token')
            response = get(f'{DOMAIN_API}/api-view/common/check-admin/', headers={
                'Authorization': f'TokenByAnhTuDev {token}'
            })
            return response.json().get('code')=='res_success'
        except:
            return False
        
    @staticmethod
    def sentiment_model(text: str) -> Dict[str, Any]:
        '''
        Sends a POST request to the sentiment analysis model API to analyze the sentiment of the provided text. Returns the server response.
        '''
        response = post(f'https://django-test-sentiment.onrender.com/api/sentiment', json={'text': text})
        return response.json()