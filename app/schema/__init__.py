'''
    Author: Nguyễn Phương Anh Tú
    
    Main Purpose:
    => Export all the modules in the schema package.
'''

'''
- UserSignInRequest, UserForgotPasswordRequest, UserSignUpRequest, UserSignInResponse, UserSignUpResponse, UserForgotPasswordResponse, and UserSignOutRequest are all related to user authentication and account management.
- CourseResponse and CoursePaginationResponse deal with the response formats for course-related data.
- CommentResponse and GetAllCommentResponse are schema definitions for comments and responses to retrieve comments.
- get_brand_imagpath, get_tech_imagpath, and get_with_relativename are utility functions to fetch image paths for brand and tech assets, as well as determining image paths based on provided names.
- TStaticTemplate is a type definition for static page templates, specifying possible values for page routing.
'''
from app.schema.user import (
    UserSignInRequest,
    UserForgotPasswordRequest,
    UserSignUpRequest,
    UserSignInResponse,
    UserSignUpResponse,
    UserForgotPasswordResponse,
    UserSignOutRequest,
)

from app.schema.course import (
    CourseResponse,
    CoursePaginationResponse
)

from app.schema.common import (
    CommentResponse,
    GetAllCommentResponse
)


from app.schema.asset import (
    get_brand_imagpath,
    get_tech_imagpath,
    get_with_relativename
)

from app.schema.pages import (
    TStaticTemplate
)