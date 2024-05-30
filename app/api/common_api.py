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
        response = post(f'{DOMAIN_API}/api-view/common/contact/', json=data)
        return response.json()
    
    @staticmethod
    def comment_course(data: Dict[str, Any]) -> CommentResponse:
        token = LocalStore.get_data('access', 'token')
        response = post(f'{DOMAIN_API}/api-view/common/comment-course/', json=data, headers={
            'Authorization': f'TokenByAnhTuDev {token}'
        })
        return response.json()

    @staticmethod
    def get_all_comments(page: Optional[int] = 1) -> GetAllCommentResponse:
        '''
            #* Đây chỉ page 1, từ kỉ thuật phân trang từ bên Backend dev
        '''
        page_query = f"?page={page}" if page > 1 else ""
        response = get(f'{DOMAIN_API}/api-view/common/get-all-comment/{page_query}')
        return response.json()
    
    @staticmethod
    def get_analysis_sentiment() -> Dict[str, Any]:
        response = get(f'{DOMAIN_API}/api-view/common/get-data-analysis/')
        return response.json()
    
    @staticmethod
    def check_admin_role() -> bool:
        try:
            token = LocalStore.get_data('access', 'token')
            response = get(f'{DOMAIN_API}/api-view/common/check-admin/', headers={
                'Authorization': f'TokenByAnhTuDev {token}'
            })
            return response.json().get('code')=='res_success'
        except:
            return False